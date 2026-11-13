# CVT motor module for a flat cardboard floor, PINCHED disc: GA37RG upright on the Lid (glued over one window), Disc hangs through it; a 15.5 mm Wheel (small LEGO tire 14.5 x 6.23, ID 11.2, stretched onto a 12.2 rim, trim its inner rib flush (it would stretch 33 pct), measure OD after fitting) and a free Roller grip the Disc from below and above inside one C-shaped Shuttle, so the clamp force cancels in the Disc.
# Window 97.2 x 101.7 mm in the 4 mm cardboard (x -41.8..55.4, y -50.85..50.85, origin on motor axis; hanging parts 93.2 x 97.7 plus 2 mm margin), Lid 117.2 x 121.7 x 5, dia 5 glue holes. Through shaft axis 29 below the floor underside (FLOOR_T 4 unconfirmed); lowest point 18.3 below the shaft axis (ServoArm underside; the three horn screw heads and the arm pin head are counterbored flush into it). Hanger bores are relieved 0.6 mm upward so the shaft can lift as the tyre squeezes. Hanger and Shuttle bores are 9.9 on the 8 AF hex (corner dia 9.24): 0.33 per side on the corners, so both slide freely (grease them).
# Ratio (contact radius / tyre radius 7.75) 2.06 to 3.35 forward only (contact radius 16 to 26 mm, travel 10 mm), reverse by running the motor backwards; 100 RPM gives 206 to 335 RPM. Print the Disc on a textured plate for more grip. Shift while the disc is turning. The Wheel with tyre (15.5 OD) squeezes 0.3 mm past the Disc face while it is slid in from +x (soft tyre, expected, it is the pinch squeeze).
# Clamp: design 35 N (20 to 40), set by two rubber rings (2 mm wire) at x +-6.8, round the Shuttle top bar and the cross pin on the RollerSlider, kept outboard of the hub; check on a kitchen scale pressing the roller. Back the rings off when parked (roller on PLA disc is about 36 MPa Hertz at 35 N). Shuttle sits on the shaft by two bearing collars either side of the Wheel (carry it along the shaft), so the force stays inside it.
# Disc hub: M3x6 lock screw from -x onto the D flat (usable engage 8.5). Shuttle top bar passes 0.8 from the hub at the innermost position. Servo is flipped (spline down), horn trimmed to 9 mm each side, ServoArm 12 mm, MG995 gives about 76 N at the ends. The pin pushes 31.9 off the shaft line and 9.5 below it, so the shuttle has a 42 mm tail, a 5 mm thick web rib under the shaft (45 degree gusset, rises from the print bed, 0.28 mm out of plane flex at the pitch load) ending in a third bearing collar: the guide spans 54 mm. Binding is tolerated up to friction 0.88 when the tail carries the pitch (it engages first: the tail collar needs 0.33 mm of tilt, the near pair 3.6 times more) and 0.52 in the worst case where only the near collar pair does (measured centre to centre: 0.82 and 0.43, that case needs 1.7 mm of tail flex). The Shuttle base plate is the lug (2.4 mm, 0.5 under the tyre), centred between the servo underside and the ServoArm: 0.95 each side once the servo screws pull the tabs up to the posts (0.2 slide in gap), servo height tolerance plus or minus 0.9 mm, so the roll stop holds under 2 deg. The lug slot is full round at its closed end 0.3 behind the pin's nearest position, prong lever 1.4 mm. Margins with that side friction: shifting while rolling 1.8 greased (0.8 dry), stopped 1.2 greased (0.5 dry): shift only while the disc turns, and grease the shaft bores.
# Hardware: 6 x M3x8 motor (up through lid), 1 x M3x6 disc lock, 4 x M3x10 servo (pilots in 4 posts, M3 washers between tab and post if a servo sits high), 1 x M3 horn screw + 2 x dia 2 horn screws (heads counterbored into the ServoArm underside), MG995 (brands vary, check body and holes), M3x16 roller axle, M3x8 arm pin screw (steel, from below, counterbored), M3x20 + nut cross pin, 2 x DriveCoupler + M3x16 (wheel_mount.py), rubber rings, and one small LEGO tire (measured 14.5 OD x 6.23 wide, ID 11.2; stretches onto the 12.2 rim to 15.5 OD): trim or squash the tire's inner rib so it sits flat (untrimmed it would stretch 33 pct). Grease the collars and roller axle (and the shaft inside the Shuttle bore): required to drive (dry losses are 68 pct of motor torque at the outer position, 42 inner; greased 23 and 14).
# Assembly (bench, Lid NOT yet in the floor, steps checked by the sweeps in verify): 1 motor, six screws from below; 2 Disc up onto D shaft, set its height with the pinch closed, lock screw; 3 Shuttle with RollerSlider and Roller (slider pushed up) slid in from -x over the Disc; 4 Wheel+tyre slid in from +x into the Shuttle pocket (before the servo, the servo body blocks this path); 5 cross pin, rubber rings; 6 servo slid in from +x under its four posts, screws up from below; 7 ServoArm up onto the horn from below, arm pin screw from below into the lug slot; 8 lower the whole module into the floor window and glue the Lid to the floor (the slider post and servo only clear the floor from above); 9 push the ThroughShaft in from the rear; 10 couplers last.
# All PLA, no supports, no TPU. Lid prints top face down; Shuttle on its leg face (-x); Wheel and Roller flat; Slider upright (use a brim).
import FreeCAD as App, Part, math

