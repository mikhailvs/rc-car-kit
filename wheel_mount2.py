# Wheel mount 2: a kingpin POST design. Mount = flat glue pad (glued under the cardboard floor) with one fat round post pointing down; Knuckle = a vertical barrel (post socket) blended into a horizontal barrel (axle bore) with a steering arm flowing out rearward; Stub (journal, hex, inboard PORT, flange) and WheelHub.
# Unlike wheel_mount.py (C yoke, trapped knuckle squeezed in sideways, one long M3x40 kingpin in plastic) nothing is trapped and nothing is squeezed: the knuckle slides straight up onto the post, ONE M3 kingpin bolt driven up from below into the post end keeps it there, steering is free on a 0.3 radial fit, the weight rides on a small thrust boss.
# Layout: the kingpin axis does NOT cross the axle axis. The post sits OFF = 10.5 mm AHEAD of the axle (axle behind the post, arm rearward), so the wheel trails the pivot by 10.5 mm (mechanical trail, self-centring). 10.5 is the smallest offset that fits the washer (dia 7) plus 0.8 gap to the pocket wall, 1.2 wall and the dia 9.9 bore. Left and right are mirror images across the car centre line, so ahead is the same y sign on both sides: the Knuckle is x symmetric, the Mount is y symmetric (turn it 180 degrees about the post for the other side). The axle stays 29.0 below the glue face.
# Modes: FREE STEER (kingpin bolt only), LOCKED for an unsteered wheel (a second M3x30 from below through the knuckle tower into a pad boss: two bolts from below = locked, one = steers; the shank has 0.3 radial in its 3.6 hole at 10.5 from the post axis, so +-1.64 degrees of toe play, about +-1.4 mm at the rim, none once tightened because the clamp pulls the knuckle up onto the thrust boss), POWERED (a JointYoke on the stub port, drive_shaft.py swing envelope, still steerable). The fits are sloppy by design (0.3 radial on the post, hex and journal fits, 0.4 end float): expect a few degrees of camber and toe slop. Future suspension: the pad is the only chassis interface, a swing arm carrying the same post can replace it.
# Retention and positive stop: the bolt runs up the post axis through a dia 6.6 pocket under a plate in the knuckle. The post end carries a dia 5.2 spigot (pilot dia 2.8 runs through it) that protrudes 0.15 below the plate; the M3 washer (dia 7 x 0.5) and the pan head (dia 6 x 3) bolt onto the spigot end and the bolt stops there, so tightening can never clamp the knuckle. Play does not depend on torque: 0.30 up (plate boss to post end), 0.15 down (plate shoulder to washer), 0.45 total. The washer overlaps the plate hole by 0.6 per side. The clamp screw down the post from the glue face is dropped: no room for 2 mm of solid between its pilot and the 11.5 mm bottom-bolt pilot, and it was only counted as preload; the root bending check is done without it.
# Hardware per wheel: 1 M3x12 pan head kingpin bolt (11.5 mm thread engaged in spigot and post), 1 M3 washer dia 7 x 0.5, optional 1 M3x30 lock bolt (5.7 mm thread in the pad boss), 1 M3x16 hub cross screw. Mount, Knuckle, Stub, WheelHub are the only prints, ONE Mount and ONE Knuckle serve all four wheels. Heads sit inside the knuckle (kingpin head 0.35 above the axle axis, lock head in a counterbore); the lowest point is the knuckle at 6.95 below the axle axis.
# Assembly: 1 Stub through the Knuckle from the inboard side; 2 WheelHub onto the stub hex, cross screw from above; 3 glue the Mount under the floor; 4 push the Knuckle (with stub, hub and wheel) straight up onto the post; 5 kingpin bolt with its washer straight up from below with a dia 6 driver; 6 optional lock bolt likewise. Pull the bolts to take the knuckle off again with the mount glued in place. All steps are translation sweeps with zero common volume in verify(), driver included.
# Sizes: Mount 40 x 33 x 25.2 mm (pad 2.6 thick, 10.5 cm2 glue face, post dia 14, two lock bosses dia 6 at 10.5 either side), Knuckle 22.6 x 53.5 x 27 mm, 12.1 cm3 together. Walls 1.2 minimum, 2.0 around the socket and bore. Knuckle = vertical barrel (post socket) blended into a horizontal barrel (axle bore) with a 3 mm arm flowing out rearward (holes at 20, 27, 34 from the kingpin axis) and a slim front tower for the lock bolt; edges are filleted where the kernel allowed (see report blend).
# Steering: 60 degrees each way free (swept limit, measured against the Mount, wheel clears the pad by 8.9 mm); powered limited by the universal joint to about 36 degrees (drive_shaft.py), not by the mount. The FLOOR needs a wheel arch: with 2 mm clearance its edge must sit at or inboard of x -4.8 from the post axis for 30 degrees, -19.7 for 45, -33.5 for 60 (worse than with the axle through the kingpin because the wheel trails; the pad's outboard edge is x 11).
# Strength (15 N vertical at the tyre centre plus 15 N sideways at the tyre contact): root 5.9 MPa (margin 2.0, offset adds 157 Nmm bending and 157 Nmm torsion, 0.3 MPa), socket bearing 3.3 MPa, kingpin bolt pull-out 30 N against 540 N (assumed 10 MPa printed PLA thread shear, an assumption not a measurement), washer shoulder 5 MPa, boss bearing 0.8 MPa.
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

