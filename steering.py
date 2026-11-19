# Steering for the RC car kit front axle: two bolt-on SteerArms, one flat TieRod per track width, a ServoMount on the JournalStub end face and one servo lever (Bellcrank). Writes Steering.FCStd; python3 make_print_project.py Steering writes Steering.3mf (AXLE_WIDE=1 style switch: STEER_WIDE=1 prints TieRod_W instead of TieRod_N).
# Frame: the axle frame of axle.py (x lateral, y fore-aft with the FRONT of the front axle at -y, z up, origin on the pivot axis). Everything here rides on the axle, so rocking never steers; Knuckle frame = kingpin is the z axis, outboard -x.
# SIMPLER THAN THE SKETCH: no Link and no second lever. The study's bellcrank only trades horn radius for lever radius (rod force is the same either way), so ONE lever (Bellcrank, radius 48) sits on the servo horn and its pin rides in a slot along the rod, which also takes up the y travel of the rod (no link, no over-centre joint). Out-of-plane angle of every pivot is 0.
# Parts: SteerArm / SteerArm_L (bolt on top of the Knuckle steering arm, U shaped so it leaves the wheel mouth, goes round the FRONT of the tyre and ends in a boss P hanging down through the rod), TieRod_N (pin to pin 171.36) / TieRod_W (224.32) with the slot, ServoMount (plate on the stub end face with 4 x M3x8 into the 4 pilots, a beam under the servo, two posts under the servo tabs), Bellcrank (lever on the horn, horn recess, boss through the rod slot).
# Levels (z): Knuckle arm 14.5 to 20.5, SteerArm 20.5 to 26.7 (touches the Knuckle arm), TieRod 15.9 to 19.7 (below the SteerArm, 0.8 gap), Bellcrank 21.2 to 26.2 (above the rod, 0.5 above the servo boss, seated on the horn top), horn plane 20.7, servo body -7.3 to 16.7, tabs 8.7 to 11.2, beam -12.3 to -8.3. Pivots are printed bosses hanging down with a 0.3 radial hole in the rod and an M3x8 + dia 7 washer from BELOW into a dia 2.8 pilot (no nuts, no clamping of the rod: 0.8 above, 0.4 below).
# Hardware: 4 x M3x12 clamp (from below through the Knuckle arm holes at y -20 and -34 into pilots in the SteerArm), 2 x M3x8 + washer at the rod pivots, 1 x M3x8 + washer at the lever pin, 4 x M3x8 mount to stub pilots: 11 M3 screws, 3 washers, no nuts; servo kit screws: 2 x M2 tab screws into dia 1.6 pilots in the posts, 1 x M2x8 horn screw.
# ASSEMBLY ORDER (each step swept or driver-proved in assembly_checks with the parts present at that step): 1 SteerArm lowered onto each Knuckle (wheels not yet on), 2 M3x12 clamp screws from below along +z, dia 6 driver; 2 wheel with its tyre already on (change to drive_hub step 9: the arm's loop round the tyre front blocks fitting the tyre afterwards) slid onto the stub from outboard; 3 TieRod lifted from below onto the two P bosses, washer and M3x8 from below at each (before the mount: the mount beam is under the rod pad); 4 ServoMount slid onto the stub end from the front, 4 x M3x8 from the front (dia 6 drivers run beside the beam and posts); 5 servo dropped in from above onto the posts, 2 M2 tab screws from above (dia 4 driver, the hole is 2.25 from the body end); 6 horn on the spline, Bellcrank lowered with its boss through the rod slot, M2 horn screw from above; 7 pin washer and M3x8 from below with the lever swung to +30 degrees (pin 24 mm off centre, 14.5 clear of the beam edge for the driver).
# Print: SteerArm -Z up (top face on the bed, boss up), TieRod +Z, Bellcrank -Z up (top face on the bed, horn recess and boss up), ServoMount +Z (beam on the bed). PLA, supports off, 0.2 layers.
# Unverified: servo, horn and spline dimensions (estimates), the printed pilots and slot wear, tab screw wall (0.25 body gap is all the 2.25 hole position allows with 1.2 walls), the rod boss fit after printing, Knuckle arm holes taken from DriveHub.
import FreeCAD as App, Part, math, os, sys
import numpy as np
from shapely.geometry import Polygon, Point
from shapely.ops import unary_union

SNAP = "/home/mikhail/Documents/cad/RC Car/"
D = {"NO_RUN": True, "__name__": "x"}
exec(compile(open(SNAP + "drive_hub.py").read(), "drive_hub.py", "exec"), D)
print_check, thin_layers = D["print_check"], D["thin_layers"]

DOC_NAME = "Steering"
OUT = "/home/mikhail/Documents/cad/RC Car/Steering.FCStd"
V = App.Vector
O = V(0, 0, 0)
X, Y, Z = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)

KX_N, KX_W = 71.68, 98.16
LOCK, ROCK, SERVO_MAX = 27.97, 13.9, 45.0
P_DX, P_DY = 14.0, 68.0
H_X, H_Y = -15.4, (-20.0, -34.0)
X_IN = 7.7
ARM_W, ARM_R, ARM_Z0, ARM_Z1 = 7.0, 4.5, 20.5, 26.7
BOSS_D, PILOT_D, PASS_D, HOLE_D = 5.6, 2.8, 3.4, 6.2
Z_BOSS = 15.5
ROD_Z0, ROD_Z1, ROD_W, ROD_PAD = 15.9, 19.7, 9.0, 10.2
LEV_R, LEV_Z0, LEV_Z1, LEV_W = 48.0, 21.2, 26.2, 10.0
HORN_Z0 = 20.7
SERVO_T = 147.0
SV_L, SV_W, SV_H, SV_TAB_W, SV_TAB_T, SV_TAB_Z, SV_HOLE, SV_SPL, SV_HORN_Z, SV_HORN_T = 23.0, 11.5, 24.0, 32.5, 2.5, 16.0, 27.5, 5.8, 28.0, 1.8
HORN_R = 13.0
SV_GAP = 0.25
YS = -(P_DY + LEV_R)
SV_ZB = HORN_Z0 - SV_HORN_Z
FACE_Y, PLATE_T = -56.0, 3.2
PIL = [(10.0, 6.0), (-10.0, 6.0), (10.0, -6.0), (-10.0, -6.0)]
HEAD_D, HEAD_H, WASH_D, WASH_T = 6.0, 3.2, 7.0, 0.5
LIM_IN, LIM_ACROSS = 15.0, 8.0