D = {"NO_RUN": True, "__name__": "differential"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/differential.py").read(), "differential.py", "exec"), D)
V, O, box, prism, rot, cyl, vcyl, hexprism = (D[k] for k in ("V", "O", "box", "prism", "rot", "cyl", "vcyl", "hexprism"))
SHAFT_AF = D["SHAFT_AF"]

DOC_NAME = "CvtModule"
OUT = "/home/mikhail/Documents/cad/RC Car/CvtModule.FCStd"
Y, Z = V(0, 1, 0), V(0, 0, 1)

SOCKET, BORE, PS_PILOT, PILOT, PS_OUT = 8.3, 9.9, 5.9, 2.8, 16.0
CPL_D, CPL_L, CPL_PIN, END_GAP = 14.0, 17.5, 4.0, 0.25
BOSS_L = PS_OUT - PS_PILOT - CPL_PIN - END_GAP

FLOOR_T, FLOOR_Z, LID_T, LID_M, WIN_M, LID_R, GH = 4.0, 29.0, 5.0, 10.0, 2.0, 8.0, 5.5
LID_Z0 = FLOOR_Z + FLOOR_T
LID_Z1 = LID_Z0 + LID_T

MOT_GB_D, MOT_GB_L, MOT_CAN_D, MOT_BODY = 37.0, 24.5, 36.2, 57.8
MOT_SH_D, MOT_FLAT_AF, MOT_FLAT_L, MOT_SH_L, MOT_BOSS_D, MOT_BOSS_L = 6.0, 5.5, 14.0, 20.0, 12.0, 5.0
MOT_PCD, MOT_HOLE_D, MOT_CB_D, MOT_CB_DEEP, MOT_BOSS_HOLE = 31.0, 3.4, 6.2, 2.5, 12.6
MOT_RPM, MOT_NM, MOT_ROT = 100.0, 0.44, 0.0
MOT_TIP = LID_Z1 - MOT_SH_L

SV_L, SV_W, SV_H = 40.7, 19.7, 36.5
SV_TAB_T, SV_TAB_Z, SV_TAB_SPAN, SV_HOLE_L, SV_HOLE_W = 2.5, 27.5, 54.5, 49.5, 10.2
SV_AXIS_END, SV_SPLINE_D, SV_SPLINE_TOP, SV_NM = 10.2, 5.0, 44.0, 1.0
HORN_R, HORN_W, HORN_T, HORN_HUB, HORN_Z = 9.0, 6.0, 1.5, 7.0, 41.0
HORN_HOLE_D, HORN_HOLE_PITCH, HORN_CENTRE_D = 2.0, 14.0, 3.2

TYRE_OD_FREE, TYRE_W, TYRE_ID, TYRE_RIB_W, TYRE_RIB_H = 14.5, 6.23, 11.2, 1.25, 1.0
RIM_D, HEX_BORE, LIP_H, LIP_V, SQUEEZE = 12.2, 8.4, 0.6, 0.2, 0.3
RIM_R = RIM_D / 2
R_T = (RIM_D + TYRE_OD_FREE - TYRE_ID) / 2
WH_H = TYRE_W / 2 + LIP_H + LIP_V

S_MIN, S_MAX = 16.0, 26.0
DISC_R, DISC_T, HUB_R, DISC_BORE, DISC_FLAT_AF = 32.0, 4.0, 7.0, 6.3, 5.8
Z_FACE = R_T - SQUEEZE
DISC_TOP = Z_FACE + DISC_T
HUB_TOP, LOCK_H = 26.5, 14.5

RR, RW, RBORE, AX_D = 3.0, 5.0, 3.2, 3.0
RING_XC, RING_W, RING_T, SLOT_UP, K_TYRE, F_MAX = 6.8, 2.0, 2.0, 0.6, 70.0, 40.0
COL_L, COL_GAP, BORE_C = 4.0, 0.3, 9.9
PK = WH_H + COL_GAP
FY = PK + COL_L
LEG_T, LEG_GAP = 8.0, 0.8
LEG_X1 = -(math.sqrt(DISC_R ** 2 - (S_MIN - FY) ** 2) + LEG_GAP)
LEG_X0 = LEG_X1 - LEG_T
PL_X1, PL_Z1 = 8.2, BORE_C / 2 + 1.75
SV_GAP, LUG_T, LUG_X1, TAIL_L = 0.2, 2.4, 38.5, 42.0
BASE_Z1 = -(R_T + 0.5)
BASE_Z0 = BASE_Z1 - LUG_T
TAIL_W, TAIL_WALL, TAIL_CZ, TAIL_XT, TAIL_SLOPE = 5.0, 2.4, 6.9, -6.0, 0.95
ROLLER_Z = DISC_TOP + RR
PRONG_R, PRONG_T, PRONG_W = 2.5, 3.0, 5.0
FORK_HY = RW / 2 + 0.4 + PRONG_T
BR_Z0 = ROLLER_Z + RR + 0.4
BR_Z1 = BR_Z0 + 1.6
UP_ST, DN_ST, BAR_T, GUS_L, GUS_D = 0.5, 1.5, 6.0, 20.0, 7.5
BAR_Z0 = BR_Z1 + UP_ST
BAR_Z1 = BAR_Z0 + BAR_T
BAR_X1 = RING_XC + RING_W / 2 + 0.6
PIN_Z, PIN_D, PIN_L = BAR_Z1 + DN_ST + 1.5, 3.0, 20.0
POST_X, POST_Y, SLOT_CLR = 3.0, 6.0, 0.4
POST_TOP = PIN_Z + 3.0

ARM_L, ARM_T, ARM_W, PIN_R, PIN_H, SLOT_W = 12.0, 6.5, 9.0, 1.5, 3.7, 3.7
AP_HEAD_D, AP_HEAD_H, AP_L = 5.5, 2.0, 8.0
HS_HEAD_D, HS_HEAD_H = 4.2, 1.8
YS = (S_MIN + S_MAX) / 2
XS = DISC_R + 1.0 + SV_W / 2
ARM_Z1 = (BASE_Z0 + BASE_Z1) / 2 - SV_GAP - (HORN_Z - 0.2 - SV_H) / 2
ARM_Z0 = ARM_Z1 - ARM_T
SV_ZT = ARM_Z1 + HORN_Z - 0.2
TAB_TOP = SV_ZT - SV_TAB_Z
POST_Z0 = TAB_TOP + SV_GAP
SLOT_XC = XS - ARM_L - 0.3

POS = (16.0, 18.5, 21.0, 23.5, 26.0)
WI, WT, HX = 37.0, 6.0, 7.5
TIP_Y = WI + WT + PS_OUT
SV_Y0, SV_Y1 = YS - (SV_L - SV_AXIS_END), YS + SV_AXIS_END
ARM_BACK = 6.0 + ARM_W / 2
WIN = (LEG_X0 - WIN_M, XS + max(SV_W / 2, ARM_BACK) + WIN_M, -(WI + WT + BOSS_L + WIN_M), WI + WT + BOSS_L + WIN_M)
LX0, LX1, LY = WIN[0] - LID_M, WIN[1] + LID_M, WIN[3] + LID_M

COLORS = dict(Lid=(0.5, 0.5, 0.55), Disc=(0.9, 0.5, 0.1), ThroughShaft=(0.7, 0.3, 0.8), Wheel=(0.2, 0.7, 0.4), Shuttle=(0.9, 0.4, 0.6),
              RollerSlider=(0.3, 0.6, 0.9), Roller=(0.9, 0.9, 0.3), ServoArm=(0.9, 0.8, 0.2))
UPS = dict(Lid=V(0, 0, -1), Disc=Z, ThroughShaft=Z, Wheel=Y, Shuttle=V(1, 0, 0), RollerSlider=Z, Roller=Y, ServoArm=Z)


def yc(r, y0, y1, x=0.0, z=0.0):
    return Part.makeCylinder(r, y1 - y0, V(x, y0, z), Y)


def tear(r, y0, y1):
    t, w = r / math.sqrt(2), r * math.sqrt(2) - r - 1
    pts = [(-t, t), (t, t), (w, r + 1), (-w, r + 1)]
    return yc(r, y0, y1).fuse(prism([V(a, y0, -b) for a, b in pts], V(0, y1 - y0, 0)))


def tear_px(r, y0, y1, x=0.0, z=0.0):
    t = r / math.sqrt(2)
    tri = prism([V(x + t, y0, z + t), V(x + t, y0, z - t), V(x + r * math.sqrt(2), y0, z)], V(0, y1 - y0, 0))
    return yc(r, y0, y1, x, z).fuse(tri)


def yhex(af, y0, y1):
    return rot(hexprism(af, y0, y1), Z, 90)


def move(s, dx=0.0, dy=0.0, dz=0.0):
    s = s.copy()
    s.translate(V(dx, dy, dz))
    return s


def turn(s, deg):
    s = s.copy()
    s.rotate(V(XS, YS, 0), Z, deg)
    return s


def soften(s, pick, r, chamfer=False):
    op = lambda sh, k, es: (sh.makeChamfer if chamfer else sh.makeFillet)(k, es).removeSplitter()
    es = [e for e in s.Edges if pick(e)]
    if not es:
        return s
    for k in (1.0, 0.6, 0.35):
        try:
            return op(s, r * k, es)
        except Exception:
            pass
    for c in [e.CenterOfMass for e in es]:
        for k in (1.0, 0.6, 0.35):
            try:
                s = op(s, r * k, [min((e for e in s.Edges if pick(e)), key=lambda e: e.CenterOfMass.distanceToPoint(c))])
                break
            except Exception:
                pass
    return s


def flat(e, z, tol=1e-6):
    return e.BoundBox.ZLength < tol and abs(e.BoundBox.ZMin - z) < tol


def vert(e, ax="Z"):
    b = e.BoundBox
    return {"X": b.YLength + b.ZLength, "Y": b.XLength + b.ZLength, "Z": b.XLength + b.YLength}[ax] < 1e-6 and getattr(b, ax + "Length") > 1e-3


def root(e, x0, x1, y0, y1):
    c = e.BoundBox.Center
    return (x0 <= abs(c.x) <= x1 if x0 == 0 else x0 <= c.x <= x1) and y0 <= abs(c.y) <= y1 and e.BoundBox.XLength < 60 and e.BoundBox.YLength < 60


def vol(a, b):
    return a.common(b).Volume


def arm_phi(s):
    return 180.0 - math.degrees(math.asin((s - YS) / ARM_L))


def build_lid():
    lid = box(LX0, LX1, -LY, LY, LID_Z0, LID_Z1)
    lid = soften(lid, lambda e: vert(e), LID_R)
    lid = soften(lid, lambda e: flat(e, LID_Z1), 1.2, True)
    lid = soften(lid, lambda e: flat(e, LID_Z0), 1.5)
    hang = []
    for sg in (1, -1):
        y0, y1 = sorted((sg * WI, sg * (WI + WT + BOSS_L)))
        h = box(-HX, HX, y0, y1, 0, LID_Z0 + 0.5).fuse(yc(HX, y0, y1)).removeSplitter()
        hang.append(soften(h, lambda e: vert(e), 2.5))
    top = LID_Z0 + 0.5
    cy = (SV_Y0 + SV_Y1) / 2
    posts = []
    for sy in (-1, 1):
        yh = cy + sy * SV_HOLE_L / 2
        a, b = (yh - 4.5, min(yh + 4.5, SV_Y0 - 0.4)) if sy < 0 else (max(yh - 4.5, SV_Y1 + 0.4), yh + 4.5)
        pb = box(XS - SV_HOLE_W / 2 - 4.5, XS + SV_HOLE_W / 2 + 4.5, a, b, POST_Z0, top)
        pb = soften(soften(pb, lambda e: vert(e), 3.0), lambda e: flat(e, POST_Z0), 1.0)
        for sx in (-1, 1):
            pb = pb.cut(vcyl(PILOT / 2, XS + sx * SV_HOLE_W / 2, yh, POST_Z0 - 1, POST_Z0 + 8))
        posts.append(pb)
    for h in hang + posts:
        lid = lid.fuse(h)
    lid = soften(lid, lambda e: flat(e, LID_Z0) and (root(e, 0, HX + 0.1, WI - 0.1, WI + WT + BOSS_L + 0.1) or root(e, XS - SV_HOLE_W / 2 - 4.6, XS + SV_HOLE_W / 2 + 4.6, SV_Y0 - 15, SV_Y1 + 15)), 2.0)
    for sg in (1, -1):
        lid = lid.cut(box(-HX - 3, HX + 3, *sorted((sg * (WI - 3), sg * WI)), LID_Z0 - 3, LID_Z0 - 0.001))
    lid = lid.cut(tear(BORE / 2, -TIP_Y, TIP_Y)).cut(yc(BORE / 2, -TIP_Y, TIP_Y, 0, SLOT_UP)).cut(vcyl(MOT_BOSS_HOLE / 2, 0, 0, LID_Z0 - 1, LID_Z1 + 1))
    for k in range(6):
        a = math.radians(60 * k + MOT_ROT)
        x, y = MOT_PCD / 2 * math.cos(a), MOT_PCD / 2 * math.sin(a)
        lid = lid.cut(vcyl(MOT_HOLE_D / 2, x, y, LID_Z0 - 1, LID_Z1 + 1)).cut(vcyl(MOT_CB_D / 2, x, y, LID_Z0 - 1, LID_Z0 + MOT_CB_DEEP))
    nx, ny = round((LX1 - LX0 - 2 * GH) / 30), round((2 * LY - 2 * GH) / 30)
    xs = [LX0 + GH + i * (LX1 - LX0 - 2 * GH) / nx for i in range(nx + 1)]
    ys = [-LY + GH + i * (2 * LY - 2 * GH) / ny for i in range(ny + 1)]
    for x, y in [(x, sg * (LY - GH)) for x in xs for sg in (1, -1)] + [(x, y) for x in (LX0 + GH, LX1 - GH) for y in ys[1:-1]]:
        lid = lid.cut(vcyl(2.5, x, y, LID_Z0 - 1, LID_Z1 + 1))
    return lid.removeSplitter()


def build_disc():
    d = vcyl(DISC_R, 0, 0, Z_FACE, DISC_TOP)
    d = soften(d, lambda e: flat(e, DISC_TOP), 1.0)
    d = d.fuse(vcyl(HUB_R, 0, 0, DISC_TOP - 0.01, HUB_TOP)).removeSplitter()
    d = soften(d, lambda e: abs(e.BoundBox.ZMin - DISC_TOP) < 0.02 and e.BoundBox.ZLength < 1e-3 and e.BoundBox.XLength < 2 * HUB_R + 0.1, 1.0)
    d = soften(d, lambda e: flat(e, HUB_TOP), 0.6, True)
    d = soften(d, lambda e: flat(e, Z_FACE) and e.BoundBox.XLength > 2 * DISC_R - 0.1, 0.8, True)
    fz = DISC_FLAT_AF - DISC_BORE / 2
    d = d.cut(vcyl(DISC_BORE / 2, 0, 0, Z_FACE - 1, HUB_TOP + 1).common(box(-fz, 5, -5, 5, Z_FACE - 2, HUB_TOP + 2)))
    return d.cut(cyl(PILOT / 2, -HUB_R - 1, -fz + 0.5, 0, Z_FACE + LOCK_H)).removeSplitter()


def build_wheel():
    h, a, b = WH_H, LIP_V, LIP_V + LIP_H
    rl = RIM_R + LIP_H
    prof = [(0, -h), (rl - a, -h), (rl, -h + a), (RIM_R, -h + b), (RIM_R, h - b), (rl, h - a), (rl - a, h), (0, h)]
    w = Part.Face(Part.makePolygon([V(r, y, 0) for r, y in prof] + [V(0, -h, 0)])).revolve(O, Y, 360)
    return w.cut(yhex(HEX_BORE, -h - 1, h + 1)).removeSplitter()


def build_tyre():
    return yc(R_T, -TYRE_W / 2, TYRE_W / 2).cut(yc(RIM_R, -TYRE_W, TYRE_W))


def build_roller():
    return yc(RR, -RW / 2, RW / 2, 0, ROLLER_Z).cut(yc(RBORE / 2, -RW, RW, 0, ROLLER_Z))


def build_shaft():
    s = yhex(SHAFT_AF, -TIP_Y, TIP_Y)
    for y in (-TIP_Y + PS_PILOT, TIP_Y - PS_PILOT):
        s = s.cut(vcyl(PILOT / 2, 0, y, -10, 10))
    return s.removeSplitter()


def slot_void():
    hx, hy = POST_X / 2 + SLOT_CLR, POST_Y / 2 + SLOT_CLR
    roof = prism([V(hx, -hy, BAR_Z0 - 1), V(hx, hy, BAR_Z0 - 1), V(hx + hy, 0, BAR_Z0 - 1)], V(0, 0, BAR_T + 2))
    return box(-hx, hx, -hy, hy, BAR_Z0 - 1, BAR_Z1 + 1).fuse(roof)


def tail():
    y0, rc = -FY - TAIL_L, BORE_C / 2 + TAIL_WALL
    t, xe = rc / math.sqrt(2), TAIL_XT - 3.5
    tri = lambda a, b: prism([V(a * t, y0, t), V(a * t, y0, -t), V(b, y0, 0)], V(0, COL_L, 0))
    col = yc(rc, y0, y0 + COL_L).fuse(tri(1, rc * math.sqrt(2))).fuse(tri(-1, -rc * math.sqrt(2) - 0.3))
    col = col.common(box(-20, BORE_C / 2 * math.sqrt(2) + TAIL_WALL, y0 - 1, y0 + COL_L + 1, -TAIL_CZ, TAIL_CZ))
    run = TAIL_SLOPE * (xe - LEG_X0)
    pts = [(TAIL_XT, y0), (TAIL_XT, -FY + 0.1), (LEG_X0, -FY + 0.1), (LEG_X0, y0 + run), (xe, y0)]
    return col.fuse(prism([V(x, y, -TAIL_W / 2) for x, y in pts], V(0, 0, TAIL_W))).removeSplitter()


def slot_cut():
    return box(SLOT_XC, LUG_X1 + 1, -SLOT_W / 2, SLOT_W / 2, BASE_Z0 - 1, BASE_Z1 + 1).fuse(vcyl(SLOT_W / 2, SLOT_XC, 0, BASE_Z0 - 1, BASE_Z1 + 1))


def build_shuttle():
    leg = box(LEG_X0, LEG_X1, -FY, FY, BASE_Z0, BAR_Z1)
    base = box(LEG_X0, LUG_X1, -FY, FY, BASE_Z0, BASE_Z1)
    bar = box(LEG_X0, BAR_X1, -FY, FY, BAR_Z0, BAR_Z1)
    fil = prism([V(LEG_X1 - 0.1, -FY, BAR_Z0 + 0.1), V(LEG_X1 + GUS_L, -FY, BAR_Z0 + 0.1), V(LEG_X1 - 0.1, -FY, BAR_Z0 - GUS_D)], V(0, 2 * FY, 0))
    sh = leg.fuse(base).fuse(bar).fuse(fil)
    for sg in (1, -1):
        y0, y1 = sorted((sg * PK, sg * FY))
        sh = sh.fuse(box(LEG_X1 - 0.1, PL_X1, y0, y1, BASE_Z1 - 0.1, PL_Z1))
    sh = sh.fuse(tail()).removeSplitter()
    sh = soften(sh, lambda e: vert(e, "X") and e.Length > 8 and abs(abs(e.BoundBox.YMin) - PK) > 0.01 and abs(abs(e.BoundBox.ZMin) - TAIL_W / 2) > 1e-3, 3.0)
    sh = soften(sh, lambda e: vert(e, "Y") and abs(e.BoundBox.XMin - LEG_X1) < 1e-3 and abs(e.BoundBox.ZMin - BASE_Z1) < 1e-3, 3.0)
    sh = soften(sh, lambda e: vert(e) and (abs(e.BoundBox.XMin - LUG_X1) < 1e-3 or abs(e.BoundBox.XMin - BAR_X1) < 1e-3) and e.Length > 2, 2.5)
    sh = soften(sh, lambda e: vert(e, "X") and abs(e.BoundBox.YMin + FY) < 1e-3 and abs(abs(e.BoundBox.ZMin) - TAIL_W / 2) < 1e-3, 1.5)
    sh = soften(sh, lambda e: e.BoundBox.XLength < 1e-6 and abs(e.BoundBox.XMin - LEG_X0) < 1e-6, 0.8, True)
    sh = soften(sh, lambda e: e.BoundBox.YLength < 1e-6 and abs(e.BoundBox.YMin + FY + TAIL_L) < 1e-6, 0.6)
    sh = sh.cut(tear_px(BORE_C / 2, -FY - TAIL_L - 1, FY + 1)).cut(slot_void())
    return sh.cut(slot_cut()).removeSplitter()


def build_slider():
    prongs = [box(-PRONG_W / 2, PRONG_W / 2, *sorted((sg * (RW / 2 + 0.4), sg * FORK_HY)), ROLLER_Z - PRONG_R, BR_Z1) for sg in (1, -1)]
    s = prongs[0].fuse(prongs[1]).fuse(box(-PRONG_W / 2, PRONG_W / 2, -FORK_HY, FORK_HY, BR_Z0, BR_Z1))
    s = s.fuse(box(-POST_X / 2, POST_X / 2, -POST_Y / 2, POST_Y / 2, BR_Z1 - 0.01, POST_TOP)).removeSplitter()
    s = soften(s, lambda e: vert(e) and e.BoundBox.ZLength > 1.0, 0.8)
    s = s.cut(yc(RBORE / 2, -FORK_HY - 1, FORK_HY + 1, 0, ROLLER_Z))
    return s.cut(cyl(RBORE / 2, -POST_X, POST_X, 0, PIN_Z)).removeSplitter()


def build_arm():
    z0, z1 = ARM_Z0, ARM_Z1
    r = ARM_W / 2
    a = box(XS - 6.0, XS + ARM_L, YS - r, YS + r, z0, z1).fuse(vcyl(r, XS - 6.0, YS, z0, z1)).fuse(vcyl(r, XS + ARM_L, YS, z0, z1)).removeSplitter()
    a = soften(soften(a, lambda e: flat(e, z1), 0.9), lambda e: flat(e, z0), 0.6, True)
    zp = z1 - HORN_T - 0.8
    a = a.cut(box(XS - HORN_R - 0.3, XS + HORN_R + 0.3, YS - HORN_W / 2 - 0.2, YS + HORN_W / 2 + 0.2, zp, z1 + 1)).cut(vcyl(HORN_HUB / 2 + 0.15, XS, YS, zp, z1 + 1))
    a = a.cut(vcyl(HORN_CENTRE_D / 2, XS, YS, z0 - 1, z1 + 1)).cut(vcyl(AP_HEAD_D / 2 + 0.15, XS, YS, z0 - 1, z0 + AP_HEAD_H)).cut(vcyl(SV_SPLINE_D / 2 + 0.2, XS, YS, SV_ZT - SV_SPLINE_TOP - 0.2, z1 + 1))
    for sg in (1, -1):
        a = a.cut(vcyl(HORN_HOLE_D / 2, XS + sg * HORN_HOLE_PITCH / 2, YS, z0 - 1, z1 + 1)).cut(vcyl(HS_HEAD_D / 2, XS + sg * HORN_HOLE_PITCH / 2, YS, z0 - 1, z0 + HS_HEAD_H))
    a = a.cut(vcyl(PIN_R, XS + ARM_L, YS, z0 - 1, z1 + 1)).cut(vcyl(AP_HEAD_D / 2 + 0.15, XS + ARM_L, YS, z0 - 1, z0 + AP_HEAD_H))
    return a.removeSplitter()


def ring(sx):
    x0 = sx * RING_XC - RING_W / 2
    top = PIN_Z + PIN_D / 2
    return box(x0, x0 + RING_W, -FY - RING_T, FY + RING_T, BAR_Z0 - RING_T, top + RING_T).cut(box(x0 - 1, x0 + RING_W + 1, -FY, FY, BAR_Z0, top))


def build_armpin():
    return vcyl(AP_HEAD_D / 2, XS + ARM_L, YS, ARM_Z0, ARM_Z0 + AP_HEAD_H).fuse(vcyl(PIN_R, XS + ARM_L, YS, ARM_Z0 + AP_HEAD_H, ARM_Z0 + AP_HEAD_H + AP_L))


def build_motor():
    f = LID_Z1
    s = vcyl(MOT_GB_D / 2, 0, 0, f, f + MOT_GB_L).fuse(vcyl(MOT_CAN_D / 2, 0, 0, f + MOT_GB_L - 0.01, f + MOT_BODY)).fuse(vcyl(MOT_BOSS_D / 2, 0, 0, f - MOT_BOSS_L, f + 0.01))
    sh = vcyl(MOT_SH_D / 2, 0, 0, MOT_TIP, f).cut(box(-5, -(MOT_FLAT_AF - MOT_SH_D / 2), -5, 5, MOT_TIP - 1, MOT_TIP + MOT_FLAT_L))
    return s.fuse(sh)


def servo_body():
    cy = (SV_Y0 + SV_Y1) / 2
    b = box(XS - SV_W / 2, XS + SV_W / 2, SV_Y0, SV_Y1, SV_ZT - SV_H, SV_ZT)
    b = b.fuse(box(XS - SV_W / 2, XS + SV_W / 2, cy - SV_TAB_SPAN / 2, cy + SV_TAB_SPAN / 2, TAB_TOP - SV_TAB_T, TAB_TOP))
    return b.fuse(vcyl(SV_SPLINE_D / 2, XS, YS, SV_ZT - SV_SPLINE_TOP, SV_ZT - SV_H + 0.1))


def build_servo(phi):
    z0, z1 = SV_ZT - HORN_Z - HORN_T, SV_ZT - HORN_Z
    horn = box(XS - HORN_R, XS + HORN_R, YS - HORN_W / 2, YS + HORN_W / 2, z0, z1).fuse(vcyl(HORN_HUB / 2, XS, YS, z0, z1))
    return servo_body().fuse(turn(horn, phi))


def sleeve(y_in, sign):
    return yc(CPL_D / 2, *sorted((y_in, y_in + sign * CPL_L))).cut(yhex(SOCKET, y_in - CPL_L - 1, y_in + CPL_L + 1))


def build_parts():
    return dict(Lid=build_lid(), Disc=build_disc(), ThroughShaft=build_shaft(), Wheel=build_wheel(), Shuttle=build_shuttle(), RollerSlider=build_slider(),
                Roller=build_roller(), ServoArm=build_arm())


def pose(parts, s, motor):
    cy = TIP_Y - PS_PILOT - CPL_PIN
    ph = arm_phi(s)
    mv = lambda n: move(parts[n], dy=s)
    return dict(Lid=parts["Lid"], Motor=motor, Disc=parts["Disc"], ThroughShaft=parts["ThroughShaft"], Wheel=mv("Wheel"), Tyre=move(build_tyre(), dy=s),
                Shuttle=mv("Shuttle"), RollerSlider=mv("RollerSlider"), Roller=mv("Roller"),
                RingP=move(ring(1), dy=s), RingN=move(ring(-1), dy=s), Axle=move(yc(AX_D / 2, -FORK_HY, FORK_HY, 0, ROLLER_Z), dy=s), Pin=move(cyl(PIN_D / 2, -PIN_L / 2, PIN_L / 2, 0, PIN_Z), dy=s),
                ServoArm=turn(parts["ServoArm"], ph), ArmPin=turn(build_armpin(), ph), Servo=build_servo(ph), CplF=sleeve(-cy, -1), CplR=sleeve(cy, 1))


def prs(*ps):
    return {frozenset(p) for p in ps}


FITS = prs(("Lid", "ThroughShaft"), ("Wheel", "ThroughShaft"), ("Shuttle", "ThroughShaft"), ("Wheel", "Shuttle"), ("Lid", "Motor"), ("Motor", "Disc"), ("Lid", "Servo"),
           ("Servo", "ServoArm"), ("ServoArm", "Shuttle"), ("ServoArm", "ArmPin"), ("ArmPin", "Shuttle"), ("RollerSlider", "Shuttle"), ("RollerSlider", "Roller"), ("RollerSlider", "Axle"), ("Roller", "Axle"),
           ("RollerSlider", "Pin"), ("Roller", "Disc"), ("ThroughShaft", "CplF"), ("ThroughShaft", "CplR"), ("Lid", "CplF"), ("Lid", "CplR"), ("Wheel", "Tyre"), ("Disc", "Tyre"), ("RingP", "Shuttle"), ("RingN", "Shuttle"), ("RingP", "Pin"), ("RingN", "Pin"))
ZERO = prs(("ServoArm", "ArmPin"), ("Lid", "Motor"), ("Disc", "Tyre"), ("Wheel", "Tyre"), ("Roller", "Disc"), ("RingP", "Shuttle"), ("RingN", "Shuttle"), ("RingP", "Pin"), ("RingN", "Pin"))
PRESS = prs(("Wheel", "Tyre"), ("Disc", "Tyre"))


def audit(P):
    ov, cl, fit = {}, {}, {}
    ns = list(P)
    for i, a in enumerate(ns):
        for b in ns[i + 1:]:
            key = frozenset((a, b))
            if key in PRESS:
                continue
            ba, bb = P[a].BoundBox, P[b].BoundBox
            gap = max(ba.XMin - bb.XMax, bb.XMin - ba.XMax, ba.YMin - bb.YMax, bb.YMin - ba.YMax, ba.ZMin - bb.ZMax, bb.ZMin - ba.ZMax)
            if gap >= 3.0 and key not in FITS:
                cl[(a, b)] = 3.0
                continue
            if vol(P[a], P[b]) > 1e-3:
                ov[(a, b)] = round(vol(P[a], P[b]), 4)
            (fit if key in FITS else cl)[(a, b)] = round(P[a].distToShape(P[b])[0], 3)
    return ov, cl, fit


def sweep(mover, still, deltas):
    return round(max(vol(move(mover, *d), still) for d in deltas), 4)


def printable(name, s):
    up = UPS[name]
    h = lambda p: p.dot(up)
    zmin = min(h(v.Point) for v in s.Vertexes)
    floor = sum(f.Area for f in s.Faces if isinstance(f.Surface, Part.Plane) and all(abs(h(v.Point) - zmin) < 1e-4 for v in f.Vertexes) and f.normalAt(0, 0).dot(up) < -0.99)
    bad = []
    for f in s.Faces:
        if isinstance(f.Surface, Part.Cylinder) and f.Surface.Radius <= 1.8:
            continue
        if isinstance(f.Surface, Part.Plane) and sorted((f.BoundBox.XLength, f.BoundBox.YLength, f.BoundBox.ZLength))[1] <= 6.0:
            continue
        u0, u1, v0, v1 = f.ParameterRange
        worst = max(f.normalAt(u0 + (u1 - u0) * i / 4, v0 + (v1 - v0) * j / 4).dot(up) * -1 for i in range(5) for j in range(5))
        if worst > 0.7072 and not (isinstance(f.Surface, Part.Plane) and abs(h(f.CenterOfMass) - zmin) < 1e-4):
            bad.append((round(worst, 3), [round(c, 1) for c in f.CenterOfMass]))
    return round(floor, 1), bad


def estimates():
    F, MU, MU_T, MU_R, MU_D, KIN, ROT, R_SH = 35.0, 0.9, 0.9, 0.35, 0.3, 0.7, 0.4, 4.6
    E = 3000.0
    est = dict(F_N=F, ratio_min=round(S_MIN / R_T, 3), ratio_max=round(S_MAX / R_T, 3), rpm_min=round(MOT_RPM * S_MIN / R_T, 1), rpm_max=round(MOT_RPM * S_MAX / R_T, 1),
               tyre_od=round(2 * R_T, 2), stretch_pct=round(100 * (RIM_D / TYRE_ID - 1), 1), hex_corner_wall=round((RIM_D - HEX_BORE * 2 / math.sqrt(3)) / 2, 2))
    est["disc_torque_Nm"] = {"inner": round(MU * F * S_MIN / 1000, 3), "outer": round(MU * F * S_MAX / 1000, 3), "inner_at_20N": round(MU * 20 * S_MIN / 1000, 3), "motor": MOT_NM}
    t_sh = MU * F * R_T
    est["shaft_torque_Nmm"] = round(t_sh, 1)
    for tag, mu in (("dry", MU_D), ("greased", 0.1)):
        col = mu * F * R_SH
        drag = mu * F * (AX_D / 2) / RR
        est["loss_" + tag] = dict(motor_limited_pct_outer=round(100 * (col + drag * R_T) / (MOT_NM * 1000 * R_T / S_MAX), 1), motor_limited_pct_inner=round(100 * (col + drag * R_T) / (MOT_NM * 1000 * R_T / S_MIN), 1), collars_Nmm=round(col, 1), roller_axle_drag_N=round(drag, 2), roller_Nmm_at_shaft=round(drag * R_T, 1),
                                  total_pct_of_shaft_torque=round(100 * (col + drag * R_T) / t_sh, 1))
    lift = BORE / 2 - SHAFT_AF / math.sqrt(3) + SLOT_UP
    est["tyre_squeeze_needed_mm"] = round(F_MAX / K_TYRE, 2)
    est["squeeze_available_mm"] = round(SQUEEZE + lift, 2)
    est["hangers_load_N"] = round(max(0.0, F_MAX - K_TYRE * (SQUEEZE + lift)), 1)
    est["rib_stretch_pct"] = round(100 * (RIM_D / (TYRE_ID - 2 * TYRE_RIB_H) - 1), 1)
    est["hertz_MPa"] = round(math.sqrt(F * E / (2 * (1 - 0.36 ** 2)) / (math.pi * RW * RR)), 1)
    est["slider_lid_clear_mm"] = round(LID_Z0 - POST_TOP - UP_ST, 2)
    n, smax, th, dfl = 400, 0.0, 0.0, 0.0
    dx = (RING_XC - LEG_X1) / n
    for i in range(n):
        x = LEG_X1 + (i + 0.5) * dx
        h = BAR_T + GUS_D * max(0.0, 1 - (x - LEG_X1) / GUS_L)
        m = F_MAX / 2 * (max(0.0, RING_XC - x) + max(0.0, -RING_XC - x))
        smax = max(smax, 6 * m / (2 * FY * h * h))
        th += m / (E * 2 * FY * h ** 3 / 12) * dx
        dfl += th * dx
    est["frame"] = dict(F_N=F_MAX, bar_MPa=round(smax, 1), corner_MPa_kt1_5=round(1.5 * smax, 1), leg_MPa=round(6 * F_MAX * -LEG_X1 / (2 * FY * LEG_T ** 2), 1), bar_deflect_mm=round(dfl, 2))
    dmax = (S_MAX - S_MIN) / 2
    th = math.asin(dmax / ARM_L)
    f_end, f_mid = SV_NM / (ARM_L / 1000) * math.cos(th), SV_NM / (ARM_L / 1000)
    a_push = XS - ARM_L * math.cos(th)
    g_len = 2 * FY + TAIL_L - COL_L
    zp = -(BASE_Z0 + BASE_Z1) / 2
    mu = {}
    for tag, span, near in (("edge", g_len + COL_L, 2 * FY), ("centre", g_len, 2 * (PK + COL_L / 2))):
        ya, rb = a_push / span, zp / near
        mu[tag] = (round(span / (2 * math.hypot(a_push, zp)), 3), round(1 / (ya + math.hypot(ya, rb) + rb), 3))
    bind = min(mu["edge"])
    kd, kg = 1 / (1 - MU_D / bind), 1 / (1 - 0.1 / bind)
    stop = (MU_T + MU_R + 2 * MU_D) * F * kd
    turn_ = ((KIN * MU_T + 0.8 * MU_R) * F + ROT * 2 * MU_D * F) * kd
    stop_g = (MU_T + MU_R + 0.2) * F * kg
    turn_g = ((KIN * MU_T + 0.8 * MU_R) * F + ROT * 0.2 * F) * kg
    lev = 1.8
    est["bind"] = dict(guide_len_mm=round(g_len, 1), push_offset_mm=round(a_push, 1), push_below_axis_mm=round(zp, 2), mu_stiff_soft_edge=mu["edge"], mu_stiff_soft_centre=mu["centre"], ratio_tolerated_mu=round(bind, 3), ratio_before=round((PK + FY) / (2 * a_push), 3), factor_dry=round(kd, 2), factor_greased=round(kg, 2),
                       side_force_N_at_72N=round(72.0 * a_push / g_len, 1), roll_up_deg=round(math.degrees(math.atan((SV_ZT - SV_H - BASE_Z1) / LUG_X1)), 2), roll_down_deg=round(math.degrees(math.atan((BASE_Z0 - ARM_Z1) / LUG_X1)), 2))
    f_side, arm, dfl, n = est["bind"]["side_force_N_at_72N"], TAIL_L - COL_L / 2, 0.0, 400
    f_z, th_z, dz = 72.0 * zp / g_len, 0.0, 0.0
    for i in range(n):
        u = (i + 0.5) * arm / n
        d = min(TAIL_XT - LEG_X0, 3.5 + (u + COL_L / 2) / TAIL_SLOPE)
        dfl += f_side * u * u / (E * TAIL_W * d ** 3 / 12) * arm / n
    for i in range(n - 1, -1, -1):
        u = (i + 0.5) * arm / n
        th_z += f_z * u / (E * min(TAIL_XT - LEG_X0, 3.5 + (u + COL_L / 2) / TAIL_SLOPE) * TAIL_W ** 3 / 12) * arm / n
        dz += th_z * arm / n
    est["tail"] = dict(side_N=f_side, root_MPa_kt1_5=round(1.5 * 6 * f_side * arm / (TAIL_W * (TAIL_XT - LEG_X0) ** 2), 1), deflect_mm=round(dfl, 3), side_z_N=round(f_z, 1), deflect_z_mm=round(dz, 3), soft_limit_z_mm=round(2 * (BORE_C / 2 - SHAFT_AF / math.sqrt(3)) * ((g_len + COL_L) / (2 * FY) - 1), 2), root_z_MPa_kt1_5=round(1.5 * 6 * f_z * arm / ((TAIL_XT - LEG_X0) * TAIL_W ** 2), 1), collar_wall_x=TAIL_WALL, collar_wall_z=round(TAIL_CZ - BORE_C / 2, 2))
    p_st, w_pr, lev_pr = SV_NM / (ARM_L / 1000), FY - SLOT_W / 2, a_push - SLOT_XC
    est["prong"] = dict(stall_N=round(p_st, 1), lever_mm=round(lev_pr, 2), width_mm=round(w_pr, 2), thick_mm=LUG_T, root_MPa_kt1_5=round(1.5 * 6 * p_st * lev_pr / (LUG_T * w_pr ** 2), 1))
    est["lug"] = dict(gap_up=round(SV_ZT - SV_H + SV_GAP - BASE_Z1, 3), gap_down=round(BASE_Z0 - ARM_Z1 - SV_GAP, 3))
    est["arm_pin"] = dict(steel_MPa_at_72N=round(72.0 * lev / (math.pi * (2 * PIN_R) ** 3 / 32), 1),
                          pla_bearing_MPa_at_72N=round(72.0 / (2 * PIN_R * ARM_T) + 6 * 72.0 * (lev + ARM_T / 2) / (2 * PIN_R * ARM_T ** 2), 1))
    est["servo"] = dict(arm_deg=round(math.degrees(th), 1), force_end_N=round(f_end, 1), force_mid_N=round(f_mid, 1), need_stopped_dry_N=round(stop, 1),
                        need_turning_dry_N=round(turn_, 1), need_stopped_greased_N=round(stop_g, 1), need_turning_greased_N=round(turn_g, 1),
                        margin_turning=round(f_end / turn_g, 2), margin_stopped=round(f_end / stop_g, 2), margin_turning_dry=round(f_end / turn_, 2), margin_stopped_dry=round(f_end / stop, 2))
    return est


def verify(parts):
    motor = build_motor()
    lid, disc, shaft, wheel, shut, sl, roll, arm = (parts[k] for k in ("Lid", "Disc", "ThroughShaft", "Wheel", "Shuttle", "RollerSlider", "Roller", "ServoArm"))
    rep, ov, cl, fit = {}, {}, {}, {}
    for s in POS:
        o, c, f = audit(pose(parts, s, motor))
        ov[s], cl[s], fit[s] = o, c, f
    rep["overlap"], rep["fits"] = ov, fit
    rep["clear_min"] = {s: min(c.values()) for s, c in cl.items()}
    rep["clear_pairs"] = {s: {k: v for k, v in c.items() if v < 1.5} for s, c in cl.items()}
    rep["contact"] = {}
    for s in POS:
        P = pose(parts, s, motor)
        rep["contact"][s] = dict(tyre_disc_overlap=round(vol(P["Tyre"], disc), 3), tyre_bite=round(P["Tyre"].optimalBoundingBox(False, False).ZMax - disc.optimalBoundingBox(False, False).ZMin, 3),
                                 roller_disc_gap=round(P["Roller"].distToShape(disc)[0], 4), roller_disc_overlap=round(vol(P["Roller"], disc), 4))
    below = [lid.common(box(-200, 200, -200, 200, -50, LID_Z0 - 0.01)), disc, wheel, build_servo(arm_phi(S_MIN)), turn(arm, arm_phi(S_MIN))] + [move(p, dy=s) for p in (shut, sl, roll) for s in (S_MIN, S_MAX)]
    below += [build_servo(arm_phi(S_MAX)), turn(arm, arm_phi(S_MAX))]
    bb = [p.optimalBoundingBox(False, False) for p in below]
    rep["below_bbox"] = [round(f(bb), 2) for f in (lambda b: min(x.XMin for x in b), lambda b: max(x.XMax for x in b), lambda b: min(x.YMin for x in b), lambda b: max(x.YMax for x in b))]
    rep["lowest"] = round(min(x.ZMin for x in bb + [shaft.optimalBoundingBox(False, False)]), 2)
    under = max((f for f in lid.Faces if abs(f.normalAt(0, 0).z + 1) < 1e-6 and isinstance(f.Surface, Part.Plane)), key=lambda f: f.Area)
    sb = shaft.optimalBoundingBox(False, False)
    rep["lid_underside_to_axis"] = round(under.BoundBox.ZMin - (sb.ZMin + sb.ZMax) / 2, 4)
    lb = lid.optimalBoundingBox(False, False)
    rep["lid_size"] = [round(lb.XLength, 1), round(lb.YLength, 1), round(LID_T, 1)]
    rep["window"] = [round(WIN[1] - WIN[0], 1), round(WIN[3] - WIN[2], 1)]
    rep["hang_extent"] = [round(WIN[1] - WIN[0] - 2 * WIN_M, 1), round(WIN[3] - WIN[2] - 2 * WIN_M, 1)]
    sw = {}
    pin_v = vcyl(PIN_R, XS + ARM_L, YS, ARM_Z1, ARM_Z1 + PIN_H)
    pin_in = vcyl(PIN_R, XS + ARM_L, YS, BASE_Z0, ARM_Z1 + PIN_H)
    for k in range(9):
        s = S_MIN + (S_MAX - S_MIN) * k / 8
        ph = arm_phi(s)
        a, sv, p, pv = turn(arm, ph), move(shut, dy=s), turn(pin_in, ph), turn(pin_v, ph)
        pin_slot = vol(p, move(slot_cut(), dy=s)) / p.Volume
        sw[round(s, 2)] = dict(arm_shuttle=round(vol(a, sv), 4), pin_in_slot=round(pin_slot, 4), pin_gap=round(pv.distToShape(sv)[0], 3),
                               captive=(vol(pv, move(sv, dy=SLOT_W / 2 - PIN_R + 0.05)) > 0 and vol(pv, move(sv, dy=-SLOT_W / 2 + PIN_R - 0.05)) > 0), pin_y_err=round(YS + ARM_L * math.sin(math.radians(ph)) - s, 6))
    rep["sweep"] = sw
    steps = {}
    mot_lid = motor.fuse(lid)
    for k in range(6):
        a = math.radians(60 * k + MOT_ROT)
        path = vcyl(3.0, MOT_PCD / 2 * math.cos(a), MOT_PCD / 2 * math.sin(a), -40, LID_Z0 + MOT_CB_DEEP)
        steps["screw%d" % k] = round(vol(path, mot_lid), 4)
    steps["disc_on"] = sweep(disc, mot_lid, [(0, 0, -i * 4.0) for i in range(0, 13)])
    base = mot_lid.fuse(disc)
    floor = box(WIN[0] - 10, WIN[1] + 10, WIN[2] - 10, WIN[3] + 10, FLOOR_Z, LID_Z0).cut(box(WIN[0], WIN[1], WIN[2], WIN[3], FLOOR_Z - 1, LID_Z0 + 1))
    ins = [(i * 4.0, 0, 0) for i in range(0, 21)]
    sv = servo_body()
    for k in ("frame_in", "wheel_in", "tyre_in", "servo_in", "arm_in", "armpin_in", "floor_in", "shaft_in"):
        steps[k] = 0.0
    for s in (S_MIN, S_MAX):
        fr = move(shut, dy=s).fuse(move(sl, dy=s, dz=UP_ST - 0.1)).fuse(move(roll, dy=s, dz=UP_ST - 0.1))
        wh = move(wheel, dy=s)
        ar = turn(arm, arm_phi(s))
        ap = turn(build_armpin(), arm_phi(s))
        run = lambda k, v: steps.__setitem__(k, max(steps[k], v))
        run("frame_in", sweep(fr, base, [(-x, 0, 0) for x, _, _ in ins]))
        run("wheel_in", sweep(wh, base.fuse(fr), ins))
        run("tyre_in", sweep(move(build_tyre(), dy=s), fr, ins))
        full = base.fuse(fr).fuse(wh)
        run("servo_in", sweep(sv, full, [(d, 0, 0) for d in range(0, 61, 2)]))
        full = full.fuse(sv)
        run("arm_in", sweep(ar, full, [(0, 0, -d) for d in range(0, 41, 2)]))
        full = full.fuse(ar)
        run("armpin_in", sweep(ap, full, [(0, 0, -d) for d in range(0, 31, 2)]))
        P = pose(parts, s, motor)
        run("floor_in", max(sweep(p, floor, [(0, 0, d) for d in range(0, 41, 2)]) for n, p in P.items() if n not in ("ThroughShaft", "CplF", "CplR")))
        run("shaft_in", sweep(shaft, full.fuse(ap).fuse(floor), [(0, 2 * TIP_Y * (1 - i / 29.0), 0) for i in range(30)]))
    z_lock = Z_FACE + LOCK_H
    full = pose(parts, S_MIN, motor)
    others = None
    for n, p in full.items():
        if n not in ("Disc", "Motor", "Tyre", "Axle", "Pin"):
            others = p if others is None else others.fuse(p)
    steps["lock_path"] = round(vol(cyl(3.0, -80, -HUB_R - 0.5, 0, z_lock), others), 4)
    rep["steps"] = steps
    inn = pose(parts, S_MIN, motor)
    rep["hub"] = dict(roller_to_hub=round(inn["Roller"].distToShape(vcyl(HUB_R, 0, 0, DISC_TOP, HUB_TOP))[0], 2),
                      roller_to_lock_screw=round(inn["Roller"].distToShape(cyl(1.5, -HUB_R - 4, -HUB_R, 0, z_lock))[0], 2),
                      slider_to_hub=round(inn["RollerSlider"].distToShape(vcyl(HUB_R, 0, 0, DISC_TOP, HUB_TOP))[0], 2),
                      shuttle_to_hub=round(inn["Shuttle"].distToShape(vcyl(HUB_R, 0, 0, DISC_TOP, HUB_TOP))[0], 2),
                      ring_to_hub=round(min(inn[k].distToShape(vcyl(HUB_R, 0, 0, DISC_TOP, HUB_TOP))[0] for k in ("RingP", "RingN")), 2),
                      engage=round(HUB_TOP - MOT_TIP, 2), screw_on_flat=MOT_TIP + 1.5 <= z_lock <= MOT_TIP + MOT_FLAT_L - 1.5)
    mb = motor.optimalBoundingBox(False, False)
    rep["motor"] = dict(inside_lid=lb.XMin < mb.XMin and mb.XMax < lb.XMax and lb.YMin < mb.YMin and mb.YMax < lb.YMax, overlap=round(vol(motor, lid), 4))
    rep["ports"] = dict(stick_front=round(-sb.YMin - WI - WT, 3), stick_rear=round(sb.YMax - WI - WT, 3),
                        end_float=round(sleeve(-(TIP_Y - PS_PILOT - CPL_PIN), -1).distToShape(lid)[0] + sleeve(TIP_Y - PS_PILOT - CPL_PIN, 1).distToShape(lid)[0], 3),
                        pilot_open=[not shaft.isInside(V(0, y, 0), 1e-6, True) and shaft.isInside(V(0, y + 2.0, 0), 1e-6, True) for y in (-TIP_Y + PS_PILOT, TIP_Y - PS_PILOT)])
    rep["shaft_travel"] = dict(shuttle_y_range=[round(S_MIN - FY - TAIL_L, 2), round(S_MAX + FY, 2)], hanger_face=WI)
    rep["shuttle_cm3"] = round(shut.Volume / 1000, 2)
    rep["print"] = {n: printable(n, s) for n, s in parts.items()}
    rep["valid"] = {n: (s.isValid(), len(s.Solids)) for n, s in parts.items()}
    return rep


def check(rep, est):
    assert all(v == (True, 1) for v in rep["valid"].values()), rep["valid"]
    assert not any(rep["overlap"].values()), rep["overlap"]
    assert min(rep["clear_min"].values()) >= 0.5, rep["clear_pairs"]
    zero = ZERO
    assert all(d > 0 for f in rep["fits"].values() for k, d in f.items() if frozenset(k) not in zero), rep["fits"]
    for c in rep["contact"].values():
        assert abs(c["tyre_bite"] - SQUEEZE) < 1e-3 and c["tyre_disc_overlap"] > 0 and c["roller_disc_gap"] < 1e-3 and c["roller_disc_overlap"] < 1e-3, c
    w = rep["below_bbox"]
    assert WIN[0] <= w[0] and w[1] <= WIN[1] and WIN[2] <= w[2] and w[3] <= WIN[3], (w, WIN)
    assert abs(rep["lid_underside_to_axis"] - (FLOOR_Z + FLOOR_T)) < 1e-6, rep
    assert all(v["arm_shuttle"] < 1e-3 and v["pin_in_slot"] > 0.999 and v["pin_gap"] >= 0.1 and v["captive"] and abs(v["pin_y_err"]) < 1e-6 for v in rep["sweep"].values()), rep["sweep"]
    assert all(v < 1e-3 for v in rep["steps"].values()), rep["steps"]
    h = rep["hub"]
    assert h["roller_to_hub"] >= 5 and h["roller_to_lock_screw"] >= 5 and h["slider_to_hub"] >= 0.5 and h["shuttle_to_hub"] >= 0.5 and h["ring_to_hub"] >= 1.0 and h["engage"] >= 8.0 and h["screw_on_flat"], h
    assert rep["motor"]["inside_lid"] and rep["motor"]["overlap"] < 1e-3, rep["motor"]
    p = rep["ports"]
    assert abs(p["stick_front"] - PS_OUT) < 1e-3 and abs(p["stick_rear"] - PS_OUT) < 1e-3 and 0.3 <= p["end_float"] <= 0.8 and all(p["pilot_open"]), p
    yr = rep["shaft_travel"]["shuttle_y_range"]
    assert yr[1] < WI - 0.5 and yr[0] > -WI + 0.5, rep["shaft_travel"]
    assert all(f >= 5.0 and not bad for f, bad in rep["print"].values()), rep["print"]
    assert est["disc_torque_Nm"]["outer"] > MOT_NM and est["hex_corner_wall"] >= 1.0 and est["servo"]["margin_turning"] >= 1.5 and est["bind"]["ratio_tolerated_mu"] >= 0.5 and max(est["bind"]["roll_up_deg"], est["bind"]["roll_down_deg"]) <= 3.0, est
    assert est["frame"]["corner_MPa_kt1_5"] <= 15.0 and est["hangers_load_N"] == 0.0 and est["loss_greased"]["motor_limited_pct_outer"] <= 30.0, est
    assert est["tail"]["root_MPa_kt1_5"] <= 15.0 and est["tail"]["deflect_mm"] <= 0.2 and est["tail"]["deflect_z_mm"] <= est["tail"]["soft_limit_z_mm"] / 4 and rep["shuttle_cm3"] < 24.0, (est["tail"], rep["shuttle_cm3"])
    assert est["prong"]["root_MPa_kt1_5"] <= 15.0 and min(est["lug"].values()) >= 0.9, (est["prong"], est["lug"])
    assert est["arm_pin"]["steel_MPa_at_72N"] <= 150.0 and est["arm_pin"]["pla_bearing_MPa_at_72N"] <= 25.0 and est["slider_lid_clear_mm"] >= 0.4, est


def main():
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    parts = build_parts()
    for n, s in parts.items():
        assert s.isValid() and len(s.Solids) == 1, n
    rep, est = verify(parts), estimates()
    print("report", rep)
    print("estimates", est)
    check(rep, est)
    placed = dict(parts, ServoArm=turn(parts["ServoArm"], arm_phi(YS)))
    for n, s in placed.items():
        o = doc.addObject("Part::Feature", n)
        o.Shape = s
        if App.GuiUp:
            o.ViewObject.ShapeColor = COLORS[n]
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