AXIS_DEPTH, PAD_T, PAD_X0, PAD_X1, PAD_Y, PAD_R = 29.0, 2.6, -29.0, 11.0, 16.5, 6.0
PAD_Z0, PAD_Z1 = AXIS_DEPTH - PAD_T, AXIS_DEPTH
POST_R, FIL_R, POST_CH = 7.0, 3.0, 0.8
FIL_Z0 = PAD_Z0 - FIL_R
SOCK_R, R_B, R_COL, BORE_R, R_H = 7.3, 9.3, 6.0, 4.95, 6.95
OFF = 10.5
Z_FLOOR, BOSS_R, BOSS_H, BOSS_GAP, DOWN_GAP, PLATE_T = 7.0, 4.5, 0.8, 0.3, 0.15, 3.0
POST_END = Z_FLOOR + BOSS_H + BOSS_GAP
Z_U = Z_FLOOR - PLATE_T
Z_SP = Z_U - DOWN_GAP
SPIG_R, SPIG_HOLE_R = 2.6, 2.9
WASHER_D, WASHER_ID, WASHER_T = 7.0, 3.2, 0.5
Z_H = Z_SP - WASHER_T
PK_R = WASHER_D / 2 + 0.8
SCREW_D, CORE_D, HEAD_D, HEAD_H, PILOT_D, CLR_D, BOLT_L, LOCK_L, SCREW_L_HUB = 3.0, 2.6, 6.0, 3.0, 2.8, 3.6, 12.0, 30.0, 16.0
PILOT_TOP = Z_H + BOLT_L + 0.4
K_TOP, K_BOT, KN_HALF = 20.0, -(BORE_R + 2.0), 11.3
SOCK_CH, OUT_CH, END_CH, BORE_CH = 0.5, 0.2, 0.5, 0.5
R_L, TW_R, TW_BASE_R, LOCK_BOSS_R, CB_R = 10.5, 3.0, 4.5, 3.0, HEAD_D / 2 + 0.3
Z_B = K_TOP + 0.8 + BOSS_GAP
Z_LS = K_BOT + 3.7
LOCK_PILOT_TOP = Z_LS + LOCK_L + 0.45
ARM_T, ARM_HOLES, ARM_HOLE, ARM_END_R = 3.0, (20.0, 27.0, 34.0), 3.6, 4.5
JOIN_FIL, ARM_FIL = 2.0, 1.5
GLUE_D = 5.0
GLUES = [(-18.0, 10.0), (-18.0, -10.0), (-6.0, 12.5), (-6.0, -12.5)]
GROOVE_W, GROOVE_D = 1.2, 0.6
WALL_MIN = 1.2

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

LOAD_V, LOAD_S, ALLOW_BEND, ALLOW_BEARING = 15.0, 15.0, 12.0, 12.0
PULL_N, TAU_THREAD = LOAD_V + LOAD_S, 10.0
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


def sh(s):
    s = s.copy()
    s.translate(V(0, -OFF, 0))
    return s


def at(s, x, y):
    s = s.copy()
    s.translate(V(x, y, 0))
    return s


def creases(u, a, b):
    out = []
    for e in u.Edges:
        v = Part.Vertex(e.valueAt((e.FirstParameter + e.LastParameter) / 2))
        if a.distToShape(v)[0] < 1e-4 and b.distToShape(v)[0] < 1e-4:
            out.append(e)
    return out


def blend(u, a, b, r):
    n, done = 0, True
    while done:
        done = False
        es = creases(u, a, b)
        mid = lambda e: e.valueAt((e.FirstParameter + e.LastParameter) / 2)
        for e, q in ((e, q) for e in es for q in (r, 0.75 * r, 0.5 * r)):
            m = mid(e)
            pair = [e] + [f for f in es if f is not e and (mid(f) - V(-m.x, m.y, m.z)).Length < 1e-3 and abs(m.x) > 1e-3]
            try:
                f = u.makeFillet(q, pair).removeSplitter()
            except Exception:
                continue
            if f.isValid() and len(f.Solids) == 1 and abs(f.Volume - u.Volume) < 0.2 * u.Volume:
                u, n, done = f, n + 1, True
                break
    BLEND[0] += n
    BLEND[1] += len(creases(u, a, b))
    return u


BLEND = [0, 0]