def mv(s, x=0.0, y=0.0, z=0.0):
    c = s.copy()
    c.translate(V(x, y, z))
    return c


def rotz(s, deg, cx=0.0, cy=0.0):
    c = s.copy()
    c.rotate(V(cx, cy, 0), Z, deg)
    return c


def cylz(r, z0, z1, x=0.0, y=0.0):
    return Part.makeCylinder(r, z1 - z0, V(x, y, z0), Z)


def cyly(r, y0, y1, x=0.0, z=0.0):
    return Part.makeCylinder(r, y1 - y0, V(x, y0, z), Y)


def box(x0, x1, y0, y1, z0, z1):
    return Part.makeBox(x1 - x0, y1 - y0, z1 - z0, V(x0, y0, z0))


def bar(p0, p1, w, z0, z1):
    L = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
    b = Part.makeBox(L, w, z1 - z0, V(0, -w / 2, z0))
    b.rotate(O, Z, math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0])))
    b.translate(V(p0[0], p0[1], 0))
    return b


def fuse(ss):
    r = ss[0]
    for s in ss[1:]:
        r = r.fuse(s)
    return r.removeSplitter()


def poly_solid(poly, z0, z1):
    pts = [V(x, y, z0) for x, y in list(poly.exterior.coords)[:-1]]
    return Part.Face(Part.makePolygon(pts + pts[:1])).extrude(V(0, 0, z1 - z0))


def rot2(a, v):
    c, s = math.cos(a), math.sin(a)
    return (c * v[0] - s * v[1], s * v[0] + c * v[1])


def bisect(f, lo, hi, n=70):
    flo = f(lo)
    assert flo * f(hi) <= 0, (lo, hi, flo, f(hi))
    for _ in range(n):
        m = (lo + hi) / 2
        if f(lo) * f(m) <= 0:
            hi = m
        else:
            lo = m
    return (lo + hi) / 2


def rod_state(kx, a):
    """left wheel a (rad, CCW), right wheel from the fixed rod length; returns b, left and right pivot points"""
    Dr = 2 * (kx + P_DX)
    r = rot2(a, (-P_DX, -P_DY))
    Pl = (-kx + r[0], r[1])

    def f(b):
        q = rot2(b, (P_DX, -P_DY))
        return math.hypot(kx + q[0] - Pl[0], q[1] - Pl[1]) - Dr

    b = 0.0 if abs(a) < 1e-12 else bisect(f, a, a + 0.2)
    q = rot2(b, (P_DX, -P_DY))
    return b, Pl, (kx + q[0], q[1])


def lever_phi(M, t):
    """lever angle (positive toward +x) whose pin lies on the slot line through the rod midpoint M with rod direction t"""
    h = lambda p: (math.sin(p) * LEV_R - M[0]) * t[0] + (YS + math.cos(p) * LEV_R - M[1]) * t[1]
    return bisect(h, -1.4, 1.4)


def state(kx, a):
    b, Pl, Pr = rod_state(kx, a)
    M = ((Pl[0] + Pr[0]) / 2, (Pl[1] + Pr[1]) / 2)
    L = math.hypot(Pr[0] - Pl[0], Pr[1] - Pl[1])
    t = ((Pr[0] - Pl[0]) / L, (Pr[1] - Pl[1]) / L)
    phi = lever_phi(M, t)
    T = (math.sin(phi) * LEV_R, YS + math.cos(phi) * LEV_R)
    n = (-t[1], t[0])
    return dict(a=a, b=b, Pl=Pl, Pr=Pr, M=M, psi=math.atan2(t[1], t[0]), phi=phi, T=T, u=(T[0] - M[0]) * n[0] + (T[1] - M[1]) * n[1])


def lock_states(kx):
    L = math.radians(LOCK)
    ar = bisect(lambda a: rod_state(kx, a)[0] - L, 0.0, 0.7)
    return dict(neutral=state(kx, 0.0), right=state(kx, ar), left=state(kx, -L))


def sweep_table(kx, n=161):
    lk = lock_states(kx)
    a0, a1 = lk["left"]["a"], lk["right"]["a"]
    return lk, [state(kx, a0 + (a1 - a0) * i / (n - 1)) for i in range(n)]


def node(kfx, kfy, kx=KX_N):
    return (-kx + kfx, kfy)


def build_arm(kx=KX_N):
    H1, H2, C1, C2, P = node(H_X, H_Y[0], kx), node(H_X, H_Y[1], kx), node(X_IN, -34.0, kx), node(X_IN, -P_DY, kx), node(-P_DX, -P_DY, kx)
    ss = [bar(H1, H2, ARM_W, ARM_Z0, ARM_Z1), bar(H2, C1, ARM_W, ARM_Z0, ARM_Z1), bar(C1, C2, ARM_W, ARM_Z0, ARM_Z1), bar(C2, P, ARM_W, ARM_Z0, ARM_Z1)]
    ss += [cylz(ARM_W / 2, ARM_Z0, ARM_Z1, *C1), cylz(ARM_W / 2, ARM_Z0, ARM_Z1, *C2)]
    ss += [cylz(ARM_R, ARM_Z0, ARM_Z1, *h) for h in (H1, H2, P)]
    ss.append(cylz(BOSS_D / 2, Z_BOSS, ARM_Z0 + 0.1, *P))
    a = fuse(ss)
    for h in (H1, H2):
        a = a.cut(cylz(PILOT_D / 2, ARM_Z0 - 1, ARM_Z1 + 1, *h))
    return a.cut(cylz(PILOT_D / 2, Z_BOSS - 1, 23.1, *P)).removeSplitter()


def horn_poly(buf=0.0):
    hub = Point(0, YS).buffer(3.5, 16)
    arm = Polygon([(-3.0, YS), (3.0, YS), (2.2, YS + HORN_R), (-2.2, YS + HORN_R)])
    end = Point(0, YS + HORN_R).buffer(2.8, 16)
    return unary_union([hub, arm, end]).buffer(buf, 16)


SLOT_U = (-21.6, 1.6)
ROD_REAR = SLOT_U[1] + HOLE_D / 2 + 3.0
ROD_END_R = ROD_W / 2


