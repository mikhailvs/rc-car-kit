# Wheel mount kit: a compact C yoke (Mount_R, Mount_L) glued under the cardboard floor, a Knuckle turning on one M3x40 kingpin ahead of the axle, a Stub (journal, WheelHub hex, inboard PORT) and WheelHub.
# Hangs under the floor: shaft axis 29 mm below the pad's glue face. The knuckle's rearward arm has three tie-rod holes.
# Wheel modes: free steer (kingpin only), locked (M3x10 from below through the bottom ear into the knuckle), powered (a JointYoke on the stub port drives it through a universal joint, still steerable).
# The yoke is relieved where the joint envelope sweeps, so the powered wheel steers about 30 degrees each way.
# Hardware per wheel: 1 M3x40 kingpin, optional 1 M3x10 lock, 1 M3x16 hub screw. Prints: Mount on its outboard face, Knuckle on its x face, Stub on its flat, Hub flange down.
# WHEEL_D is a stand-in for the wheel; retune PAD_Y0 and PAD_Y1 if it changes.
import FreeCAD as App, Part, math

D = {"NO_RUN": True, "__name__": "differential"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/differential.py").read(), "differential.py", "exec"), D)
V, O, cyl, box, hexprism, rot, vcyl = (D[k] for k in ("V", "O", "cyl", "box", "hexprism", "rot", "vcyl"))
build_wheel_hub, SHAFT_AF = D["build_wheel_hub"], D["SHAFT_AF"]

DOC_NAME = "WheelMount"
OUT = "/home/mikhail/Documents/cad/RC Car/WheelMount.FCStd"
X, Y, Z = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
OLD_MOUNT_VOL = 34569.3

AXIS_DEPTH, KY, LOCK_Y = 29.0, 8.0, -1.5
KN_HALF, KN_Y0, KN_Y1, KN_Z, KN_R = 7.0, -8.5, 13.0, 12.0, 4.0
AXLE_BORE, KING_BORE, PILOT, PILOT_DEEP = 9.9, 3.4, 2.8, 5.5
ARM_Z, ARM_END, ARM_HOLE, ARM_HOLES, ARM_R = 2.5, -30.0, 3.2, (20.0, 27.0, 34.0), 3.0

FL_D, FL_X0, FL_X1, JOURNAL_D, PORT_L, PORT_PILOT, SH_HOLE_D = 12.0, -9.2, -7.0, 9.3, 16.0, 5.9, 2.8
HUB_X0 = 7.5
HUB_DX = HUB_X0 - D["WH_X0"]
HUB_X1 = D["WH_X1"] + HUB_DX
HEX_END = HUB_X1 + 0.5
SH_HOLE_X = D["SHAFT_HOLE_X"] + HUB_DX
PORT_X0 = FL_X0 - PORT_L

CLR, EAR_T = 0.3, 5.0
EAR_Z0 = KN_Z + CLR
EAR_Z1 = EAR_Z0 + EAR_T
REAR_Y, WEB_Y0, WEB_Y1 = -7.5, 18.0, 22.5
PAD_Z0, PAD_Z1, PAD_X0, PAD_Y0, PAD_Y1 = AXIS_DEPTH - 4.0, AXIS_DEPTH, -33.0, -20.0, 28.0
GLUE_D = 5.0
GLUES = [(x, y) for x in (-28.0, -17.0) for y in (-14.0, 4.0, 22.0)] + [(0.0, -14.0)]
KING_LEN, KING_TOP, LOCK_LEN, PIN_R = 40.0, 24.0, 10.0, 1.3
KING_TIP, LOCK_TIP = -EAR_Z1 + KING_LEN, -EAR_Z1 + LOCK_LEN
WHEEL_D, WHEEL_T, STEER_MAX = 100.0, 10.0, 32.0

ENV_R, ENV_CENTRE, ENV_CONE_L, ENV_DEG, ENV_CLR = 12.5, PORT_X0 - 8.0, 40.0, 30.0, 1.0
RELIEF_DEG, RELIEF_CLR = 30.0, 1.3

PRINT_UP = dict(Mount_R="-X", Mount_L="+X", Knuckle="+X", Stub="+Z", WheelHub="-X")
MOUNT_L_DX = 90.0
COLORS = dict(Mount_R=(0.5, 0.5, 0.55), Mount_L=(0.5, 0.5, 0.55), Knuckle=(0.2, 0.5, 0.9), Stub=(0.7, 0.3, 0.8), WheelHub=(0.9, 0.4, 0.6))


def prism(pts, fillets, to3, ext):
    p = [to3(*q) for q in pts]
    sh = Part.Face(Part.makePolygon(p + p[:1])).extrude(ext)
    for r, corners in fillets:
        for c in corners:
            mid = to3(*c) + ext * 0.5
            sh = sh.makeFillet(r, [e for e in sh.Edges if (e.CenterOfMass - mid).Length < 1e-6])
    return sh


def build_knuckle():
    pts = [(KN_Y0, KN_Z), (KN_Y1, KN_Z), (KN_Y1, -KN_Z), (KN_Y0, -KN_Z), (KN_Y0, -ARM_Z), (ARM_END, -ARM_Z), (ARM_END, ARM_Z), (KN_Y0, ARM_Z)]
    fil = [(KN_R, [(KN_Y1, KN_Z), (KN_Y1, -KN_Z), (KN_Y0, KN_Z), (KN_Y0, -KN_Z)]), (ARM_R, [(KN_Y0, ARM_Z), (KN_Y0, -ARM_Z)]),
           (ARM_Z - 0.01, [(ARM_END, ARM_Z), (ARM_END, -ARM_Z)])]
    k = prism(pts, fil, lambda y, z: V(-KN_HALF, y, z), V(2 * KN_HALF, 0, 0))
    k = k.cut(cyl(AXLE_BORE / 2, -KN_HALF - 1, KN_HALF + 1)).cut(vcyl(KING_BORE / 2, 0, KY, -KN_Z - 1, KN_Z + 1))
    for z0, z1 in ((KN_Z - PILOT_DEEP, KN_Z + 1), (-KN_Z - 1, -KN_Z + PILOT_DEEP)):
        k = k.cut(vcyl(PILOT / 2, 0, LOCK_Y, z0, z1))
    for h in ARM_HOLES:
        k = k.cut(vcyl(ARM_HOLE / 2, 0, KY - h, -2 * ARM_Z, 2 * ARM_Z))
    return k.removeSplitter()


def build_stub():
    s = hexprism(SHAFT_AF, PORT_X0, HEX_END).fuse(cyl(FL_D / 2, FL_X0, FL_X1)).fuse(cyl(JOURNAL_D / 2, FL_X1, KN_HALF))
    s = s.cut(box(-40, 40, -10, 10, -10, -SHAFT_AF / 2))
    for x in (PORT_X0 + PORT_PILOT, SH_HOLE_X):
        s = s.cut(vcyl(SH_HOLE_D / 2, x, 0, -10, 10))
    return s.removeSplitter()


def build_hub():
    h = build_wheel_hub()
    h.translate(V(HUB_DX, 0, 0))
    return h


def envelope(grow=0.0):
    c = cyl(ENV_R + grow, PORT_X0 - grow, FL_X0 + grow)
    h = ENV_CONE_L + 2 * grow
    cone = Part.makeCone(0, h * math.tan(math.radians(ENV_DEG)), h, V(ENV_CENTRE + 2 * grow, 0, 0), -X)
    return c, cone


def rk(s, deg):
    s = s.copy()
    s.rotate(V(0, KY, 0), Z, deg)
    return s


def relief():
    c = envelope(RELIEF_CLR)[0]
    win = box(-KN_HALF - 1, KN_HALF + 1, REAR_Y - 1, WEB_Y1 + 1, -EAR_Z1 - 1, PAD_Z1)
    steps = int(RELIEF_DEG)
    cs = [rk(c, a).common(win) for a in range(-steps, steps + 1)]
    return cs[0].fuse(cs[1:])


def build_mount():
    pts = [(REAR_Y, PAD_Z1), (WEB_Y1, PAD_Z1), (WEB_Y1, -EAR_Z1), (REAR_Y, -EAR_Z1), (REAR_Y, -EAR_Z0), (WEB_Y0, -EAR_Z0), (WEB_Y0, EAR_Z0),
           (REAR_Y, EAR_Z0)]
    fil = [(5.0, [(WEB_Y1, -EAR_Z1), (WEB_Y0, -EAR_Z0), (WEB_Y0, EAR_Z0)]), (EAR_T / 2 - 0.01, [(REAR_Y, -EAR_Z1), (REAR_Y, -EAR_Z0)]),
           (3.0, [(REAR_Y, EAR_Z0)])]
    m = prism(pts, fil, lambda y, z: V(-KN_HALF, y, z), V(2 * KN_HALF, 0, 0))
    pr = (PAD_Z1 - PAD_Z0) / 2 - 0.01
    pad_pts = [(PAD_Y0, PAD_Z0), (PAD_Y1, PAD_Z0), (PAD_Y1, PAD_Z1), (PAD_Y0, PAD_Z1)]
    m = m.fuse(prism(pad_pts, [(pr, pad_pts)], lambda y, z: V(PAD_X0, y, z), V(KN_HALF - PAD_X0, 0, 0)))
    m = m.cut(vcyl(KING_BORE / 2, 0, KY, -EAR_Z1 - 1, -EAR_Z0 + 1)).cut(vcyl(PILOT / 2, 0, KY, EAR_Z0 - 1, KING_TOP))
    m = m.cut(vcyl(KING_BORE / 2, 0, LOCK_Y, -EAR_Z1 - 1, -EAR_Z0 + 1))
    for x, y in GLUES:
        m = m.cut(vcyl(GLUE_D / 2, x, y, PAD_Z0 - 1, PAD_Z1 + 1))
    return m.cut(relief()).removeSplitter()


def vol(a, b):
    return a.common(b).Volume


def pose(P, left):
    f = (lambda s: rot(s, Y, 180)) if left else (lambda s: s)
    return {"Mount": P["Mount_L" if left else "Mount_R"], **{n: f(P[n]) for n in ("Knuckle", "Stub", "WheelHub", "Disc", "Cyl", "Cone", "CylN", "ConeN")}}


def first_contact(fixed, moving, sign, top=90.0):
    hit = lambda a: [(f, n) for f in fixed for n, s in moving(sign * a).items() if vol(fixed[f], s) > 1e-3]
    a = 0.0
    while a < top and not hit(a):
        a += 2.0
    if a >= top:
        return top, []
    lo, hi = a - 2.0, a
    for _ in range(6):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if hit(mid) else (mid, hi)
    return round(hi, 2), hit(hi)


def ranges(ps, names):
    return tuple(first_contact(dict(Mount=ps["Mount"]), lambda a: {n: rk(ps[n], a) for n in names}, s) for s in (1, -1))


def overlaps(ps):
    ns = ["Mount", "Knuckle", "Stub", "WheelHub"]
    return {(a, b): round(vol(ps[a], ps[b]), 4) for i, a in enumerate(ns) for b in ns[i + 1:] if vol(ps[a], ps[b]) > 1e-3}


def alignment(ps):
    pins = [(vcyl(PIN_R, 0, KY, -EAR_Z1 - 1, KING_TIP), "king"), (vcyl(PIN_R, 0, LOCK_Y, -EAR_Z1 - 1, LOCK_TIP), "lock")]
    return [(t, n, round(vol(pin, ps[n]), 4)) for pin, t in pins for n in ("Mount", "Knuckle") if vol(pin, ps[n]) > 1e-3]


def grip(s, y, z0, z1):
    zs = [z0 + 0.1 * i + 0.05 for i in range(int(round((z1 - z0) / 0.1)))]
    return round(0.1 * sum(s.isInside(V(1.6, y, z), 1e-6, True) for z in zs), 2)


def clearance(ps, lim):
    out = {}
    for n, key in (("cyl", "CylN"), ("cone", "ConeN")):
        out[n] = round(min(ps["Mount"].distToShape(rk(ps[key], a))[0] for a in range(-lim, lim + 1)), 3)
    return out


def print_check(s, up):
    ax = V(*[(1 if up[0] == "+" else -1) if a == up[1] else 0 for a in "XYZ"])
    s = s.copy()
    s.transformShape(App.Placement(V(), App.Rotation(ax, Z)).toMatrix())
    s.translate(V(0, 0, -s.optimalBoundingBox(False, False).ZMin))
    floor = sum(f.Area for f in s.Faces if f.BoundBox.ZMax < 1e-4 and isinstance(f.Surface, Part.Plane))
    worst, where = 0.0, None
    for f in s.Faces:
        if f.BoundBox.ZMax < 1.0:
            continue
        u0, u1, v0, v1 = f.ParameterRange
        for i in range(7):
            for j in range(7):
                u, v = u0 + (u1 - u0) * (i + 0.5) / 7, v0 + (v1 - v0) * (j + 0.5) / 7
                n, p = f.normalAt(u, v), f.valueAt(u, v)
                if isinstance(f.Surface, Part.Cylinder) and f.Surface.Radius < 3.6:
                    c, a = f.Surface.Center, f.Surface.Axis
                    if (p - c - a * (p - c).dot(a)).dot(n) < 0:
                        continue
                if -n.z > worst:
                    worst, where = -n.z, (type(f.Surface).__name__, round(p.x, 1), round(p.y, 1), round(p.z, 1))
    return dict(floor=round(floor, 1), overhang_nz=round(worst, 3), at=where)


def verify(P):
    ps, pl = pose(P, False), pose(P, True)
    un, pw = ("Knuckle", "Stub", "WheelHub"), ("Knuckle", "Stub", "WheelHub", "Cyl", "Cone")
    mr = P["Mount_R"]
    rep = dict(overlap=overlaps(ps), overlap_left=overlaps(pl), align=alignment(ps), align_left=alignment(pl),
               range=ranges(ps, un), range_left=ranges(pl, un), powered=ranges(ps, pw), powered_left=ranges(pl, pw),
               disc=tuple(first_contact(dict(Mount=ps["Mount"]), lambda a: {"Disc": rk(ps["Disc"], a)}, s) for s in (1, -1)),
               disc_left=tuple(first_contact(dict(Mount=pl["Mount"]), lambda a: {"Disc": rk(pl["Disc"], a)}, s) for s in (1, -1)))
    rep["mirror"] = round(mr.mirror(O, X).cut(P["Mount_L"]).Volume + P["Mount_L"].cut(mr.mirror(O, X)).Volume, 4)
    rep["screws"] = dict(king_thread=grip(mr, KY, EAR_Z0, KING_TIP), king_pilot_top=round(KING_TOP - KING_TIP, 2),
                         lock_engage=grip(P["Knuckle"], LOCK_Y, -KN_Z, LOCK_TIP), lock_spare=round(-KN_Z + PILOT_DEEP - LOCK_TIP, 2))
    rep["clear_env"] = clearance(ps, 28)
    rep["clear_env_left"] = clearance(pl, 28)
    rep["axis_to_glue_face"] = round(mr.BoundBox.ZMax, 3)
    rep["vol"] = dict(new=round(mr.Volume, 1), old=OLD_MOUNT_VOL, ratio=round(mr.Volume / OLD_MOUNT_VOL, 3))
    b = mr.BoundBox
    rep["bbox"] = tuple(round(v, 2) for v in (b.XMin, b.XMax, b.YMin, b.YMax, b.ZMin, b.ZMax)), (round(b.XLength, 1), round(b.YLength, 1), round(b.ZLength, 1))
    rep["glue_edge"] = round(min(min(x - PAD_X0, KN_HALF - x, y - PAD_Y0, PAD_Y1 - y) - GLUE_D / 2 for x, y in GLUES), 2)
    rep["print"] = {n: print_check(P[n], PRINT_UP[n]) for n in PRINT_UP}
    return rep


def check(rep):
    assert not rep["overlap"] and not rep["overlap_left"], rep
    assert not rep["align"] and not rep["align_left"], rep
    for k in ("range", "range_left"):
        assert min(r[0] for r in rep[k]) >= 35.0, rep[k]
    for k in ("powered", "powered_left"):
        assert min(r[0] for r in rep[k]) >= 28.0, rep[k]
    assert min(r[0] for k in ("disc", "disc_left") for r in rep[k]) >= STEER_MAX, (rep["disc"], rep["disc_left"])
    assert rep["mirror"] < 1e-3, rep["mirror"]
    s = rep["screws"]
    assert s["king_thread"] >= 8.0 and s["king_pilot_top"] >= 0 and s["lock_engage"] >= 4.0 and s["lock_spare"] >= 0, s
    assert min(min(rep[k].values()) for k in ("clear_env", "clear_env_left")) >= 1.0, rep["clear_env"]
    assert abs(rep["axis_to_glue_face"] - AXIS_DEPTH) < 1e-6 and rep["glue_edge"] >= 1.5, rep
    assert rep["vol"]["ratio"] <= 0.6, rep["vol"]
    assert all(p["floor"] >= 5.0 and p["overhang_nz"] <= 0.7072 for p in rep["print"].values()), rep["print"]
    assert KY - KING_BORE / 2 - AXLE_BORE / 2 >= 1.2 and LOCK_Y - PILOT / 2 + KN_Z - PILOT_DEEP >= 0


def build_parts():
    P = dict(Mount_R=build_mount(), Knuckle=build_knuckle(), Stub=build_stub(), WheelHub=build_hub())
    P["Mount_L"] = P["Mount_R"].mirror(O, X)
    P["Disc"] = cyl(WHEEL_D / 2, HUB_X1, HUB_X1 + WHEEL_T)
    P["Cyl"], P["Cone"] = envelope(ENV_CLR)
    P["CylN"], P["ConeN"] = envelope()
    return P


def main():
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    P = build_parts()
    for n in PRINT_UP:
        assert P[n].isValid() and len(P[n].Solids) == 1, n
        o = doc.addObject("Part::Feature", n)
        o.Shape = P[n]
        if n == "Mount_L":
            o.Placement = App.Placement(V(MOUNT_L_DX, 0, 0), App.Rotation())
        if App.GuiUp:
            o.ViewObject.ShapeColor = COLORS[n]
    rep = verify(P)
    print("report", rep)
    check(rep)
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
