# Wheel mount 2: a kingpin POST design. Mount = flat glue pad (glued under the cardboard floor) with one fat round post pointing down; Knuckle = one compact barrel that pushes UP onto the post (blind socket above, axle bore below); Stub (journal, hex, inboard PORT, flange) and WheelHub.
# Unlike wheel_mount.py (C yoke, trapped knuckle squeezed in sideways, one long M3x40 kingpin in plastic) nothing is trapped and nothing is squeezed: the knuckle slides straight up onto the post, two M3 shanks lying in a groove on the post keep it there, steering is free on a 0.3 radial fit, the weight rides on a small thrust boss.
# Modes: FREE STEER (two retention screws), LOCKED (a third M3 through a knuckle lug into a notch in the post at straight ahead, fit 0.1 per side, +-1.8 degrees of toe play, about +-1.6 mm at the rim), POWERED (a JointYoke on the stub port, drive_shaft.py swing envelope, still steerable). The fits are sloppy by design (0.3 radial on the post, hex and journal fits, 0.4 end float): expect a few degrees of camber and toe slop. Future suspension: the pad is the only chassis interface, a swing arm carrying the same post can replace it.
# Hardware per wheel: 1 M3x16 clamp screw (post from the glue face, 11 mm thread), 2 M3x25 retention screws (one per lug, 6.2 mm thread each, tips stand about 2.4 mm out of the lug), optional 1 M3x25 lock screw (6.2 mm thread, front lug), 1 M3x16 hub cross screw. Mount, Knuckle, Stub, WheelHub are the only prints, ONE Mount and ONE Knuckle serve all four wheels (Knuckle outline is x symmetric, arm rearward on both sides, but its screw holes are not: clearance on -x, pilot on +x, so on a mirrored side a screw self-taps the pilot first and then the far side; Mount is y symmetric, so turn it 180 degrees about the post for the other side).
# Assembly: 1 clamp screw into the Mount from the glue face, then glue the Mount under the floor; 2 Stub through the Knuckle from the inboard side; 3 WheelHub onto the stub hex, cross screw from above; 4 push the Knuckle (with stub and hub) straight up onto the post; 5 both retention screws from the inboard side (shanks sit in the post groove); 6 optional lock screw likewise. Pull the retention screws to take the knuckle off again with the mount glued in place.
# Sizes: Mount 40 x 33 x 20.9 mm (pad 2.6 thick, a deliberate volume tradeoff for the 12 cm3 budget, 10.2 cm2 glue face, post dia 14), Knuckle 22.6 x 50 x 28 mm, 11.85 cm3 together (old mount 15.7 cm3). Vertical play 0.45 (0.3 up on the boss, 0.15 down on the groove flank), 0.4 end float on the stub. Groove bending margin 1.6 (root 2.0), retention lip bearing 10 MPa per screw.
# Steering: 60 degrees each way free (swept limit, measured against the Mount, wheel clears the pad by 8.9 mm); powered limited by the universal joint to about 36 degrees (drive_shaft.py), not by the mount. The FLOOR needs a wheel arch: with 2 mm clearance its edge must sit at or inboard of x 0.5 from the post axis for 30 degrees, -12 for 45, -24 for 60 (the pad's outboard edge is x 11).
# Prints: Mount glue face down (post up), Knuckle flat on its bottom (socket up, arm on the bed), Stub on its flat, WheelHub flange down. The hub hex socket (8.2 on 8.0 AF) is the kit standard from differential.py. Steering ranges, volumes, clearances and stresses are printed in the report and asserted in check().
import FreeCAD as App, Part, math