def build_rod(kx):
    hx = kx + P_DX
    y0 = -P_DY
    pad_f = y0 + SLOT_U[0] - HOLE_D / 2 - 2.0
    r = fuse([bar((-hx, y0), (hx, y0), ROD_W, ROD_Z0, ROD_Z1), cylz(ROD_END_R, ROD_Z0, ROD_Z1, -hx, y0), cylz(ROD_END_R, ROD_Z0, ROD_Z1, hx, y0),
              box(-ROD_PAD / 2, ROD_PAD / 2, pad_f, y0 + ROD_REAR, ROD_Z0, ROD_Z1)])
    for sx in (-hx, hx):
        r = r.cut(cylz(HOLE_D / 2, ROD_Z0 - 1, ROD_Z1 + 1, sx, y0))
    slot = fuse([box(-HOLE_D / 2, HOLE_D / 2, y0 + SLOT_U[0], y0 + SLOT_U[1], ROD_Z0 - 1, ROD_Z1 + 1), cylz(HOLE_D / 2, ROD_Z0 - 1, ROD_Z1 + 1, 0, y0 + SLOT_U[0]),
                 cylz(HOLE_D / 2, ROD_Z0 - 1, ROD_Z1 + 1, 0, y0 + SLOT_U[1])])
    return r.cut(slot).removeSplitter()


def build_lever():
    T = (0.0, YS + LEV_R)
    S = (0.0, YS)
    l = fuse([bar(S, T, LEV_W, LEV_Z0, LEV_Z1), cylz(6.0, LEV_Z0, LEV_Z1, *S), cylz(4.5, LEV_Z0, LEV_Z1, *T), cylz(BOSS_D / 2, Z_BOSS, LEV_Z0 + 0.1, *T)])
    l = l.cut(poly_solid(horn_poly(0.3), LEV_Z0 - 1, HORN_Z0 + SV_HORN_T)).cut(cylz(1.2, LEV_Z0 - 1, LEV_Z1 + 1, *S))
    return l.cut(cylz(PILOT_D / 2, Z_BOSS - 1, 23.1, *T)).removeSplitter()


def sv_geom():
    yc = YS + SV_SPL - SV_L / 2
    return dict(yc=yc, yf=yc - SV_L / 2, yr=yc + SV_L / 2, tab_f=yc - SV_TAB_W / 2, tab_r=yc + SV_TAB_W / 2, hole_f=yc - SV_HOLE / 2, hole_r=yc + SV_HOLE / 2)


def build_mount():
    g = sv_geom()
    yp = FACE_Y - PLATE_T
    z0, z1, zt = SV_ZB - 5.0, 9.0, SV_ZB + SV_TAB_Z
    ch, ct = 4.0, 2.0
    pl = [(-13.4 + ch, z0), (13.4 - ch, z0), (13.4, z0 + ch), (13.4, z1 - ct), (13.4 - ct, z1), (-13.4 + ct, z1), (-13.4, z1 - ct), (-13.4, z0 + ch)]
    pts = [V(x, FACE_Y, z) for x, z in pl]
    plate = Part.Face(Part.makePolygon(pts + pts[:1])).extrude(V(0, -PLATE_T, 0))
    zb0 = z0
    beam = box(-6.5, 6.5, g["tab_f"], yp, zb0, zb0 + 4.0)
    pw = 4.0
    rear = box(-pw, pw, g["yr"] + SV_GAP, g["tab_r"], zb0 + 3.0, zt)
    front = box(-pw, pw, g["tab_f"], g["yf"] - SV_GAP, zb0 + 3.0, zt)
    m = fuse([plate, beam, rear, front])
    for x, z in PIL:
        m = m.cut(cyly(PASS_D / 2, yp - 1, FACE_Y + 1, x, z))
    for hy in (g["hole_f"], g["hole_r"]):
        m = m.cut(cylz(0.8, zt - 4.0, zt + 1, 0, hy))
    return m.removeSplitter()


def screw(p, d, L, dia=3.0, head_d=HEAD_D, head_h=HEAD_H):
    """returns (screw solid, head solid, shank solid); p is the head bearing face centre, d the direction the shank runs"""
    sh = Part.makeCylinder(dia / 2, L, p, d)
    hd = Part.makeCylinder(head_d / 2, head_h, p - d * head_h, d)
    return sh.fuse(hd).removeSplitter(), hd, sh


def washer(x, y, z0):
    return cylz(WASH_D / 2, z0, z0 + WASH_T, x, y).cut(cylz(1.6, z0 - 1, z0 + 2, x, y))


def build_servo():
    g = sv_geom()
    S = (0.0, YS)
    b = box(-SV_W / 2, SV_W / 2, g["yf"], g["yr"], SV_ZB, SV_ZB + SV_H)
    for y0, y1, hy in ((g["tab_f"], g["yf"], g["hole_f"]), (g["yr"], g["tab_r"], g["hole_r"])):
        t = box(-SV_W / 2, SV_W / 2, y0, y1, SV_ZB + SV_TAB_Z, SV_ZB + SV_TAB_Z + SV_TAB_T)
        b = b.fuse(t.cut(cylz(1.1, SV_ZB, SV_ZB + 40, 0, hy)))
    b = b.fuse(cylz(4.5, SV_ZB + SV_H, HORN_Z0, *S)).fuse(cylz(2.4, HORN_Z0, HORN_Z0 + 1.3, *S))
    return b.cut(cylz(0.9, HORN_Z0 + 1.3 - 8.0, HORN_Z0 + 3, *S)).removeSplitter()


def build_horn():
    h = poly_solid(horn_poly(0.0), HORN_Z0, HORN_Z0 + SV_HORN_T)
    return h.cut(cylz(2.4, HORN_Z0 - 1, HORN_Z0 + 3, 0, YS)).cut(cylz(1.0, HORN_Z0 - 1, HORN_Z0 + 3, 0, YS + HORN_R))