def build_mount():
    pts = [(0, Z_SP), (SPIG_R - 0.3, Z_SP), (SPIG_R, Z_SP + 0.3), (SPIG_R, POST_END), (POST_R - POST_CH, POST_END), (POST_R, POST_END + POST_CH), (POST_R, FIL_Z0)]
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
    boss = revz([(0, Z_B), (LOCK_BOSS_R - 0.5, Z_B), (LOCK_BOSS_R, Z_B + 0.5), (LOCK_BOSS_R, PAD_Z0 + 1), (0, PAD_Z0 + 1)])
    for s in (1, -1):
        m = m.fuse(at(boss, 0, s * R_L))
    m = m.cut(vcyl(PILOT_D / 2, 0, 0, Z_SP - 1, PILOT_TOP))
    for s in (1, -1):
        m = m.cut(vcyl(PILOT_D / 2, 0, s * R_L, Z_B - 1, LOCK_PILOT_TOP))
    for x, y in GLUES:
        m = m.cut(vcyl(GLUE_D / 2, x, y, PAD_Z0 - 1, PAD_Z1 + 1))
    for s in (1, -1):
        m = m.cut(box(-27.0, -6.0, s * 5.0 - GROOVE_W / 2, s * 5.0 + GROOVE_W / 2, PAD_Z1 - GROOVE_D, PAD_Z1 + 1))
    m = m.cut(box(-12.0 - GROOVE_W / 2, -12.0 + GROOVE_W / 2, -13.0, 13.0, PAD_Z1 - GROOVE_D, PAD_Z1 + 1))
    return m.removeSplitter()


def pear():
    r1, r2, d = R_COL, TW_BASE_R, R_L
    s = (r1 - r2) / d
    c = math.sqrt(1 - s * s)
    p1, p2 = V(r1 * c, r1 * s, K_BOT), V(r2 * c, d + r2 * s, K_BOT)
    q = [p1, p2, V(-p2.x, p2.y, K_BOT), V(-p1.x, p1.y, K_BOT)]
    web = Part.Face(Part.makePolygon(q + q[:1])).extrude(V(0, 0, Z_U - K_BOT))
    return web.fuse(vcyl(r1, 0, 0, K_BOT, Z_U)).fuse(vcyl(r2, 0, d, K_BOT, Z_U)).removeSplitter()


def build_horizontal():
    a = R_H * math.sin(math.pi / 4)
    b = 2 * a + K_BOT
    kp = [V(-KN_HALF, -OFF + y, z) for y, z in ((-a, -a), (a, -a), (b, K_BOT), (-b, K_BOT))]
    keel = Part.Face(Part.makePolygon(kp + kp[:1])).extrude(V(2 * KN_HALF, 0, 0))
    h = Part.makeCylinder(R_H, 2 * KN_HALF, V(-KN_HALF, -OFF, 0), X).fuse(keel).removeSplitter()
    return h.makeChamfer(END_CH, [e for e in h.Edges if abs(abs(e.BoundBox.XMin) - KN_HALF) < 1e-6 and abs(abs(e.BoundBox.XMax) - KN_HALF) < 1e-6])


def build_tower():
    t = revz([(0, K_BOT), (TW_BASE_R, K_BOT), (TW_BASE_R, Z_U), (TW_R, Z_U + (TW_BASE_R - TW_R)), (TW_R, K_TOP - 0.3), (TW_R - 0.3, K_TOP), (0, K_TOP)])
    return at(t, 0, R_L)


def build_arm():
    e = ARM_HOLES[-1]
    pts = [V(-3.0, -3.0, K_BOT), V(3.0, -3.0, K_BOT), V(6.0, -14.0, K_BOT), V(ARM_END_R, -e, K_BOT), V(-ARM_END_R, -e, K_BOT), V(-6.0, -14.0, K_BOT)]
    a = Part.Face(Part.makePolygon(pts + pts[:1])).extrude(V(0, 0, ARM_T))
    return a.fuse(Part.makeCylinder(ARM_END_R, ARM_T, V(0, -e, K_BOT)))


