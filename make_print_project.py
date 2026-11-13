#!/usr/bin/env python3
"""FreeCAD side (headless) orients and meshes each unique part, Bambu Studio CLI builds the project."""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

FREECAD = "/home/mikhail/AppImages/astocad.appimage"
BAMBU = "/home/mikhail/AppImages/bambustudio.appimage"
HERE = os.path.dirname(os.path.abspath(__file__))
DOC = os.environ.get("PRINT_DOC") or (sys.argv[1] if len(sys.argv) > 1 else "Differential")
FCSTD = os.path.join(HERE, DOC + ".FCStd")
OUT = os.path.join(HERE, DOC + ".3mf")
SYS = os.path.expanduser("~/.config/BambuStudio/system/BBL")
MACHINE = "machine/Bambu Lab P1S 0.4 nozzle.json"
PROCESS = "process/0.20mm Standard @BBL X1C.json"
FILAMENT = "filament/Bambu PLA Matte @BBL X1C.json"
DEFLECTION = 0.02
MIN_FLOOR_AREA = 5.0

# document axis that points up on the bed; identical parts are detected from geometry
UPS = {"WheelMount": {"Mount_R": "-X", "Mount_L": "+X", "Knuckle": "+X", "Stub": "+Z", "WheelHub": "-X"},
       "MotorModule": {"Bracket": "+Y", "MotorGear": "-Y", "ShaftGear": "-Y", "ThroughShaft": "+Z"},
       "CvtModule": {"Lid": "-Z", "Disc": "+Z", "ThroughShaft": "+Z", "Wheel": "+Y", "Shuttle": "+X", "RollerSlider": "+Z", "Roller": "+Y", "ServoArm": "+Z"},
       "DriveShaft": {"JointYoke_1": "+X", "JointYoke_2": "-X", "JointYoke_3": "+X", "JointYoke_4": "-X", "JointCross_1": "+X", "JointCross_2": "-X", "SlideRod": "+Y", "SlideTube": "+X"}}
COPIES = {"WheelMount": {"Mount_R": 1, "Mount_L": 1, "Knuckle": 2, "Stub": 2, "WheelHub": 2},
          "MotorModule": {"Bracket": 1, "MotorGear": 1, "ShaftGear": 1, "ThroughShaft": 1},
          "CvtModule": {"Lid": 1, "Disc": 1, "ThroughShaft": 1, "Wheel": 1, "Shuttle": 1, "RollerSlider": 1, "Roller": 1, "ServoArm": 1},
          "DriveShaft": {"JointYoke_1": 4, "JointCross_1": 2, "SlideRod": 1, "SlideTube": 1},
          "Differential": {"Carrier": 1, "Cap": 1, "Bushing_L": 1, "Bushing_R": 1, "SideGear_L": 2, "SpiderGear_1": 2, "SpiderPin": 1, "HalfShaft_L": 1, "HalfShaft_R": 1, "PinionA": 2, "PinionShaftA": 2, "IdlerRing": 1, "CaseTop": 1, "CaseBottom": 1}}
MIRRORED = {"WheelMount": ("Mount_L",)}  # mirror images never share a print group
SKIP = {"DriveShaft": ("DummyPort_1", "DummyPort_2", "Shown_JointYoke_1", "Shown_JointYoke_2", "Shown_JointYoke_3", "Shown_JointYoke_4", "Shown_JointCross_1", "Shown_JointCross_2", "Shown_SlideRod", "Shown_SlideTube")}
UP = UPS.get(DOC) or {
    "Carrier": "+X", "Cap": "-X", "Bushing_L": "+X", "Bushing_R": "+X",
    "SideGear_L": "+X", "SideGear_R": "-X", "SpiderGear_1": "+Y", "SpiderGear_2": "-Y",
    "SpiderPin": "-Z", "HalfShaft_L": "+Z", "HalfShaft_R": "+Z",
    "PinionA": "+Y", "PinionB": "-Y", "PinionShaftA": "+Z", "PinionShaftB": "+Z",
    "IdlerRing": "-X", "CaseTop": "-Z", "CaseBottom": "+Z",
}


def fail(msg):
    print(msg, flush=True)
    os._exit(1)