def build_refs(kx=KX_N):
    """name -> (shape, motion group); the narrow left side is built, the right side is mirrored where listed"""
    g = sv_geom()
    S = (0.0, YS)
    R, hd = {}, {}
    H1, H2, P = node(H_X, H_Y[0], kx), node(H_X, H_Y[1], kx), node(-P_DX, -P_DY, kx)
    for i, h in enumerate((H1, H2), 1):
        R["Ref_ClampL_%d" % i], hd["Ref_ClampL_%d" % i] = (lambda t: (t[0], (t[1], t[2], V(h[0], h[1], ARM_Z0 - 6.0), Z)))(screw(V(h[0], h[1], ARM_Z0 - 6.0), Z, 12.0))
    R["Ref_PScrewL"], hd["Ref_PScrewL"] = (lambda t: (t[0], (t[1], t[2], V(P[0], P[1], Z_BOSS - 0.5), Z)))(screw(V(P[0], P[1], Z_BOSS - 0.5), Z, 8.0))
    R["Ref_PWasherL"] = washer(P[0], P[1], Z_BOSS - 0.5)
    T = (0.0, YS + LEV_R)
    R["Ref_PinScrew"], hd["Ref_PinScrew"] = (lambda t: (t[0], (t[1], t[2], V(T[0], T[1], Z_BOSS - 0.5), Z)))(screw(V(T[0], T[1], Z_BOSS - 0.5), Z, 8.0))
    R["Ref_PinWasher"] = washer(T[0], T[1], Z_BOSS - 0.5)
    for i, (x, z) in enumerate(PIL, 1):
        R["Ref_MountScrew_%d" % i], hd["Ref_MountScrew_%d" % i] = (lambda t: (t[0], (t[1], t[2], V(x, FACE_Y - PLATE_T, z), Y)))(screw(V(x, FACE_Y - PLATE_T, z), Y, 8.0))
    zt = SV_ZB + SV_TAB_Z + SV_TAB_T
    for i, hy in enumerate((g["hole_f"], g["hole_r"]), 1):
        R["Ref_TabScrew_%d" % i], hd["Ref_TabScrew_%d" % i] = (lambda t: (t[0], (t[1], t[2], V(0, hy, zt), -Z)))(screw(V(0, hy, zt), -Z, 6.0, 2.0, 4.0, 1.6))
    R["Ref_HornScrew"], hd["Ref_HornScrew"] = (lambda t: (t[0], (t[1], t[2], V(S[0], S[1], LEV_Z1), -Z)))(screw(V(S[0], S[1], LEV_Z1), -Z, 8.0, 2.0, 4.0, 1.6))
    R["Ref_Servo"] = build_servo()
    R["Ref_Horn"] = build_horn()
    return R, hd


GROUP_N = ("Knuckle", "StubYoke", "Wheel", "Tyre", "PivotBush_1", "PivotBush_2", "Sleeve_1", "Sleeve_2", "PivotScrew_U", "PivotScrew_L", "LockScrew", "HubScrew", "HubWasher")


def mirx(s):
    return s.mirror(O, X)


def load_scene():
    ax = App.openDocument(SNAP + "Axle.FCStd")
    rf = App.openDocument(SNAP + "RodFrame.FCStd")
    AX = {o.Name: o.Shape for o in ax.Objects if getattr(o, "Shape", None) and o.Shape.Solids}
    arms = ("Arm_N", "Arm_N_L", "Arm_W", "Arm_W_L")
    static = {n: s for n, s in AX.items() if not n.startswith(("Ref_N_", "Ref_W_")) and n not in arms}
    sc = dict(static=static)
    sc["arm"] = {"N": dict(L=AX["Arm_N"], R=mv(AX["Arm_N_L"], 0, 0, -160)), "W": dict(L=mv(AX["Arm_W"], 0, 0, -100), R=AX["Arm_W_L"])}
    gl = {n: AX["Ref_N_" + n] for n in GROUP_N}
    gr = {n: AX["Ref_W_" + n] for n in GROUP_N}
    sc["grp"] = {"N": dict(L=gl, R={n: mirx(s) for n, s in gl.items()}), "W": dict(R=gr, L={n: mirx(s) for n, s in gr.items()})}
    stub = static["JournalStub"]
    ys = [x.BoundBox.YMax for x in rf.getObject("Ref_Axle_F").Shape.Solids if abs(x.Volume - stub.Volume) < 2.0 and abs(x.BoundBox.XLength - stub.BoundBox.XLength) < 0.1]
    assert len(ys) == 1, ys
    global YF
    YF = ys[0] + stub.BoundBox.YMin
    fr = {}
    for o in rf.Objects:
        if not (getattr(o, "Shape", None) and o.Shape.Solids):
            continue
        if o.Name.startswith("Shown_") or o.Name in ("Ref_Springs_F", "Ref_Rod_1", "Ref_Rod_2", "Ref_Nuts", "Ref_Screws", "GearboxCradle"):
            s = o.Shape.copy()
            s.translate(V(0, -YF, 0))
            s.rotate(O, Z, 180.0)
            fr[o.Name] = s
    sc["frame"] = fr
    return sc


YF = 186.1


def mine_neutral(wide):
    """name -> (shape, motion group) at the neutral pose; the narrow left side is built, the right side mirrored, wide moves the arm groups outboard"""
    R, hd = build_refs()
    arm = build_arm()
    m = {"SteerArm": (arm, "armL"), "SteerArm_L": (mirx(arm), "armR"), "TieRod": (build_rod(KX_W if wide else KX_N), "rod"), "Bellcrank": (build_lever(), "lev"), "ServoMount": (build_mount(), "fix")}
    grp = lambda n: "armL" if n.startswith(("Ref_ClampL", "Ref_PScrewL", "Ref_PWasherL")) else "lev" if n in ("Ref_PinScrew", "Ref_PinWasher", "Ref_Horn", "Ref_HornScrew") else "fix"
    for n, s in R.items():
        m[n] = (s, grp(n))
        if grp(n) == "armL":
            m[n.replace("ClampL", "ClampR").replace("ScrewL", "ScrewR").replace("WasherL", "WasherR")] = (mirx(s), "armR")
    if wide:
        dx = KX_W - KX_N
        m = {n: ((mv(s, -dx) if g == "armL" else mv(s, dx) if g == "armR" else s), g) for n, (s, g) in m.items()}
    return m, hd


def put_mine(m, kx, stt, rock=0.0):
    out = {}
    a, b = math.degrees(stt["a"]), math.degrees(stt["b"])
    for n, (s, g) in m.items():
        if g == "armL":
            s = rotz(s, a, -kx, 0)
        elif g == "armR":
            s = rotz(s, b, kx, 0)
        elif g == "rod":
            s = mv(rotz(s, math.degrees(stt["psi"]), 0, -P_DY), stt["M"][0], stt["M"][1] + P_DY)
        elif g == "lev":
            s = rotz(s, -math.degrees(stt["phi"]), 0, YS)
        if rock:
            s = s.copy()
            s.rotate(O, Y, rock)
        out[n] = s
    return out