def build_knuckle():
    vb = revz([(0, Z_U), (R_B, Z_U), (R_B, K_TOP - OUT_CH), (R_B - OUT_CH, K_TOP), (0, K_TOP)])
    vb = vb.fuse(revz([(0, Z_U - (R_B - R_COL)), (R_COL, Z_U - (R_B - R_COL)), (R_B, Z_U), (0, Z_U)])).removeSplitter()
    hb = build_horizontal()
    k = blend(vb.fuse(hb).removeSplitter(), vb, hb, JOIN_FIL)
    low = pear().fuse(build_tower()).removeSplitter()
    k = k.fuse(low).removeSplitter()
    arm = build_arm()
    k = blend(k.fuse(arm).removeSplitter(), k, arm, ARM_FIL)
    k = k.cut(box(-30, 30, -60, 40, K_BOT - 10, K_BOT))
    k = k.cut(revz([(0, Z_FLOOR), (SOCK_R, Z_FLOOR), (SOCK_R, K_TOP - SOCK_CH - 0.1), (SOCK_R + SOCK_CH, K_TOP), (SOCK_R + SOCK_CH, K_TOP + 1), (0, K_TOP + 1)]))
    k = k.fuse(revz([(2.0, Z_FLOOR - 0.1), (BOSS_R, Z_FLOOR - 0.1), (BOSS_R, Z_FLOOR + BOSS_H), (2.0, Z_FLOOR + BOSS_H)]))
    k = k.cut(vcyl(SPIG_HOLE_R, 0, 0, Z_U - 1, Z_FLOOR + BOSS_H + 1)).cut(Part.makeCone(SPIG_HOLE_R, SPIG_HOLE_R + 0.6, 0.6, V(0, 0, Z_FLOOR + BOSS_H - 0.6), Z))
    k = k.cut(revz([(0, K_BOT - 1), (PK_R + 1.5, K_BOT - 1), (PK_R, K_BOT + 0.5), (PK_R, Z_U), (0, Z_U)]))
    bore = revx([(-KN_HALF - 1, 0), (-KN_HALF - 1, BORE_R + BORE_CH + 1), (-KN_HALF, BORE_R + BORE_CH), (-KN_HALF + BORE_CH, BORE_R), (KN_HALF - BORE_CH, BORE_R),
                 (KN_HALF, BORE_R + BORE_CH), (KN_HALF + 1, BORE_R + BORE_CH + 1), (KN_HALF + 1, 0)])
    k = k.cut(sh(bore))
    k = k.cut(vcyl(CLR_D / 2, 0, R_L, K_BOT - 1, K_TOP + 1)).cut(vcyl(CB_R, 0, R_L, K_BOT - 1, Z_LS))
    for h in ARM_HOLES:
        k = k.cut(vcyl(ARM_HOLE / 2, 0, -h, K_BOT - 1, K_BOT + ARM_T + 1))
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


def screw(p, d, length=BOLT_L, dia=SCREW_D):
    return Part.makeCylinder(dia / 2, length, p, d).fuse(Part.makeCylinder(HEAD_D / 2, HEAD_H, p - d * HEAD_H, d))


def washer():
    return Part.makeCylinder(WASHER_D / 2, WASHER_T, V(0, 0, Z_SP - WASHER_T), Z).cut(Part.makeCylinder(WASHER_ID / 2, WASHER_T, V(0, 0, Z_SP - WASHER_T), Z))


def build_yoke_on_port():
    y = build_yoke()
    y.translate(V(-S["AX"], 0, 0))
    y = rot(y, Z, 180)
    y.translate(V(PORT_X0 - TIP_J, 0, 0))
    return sh(y)


def envelope(grow=0.0):
    c = cyl(ENV_R + grow, PORT_X0 - grow, FL_X0 + grow)
    h = ENV_CONE_L + 2 * grow
    return sh(c), sh(Part.makeCone(0, h * math.tan(math.radians(ENV_DEG)), h, V(ENV_CENTRE + 2 * grow, 0, 0), -X))


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


def flip(s):
    s = s.copy()
    s.rotate(V(0, -OFF, 0), Z, 180)
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
            bad.append((type(f.Surface).__name__, round(getattr(f.Surface, "Radius", 0.0), 2), round(area, 1), round(4 * f.Area / f.Length, 1)))
    return round(floor, 1), bad


def print_ok(bad):
    return all((k == "Cylinder" and r <= 5.05) or (k == "Plane" and span <= 10.0) or (k == "BSplineSurface" and a <= 1.0) for k, r, a, span in bad)


def strength(eng_bolt, eng_lock):
    xt, zc = HUB_X1 + WHEEL_T / 2, -WHEEL_D / 2
    My = lambda z: LOAD_V * xt + LOAD_S * (z - zc)
    Mx = LOAD_V * OFF
    M = lambda z: math.hypot(My(z), Mx)
    T = LOAD_S * OFF
    sec = lambda d: math.pi * d ** 3 / 32
    le = K_TOP - POST_END
    fb = M((POST_END + K_TOP) / 2) / (le * 2 / 3)
    sig, tau = M(FIL_Z0) / sec(2 * POST_R), T / (2 * sec(2 * POST_R))
    eq = math.sqrt(sig ** 2 + 3 * tau ** 2)
    ring = math.pi / 4 * (WASHER_D ** 2 - (2 * SPIG_HOLE_R) ** 2)
    pull = lambda le_: TAU_THREAD * 0.5 * math.pi * SCREW_D * le_
    t_web = Z_FLOOR - BORE_R
    return dict(root_MPa=round(eq, 2), root_bending_MPa=round(sig, 2), root_torsion_MPa=round(tau, 2), root_margin=round(ALLOW_BEND / eq, 2),
                offset_moment_Nmm=round(Mx, 1), offset_torsion_Nmm=round(T, 1), bearing_post_socket_MPa=round(fb / (2 * POST_R * le / 3), 2),
                pull_load_N=PULL_N, thread_tau_MPa_assumed=TAU_THREAD, bolt_pull_capacity_N=round(pull(eng_bolt), 1), bolt_pull_margin=round(pull(eng_bolt) / PULL_N, 2),
                lock_pull_capacity_N=round(pull(eng_lock), 1), lock_pull_margin=round(pull(eng_lock) / PULL_N, 2),
                shoulder_MPa=round(PULL_N / (0.5 * ring), 2), washer_ring_mm2=round(ring, 1),
                boss_bearing_MPa=round((LOAD_V + LOAD_S) / (math.pi * (BOSS_R ** 2 - SPIG_HOLE_R ** 2)), 2),
                web_shear_MPa=round((LOAD_V + LOAD_S) / (math.pi * 2 * BOSS_R * t_web), 2), allow_bend=ALLOW_BEND, allow_bearing=ALLOW_BEARING)


