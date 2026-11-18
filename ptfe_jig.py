# PtfeJig: printed jig that cuts PTFE tube into bearing liners, plus a go/no-go gauge for the cut liners. Puck prints flat, pocket up, no supports. GoGauge prints flat.
# GoGauge slot 8.3 is deliberately the same nominal as the kit's printed 8.3 pocket, so both shrink alike when printed.
# Use: push the tube down over the pin to the pocket floor, lay a fresh blade flat on the top face, draw it through the tube while turning the tube; the piece left in the pocket is one liner, push it out from below through the two holes.
import FreeCAD as App, Part, math

D = {"NO_RUN": True, "__name__": "x"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/drive_hub.py").read(), "drive_hub.py", "exec"), D)
print_check = D["print_check"]

DOC_NAME = "PtfeJig"
OUT = "/home/mikhail/Documents/cad/RC Car/PtfeJig.FCStd"
V = App.Vector
TUBE_OD, TUBE_ID, CUT_L = 12.0, 10.0, 8.0
OD_CLR, ID_CLR = 0.7, 0.6
POCKET_D, PIN_D = TUBE_OD + OD_CLR, TUBE_ID - ID_CLR
PIN_BELOW, PIN_CH, MOUTH_CH = 0.3, 0.5, 0.4
BASE, PUCK_D = 4.0, 48.0
TOP = BASE + CUT_L
EJECT_D = 3.6
FLUTES, FLUTE_R, FLUTE_DEPTH = 7, 3.0, 1.5
SLOT_GO, SLOT_NOGO, SLOT_W = 8.3, 7.7, 12.6
G_T, G_M, G_R = 3.0, 4.0, 3.0


def cyl(r, z0, z1, x=0.0, y=0.0):
    return Part.makeCylinder(r, z1 - z0, V(x, y, z0), V(0, 0, 1))


def cone(r0, r1, z0, z1):
    return Part.makeCone(r0, r1, z1 - z0, V(0, 0, z0), V(0, 0, 1))


def build_puck():
    s = cyl(PUCK_D / 2, 0, TOP)
    for i in range(FLUTES):
        a = 2 * math.pi * i / FLUTES
        c = PUCK_D / 2 + FLUTE_R - FLUTE_DEPTH
        s = s.cut(cyl(FLUTE_R, -1, TOP + 1, c * math.cos(a), c * math.sin(a)))
    pocket = cyl(POCKET_D / 2, BASE, TOP + 1).fuse(cone(POCKET_D / 2, POCKET_D / 2 + MOUTH_CH, TOP - MOUTH_CH, TOP))
    s = s.cut(pocket)
    pin = cyl(PIN_D / 2, BASE - 0.5, TOP - PIN_BELOW - PIN_CH).fuse(cone(PIN_D / 2, PIN_D / 2 - PIN_CH, TOP - PIN_BELOW - PIN_CH, TOP - PIN_BELOW))
    s = s.fuse(pin)
    rm = (TUBE_OD + TUBE_ID) / 4
    for sx in (1, -1):
        s = s.cut(cyl(EJECT_D / 2, -1, TOP + 1, sx * rm, 0))
    return s.removeSplitter()


def build_gauge():
    w = 3 * G_M + SLOT_GO + SLOT_NOGO
    h = SLOT_W + 2 * G_M
    p = Part.makeBox(w, h, G_T)
    p = p.makeFillet(G_R, [e for e in p.Edges if abs(e.tangentAt(e.FirstParameter).z) > 0.99])
    p.translate(V(70.0, -h / 2, 0))
    for x0, ln in ((G_M, SLOT_GO), (2 * G_M + SLOT_GO, SLOT_NOGO)):
        p = p.cut(Part.makeBox(ln, SLOT_W, G_T + 2, V(70.0 + x0, -SLOT_W / 2, -1)))
    return p.removeSplitter()


def probe(s, x, y, z):
    return s.isInside(V(x, y, z), 1e-6, True)


def verify(P):
    puck, gauge = P["Puck"], P["GoGauge"]
    rep = {}
    rm = (TUBE_OD + TUBE_ID) / 4
    floor = [f for f in puck.Faces if isinstance(f.Surface, Part.Plane) and abs(f.BoundBox.ZMin - BASE) < 1e-6 and abs(f.BoundBox.ZMax - BASE) < 1e-6]
    rep["pocket_depth"] = TOP - floor[0].BoundBox.ZMin
    rep["top_z"] = puck.BoundBox.ZMax
    rep["pin_below_top"] = TOP - max(v.Point.z for e in puck.Edges for v in e.Vertexes if math.hypot(v.Point.x, v.Point.y) < PIN_D / 2 + 1e-6 and v.Point.z < TOP - 1e-6)
    r_out = PUCK_D / 2 - FLUTE_DEPTH
    rep["guide_width"] = r_out - (POCKET_D / 2 + MOUTH_CH)
    rep["rad_od"] = (POCKET_D - TUBE_OD) / 2
    rep["rad_id"] = (TUBE_ID - PIN_D) / 2
    rep["ring_wall"] = r_out - POCKET_D / 2
    rep["pin_solid_ring_empty"] = [probe(puck, 0, 0, BASE + 1), probe(puck, 0, 0, TOP - 1), not probe(puck, rm, 0, BASE + 1), not probe(puck, 0, 0, TOP - 0.1)]
    ann = cyl(TUBE_OD / 2, BASE, TOP).cut(cyl(TUBE_ID / 2, BASE - 1, TOP + 1))
    rep["rod_overlap"], rep["rod_ann_mm2"] = [], []
    for sx in (1, -1):
        rod = cyl(1.5, -8.0, TOP, sx * rm, 0)
        rep["rod_overlap"].append(round(rod.common(puck).Volume, 6))
        rep["rod_ann_mm2"].append(round(rod.common(ann).Volume / CUT_L, 2))
    af = Part.Face(Part.Wire(Part.makeCircle(TUBE_OD / 2, V(0, 0, BASE)))).cut(Part.Face(Part.Wire(Part.makeCircle(TUBE_ID / 2, V(0, 0, BASE)))))
    rep["ring_floor_under_tube"] = round(sum(af.common(f).Area for f in puck.Faces if isinstance(f.Surface, Part.Plane) and abs(f.BoundBox.ZMin - BASE) < 1e-6 and f.BoundBox.ZLength < 1e-6), 2)
    rep["pin_web"] = 2 * (rm - EJECT_D / 2)
    rep["notch_out"] = rm + EJECT_D / 2 - (POCKET_D / 2 + MOUTH_CH)
    rep["guide_beyond_notch"] = PUCK_D / 2 - FLUTE_DEPTH - (rm + EJECT_D / 2)
    rep["valid"] = {n: (s.isValid(), len(s.Solids)) for n, s in P.items()}
    rep["vol"] = {n: round(s.Volume, 1) for n, s in P.items()}
    rep["size"] = {n: tuple(round(v, 2) for v in (s.BoundBox.XLength, s.BoundBox.YLength, s.BoundBox.ZLength)) for n, s in P.items()}
    rep["gauge_slots"] = [(probe(gauge, 70 + G_M + SLOT_GO / 2, 0, 1.5), probe(gauge, 70 + 2 * G_M + SLOT_GO + SLOT_NOGO / 2, 0, 1.5))]
    rep["print"] = {n: print_check(s, "+Z") for n, s in P.items()}
    return rep


def check(rep):
    assert abs(rep["pocket_depth"] - CUT_L) < 0.01, rep["pocket_depth"]
    assert abs(rep["top_z"] - (BASE + CUT_L)) < 1e-6
    assert rep["pin_below_top"] >= PIN_BELOW - 1e-6 and rep["pin_below_top"] <= PIN_BELOW + PIN_CH + 1e-6, rep["pin_below_top"]
    assert PIN_D / 2 < TUBE_ID / 2 and PIN_D < POCKET_D
    assert 0.25 <= rep["rad_od"] <= 0.4 and 0.25 <= rep["rad_id"] <= 0.4 and rep["ring_floor_under_tube"] >= 15.0, rep
    assert rep["guide_width"] >= 12.0 and rep["ring_wall"] >= 1.2, rep
    assert POCKET_D / 2 - PIN_D / 2 - 1.0 >= 0.4 and MOUTH_CH <= 0.5
    assert 1.2 <= TOP - BASE and BASE >= 1.2 and abs(TOP - BASE - CUT_L) < 1e-9
    assert all(v < 1e-6 for v in rep["rod_overlap"]) and all(v >= 2.5 for v in rep["rod_ann_mm2"]) and rep["pin_web"] >= 1.2 and rep["guide_beyond_notch"] >= 12.0 and rep["pin_solid_ring_empty"] == [True] * 4, rep
    assert all(v == (True, 1) for v in rep["valid"].values()), rep["valid"]
    assert rep["gauge_slots"] == [(False, False)], rep["gauge_slots"]
    assert abs((SLOT_GO - 8.0) - 0.3) < 1e-9 and SLOT_NOGO < CUT_L - 0.2 and SLOT_W >= TUBE_OD + 0.5
    for n, r in rep["print"].items():
        assert not r["p1"] and not r["p2"] and not r["p5"], (n, r)
        assert r["floor"] >= 60.0 and r["thin_mm2"] < 0.5, (n, r)


def main():
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    P = {"Puck": build_puck(), "GoGauge": build_gauge()}
    rep = verify(P)
    print("report", rep, flush=True)
    check(rep)
    for n, s in P.items():
        o = doc.addObject("Part::Feature", n)
        o.Shape = s
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