def put_others(sc, wide, kx, stt):
    gk = "W" if wide else "N"
    out = {n: (s, "axle") for n, s in sc["static"].items()}
    out["Arm_L"] = (sc["arm"][gk]["L"], "axle")
    out["Arm_R"] = (sc["arm"][gk]["R"], "axle")
    for side, ang, cx in (("L", math.degrees(stt["a"]), -kx), ("R", math.degrees(stt["b"]), kx)):
        for n, s in sc["grp"][gk][side].items():
            out["%s_%s" % (side, n)] = (rotz(s, ang, cx, 0), "wheel" if n in ("Wheel", "Tyre") else "axle")
    return out


JOINT = set()


def _jn(a, bs):
    for b in bs:
        JOINT.add(frozenset((a, b)))


for _s in "LR":
    _arm = "SteerArm" if _s == "L" else "SteerArm_L"
    _jn(_arm, [_s + "_Knuckle", "TieRod", "Ref_PScrew" + _s, "Ref_PWasher" + _s] + ["Ref_Clamp%s_%d" % (_s, i) for i in (1, 2)])
    _jn("TieRod", ["Ref_PScrew" + _s, "Ref_PWasher" + _s])
    _jn("Ref_PScrew" + _s, ["Ref_PWasher" + _s])
    _jn(_s + "_Knuckle", ["Ref_Clamp%s_%d" % (_s, i) for i in (1, 2)])
_jn("TieRod", ["Bellcrank", "Ref_PinScrew", "Ref_PinWasher"])
_jn("Bellcrank", ["Ref_Horn", "Ref_Servo", "Ref_HornScrew", "Ref_PinScrew", "Ref_PinWasher"])
_jn("Ref_PinScrew", ["Ref_PinWasher"])
_jn("Ref_Horn", ["Ref_Servo", "Ref_HornScrew"])
_jn("Ref_HornScrew", ["Ref_Servo"])
_jn("ServoMount", ["Ref_Servo", "Ref_TabScrew_1", "Ref_TabScrew_2", "JournalStub"] + ["Ref_MountScrew_%d" % i for i in range(1, 5)])
_jn("Ref_Servo", ["Ref_TabScrew_1", "Ref_TabScrew_2"])
_jn("JournalStub", ["Ref_MountScrew_%d" % i for i in range(1, 5)])


def near(a, b, tol):
    bb = V(tol, tol, tol)
    ba, bc = a.BoundBox, b.BoundBox
    return not (ba.XMax + tol < bc.XMin or bc.XMax + tol < ba.XMin or ba.YMax + tol < bc.YMin or bc.YMax + tol < ba.YMin or ba.ZMax + tol < bc.ZMin or bc.ZMax + tol < ba.ZMin)


def pairmin(A, B, tol, skip_same=False):
    """minimum distance over near pairs; returns (value, names)"""
    best = (1e9, None)
    for na, sa in A.items():
        for nb, sb in B.items():
            if na == nb or frozenset((na, nb)) in JOINT or not near(sa, sb, tol):
                continue
            d = sa.distToShape(sb)[0]
            if d < best[0]:
                best = (d, (na, nb))
    return best


def clearance(sc, wide, steer_keys, rocks):
    kx = KX_W if wide else KX_N
    m, hd = mine_neutral(wide)
    lk = steer_states(kx)
    res = dict(frame=(1e9, None), wheel=(1e9, None), axle=(1e9, None), self=(1e9, None), joint={})
    upd = lambda k, v: res.__setitem__(k, v) if v[0] < res[k][0] else None
    for key in steer_keys:
        stt = lk[key]
        mine = put_mine(m, kx, stt)
        oth = put_others(sc, wide, kx, stt)
        for cat in ("wheel", "axle"):
            upd(cat, pairmin({n: s for n, s in mine.items()}, {n: s for n, (s, c) in oth.items() if c == cat}, 3.0))
        names = list(mine)
        for i, na in enumerate(names):
            for nb in names[i + 1:]:
                if not near(mine[na], mine[nb], 3.0):
                    continue
                d = mine[na].distToShape(mine[nb])[0]
                if frozenset((na, nb)) in JOINT:
                    k = tuple(sorted((na, nb)))
                    res["joint"][k] = min(res["joint"].get(k, 1e9), d)
                else:
                    upd("self", (d, (na, nb, key)))
        for rock in rocks:
            mr = put_mine(m, kx, stt, rock)
            upd("frame", pairmin(mr, sc["frame"], 3.0))
    return res


def steer_states(kx):
    lk = lock_states(kx)
    for k, d in (("l12", -12.0), ("r12", 12.0), ("l20", -20.0), ("r20", 20.0)):
        lk[k] = state(kx, math.radians(d))
    return lk


def phi_state(kx, phi_deg):
    a = bisect(lambda a: state(kx, a)["phi"] - math.radians(phi_deg), -0.6, 0.6, 50)
    return state(kx, a)


def vol(a, b):
    return a.common(b).Volume if near(a, b, 0.0) else 0.0


def sweep(mov, fixed, v, length, step=1.0):
    """largest common volume while mov (dict) travels along unit v, ending at its drawn position"""
    worst = 0.0
    for k in range(int(round(length / step)) + 1):
        off = v * (-length + k * step)
        for a in mov.values():
            m = mv(a, off.x, off.y, off.z)
            for b in fixed.values():
                if near(m, b, 0.0):
                    worst = max(worst, m.common(b).Volume)
    return round(worst, 4)


def driver(p, d, L=60.0, r=3.0):
    """dia 6 driver starting at the head back face p and running back along -d"""
    return Part.makeCylinder(r, L, p, -d)


def axis_len(s, d):
    b = s.BoundBox
    return max(b.XLength * abs(d.x), b.YLength * abs(d.y), b.ZLength * abs(d.z))


PRINT_UP = dict(SteerArm=("-", "Z"), SteerArm_L=("-", "Z"), TieRod_N=("+", "Z"), TieRod_W=("+", "Z"), ServoMount=("+", "Z"), Bellcrank=("-", "Z"))
COPIES = dict(SteerArm=1, SteerArm_L=1, TieRod_N=1, TieRod_W=1, ServoMount=1, Bellcrank=1)