def build_parts():
    P = dict(Mount=build_mount(), Knuckle=build_knuckle(), Stub=sh(build_stub()), WheelHub=sh(build_hub()))
    P["Ref_Floor"] = box(FLOOR_X0, FLOOR_X1, -70, 70, AXIS_DEPTH, AXIS_DEPTH + FLOOR_T)
    P["Ref_Disc"] = sh(cyl(WHEEL_D / 2, HUB_X1, HUB_X1 + WHEEL_T))
    P["Ref_KingpinBolt"] = screw(V(0, 0, Z_H), Z)
    P["Ref_Washer"] = washer()
    P["Ref_LockBolt"] = screw(V(0, R_L, Z_LS), Z, LOCK_L)
    P["Ref_HubScrew"] = screw(V(SH_X, -OFF, WH_BD / 2), -Z, SCREW_L_HUB)
    P["Ref_JointYoke"] = build_yoke_on_port()
    return P


def cores():
    return dict(kp=screw(V(0, 0, Z_H), Z, BOLT_L, CORE_D), lock=screw(V(0, R_L, Z_LS), Z, LOCK_L, CORE_D), hub=screw(V(SH_X, -OFF, WH_BD / 2), -Z, SCREW_L_HUB, CORE_D))


def assembly(P):
    M, K, St, H, Dc, Fl, Yk, W = (P[n] for n in ("Mount", "Knuckle", "Stub", "WheelHub", "Ref_Disc", "Ref_Floor", "Ref_JointYoke", "Ref_Washer"))
    C = cores()
    drv = dict(kp=driver(V(0, 0, Z_H - HEAD_H), -Z), lock=driver(V(0, R_L, Z_LS - HEAD_H), -Z), hub=driver(V(SH_X, -OFF, WH_BD / 2 + HEAD_H), Z))
    r = {}
    r["1_stub_through_knuckle"] = sweep(dict(s=St), dict(K=K), -X)
    r["2_hub_on_stub"] = sweep(dict(h=H), dict(s=St, K=K), X)
    allfix = dict(M=M, K=K, s=St, h=H, d=Dc, F=Fl, y=Yk)
    r["3_hub_screw_and_driver"] = sweep(dict(c=C["hub"], dr=drv["hub"]), allfix, Z)
    r["4_knuckle_up_onto_post"] = sweep(dict(k=K, s=St, h=H, d=Dc, y=Yk, c=C["hub"]), dict(M=M, F=Fl), -Z)
    r["5_kingpin_bolt_and_driver"] = sweep(dict(b=C["kp"], w=W, dr=drv["kp"]), allfix, -Z)
    r["6_lock_bolt_and_driver"] = sweep(dict(b=C["lock"], dr=drv["lock"]), dict(allfix, kb=C["kp"], w=W), -Z)
    r["final_core_overlaps"] = {n: round(max(vol(c, b) for b in allfix.values()), 4) for n, c in C.items()}
    return r