def freecad_side(build):
    import FreeCAD
    import MeshPart
    import Part

    doc = FreeCAD.openDocument(FCSTD)
    shapes = {}
    for o in doc.Objects:
        if o.TypeId != "Part::Feature" or not getattr(o, "Shape", None) or not o.Shape.Solids:
            continue
        if o.Name in SKIP.get(DOC, ()):
            continue
        if o.Name not in UP:
            fail("FAIL: part %s has no print orientation in UP" % o.Name)
        shapes[o.Name] = o.Shape

    def orient(name):
        sign, axis = UP[name]
        up = FreeCAD.Vector(*[(1 if sign == "+" else -1) if a == axis else 0 for a in "XYZ"])
        s = shapes[name].copy()
        s.transformShape(FreeCAD.Placement(FreeCAD.Vector(), FreeCAD.Rotation(up, FreeCAD.Vector(0, 0, 1))).toMatrix())
        s.translate(FreeCAD.Vector(0, 0, -s.optimalBoundingBox(False, False).ZMin))
        floor = sum(f.Area for f in s.Faces if f.BoundBox.ZMax < 1e-4 and isinstance(f.Surface, Part.Plane))
        if floor < MIN_FLOOR_AREA:
            fail("FAIL: %s has no planar floor face (area %.2f) when printed with %s up" % (name, floor, UP[name]))
        return s

    dims = lambda s: sorted((s.optimalBoundingBox(False, False).XLength, s.optimalBoundingBox(False, False).YLength, s.optimalBoundingBox(False, False).ZLength))
    groups = []
    for name in shapes:
        s = orient(name)
        for g in groups:
            c = g["shape"]
            if (name in MIRRORED.get(DOC, ())) == (g["members"][0] in MIRRORED.get(DOC, ())) and abs(c.Volume - s.Volume) <= 1e-3 * c.Volume and all(abs(x - y) <= 0.1 for x, y in zip(dims(c), dims(s))):
                g["members"].append(name)
                break
        else:
            groups.append(dict(shape=s, members=[name]))
    manifest = []
    for g in groups:
        s, name = g["shape"], g["members"][0]
        b = s.optimalBoundingBox(False, False)
        mesh = MeshPart.meshFromShape(s, LinearDeflection=DEFLECTION, AngularDeflection=0.1)
        mesh.write(os.path.join(build, name + ".stl"))
        manifest.append(dict(name=name, copies=COPIES.get(DOC, {}).get(name, len(g["members"])), members=g["members"],
                             size=[b.XLength, b.YLength, b.ZLength], volume=s.Volume, facets=mesh.CountFacets))
    json.dump(manifest, open(os.path.join(build, "manifest.json"), "w"), indent=1)


def run_freecad(build):
    env = dict(os.environ, APPIMAGE_EXTRACT_AND_RUN="1", PRINT_BUILD=build, PRINT_DOC=DOC)
    path = os.path.abspath(__file__)
    code = "exec(compile(open(%r).read(), %r, 'exec'), {'__name__': 'freecad_side', '__file__': %r})" % (path, path, path)
    r = subprocess.run([FREECAD, "-c", code], env=env, capture_output=True, text=True)
    if r.returncode or not os.path.exists(os.path.join(build, "manifest.json")):
        sys.exit("FreeCAD step failed:\n" + r.stdout[-3000:] + r.stderr[-3000:])
    return json.load(open(os.path.join(build, "manifest.json")))


def flatten(rel, build):
    # the CLI ignores "inherits", so merge the parent chain into one JSON
    def merged(path):
        j = json.load(open(path))
        parent = j.pop("inherits", None)
        base = merged(os.path.join(os.path.dirname(path), parent + ".json")) if parent else {}
        return {**base, **j}

    out = os.path.join(build, os.path.basename(rel))
    json.dump(merged(os.path.join(SYS, rel)), open(out, "w"))
    return out


def run_bambu(build, manifest):
    env = dict(os.environ, APPIMAGE_EXTRACT_AND_RUN="1")
    machine, process, filament = (flatten(p, build) for p in (MACHINE, PROCESS, FILAMENT))
    cmd = [BAMBU, "--orient", "0", "--arrange", "1",
           "--clone-objects", ",".join(str(m["copies"]) for m in manifest),
           "--load-settings", machine + ";" + process,
           "--load-filaments", filament,
           "--outputdir", build, "--export-3mf", "raw.3mf"] + [m["name"] + ".stl" for m in manifest]
    r = subprocess.run(cmd, cwd=build, env=env, capture_output=True, text=True)
    res = json.load(open(os.path.join(build, "result.json")))
    if r.returncode or res["return_code"]:
        sys.exit("Bambu Studio failed:\n" + r.stdout[-3000:] + json.dumps(res))


def rename_objects(src, dst):
    # the CLI names objects "<file>.stl" or "<file>.stl_N"; restore plain part names
    with zipfile.ZipFile(src) as zi, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zi.infolist():
            data = zi.read(item.filename)
            if item.filename == "Metadata/model_settings.config":
                data = re.sub(rb'(key="name" value="\w+)\.stl', rb"\1", data)
            zo.writestr(item, data)


def main():
    build = tempfile.mkdtemp(prefix="print_build_")
    try:
        manifest = run_freecad(build)
        run_bambu(build, manifest)
        rename_objects(os.path.join(build, "raw.3mf"), OUT)
    finally:
        shutil.rmtree(build, ignore_errors=True)
    for m in manifest:
        print("%-14s x%d  %s" % (m["name"], m["copies"], " ".join("%.1f" % v for v in m["size"])))
    print("wrote", OUT)


if __name__ == "freecad_side":
    freecad_side(os.environ["PRINT_BUILD"])
elif __name__ == "__main__":
    main()