def build_parts():
    m, hd = mine_neutral(False)
    P = dict(SteerArm=m["SteerArm"][0], SteerArm_L=m["SteerArm_L"][0], TieRod_N=m["TieRod"][0], TieRod_W=build_rod(KX_W), ServoMount=m["ServoMount"][0], Bellcrank=m["Bellcrank"][0])
    return P, m, hd


def kin_report(kx):
    lk, tab = sweep_table(kx, 241)
    r = {}
    for key, inner_is in (("left", "a"), ("right", "b")):
        st = lk[key]
        ang = (abs(math.degrees(st["a"])), abs(math.degrees(st["b"])))
        inner, outer = max(ang), min(ang)
        r[key] = dict(inner=round(inner, 3), outer=round(outer, 3), phi=round(abs(math.degrees(st["phi"])), 2))
    a = np.array([s["a"] for s in tab])
    phi = np.array([s["phi"] for s in tab])
    b = np.array([s["b"] for s in tab])
    r["monotone"] = bool(np.all(np.diff(phi) > 0) and np.all(np.diff(b) > 0))
    r["u"] = (round(min(s["u"] for s in tab), 3), round(max(s["u"] for s in tab), 3))
    cosg = []
    for s in tab:
        t = (math.cos(s["psi"]), math.sin(s["psi"]))
        v = (math.cos(s["phi"]), -math.sin(s["phi"]))
        cosg.append(abs(v[0] * t[0] + v[1] * t[1]))
    r["lever_cos"] = round(min(cosg), 3)
    arm = []
    for s in tab:
        t = (math.cos(s["psi"]), math.sin(s["psi"]))
        for P, K in ((s["Pl"], (-kx, 0.0)), (s["Pr"], (kx, 0.0))):
            rr = (P[0] - K[0], P[1] - K[1])
            arm.append(abs(rr[0] * t[1] - rr[1] * t[0]))
    r["arm_min"] = round(min(arm), 2)
    r["arm_neutral"] = round(math.hypot(P_DX, P_DY), 2)
    dphi = np.gradient(phi, a)
    db = np.gradient(b, a)
    Te = SERVO_T * dphi / (1.0 + db)
    r["T_each_min"] = round(float(Te.min()), 1)
    r["T_total_min"] = round(float(2 * Te.min()), 1)
    r["rod_travel"] = round(abs(lk["right"]["M"][0]), 2)
    r["oop_deg"] = 0.0
    return r, lk


NEED_T = 126.0


def strength():
    F, Fh = 12.0, 15.0
    t_arm = ARM_Z1 - ARM_Z0
    M_root = F * (P_DY + H_Y[1])
    out = dict(arm_root_MPa=round(6 * M_root / (t_arm * ARM_W ** 2), 2))
    dy = abs(H_Y[0] - H_Y[1])
    Fs = math.hypot(F * (P_DY + (H_Y[0] + H_Y[1]) / 2) / dy, F / 2)
    eng = 12.0 - 6.0
    out["clamp_screw_N"] = round(Fs, 1)
    out["clamp_bearing_MPa"] = round(Fs / (3.0 * eng), 2)
    out["clamp_thread_shear_MPa"] = round(Fs / (math.pi * 3.0 * eng), 2)
    g = sv_geom()
    M = Fh * abs(YS - FACE_Y)
    T = M / 20.0 / 2.0
    out["mount_tension_N"] = round(T, 1)
    out["mount_thread_shear_MPa"] = round(T / (math.pi * 3.0 * (8.0 - PLATE_T)), 2)
    out["mount_head_bearing_MPa"] = round(T / (math.pi / 4 * (HEAD_D ** 2 - PASS_D ** 2)), 2)
    out["mount_beam_MPa"] = round(6 * M / (4.0 * 13.0 ** 2), 2)
    return out


def print_report(P):
    r = {}
    for n, s in P.items():
        r[n] = dict(valid=(s.isValid(), len(s.Solids)), cm3=round(s.Volume / 1000, 2), size=tuple(round(v, 1) for v in (s.optimalBoundingBox(False, False).XLength, s.optimalBoundingBox(False, False).YLength, s.optimalBoundingBox(False, False).ZLength)),
                    pc=print_check(s, PRINT_UP[n]), thin=thin_layers(s, PRINT_UP[n]))
    return r