def steering(P):
    M = P["Mount"]
    Mup = M.common(box(-60, 60, -60, 60, Z_B - 0.05, 40))
    c, cone = envelope()
    items = {"Knuckle": (P["Knuckle"], 0.3, M), "KnuckleUpper": (P["Knuckle"], 0.8, Mup), "Stub": (P["Stub"], 0.8, M), "WheelHub": (P["WheelHub"], 0.8, M),
             "Disc": (P["Ref_Disc"], 2.0, M),
             "EnvCyl": (c, 1.0, M), "EnvCone": (cone, 1.0, M), "JointYoke": (P["Ref_JointYoke"], 0.8, M)}
    res = {n: {1: dict(min=1e9, fail=None), -1: dict(min=1e9, fail=None)} for n in items}
    for sg in (1, -1):
        for a in range(0, TOP_ANGLE + 1, STEP):
            for n, (sh_, lim, ref) in items.items():
                r = res[n][sg]
                if r["fail"] is not None:
                    continue
                d = ref.distToShape(rk(sh_, sg * a))[0]
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
    M, K, St, H, Dc = P["Mount"], P["Knuckle"], P["Stub"], P["WheelHub"], P["Ref_Disc"]
    rep = {}
    rep["valid"] = {n: (P[n].isValid(), len(P[n].Solids)) for n in P}
    ob = lambda s: s.optimalBoundingBox(False, False)
    rep["vol_mm3"] = dict(Mount=round(M.Volume, 1), Knuckle=round(K.Volume, 1), Stub=round(St.Volume, 1), WheelHub=round(H.Volume, 1), mount_plus_knuckle=round(M.Volume + K.Volume, 1))
    rep["bbox"] = {n: tuple(round(v, 2) for v in (ob(P[n]).XMin, ob(P[n]).XMax, ob(P[n]).YMin, ob(P[n]).YMax, ob(P[n]).ZMin, ob(P[n]).ZMax)) for n in PRINT_UP}
    kb, mb = ob(K), ob(M)
    low = min(kb.ZMin, mb.ZMin, ob(P["Ref_KingpinBolt"]).ZMin, ob(P["Ref_LockBolt"]).ZMin, ob(P["Ref_Washer"]).ZMin)
    rep["slim"] = dict(width_below_pad=round(max(kb.XLength, 2 * POST_R), 2), lowest_below_axle=round(-low, 2), mount_x_extent=(round(mb.XMin, 2), round(mb.XMax, 2)))
    gl = sum(f.Area for f in M.Faces if isinstance(f.Surface, Part.Plane) and abs(f.BoundBox.ZMin - AXIS_DEPTH) < 1e-6 and abs(f.BoundBox.ZMax - AXIS_DEPTH) < 1e-6)
    rep["glue_area_mm2"] = round(gl, 1)
    axes = lambda s, r: [(f.Surface.Center, f.Surface.Axis) for f in s.Faces if isinstance(f.Surface, Part.Cylinder) and abs(f.Surface.Radius - r) < 1e-6]
    ba, pa = axes(K, BORE_R)[0], axes(M, POST_R)[0]
    ln = lambda c, a: Part.makeLine(c - a * 60, c + a * 60)
    rep["axes"] = dict(bore_z=round(ba[0].z, 6), bore_y=round(ba[0].y, 6), glue_to_axle=round(mb.ZMax - ba[0].z, 6), axis_dist=round(ln(*ba).distToShape(ln(*pa))[0], 6),
                       bore_dir=tuple(round(abs(c), 3) for c in ba[1]), post_dir=tuple(round(abs(c), 3) for c in pa[1]),
                       arm_hole_y=sorted(round(-f.Surface.Center.y, 2) for f in K.Faces if isinstance(f.Surface, Part.Cylinder) and abs(f.Surface.Radius - ARM_HOLE / 2) < 1e-6 and f.Surface.Center.y < 0))
    xor = lambda a, b: round(a.cut(b).Volume + b.cut(a).Volume, 3)
    mx = lambda s: s.mirror(O, X)
    St0, H0 = moved(St, Y, OFF), moved(H, Y, OFF)
    rep["sym"] = dict(knuckle_x=xor(K, mx(K)), mount_y=xor(M, M.mirror(O, Y)), mount_rot180_vs_mirror_x=xor(rot(M, Z, 180), mx(M)),
                      stub_flip_vs_mirror=xor(flip(St), mx(St)), hub_flip_vs_mirror=xor(flip(H), mx(H)), disc_flip_vs_mirror=xor(flip(Dc), mx(Dc)))
    Mr, Fr = rot(M, Z, 180), mx(P["Ref_Floor"])
    rep["mirror"] = dict(axle_y_left=rep["axes"]["bore_y"], axle_y_right=round(flip(St).BoundBox.Center.y, 4),
                         right_up_onto_post=sweep(dict(k=K, s=flip(St), h=flip(H), d=flip(Dc), y=flip(P["Ref_JointYoke"])), dict(M=Mr, F=Fr), -Z),
                         right_disc_min=round(min(Mr.distToShape(rk(flip(Dc), a))[0] for a in (45, -45, 60, -60)), 3))
    rep["asm"] = assembly(P)
    res, lims = steering(P)
    rep["steer"] = {n: {sg: (round(res[n][sg]["min"], 3), res[n][sg]["fail"]) for sg in (1, -1)} for n in res}
    rep["range_free"] = rng(res, ("Knuckle", "KnuckleUpper", "Stub", "WheelHub", "Disc"))
    rep["range_powered_geometry"] = rng(res, tuple(res))
    rep["range_powered"] = tuple(min(a, int(JOINT_MAX_DEG)) for a in rep["range_powered_geometry"])
    rep["floor_arch_edge_x"] = {a: min(floor_arch(Dc, a), floor_arch(Dc, -a)) for a in (30, 45, 60)}
    rep["lims"] = lims
    boss = K.common(vcyl(BOSS_R + 0.5, 0, 0, Z_FLOOR + BOSS_H - 0.3, Z_FLOOR + BOSS_H + 0.5))
    top = M.common(box(-30, 30, -30, 30, Z_B - 0.05, 40))
    fl = St.common(box(FL_X0 - 1, FL_X1 + 0.01, -40, 40, -20, 20))
    kw = P["Ref_KingpinBolt"].fuse(P["Ref_Washer"])
    play_up, play_dn = travel(K, M, Z), travel(K, kw, -Z)
    shank = Part.makeCylinder(SCREW_D / 2, LOCK_L, V(0, R_L, Z_LS), Z)
    toe = [min(travel_rot(K, shank, sg), 10.0) for sg in (1, -1)]
    rep["fits"] = dict(post_radial=round(moved(K, Z, -1.0).distToShape(M)[0], 3), stub_radial=round(moved(St, X, -1.0).distToShape(K)[0], 3),
                       boss_gap=round(M.distToShape(boss)[0], 3), play_up=round(play_up, 3), play_down=round(play_dn, 3), play_total=round(play_up + play_dn, 3),
                       washer_to_pocket=round(K.distToShape(moved(P["Ref_Washer"], Z, -1.0))[0], 3), head_to_pocket=round(K.distToShape(moved(P["Ref_KingpinBolt"], Z, -1.0))[0], 3),
                       washer_on_spigot_end=round(P["Ref_Washer"].distToShape(M)[0], 6), lock_boss_gap=round(top.distToShape(K)[0], 3),
                       toe_play_deg=tuple(round(t, 2) for t in toe), toe_play_mm_at_rim=tuple(round(WHEEL_D / 2 * math.radians(t), 2) for t in toe),
                       float_in=round(fl.distToShape(K)[0], 3), float_out=round(H.distToShape(K)[0], 3), stub_vs_knuckle=round(St.distToShape(K)[0], 3))
    rep["fits"]["end_float"] = round(rep["fits"]["float_in"] + rep["fits"]["float_out"], 3)
    pt = St0.common(box(PORT_X0 - 1, FL_X0, -10, 10, -10, 10))
    pb = ob(pt)
    rep["port"] = dict(len_from_flange=round(FL_X0 - ob(St).XMin, 3), len_from_stationary=round(-KN_HALF - ob(St).XMin, 3), af=round(pb.ZLength, 3), corners=round(pb.YLength, 3),
                       vol=round(pt.Volume, 2), vol_ref=round(2 * math.sqrt(3) * (SHAFT_AF / 2) ** 2 * (FL_X0 - PORT_X0) - math.pi * 1.4 ** 2 * SHAFT_AF, 2),
                       pilot_open=not St0.isInside(V(PORT_X0 + PORT_PILOT, 0, 0), 1e-7, True), pilot_wall=St0.isInside(V(PORT_X0 + PORT_PILOT + 2.0, 0, 0), 1e-7, True),
                       hex_end_inside_hub=HEX_END < HUB_X1)
    rep["walls"] = dict(
        socket=thick_ok(R_B - SOCK_R, 2.0, run_len(K, V(SOCK_R + 0.005, 0, 15), X, 5)),
        bore_top=thick_ok(R_H - BORE_R, 2.0, run_len(K, V(5, -OFF, BORE_R + 0.005), Z, 5)),
        under_bore=thick_ok(-K_BOT - BORE_R, 2.0, run_len(K, V(5, -OFF, -BORE_R - 0.005), -Z, 5)),
        pocket_bore=thick_ok(OFF - PK_R - BORE_R, WALL_MIN, run_len(K, V(0, -PK_R - 0.005, 0.05), -Y, 4)),
        tower_hole=thick_ok(TW_R - CLR_D / 2, WALL_MIN, run_len(K, V(CLR_D / 2 + 0.005, R_L, 10), X, 5)),
        tower_cb=thick_ok(TW_BASE_R - CB_R, WALL_MIN, run_len(K, V(CB_R + 0.005, R_L, K_BOT + 1.0), X, 5)),
        spigot=thick_ok(SPIG_R - PILOT_D / 2, WALL_MIN, run_len(M, V(PILOT_D / 2 + 0.005, 0, (Z_SP + POST_END) / 2), X, 3)),
        lock_boss=thick_ok(LOCK_BOSS_R - PILOT_D / 2, WALL_MIN, run_len(M, V(PILOT_D / 2 + 0.005, R_L, 24.0), X, 3)),
        rim_top=min(rad_wall(K, K_TOP - 0.01 - 0.1 * i) for i in range(10)),
        arm_rim=round(ARM_END_R - ARM_HOLE / 2, 2), arm_t=ARM_T, plate=PLATE_T, kp_pilot_to_glue=round(AXIS_DEPTH - PILOT_TOP, 2), lock_pilot_to_glue=round(AXIS_DEPTH - LOCK_PILOT_TOP, 2))
    ring = (X, -X, Y, -Y)
    rep["engage"] = dict(kingpin_bolt=thread_len(M, V(0, 0, Z_H), Z, ring, BOLT_L), lock_bolt=thread_len(M, V(0, R_L, Z_LS), Z, ring, LOCK_L),
                         hub_stub=thread_len(St, V(SH_X, -OFF, WH_BD / 2), -Z, (X,), SCREW_L_HUB), hub_hub=thread_len(H, V(SH_X, -OFF, WH_BD / 2), -Z, (X,), SCREW_L_HUB))
    rep["blend"] = dict(filleted=BLEND[0], sharp_creases_left=BLEND[1])
    rep["strength"] = strength(rep["engage"]["kingpin_bolt"], rep["engage"]["lock_bolt"])
    rep["print"] = {n: print_check(P[n], PRINT_UP[n]) for n in PRINT_UP}
    return rep