D = {"NO_RUN": True, "__name__": "differential"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/differential.py").read(), "differential.py", "exec"), D)
V, O, cyl, box, hexprism, rot, vcyl = (D[k] for k in ("V", "O", "cyl", "box", "hexprism", "rot", "vcyl"))
SHAFT_AF, WH_FD, WH_FT, WH_BD, WH_SOCKET, WH_GLUE_D, WH_GLUE_R, WH_SCREW_NEAR, WH_SCREW_FAR = (D[k] for k in (
    "SHAFT_AF", "WH_FD", "WH_FT", "WH_BD", "WH_SOCKET", "WH_GLUE_D", "WH_GLUE_R", "WH_SCREW_NEAR", "WH_SCREW_FAR"))
S = {"NO_RUN": True, "__name__": "drive_shaft"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/drive_shaft.py").read(), "drive_shaft.py", "exec"), S)
build_yoke, TIP_J = S["build_yoke"], S["TIP_J"]

DOC_NAME = "WheelMount2"
OUT = "/home/mikhail/Documents/cad/RC Car/WheelMount2.FCStd"
X, Y, Z = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
OLD_MOUNT_VOL = 15700.0

AXIS_DEPTH, PAD_T, PAD_X0, PAD_X1, PAD_Y, PAD_R = 29.0, 2.6, -29.0, 11.0, 16.5, 6.0
PAD_Z0, PAD_Z1 = AXIS_DEPTH - PAD_T, AXIS_DEPTH
POST_R, GROOVE_R, FIL_R, POST_CH = 7.0, 6.2, 3.0, 0.8
FIL_Z0 = PAD_Z0 - FIL_R
SOCK_R, R_V, R_B, BORE_R = 7.3, 9.85, 9.3, 4.95
Z_FLOOR, BOSS_R, BOSS_H, BOSS_GAP = 7.0, 3.5, 0.8, 0.3
POST_END = Z_FLOOR + BOSS_H + BOSS_GAP
Z_C, RET_DOWN, UP_GAP = 10.5, 0.15, 0.5
RET_Y, LOCK_Y, LOCK_Z, LUG_R, NOTCH_R, RELIEF_R, WALL_MIN = 8.05, 7.8, 17.5, 3.2, 1.6, 1.85, 1.2
SCREW_D, CORE_D, HEAD_D, HEAD_H, SCREW_L, RET_L, LOCK_L = 3.0, 2.6, 5.5, 3.0, 16.0, 25.0, 25.0
CLAMP_CB_D, CLAMP_CLR, CLAMP_PILOT = 6.0, 3.6, 2.8
CB_DEPTH = HEAD_H + 0.2
CB_Z = PAD_Z1 - CB_DEPTH
CLAMP_TIP = CB_Z - SCREW_L
CLAMP_CLR_Z = CB_Z - 5.0
K_TOP, K_BOT, KN_HALF, COL_X0, COL_UP = 21.0, -6.95, 11.3, 8.0, 7.0
LUG_X = KN_HALF
SOCK_CH, OUT_CH, LUG_FIL, ARM_FIL = 0.5, 0.2, 0.8, 1.5
ARM_T, ARM_HOLES, ARM_HOLE, ARM_END_R = 3.0, (20.0, 27.0, 34.0), 3.6, 4.5
GLUE_D = 5.0
GLUES = [(-18.0, 10.0), (-18.0, -10.0), (-6.0, 12.5), (-6.0, -12.5)]
GROOVE_W, GROOVE_D = 1.2, 0.6

FL_D, FL_T, JOURNAL_D, PORT_L, PORT_PILOT, SH_HOLE_D = 13.0, 2.2, 9.3, 16.0, 5.9, 2.8
G_IN, G_OUT = 0.2, 0.2
FL_X1 = -KN_HALF - G_IN
FL_X0 = FL_X1 - FL_T
PORT_X0 = FL_X0 - PORT_L
HUB_X0 = KN_HALF + G_OUT
HUB_X1 = HUB_X0 + 15.0
HEX_END = HUB_X1 - 0.2
SH_X = HUB_X0 + 7.0
WHEEL_D, WHEEL_T = 100.0, 10.0
FLOOR_T, FLOOR_X0, FLOOR_X1 = 4.0, -90.0, 12.0
ENV_R, ENV_CENTRE, ENV_CONE_L, ENV_DEG = 12.5, PORT_X0 - 8.0, 40.0, 30.0
JOINT_MAX_DEG = 36.0

TAN = SCREW_D / 2 * math.sqrt(2) - (RET_Y - GROOVE_R)
Z_S = Z_C + RET_DOWN + TAN
Z_U = Z_S + TAN + UP_GAP
RET_Y_IN = RET_Y - SCREW_D / 2
XR0 = math.sqrt(SOCK_R ** 2 - (min(RET_Y, LOCK_Y) - 1.4 - WALL_MIN) ** 2)
LOAD_V, LOAD_S, ALLOW_BEND, ALLOW_BEARING = 15.0, 15.0, 12.0, 12.0
TOP_ANGLE, STEP = 60, 2

PRINT_UP = dict(Mount="-Z", Knuckle="+Z", Stub="+Z", WheelHub="-X")
COLORS = dict(Mount=(0.5, 0.5, 0.55), Knuckle=(0.2, 0.5, 0.9), Stub=(0.7, 0.3, 0.8), WheelHub=(0.9, 0.4, 0.6))


def revz(pts):
    p = [V(r, 0, z) for r, z in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).revolve(O, Z, 360)


def revx(pts):
    p = [V(x, r, 0) for x, r in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).revolve(O, X, 360)


def zedges(s, z):
    return [e for e in s.Edges if abs(e.BoundBox.ZMin - z) < 1e-6 and abs(e.BoundBox.ZMax - z) < 1e-6]


def build_mount():
    pts = [(0, POST_END), (POST_R - POST_CH, POST_END), (POST_R, POST_END + POST_CH), (POST_R, Z_C - (POST_R - GROOVE_R)), (GROOVE_R, Z_C), (GROOVE_R, Z_U),
           (POST_R, Z_U + POST_R - GROOVE_R), (POST_R, FIL_Z0)]
    pv = [V(r, 0, z) for r, z in pts]
    ed = [Part.makeLine(a, b) for a, b in zip(pv, pv[1:])]
    c = (POST_R + FIL_R, FIL_Z0)
    mid = V(c[0] - FIL_R * math.cos(math.pi / 4), 0, c[1] + FIL_R * math.sin(math.pi / 4))
    top = [V(POST_R + FIL_R, 0, PAD_Z0), V(POST_R + FIL_R, 0, PAD_Z0 + 1), V(0, 0, PAD_Z0 + 1), pv[0]]
    ed.append(Part.Arc(pv[-1], mid, top[0]).toShape())
    ed += [Part.makeLine(a, b) for a, b in zip(top, top[1:])]
    post = Part.Face(Part.Wire(ed)).revolve(O, Z, 360)
    pad = box(PAD_X0, PAD_X1, -PAD_Y, PAD_Y, PAD_Z0, PAD_Z1)
    pad = pad.makeFillet(PAD_R, [e for e in pad.Edges if abs(e.Vertexes[0].Z - e.Vertexes[1].Z) > 1e-6])
    pad = pad.makeChamfer(0.8, zedges(pad, PAD_Z0))
    pad = pad.makeChamfer(0.6, zedges(pad, PAD_Z1))
    m = pad.fuse(post)
    m = m.cut(vcyl(CLAMP_CB_D / 2, 0, 0, CB_Z, PAD_Z1 + 1)).cut(vcyl(CLAMP_CLR / 2, 0, 0, CLAMP_CLR_Z, CB_Z + 0.1))
    m = m.cut(vcyl(CLAMP_PILOT / 2, 0, 0, CLAMP_TIP - 0.4, CLAMP_CLR_Z + 0.1))
    for s in (1, -1):
        m = m.cut(Part.makeCylinder(NOTCH_R, 20, V(-10, s * LOCK_Y, LOCK_Z), X))
    for x, y in GLUES:
        m = m.cut(vcyl(GLUE_D / 2, x, y, PAD_Z0 - 1, PAD_Z1 + 1))
    for s in (1, -1):
        m = m.cut(box(-27.0, -6.0, s * 5.0 - GROOVE_W / 2, s * 5.0 + GROOVE_W / 2, PAD_Z1 - GROOVE_D, PAD_Z1 + 1))
    m = m.cut(box(-12.0 - GROOVE_W / 2, -12.0 + GROOVE_W / 2, -13.0, 13.0, PAD_Z1 - GROOVE_D, PAD_Z1 + 1))
    return m.removeSplitter()


def xcyl(r, y, z, x0=-LUG_X, x1=LUG_X):
    return Part.makeCylinder(r, x1 - x0, V(x0, y, z), X)


def lug(s):
    r, q = LUG_R, LUG_R * math.sin(math.pi / 4)
    tp = [V(-LUG_X, s * (RET_Y + dy), Z_S + dz) for dy, dz in ((-q, -q), (0, -2 * q), (q, -q), (0, 0))]
    tear = Part.Face(Part.makePolygon(tp + tp[:1])).extrude(V(2 * LUG_X, 0, 0))
    y0, y1 = sorted((s * (max(RET_Y, LOCK_Y) - LUG_R), s * (min(RET_Y, LOCK_Y) + LUG_R)))
    l = tear.fuse(xcyl(r, s * RET_Y, Z_S)).fuse(box(-LUG_X, LUG_X, y0, y1, Z_S, LOCK_Z)).fuse(xcyl(r, s * LOCK_Y, LOCK_Z))
    l = l.common(box(-LUG_X, LUG_X, -20, 20, -20, K_TOP)).removeSplitter()
    l = l.makeChamfer(LUG_FIL, [e for e in l.Edges if abs(abs(e.BoundBox.XMin) - LUG_X) < 1e-6 and abs(abs(e.BoundBox.XMax) - LUG_X) < 1e-6])
    return l.cut(box(-XR0, XR0, -20, 20, -20, K_TOP + 1))


def build_arm():
    pts = [V(-5.0, -5.0, K_BOT), V(5.0, -5.0, K_BOT), V(ARM_END_R, -ARM_HOLES[-1], K_BOT), V(-ARM_END_R, -ARM_HOLES[-1], K_BOT)]
    a = Part.Face(Part.makePolygon(pts + pts[:1])).extrude(V(0, 0, ARM_T))
    return a.fuse(Part.makeCylinder(ARM_END_R, ARM_T, V(0, -ARM_HOLES[-1], K_BOT)))


def build_knuckle(holes=True):
    k = revz([(0, K_BOT), (R_B - 1.0, K_BOT), (R_B, K_BOT + 1.0), (R_B, K_TOP - OUT_CH), (R_B - OUT_CH, K_TOP), (0, K_TOP)])
    col = revx([(COL_X0, 0), (COL_X0, R_V), (KN_HALF - 0.8, R_V), (KN_HALF, R_V - 0.8), (KN_HALF, 0)]).common(box(0, 20, -20, 20, -20, 0))
    col = col.fuse(revx([(COL_X0, 0), (COL_X0, COL_UP), (KN_HALF - 0.8, COL_UP), (KN_HALF, COL_UP - 0.8), (KN_HALF, 0)]))
    k = k.fuse(col).fuse(col.mirror(O, X)).fuse(build_arm())
    zt = K_BOT + ARM_T
    k = k.makeFillet(ARM_FIL, [e for e in k.Edges if abs(e.BoundBox.ZMin - e.BoundBox.ZMax) < 1e-6 and abs(e.BoundBox.ZMin - zt) < 1e-6 and e.BoundBox.YMax < -R_B * 0.5 and e.BoundBox.YMin > -R_B - 0.01])
    for s in (1, -1):
        k = k.fuse(lug(s))
    k = k.cut(box(-30, 30, -60, 30, K_BOT - 10, K_BOT))
    k = k.cut(revz([(0, Z_FLOOR), (SOCK_R, Z_FLOOR), (SOCK_R, K_TOP - SOCK_CH - 0.1), (SOCK_R + SOCK_CH, K_TOP), (SOCK_R + SOCK_CH, K_TOP + 1), (0, K_TOP + 1)]))
    k = k.cut(revx([(-KN_HALF - 1, 0), (-KN_HALF - 1, BORE_R + 1.8), (-KN_HALF, BORE_R + 0.8), (-KN_HALF + 0.8, BORE_R), (KN_HALF - 0.8, BORE_R),
                    (KN_HALF, BORE_R + 0.8), (KN_HALF + 1, BORE_R + 1.8), (KN_HALF + 1, 0)]))
    k = k.fuse(vcyl(BOSS_R, 0, 0, Z_FLOOR - 0.1, Z_FLOOR + BOSS_H))
    for h in ARM_HOLES:
        k = k.cut(vcyl(ARM_HOLE / 2, 0, -h, K_BOT - 1, K_BOT + ARM_T + 1))
    for s in (1, -1):
        for y, z in ((s * RET_Y, Z_S), (s * LOCK_Y, LOCK_Z)):
            xr = XR0
            k = k.cut(Part.makeCylinder(RELIEF_R, 2 * xr, V(-xr, y, z), X))
            if holes:
                k = k.cut(Part.makeCylinder(CLAMP_CLR / 2, LUG_X + 1 - xr, V(-LUG_X - 1, y, z), X)).cut(Part.makeCylinder(CLAMP_PILOT / 2, LUG_X + 1 - xr, V(xr, y, z), X))
    return k.removeSplitter()


def build_stub():
    s = hexprism(SHAFT_AF, PORT_X0, HEX_END).fuse(cyl(FL_D / 2, FL_X0, FL_X1)).fuse(cyl(JOURNAL_D / 2, FL_X1, KN_HALF))
    s = s.cut(box(-80, 80, -12, 12, -12, -SHAFT_AF / 2))
    for x in (PORT_X0 + PORT_PILOT, SH_X):
        s = s.cut(vcyl(SH_HOLE_D / 2, x, 0, -10, 10))
    return s.removeSplitter()


def build_hub():
    h = cyl(WH_FD / 2, HUB_X1 - WH_FT, HUB_X1).fuse(cyl(WH_BD / 2, HUB_X0, HUB_X1 - WH_FT))
    h = h.cut(hexprism(WH_SOCKET, HUB_X0 - 1, HUB_X1 + 1))
    h = h.cut(Part.makeCone(5.9, WH_SOCKET / math.sqrt(3), 1.2, V(HUB_X0 - 0.01, 0, 0), X))
    for k in range(6):
        a = math.radians(60 * k)
        h = h.cut(cyl(WH_GLUE_D / 2, HUB_X1 - WH_FT - 1, HUB_X1 + 1, WH_GLUE_R * math.cos(a), WH_GLUE_R * math.sin(a)))
    h = h.cut(Part.makeCylinder(WH_SCREW_NEAR / 2, 10, V(SH_X, 0, 0), Z))
    return h.cut(Part.makeCylinder(WH_SCREW_FAR / 2, 10, V(SH_X, 0, -10), Z)).removeSplitter()


def screw(p, d, length=SCREW_L, dia=SCREW_D):
    return Part.makeCylinder(dia / 2, length, p, d).fuse(Part.makeCylinder(HEAD_D / 2, HEAD_H, p - d * HEAD_H, d))


def build_yoke_on_port():
    y = build_yoke()
    y.translate(V(-S["AX"], 0, 0))
    y = rot(y, Z, 180)
    y.translate(V(PORT_X0 - TIP_J, 0, 0))
    return y


def envelope(grow=0.0):
    c = cyl(ENV_R + grow, PORT_X0 - grow, FL_X0 + grow)
    h = ENV_CONE_L + 2 * grow
    return c, Part.makeCone(0, h * math.tan(math.radians(ENV_DEG)), h, V(ENV_CENTRE + 2 * grow, 0, 0), -X)


def vol(a, b):
    return a.common(b).Volume if a.BoundBox.intersect(b.BoundBox) else 0.0


def moved(s, v, t):
    c = s.copy()
    c.translate(v * t)
    return c


def rk(s, deg):
    s = s.copy()
    s.rotate(O, Z, deg)
    return s


def sweep(mov, fixed, v, length=40.0, step=1.0):
    worst = 0.0
    for i in range(int(round(length / step)) + 1):
        for a in mov.values():
            m = moved(a, v, length - i * step)
            worst = max(worst, max(vol(m, b) for b in fixed.values()))
    return round(worst, 4)


def run_len(s, p, d, length, step=0.02):
    tot, started = 0.0, False
    for i in range(int(length / step)):
        if s.isInside(p + d * (i * step), 1e-7, True):
            tot, started = tot + step, True
        elif started:
            break
    return round(tot, 2)


def thread_len(s, p, d, perps, length):
    return round(0.1 * sum(all(s.isInside(p + d * (0.1 * i + 0.05) + q * (SCREW_D / 2 - 0.05), 1e-7, True) for q in perps) for i in range(int(length * 10))), 2)


def travel(s, fixed, v, hi=3.0):
    lo = 0.0
    if fixed.distToShape(moved(s, v, hi))[0] > 1e-6:
        return hi
    for _ in range(14):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if fixed.distToShape(moved(s, v, mid))[0] > 1e-6 else (lo, mid)
    return lo


def travel_rot(s, fixed, sg, hi=10.0):
    lo = 0.0
    if fixed.distToShape(rk(s, sg * hi))[0] > 1e-6:
        return hi
    for _ in range(14):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if fixed.distToShape(rk(s, sg * mid))[0] > 1e-6 else (lo, mid)
    return lo


def rad_wall(s, z):
    n = sum(s.isInside(V(SOCK_R - 0.05 + 0.005 * i, 0, z), 1e-7, True) for i in range(int((R_B - SOCK_R + 0.4) / 0.005)))
    return round(0.005 * n, 3)


def floor_arch(disc, deg, clr=2.0):
    d = rk(disc, deg)
    lo, hi = -80.0, FLOOR_X1
    if box(FLOOR_X0, hi, -70, 70, AXIS_DEPTH, AXIS_DEPTH + FLOOR_T).distToShape(d)[0] >= clr:
        return hi
    for _ in range(18):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if box(FLOOR_X0, mid, -70, 70, AXIS_DEPTH, AXIS_DEPTH + FLOOR_T).distToShape(d)[0] >= clr else (lo, mid)
    return round(lo, 1)


def driver(p, d):
    return Part.makeCylinder(3.0, 60.0, p, d)


def print_check(s, up):
    sign, axis = up
    u = V(*[(1 if sign == "+" else -1) if a == axis else 0 for a in "XYZ"])
    s = s.copy()
    s.transformShape(App.Placement(V(), App.Rotation(u, Z)).toMatrix())
    s.translate(V(0, 0, -s.optimalBoundingBox(False, False).ZMin))
    floor, bad = 0.0, []
    lim = -math.sin(math.radians(45.0))
    for f in s.Faces:
        if f.BoundBox.ZMax < 1e-4 and isinstance(f.Surface, Part.Plane):
            floor += f.Area
            continue
        pts, tris = f.tessellate(0.1)
        area = 0.0
        for i, j, k in tris:
            n = (pts[j] - pts[i]).cross(pts[k] - pts[i])
            if n.Length and n.z / n.Length < lim + 0.05:
                u2, v2 = f.Surface.parameter((pts[i] + pts[j] + pts[k]) * (1 / 3))
                if f.normalAt(u2, v2).z < lim - 1e-3:
                    area += n.Length / 2
        if area > 0.05:
            bb = f.optimalBoundingBox(False, False)
            bad.append((type(f.Surface).__name__, round(getattr(f.Surface, "Radius", 0.0), 2), round(area, 1), round(4 * f.Area / f.Length, 1)))
    return round(floor, 1), bad


def print_ok(bad):
    return all((k == "Cylinder" and r <= 5.05) or (k == "Plane" and span <= 10.0) for k, r, a, span in bad)


def strength():
    xt, zc = HUB_X1 + WHEEL_T / 2, -WHEEL_D / 2
    M = lambda z: LOAD_V * xt + LOAD_S * (z - zc)
    sec = lambda d: math.pi * d ** 3 / 32
    le = K_TOP - POST_END
    lever = le * 2 / 3
    fb = M((POST_END + K_TOP) / 2) / lever
    seg = lambda d, R: R * R * math.acos(d / R) - d * math.sqrt(R * R - d * d)
    area = seg(RET_Y_IN, POST_R)
    t_web = Z_FLOOR - BORE_R
    return dict(root_MPa=round(M(FIL_Z0) / sec(2 * POST_R), 2), groove_MPa=round(M(Z_U) / sec(2 * GROOVE_R), 2),
                root_margin=round(ALLOW_BEND / (M(FIL_Z0) / sec(2 * POST_R)), 2), groove_margin=round(ALLOW_BEND / (M(Z_U) / sec(2 * GROOVE_R)), 2),
                bearing_post_socket_MPa=round(fb / (2 * POST_R * le / 3), 2), retention_pull_N_per_screw=LOAD_V,
                retention_shank_shear_MPa=round(LOAD_V / (math.pi / 4 * 2.5 ** 2), 2), retention_plastic_bearing_MPa=round(LOAD_V / area, 2),
                boss_bearing_MPa=round((LOAD_V + LOAD_S) / (math.pi * BOSS_R ** 2), 2),
                web_shear_MPa=round((LOAD_V + LOAD_S) / (math.pi * 2 * BOSS_R * t_web), 2), allow_bend=ALLOW_BEND, allow_bearing=ALLOW_BEARING)


def build_parts():
    P = dict(Mount=build_mount(), Knuckle=build_knuckle(), Stub=build_stub(), WheelHub=build_hub())
    P["Ref_Floor"] = box(FLOOR_X0, FLOOR_X1, -70, 70, AXIS_DEPTH, AXIS_DEPTH + FLOOR_T)
    P["Ref_Disc"] = cyl(WHEEL_D / 2, HUB_X1, HUB_X1 + WHEEL_T)
    P["Ref_ClampScrew"] = screw(V(0, 0, CB_Z), -Z)
    P["Ref_RetScrew"] = screw(V(-LUG_X, -RET_Y, Z_S), X, RET_L)
    P["Ref_RetScrew2"] = screw(V(-LUG_X, RET_Y, Z_S), X, RET_L)
    P["Ref_LockScrew"] = screw(V(-LUG_X, LOCK_Y, LOCK_Z), X, LOCK_L)
    P["Ref_HubScrew"] = screw(V(SH_X, 0, WH_BD / 2), -Z)
    P["Ref_JointYoke"] = build_yoke_on_port()
    return P


def cores(P):
    return dict(clamp=screw(V(0, 0, CB_Z), -Z, dia=CORE_D), ret=screw(V(-LUG_X, -RET_Y, Z_S), X, RET_L, CORE_D), ret2=screw(V(-LUG_X, RET_Y, Z_S), X, RET_L, CORE_D),
                lock=screw(V(-LUG_X, LOCK_Y, LOCK_Z), X, LOCK_L, CORE_D), hub=screw(V(SH_X, 0, WH_BD / 2), -Z, dia=CORE_D))


def assembly(P):
    M, K, St, H, Dc, Fl, Yk = (P[n] for n in ("Mount", "Knuckle", "Stub", "WheelHub", "Ref_Disc", "Ref_Floor", "Ref_JointYoke"))
    C = cores(P)
    r = {}
    r["1_clamp_into_mount"] = sweep(dict(c=C["clamp"]), dict(M=M), Z)
    r["2_stub_through_knuckle"] = sweep(dict(s=St), dict(K=K), -X)
    r["3_hub_on_stub"] = sweep(dict(h=H), dict(s=St, K=K), X)
    r["3_hub_screw"] = sweep(dict(c=C["hub"]), dict(h=H, s=St, K=K, D=Dc, F=Fl, M=M), Z)
    r["4_knuckle_up_onto_post"] = sweep(dict(k=K, s=St, h=H, d=Dc, c=C["hub"]), dict(M=M, F=Fl, c=C["clamp"]), -Z)
    allfix = dict(M=M, K=K, s=St, h=H, d=Dc, F=Fl, y=Yk)
    r["5_retention_screws"] = sweep(dict(c=C["ret"], c2=C["ret2"]), allfix, -X)
    r["6_lock_screw"] = sweep(dict(c=C["lock"]), dict(allfix, r=C["ret"], r2=C["ret2"]), -X)
    drv = dict(ret=driver(V(-LUG_X - HEAD_H, -RET_Y, Z_S), -X), ret2=driver(V(-LUG_X - HEAD_H, RET_Y, Z_S), -X), lock=driver(V(-LUG_X - HEAD_H, LOCK_Y, LOCK_Z), -X), hub=driver(V(SH_X, 0, WH_BD / 2 + HEAD_H), Z))
    allc = dict(allfix, cl=C["clamp"], cr=C["ret"], cr2=C["ret2"], cll=C["lock"], ch=C["hub"])
    own = dict(ret="cr", ret2="cr2", lock="cll", hub="ch")
    r["drivers"] = {n: round(max(vol(d, b) for k, b in allc.items() if k != own[n]), 4) for n, d in drv.items()}
    r["final_core_overlaps"] = {n: round(max(vol(c, b) for b in allfix.values()), 4) for n, c in C.items()}
    return r


def steering(P):
    M = P["Mount"]
    Mup = M.common(box(-60, 60, -60, 60, FIL_Z0 - 0.05, 40))
    c, cone = envelope()
    items = {"Knuckle": (P["Knuckle"], 0.3, M), "KnuckleUpper": (P["Knuckle"], 0.8, Mup), "Stub": (P["Stub"], 0.8, M), "WheelHub": (P["WheelHub"], 0.8, M),
             "Disc": (P["Ref_Disc"], 2.0, M),
             "EnvCyl": (c, 1.0, M), "EnvCone": (cone, 1.0, M), "JointYoke": (P["Ref_JointYoke"], 0.8, M)}
    res = {n: {1: dict(min=1e9, fail=None), -1: dict(min=1e9, fail=None)} for n in items}
    for sg in (1, -1):
        for a in range(0, TOP_ANGLE + 1, STEP):
            for n, (sh, lim, ref) in items.items():
                r = res[n][sg]
                if r["fail"] is not None:
                    continue
                d = ref.distToShape(rk(sh, sg * a))[0]
                r["min"] = min(r["min"], d)
                if d < lim - 1e-6:
                    r["fail"] = a
    return res, {n: it[1] for n, it in items.items()}


def rng(res, names):
    return tuple(min((res[n][sg]["fail"] - STEP) if res[n][sg]["fail"] is not None else TOP_ANGLE for n in names) for sg in (1, -1))


def thick_ok(nom, rule, meas):
    assert nom >= rule - 1e-9 and abs(meas - nom) < 0.1, (nom, rule, meas)
    return round(meas, 2)


def verify(P):
    M, K, St, H = P["Mount"], P["Knuckle"], P["Stub"], P["WheelHub"]
    rep = {}
    rep["valid"] = {n: (P[n].isValid(), len(P[n].Solids)) for n in P}
    ob = lambda s: s.optimalBoundingBox(False, False)
    rep["vol_mm3"] = dict(Mount=round(M.Volume, 1), Knuckle=round(K.Volume, 1), Stub=round(St.Volume, 1), WheelHub=round(H.Volume, 1),
                          mount_plus_knuckle=round(M.Volume + K.Volume, 1), old_mount=OLD_MOUNT_VOL)
    rep["bbox"] = {n: tuple(round(v, 2) for v in (ob(P[n]).XMin, ob(P[n]).XMax, ob(P[n]).YMin, ob(P[n]).YMax, ob(P[n]).ZMin, ob(P[n]).ZMax)) for n in PRINT_UP}
    kb, mb = ob(K), ob(M)
    rep["slim"] = dict(width_below_pad=round(max(kb.XLength, 2 * POST_R), 2), lowest_below_axle=round(-min(kb.ZMin, mb.ZMin), 2), mount_x_extent=(round(mb.XMin, 2), round(mb.XMax, 2)))
    gl = sum(f.Area for f in M.Faces if isinstance(f.Surface, Part.Plane) and abs(f.BoundBox.ZMin - AXIS_DEPTH) < 1e-6 and abs(f.BoundBox.ZMax - AXIS_DEPTH) < 1e-6)
    rep["glue_area_mm2"] = round(gl, 1)
    axes = lambda s, r: [(f.Surface.Center, f.Surface.Axis) for f in s.Faces if isinstance(f.Surface, Part.Cylinder) and abs(f.Surface.Radius - r) < 1e-6]
    ba, pa = axes(K, BORE_R)[0], axes(M, POST_R)[0]
    ln = lambda c, a: Part.makeLine(c - a * 60, c + a * 60)
    rep["axes"] = dict(bore_z=round(ba[0].z, 6), glue_to_axle=round(mb.ZMax - ba[0].z, 6), axis_dist=round(ln(*ba).distToShape(ln(*pa))[0], 6), bore_dir=tuple(round(abs(c), 3) for c in ba[1]),
                       post_dir=tuple(round(abs(c), 3) for c in pa[1]))
    kb0 = build_knuckle(holes=False)
    xor = lambda a, b: round(a.cut(b).Volume + b.cut(a).Volume, 3)
    rep["sym"] = dict(knuckle_x=xor(kb0, kb0.mirror(O, X)), mount_y=xor(M, M.mirror(O, Y)), mount_rot180_vs_mirror_x=xor(rot(M, Z, 180), M.mirror(O, X)))
    rep["asm"] = assembly(P)
    res, lims = steering(P)
    rep["steer"] = {n: {sg: (round(res[n][sg]["min"], 3), res[n][sg]["fail"]) for sg in (1, -1)} for n in res}
    rep["range_free"] = rng(res, ("Knuckle", "KnuckleUpper", "Stub", "WheelHub", "Disc"))
    rep["range_powered_geometry"] = rng(res, tuple(res))
    rep["range_powered"] = tuple(min(a, int(JOINT_MAX_DEG)) for a in rep["range_powered_geometry"])
    rep["floor_arch_edge_x"] = {a: floor_arch(P["Ref_Disc"], a) for a in (30, 45, 60)}
    rep["lims"] = lims
    boss = K.common(vcyl(BOSS_R + 0.5, 0, 0, Z_FLOOR + BOSS_H - 0.3, Z_FLOOR + BOSS_H + 0.5))
    top = M.common(box(-30, 30, -30, 30, Z_U - 0.01, 40))
    fl = St.common(box(FL_X0 - 1, FL_X1 + 0.01, -10, 10, -10, 10))
    rets = (P["Ref_RetScrew"], P["Ref_RetScrew2"])
    root = M.common(vcyl(GROOVE_R + 0.01, 0, 0, Z_C - 1, Z_U + 1))
    play_up = min(travel(a, M, Z) for a in (K,) + rets)
    play_dn = min(travel(a, M, -Z) for a in (K,) + rets)
    toe = [min(travel_rot(P["Ref_LockScrew"], M, sg), 10.0) for sg in (1, -1)]
    rep["fits"] = dict(post_radial=round(moved(K, Z, -1.0).distToShape(M)[0], 3), stub_radial=round(moved(St, X, -1.0).distToShape(K)[0], 3),
                       boss_gap=round(M.distToShape(boss)[0], 3), play_up=round(play_up, 3), play_down=round(play_dn, 3), play_total=round(play_up + play_dn, 3),
                       ret_top_gap=round(min(top.distToShape(r)[0] for r in rets), 3), ret_root_gap=round(min(r.distToShape(root)[0] for r in rets), 3),
                       ret_flank_gap=round(M.distToShape(rets[0])[0], 3), ret_flank_gap_at_60=round(M.distToShape(rk(rets[0], 60))[0], 3),
                       lock_notch_gap=round(P["Ref_LockScrew"].distToShape(M)[0], 3), toe_play_deg=tuple(round(t, 2) for t in toe), toe_play_mm_at_rim=tuple(round(WHEEL_D / 2 * math.radians(t), 2) for t in toe),
                       float_in=round(fl.distToShape(K)[0], 3), float_out=round(H.distToShape(K)[0], 3), stub_vs_knuckle=round(St.distToShape(K)[0], 3))
    rep["fits"]["end_float"] = round(rep["fits"]["float_in"] + rep["fits"]["float_out"], 3)
    pt = St.common(box(PORT_X0 - 1, FL_X0, -10, 10, -10, 10))
    pb = ob(pt)
    rep["port"] = dict(len_from_flange=round(FL_X0 - ob(St).XMin, 3), len_from_stationary=round(-KN_HALF - ob(St).XMin, 3), af=round(pb.ZLength, 3), corners=round(pb.YLength, 3),
                       vol=round(pt.Volume, 2), vol_ref=round(2 * math.sqrt(3) * (SHAFT_AF / 2) ** 2 * (FL_X0 - PORT_X0) - math.pi * 1.4 ** 2 * SHAFT_AF, 2),
                       pilot_open=not St.isInside(V(PORT_X0 + PORT_PILOT, 0, 0), 1e-7, True), pilot_wall=St.isInside(V(PORT_X0 + PORT_PILOT + 2.0, 0, 0), 1e-7, True),
                       hex_end_inside_hub=HEX_END < HUB_X1)
    rep["walls"] = dict(
        socket=thick_ok(R_B - SOCK_R, 2.0, run_len(K, V(SOCK_R + 0.005, 0, 15), X, 5)),
        web_floor_bore=thick_ok(Z_FLOOR - BORE_R, 2.0, run_len(K, V(5, 0, BORE_R + 0.005), Z, 5)),
        under_bore=thick_ok(BORE_R + K_BOT * -1 - 2 * BORE_R, 2.0, run_len(K, V(5, 0, -BORE_R - 0.005), -Z, 5)),
        lug_above_lock=thick_ok(LUG_R - CLAMP_CLR / 2, WALL_MIN, run_len(K, V(-XR0 - 1.5, LOCK_Y, LOCK_Z + CLAMP_CLR / 2 + 0.005), Z, 5)),
        relief_web=thick_ok(LOCK_Z - Z_S - 2 * RELIEF_R, WALL_MIN, run_len(K, V(0, RET_Y, Z_S + RELIEF_R + 0.005), Z, 3)),
        rim_top=min(rad_wall(K, K_TOP - 0.01 - 0.1 * i) for i in range(10)),
        lug_cb=round(LUG_R - CLAMP_CLR / 2, 2), arm_rim=round(ARM_END_R - ARM_HOLE / 2, 2), arm_t=ARM_T,
        post_to_clamp=round(GROOVE_R - CLAMP_PILOT / 2, 2), notch_to_clamp=round(LOCK_Y - NOTCH_R - CLAMP_PILOT / 2, 2), clamp_end=round(CLAMP_TIP - 0.4 - POST_END, 2),
        pad_under_groove=round(PAD_T - GROOVE_D, 2))
    ring = (Z, -Z, Y, -Y)
    rep["engage"] = dict(clamp=thread_len(M, V(0, 0, CB_Z), -Z, (X, -X, Y, -Y), SCREW_L), ret=thread_len(K, V(-LUG_X, -RET_Y, Z_S), X, ring, RET_L), ret2=thread_len(K, V(-LUG_X, RET_Y, Z_S), X, ring, RET_L),
                         lock=thread_len(K, V(-LUG_X, LOCK_Y, LOCK_Z), X, ring, LOCK_L),
                         hub_stub=thread_len(St, V(SH_X, 0, WH_BD / 2), -Z, (X,), SCREW_L), hub_hub=thread_len(H, V(SH_X, 0, WH_BD / 2), -Z, (X,), SCREW_L),
                         clamp_tip_to_post_end=round(CLAMP_TIP - POST_END, 2))
    rep["strength"] = strength()
    rep["print"] = {n: print_check(P[n], PRINT_UP[n]) for n in PRINT_UP}
    return rep


def check(rep):
    assert all(v[0] and v[1] == 1 for v in rep["valid"].values()), rep["valid"]
    v = rep["vol_mm3"]
    assert v["mount_plus_knuckle"] <= 12000.0 and v["Mount"] < 0.5 * v["old_mount"] and v["Mount"] + v["Knuckle"] < v["old_mount"], v
    s = rep["slim"]
    assert s["width_below_pad"] <= 24.0 and s["lowest_below_axle"] <= 9.0 and s["mount_x_extent"][1] <= 11.0 + 1e-6, s
    assert 950.0 <= rep["glue_area_mm2"] <= 1250.0, rep["glue_area_mm2"]
    a = rep["axes"]
    assert abs(a["glue_to_axle"] - AXIS_DEPTH) < 1e-6 and abs(a["bore_z"]) < 1e-6 and a["axis_dist"] < 1e-6 and a["bore_dir"] == (1.0, 0.0, 0.0) and a["post_dir"] == (0.0, 0.0, 1.0), a
    assert max(rep["sym"].values()) < 0.1, rep["sym"]
    assert not any(rep["asm"]["drivers"].values()) and not any(rep["asm"]["final_core_overlaps"].values()), rep["asm"]
    assert all(rep["asm"][k] < 1e-3 for k in rep["asm"] if k[0].isdigit()), rep["asm"]
    st = rep["steer"]
    for n, lim in rep["lims"].items():
        for sg in (1, -1):
            assert st[n][sg][0] >= lim - 1e-6, (n, sg, st[n][sg], lim)
    assert min(rep["range_free"]) >= 45 and min(rep["range_powered"]) >= 30, (rep["range_free"], rep["range_powered"])
    f = rep["fits"]
    assert f["post_radial"] >= 0.3 - 1e-6 and f["stub_radial"] >= 0.3 - 1e-6, f
    assert f["boss_gap"] >= BOSS_GAP - 1e-6 and f["ret_root_gap"] >= 0.3 - 1e-6 and f["ret_top_gap"] >= 0.3 - 1e-6, f
    assert f["play_up"] >= BOSS_GAP - 2e-3 and f["play_down"] >= RET_DOWN - 2e-3 and 0.3 <= f["play_total"] <= 0.5 + 2e-3, f
    assert abs(f["ret_flank_gap"] - f["ret_flank_gap_at_60"]) < 1e-3 and f["lock_notch_gap"] >= NOTCH_R - SCREW_D / 2 - 1e-3, f
    assert 0.3 - 1e-6 <= f["end_float"] <= 0.5 + 1e-6 and f["float_in"] >= 0.15 and f["float_out"] >= 0.15 and f["stub_vs_knuckle"] >= 0.15, f
    p = rep["port"]
    assert abs(p["len_from_flange"] - PORT_L) < 1e-6 and p["len_from_stationary"] >= PORT_L and abs(p["af"] - SHAFT_AF) < 1e-6, p
    assert abs(p["vol"] - p["vol_ref"]) < 0.05 and p["pilot_open"] and p["pilot_wall"], p
    w = rep["walls"]
    assert w["rim_top"] >= WALL_MIN and w["relief_web"] >= WALL_MIN and w["lug_above_lock"] >= WALL_MIN and w["lug_cb"] >= 1.2 and w["arm_rim"] >= 1.2 and w["post_to_clamp"] >= 1.2 and w["notch_to_clamp"] >= 1.2 and w["clamp_end"] >= 1.2 and w["pad_under_groove"] >= 1.2 and w["arm_t"] >= 1.2, w
    e = rep["engage"]
    assert e["clamp"] >= 8.0 and e["ret"] >= 6.0 and e["ret2"] >= 6.0 and e["lock"] >= 6.0 and e["hub_stub"] + e["hub_hub"] >= 6.0 and e["clamp_tip_to_post_end"] >= 1.2, e
    t = rep["strength"]
    assert t["root_margin"] >= 1.5 and t["groove_margin"] >= 1.5 and t["root_MPa"] <= ALLOW_BEND and t["groove_MPa"] <= ALLOW_BEND and t["bearing_post_socket_MPa"] <= ALLOW_BEARING, t
    assert t["retention_plastic_bearing_MPa"] <= ALLOW_BEARING and t["boss_bearing_MPa"] <= ALLOW_BEARING and t["web_shear_MPa"] <= ALLOW_BEARING and t["retention_shank_shear_MPa"] <= 100.0, t
    for n, (floor, bad) in rep["print"].items():
        assert floor >= 5.0 and print_ok(bad), (n, floor, bad)


def main():
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    P = build_parts()
    for n, s in P.items():
        assert s.isValid() and len(s.Solids) == 1, n
        o = doc.addObject("Part::Feature", n)
        o.Shape = s
        if App.GuiUp and n in COLORS:
            o.ViewObject.ShapeColor = COLORS[n]
    rep = verify(P)
    print("report", rep)
    check(rep)
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