def assembly_checks(sc):
    kx = KX_N
    m, hd = mine_neutral(False)
    lk = steer_states(kx)
    neutral = lk["neutral"]
    mine = put_mine(m, kx, neutral)
    oth = {n: s for n, (s, c) in put_others(sc, False, kx, neutral).items()}
    ALL = dict(mine, **oth)
    r = {}
    sel = lambda excl_names=(), excl_prefix=(): {n: s for n, s in ALL.items() if n not in excl_names and not n.startswith(tuple(excl_prefix))}
    wheels = ("L_Wheel", "L_Tyre", "R_Wheel", "R_Tyre")
    late = ("TieRod", "Bellcrank", "Ref_Horn", "Ref_HornScrew", "Ref_PinScrew", "Ref_PinWasher", "Ref_PScrewL", "Ref_PScrewR", "Ref_PWasherL", "Ref_PWasherR", "Ref_Servo", "Ref_TabScrew_1", "Ref_TabScrew_2", "ServoMount") + tuple("Ref_MountScrew_%d" % i for i in range(1, 5))

    def drv(name, present, L=60.0):
        h, sh, p, d = hd_all[name]
        back = p - d * axis_len(h, d)
        c = driver(back, d, L, 2.0 if name.startswith(("Ref_TabScrew", "Ref_HornScrew")) else 3.0)
        return max([c.common(s).Volume for n, s in present.items() if n != name and near(c, s, 0.0)] or [0.0])
    hd_all = {}
    for n, (h, sh, p, d) in hd.items():
        hd_all[n] = (h, sh, p, d)
        if n.startswith(("Ref_ClampL", "Ref_PScrewL")):
            hd_all[n.replace("ClampL", "ClampR").replace("PScrewL", "PScrewR")] = (mirx(h), mirx(sh), V(-p.x, p.y, p.z), V(-d.x, d.y, d.z))
    # step 1: arms drop onto the Knuckle arms, clamp screws from below (wheels not yet on)
    s1 = sel(late + wheels + ("SteerArm", "SteerArm_L", "Ref_ClampL_1", "Ref_ClampL_2", "Ref_ClampR_1", "Ref_ClampR_2"))
    r["1_arm_drop"] = sweep({"SteerArm": mine["SteerArm"], "SteerArm_L": mine["SteerArm_L"]}, {n: s for n, s in s1.items() if n not in ("L_Knuckle", "R_Knuckle")}, -Z, 40.0)
    s1b = dict(s1, SteerArm=mine["SteerArm"], SteerArm_L=mine["SteerArm_L"])
    for n in ("Ref_ClampL_1", "Ref_ClampL_2", "Ref_ClampR_1", "Ref_ClampR_2"):
        r["1_driver_" + n] = drv(n, dict(s1b, **{k: ALL[k] for k in ("Ref_ClampL_1", "Ref_ClampL_2", "Ref_ClampR_1", "Ref_ClampR_2")}))
    # step 2: wheel and tyre (tyre already on the wheel) slide onto the stub from outboard
    fx = {n: s for n, s in sel(late + wheels + tuple("L_" + k for k in ("HubScrew", "HubWasher")) + tuple("R_" + k for k in ("HubScrew", "HubWasher"))).items() if not n.startswith(("L_", "R_"))}
    r["2_wheel_L"] = sweep({"W": oth["L_Wheel"], "T": oth["L_Tyre"]}, fx, X, 40.0)
    r["2_wheel_R"] = sweep({"W": oth["R_Wheel"], "T": oth["R_Tyre"]}, fx, -X, 40.0)
    # step 3: rod lifted from below onto the P bosses, washers and screws from below (wheels on, mount not yet)
    s3 = sel(("TieRod", "Bellcrank", "Ref_Horn", "Ref_HornScrew", "Ref_PinScrew", "Ref_PinWasher", "Ref_PScrewL", "Ref_PScrewR", "Ref_PWasherL", "Ref_PWasherR", "Ref_Servo", "Ref_TabScrew_1", "Ref_TabScrew_2", "ServoMount") + tuple("Ref_MountScrew_%d" % i for i in range(1, 5)))
    r["3_rod_up"] = sweep({"TieRod": mine["TieRod"]}, s3, Z, 40.0)
    s3b = dict(s3, TieRod=mine["TieRod"])
    for n in ("Ref_PScrewL", "Ref_PScrewR"):
        r["3_driver_" + n] = drv(n, dict(s3b, **{k: ALL[k] for k in ("Ref_PScrewL", "Ref_PScrewR", "Ref_PWasherL", "Ref_PWasherR")}))
    # step 4: mount slides onto the stub end from the front, 4 screws from the front
    s4 = sel(("Bellcrank", "Ref_Horn", "Ref_HornScrew", "Ref_PinScrew", "Ref_PinWasher", "Ref_Servo", "Ref_TabScrew_1", "Ref_TabScrew_2", "ServoMount") + tuple("Ref_MountScrew_%d" % i for i in range(1, 5)))
    r["4_mount_in"] = sweep({"ServoMount": mine["ServoMount"]}, s4, Y, 40.0)
    s4b = dict(s4, ServoMount=mine["ServoMount"])
    for i in range(1, 5):
        r["4_driver_%d" % i] = drv("Ref_MountScrew_%d" % i, dict(s4b, **{"Ref_MountScrew_%d" % j: ALL["Ref_MountScrew_%d" % j] for j in range(1, 5)}))
    # step 5: servo dropped in from above, tab screws from above
    s5 = sel(("Bellcrank", "Ref_Horn", "Ref_HornScrew", "Ref_PinScrew", "Ref_PinWasher", "Ref_Servo", "Ref_TabScrew_1", "Ref_TabScrew_2"))
    r["5_servo_down"] = sweep({"Ref_Servo": mine["Ref_Servo"]}, s5, -Z, 40.0)
    s5b = dict(s5, Ref_Servo=mine["Ref_Servo"], Ref_TabScrew_1=ALL["Ref_TabScrew_1"], Ref_TabScrew_2=ALL["Ref_TabScrew_2"])
    for n in ("Ref_TabScrew_1", "Ref_TabScrew_2"):
        r["5_driver_" + n] = drv(n, s5b)
    # step 6: horn on the spline, lever lowered with its boss through the slot, horn screw from above
    s6 = sel(("Bellcrank", "Ref_HornScrew", "Ref_PinScrew", "Ref_PinWasher"))
    r["6_lever_down"] = sweep({"Bellcrank": mine["Bellcrank"]}, s6, -Z, 40.0)
    s6b = dict(s6, Bellcrank=mine["Bellcrank"], Ref_HornScrew=ALL["Ref_HornScrew"])
    r["6_driver_horn"] = drv("Ref_HornScrew", s6b)
    # step 7: pin washer and screw from below with the lever swung to +30 degrees
    st30 = phi_state(kx, 30.0)
    mine30 = put_mine(m, kx, st30)
    oth30 = {n: s for n, (s, c) in put_others(sc, False, kx, st30).items()}
    ALL30 = dict(mine30, **oth30)
    h, sh, p, d = hd_all["Ref_PinScrew"]
    pin = rotz(h, -math.degrees(st30["phi"]), 0, YS)
    c = driver(V(st30["T"][0], st30["T"][1], p.z - axis_len(h, d)), d)
    r["7_pin_driver"] = max([c.common(s).Volume for n, s in ALL30.items() if near(c, s, 0.0)] or [0.0])
    r["7_pin_x"] = round(st30["T"][0], 2)
    r["7_beam_edge_gap"] = round(st30["T"][0] - 3.0 - 6.5, 2)
    return r, hd_all, mine