def check(rep):
    assert all(v[0] and v[1] == 1 for v in rep["valid"].values()), rep["valid"]
    v = rep["vol_mm3"]
    assert v["mount_plus_knuckle"] <= 13000.0, v
    s = rep["slim"]
    assert s["width_below_pad"] <= 24.0 and s["lowest_below_axle"] <= 9.0 and s["mount_x_extent"][1] <= 11.0 + 1e-6, s
    assert 950.0 <= rep["glue_area_mm2"] <= 1250.0, rep["glue_area_mm2"]
    a = rep["axes"]
    assert abs(a["glue_to_axle"] - AXIS_DEPTH) < 1e-6 and abs(a["bore_z"]) < 1e-6 and abs(a["axis_dist"] - OFF) < 1e-6 and abs(a["bore_y"] + OFF) < 1e-6, a
    assert a["bore_dir"] == (1.0, 0.0, 0.0) and a["post_dir"] == (0.0, 0.0, 1.0) and a["arm_hole_y"] == list(ARM_HOLES), a
    assert max(rep["sym"].values()) < 0.1, rep["sym"]
    m = rep["mirror"]
    assert m["axle_y_left"] == m["axle_y_right"] == -OFF and m["right_up_onto_post"] < 1e-3 and m["right_disc_min"] >= 2.0, m
    assert all(rep["asm"][k] < 1e-3 for k in rep["asm"] if k[0].isdigit()) and not any(rep["asm"]["final_core_overlaps"].values()), rep["asm"]
    st = rep["steer"]
    for n, lim in rep["lims"].items():
        for sg in (1, -1):
            assert st[n][sg][0] >= lim - 1e-6, (n, sg, st[n][sg], lim)
    assert min(rep["range_free"]) >= 45 and min(rep["range_powered"]) >= 30, (rep["range_free"], rep["range_powered"])
    f = rep["fits"]
    assert f["post_radial"] >= 0.3 - 1e-6 and f["stub_radial"] >= 0.3 - 1e-6 and f["boss_gap"] >= BOSS_GAP - 1e-6, f
    assert abs(f["play_up"] - BOSS_GAP) < 2e-3 and abs(f["play_down"] - DOWN_GAP) < 2e-3 and 0.3 <= f["play_total"] <= 0.5 + 2e-3, f
    assert f["washer_to_pocket"] >= 0.8 - 1e-6 and f["head_to_pocket"] >= 0.8 - 1e-6 and f["washer_on_spigot_end"] < 1e-6 and f["lock_boss_gap"] >= 0.8 + BOSS_GAP - 1e-3, f
    assert 0.3 - 1e-6 <= f["end_float"] <= 0.5 + 1e-6 and f["float_in"] >= 0.15 and f["float_out"] >= 0.15 and f["stub_vs_knuckle"] >= 0.15, f
    p = rep["port"]
    assert abs(p["len_from_flange"] - PORT_L) < 1e-6 and p["len_from_stationary"] >= PORT_L and abs(p["af"] - SHAFT_AF) < 1e-6, p
    assert abs(p["vol"] - p["vol_ref"]) < 0.05 and p["pilot_open"] and p["pilot_wall"], p
    w = rep["walls"]
    assert w["rim_top"] >= WALL_MIN and w["arm_rim"] >= WALL_MIN and w["arm_t"] >= WALL_MIN and w["plate"] >= WALL_MIN and w["kp_pilot_to_glue"] >= WALL_MIN and w["lock_pilot_to_glue"] >= WALL_MIN, w
    assert w["pocket_bore"] - (OFF - PK_R - BORE_R) < 0.1 and OFF - PK_R - BORE_R - WALL_MIN < 0.1, w
    e = rep["engage"]
    assert e["kingpin_bolt"] >= 6.0 and e["lock_bolt"] >= 5.0 and e["hub_stub"] + e["hub_hub"] >= 6.0, e
    t = rep["strength"]
    assert t["root_margin"] >= 1.5 and t["bearing_post_socket_MPa"] <= ALLOW_BEARING / 1.5 and t["bolt_pull_margin"] >= 1.5 and t["lock_pull_margin"] >= 1.5, t
    assert t["shoulder_MPa"] <= ALLOW_BEARING / 1.5 and t["boss_bearing_MPa"] <= ALLOW_BEARING / 1.5 and t["web_shear_MPa"] <= ALLOW_BEARING / 1.5, t
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
    print("report", rep, flush=True)
    check(rep)
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