def seat_checks(mine, hd_all, sc):
    kx = KX_N
    oth = {n: s for n, (s, c) in put_others(sc, False, kx, state(kx, 0.0)).items()}
    ALL = dict(mine, **oth)
    out = {}
    pairs = []
    for side, arm, kn in (("L", "SteerArm", "L_Knuckle"), ("R", "SteerArm_L", "R_Knuckle")):
        for i in (1, 2):
            pairs.append(("Ref_Clamp%s_%d" % (side, i), kn, arm, None))
        pairs.append(("Ref_PScrew" + side, "Ref_PWasher" + side, arm, "Ref_PWasher" + side))
    pairs.append(("Ref_PinScrew", "Ref_PinWasher", "Bellcrank", "Ref_PinWasher"))
    for i in range(1, 5):
        pairs.append(("Ref_MountScrew_%d" % i, "ServoMount", "JournalStub", None))
    for i in (1, 2):
        pairs.append(("Ref_TabScrew_%d" % i, "Ref_Servo", "ServoMount", None))
    pairs.append(("Ref_HornScrew", "Bellcrank", "Ref_Servo", None))
    for scr, seat, host, wash in pairs:
        h, sh, p, d = hd_all[scr]
        seat_d = h.distToShape(ALL[seat])[0]
        e = {}
        e["seat_gap"] = round(seat_d, 6)
        if wash:
            e["washer_on_host"] = round(ALL[wash].distToShape(ALL[host])[0], 6)
        com = sh.common(ALL[host])
        e["engaged_mm"] = round(axis_len(com, d), 2) if com.Volume > 1e-9 else 0.0
        out[scr] = e
    return out


def verify():
    rep = {}
    P, m, hd = build_parts()
    rep["parts"] = print_report(P)
    sc = load_scene()
    rep["kin"] = {"N": kin_report(KX_N)[0], "W": kin_report(KX_W)[0]}
    keys = ("left", "l20", "l12", "neutral", "r12", "r20", "right")
    rep["clear_N"] = clearance(sc, False, keys, (-ROCK, 0.0, ROCK))
    rep["clear_W"] = clearance(sc, True, ("left", "right"), (-ROCK, 0.0, ROCK))
    rep["asm"], hd_all, mine = assembly_checks(sc)
    rep["seat"] = seat_checks(mine, hd_all, sc)
    rep["strength"] = strength()
    tyre = sc["grp"]["N"]["L"]["Tyre"].BoundBox
    rep["servo_ahead"] = dict(tyre_front=round(tyre.YMin, 2), servo_front=round(mine["Ref_Servo"].BoundBox.YMin, 2), body_front=round(sv_geom()["yf"], 2),
                              mount_front=round(mine["ServoMount"].BoundBox.YMin, 2))
    rep["screws"] = dict(M3=sum(1 for n in mine if n.startswith(("Ref_Clamp", "Ref_PScrew", "Ref_PinScrew", "Ref_MountScrew"))), M2=sum(1 for n in mine if n.startswith(("Ref_TabScrew", "Ref_HornScrew"))),
                         washers=sum(1 for n in mine if "Washer" in n))
    return rep, P, mine


def check(rep):
    for n, r in rep["parts"].items():
        assert r["valid"] == (True, 1), (n, r)
        pc = r["pc"]
        assert not pc["p1"] and not pc["p2"] and not pc["p5"] and pc["floor"] >= 60.0 and pc["thin_mm2"] < 0.5, (n, pc)
        assert r["thin"][0] <= 0.3, (n, r["thin"])
    assert sum(r["cm3"] for n, r in rep["parts"].items() if n != "TieRod_W") + rep["parts"]["TieRod_W"]["cm3"] <= 35.0, rep["parts"]
    for w, k in rep["kin"].items():
        for side in ("left", "right"):
            assert abs(k[side]["inner"] - LOCK) < 1e-6 and LOCK - 4.0 < k[side]["outer"] <= LOCK + 1e-9 and k[side]["phi"] <= SERVO_MAX, (w, k)
        assert k["monotone"] and k["lever_cos"] >= 0.5 and k["arm_min"] >= 0.75 * k["arm_neutral"] and k["oop_deg"] == 0.0, (w, k)
        assert k["u"][0] - SLOT_U[0] >= 1.5 and SLOT_U[1] - k["u"][1] >= 1.5 and ROD_REAR - (SLOT_U[1] + HOLE_D / 2) >= 3.0, (w, k["u"])
    for w in ("clear_N", "clear_W"):
        c = rep[w]
        assert c["frame"][0] >= 0.8 and c["wheel"][0] >= 2.0 and c["axle"][0] >= 0.8 and c["self"][0] >= 0.8, (w, c)
        assert c["joint"][("Bellcrank", "Ref_Servo")] >= 0.5 - 1e-6, c["joint"]
        for k, v in c["joint"].items():
            if k in (("SteerArm", "TieRod"), ("SteerArm_L", "TieRod"), ("Bellcrank", "TieRod")) or "Washer" in k[0] + k[1] and "TieRod" in k:
                assert v >= 0.15, (w, k, v)
    for k, v in rep["asm"].items():
        if k[0].isdigit() and not k.startswith("7_pin_x") and not k.startswith("7_beam"):
            assert v < 1e-3, (k, v)
    assert rep["asm"]["7_beam_edge_gap"] >= 10.0
    for n, e in rep["seat"].items():
        assert e["seat_gap"] < 1e-6 and e.get("washer_on_host", 0.0) < 1e-6, (n, e)
        need = 5.5 if n.startswith("Ref_Clamp") else 6.5 if "Scr" in n and n.startswith(("Ref_PScrew", "Ref_PinScrew")) else 4.5 if n.startswith("Ref_Mount") else 3.0
        assert need <= e["engaged_mm"] <= (7.5 if n.startswith("Ref_Mount") else 99.0), (n, e)
    s = rep["strength"]
    assert s["arm_root_MPa"] <= LIM_IN and s["clamp_bearing_MPa"] <= LIM_IN and s["clamp_thread_shear_MPa"] <= LIM_ACROSS, s
    assert s["mount_thread_shear_MPa"] <= LIM_ACROSS and s["mount_head_bearing_MPa"] <= LIM_IN and s["mount_beam_MPa"] <= LIM_IN, s
    assert rep["screws"]["M3"] <= 16 and rep["screws"]["M3"] + rep["screws"]["M2"] <= 16 + 3, rep["screws"]


def put(doc, name, shape):
    assert shape.isValid() and len(shape.Solids) == 1, name
    o = doc.addObject("Part::Feature", name)
    o.Shape = shape
    return o


def main():
    rep, P, mine = verify()
    for k, v in rep.items():
        print("report", k, v, flush=True)
    check(rep)
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    for n in ("SteerArm", "SteerArm_L", "ServoMount", "Bellcrank"):
        put(doc, n, mine[n])
    put(doc, "TieRod_N", mine["TieRod"])
    put(doc, "TieRod_W", mv(P["TieRod_W"], 0, 0, 40.0))
    for n, s in mine.items():
        if n.startswith("Ref_"):
            put(doc, n, s)
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
