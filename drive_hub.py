# DriveHub: a wheel hub that is DRIVEN and STEERED with the drive joint centred on the kingpin inside a dished wheel (front wheel drive layout). One generator script, DriveHub.FCStd, print plate by make_print_project.py DriveHub.
# Layout (document frame, the kingpin is the Z axis through the joint centre, the axle is the X axis, outboard is -X, ahead is +Y, axle 29.0 below the pad top): the JointCross centre lies on the kingpin axis AND on the wheel axle axis (measured in verify, axle_axis and kingpin_axis). StubYoke = a fork identical to the kit yoke (same ears, gap, pin hole and head counterbore, so JointCross and the M3x20 pins fit unchanged, ear tips are half octagons so it prints) on an 8.0 AF hex stub that runs outboard through the Knuckle. The stub fork carries the horizontal pin (along Y), the DoubleFork on the inboard side carries the vertical pin (along Z), so steering is absorbed by the vertical hinge and suspension travel by the horizontal one. Knuckle = octagonal barrel (17.3 across flats) with the two kit liner pockets (PTFE 10 ID x 12 OD x 8.0 as plain bearings, placeholder Sleeve_1 and Sleeve_2, teardrop roofs, lip, lead-ins as in wheel_mount2.py), a riser and two 6 mm arms at z +-14.5 to +-20.5 that reach over and under the 12.5 joint swing sphere to the kingpin pivots (arm face 14.5 from the joint centre, 2.0 outside the sphere), and a steering arm pointing rearward, -Y, 6 thick so the root sees 4.5 MPa across layers at 10 N (tie rod holes dia 3.6 at 20, 27, 34 behind the kingpin, z 16.5 to 20.5). HubCarrier = pad 40 x 33 x 2.6 (outline, four dia 5.0 holes at x +18 / +7.2 relative to the kingpin, top face 29.0 above the axle, as the wheel_mount2 Mount mirrored because outboard is -X), two lug blocks (z 21.9 to 29 and -29 to -21.9, bore dia 6.2, head counterbore dia 7.7), and ONE flared strut on the front (+Y) side joining them, open inboard and rearward so the drive link passes (strut inner face 13.8 off the axis, 1.3 outside the swing sphere). Left and right: StubYoke, Wheel, Tyre, PivotBush and Sleeves are shared; HubCarrier and Knuckle are NOT symmetric, so the other side uses HubCarrier_L and Knuckle_L, the exact mirror images (in the document and the print map, MIRRORED), which keeps both steering arms rearward so one straight tie rod links them.
# Pivots (two, one from above, one from below): PivotBush (printed, flange dia 10 x 1.2, tube OD 5.6 ID 3.2) sits on the knuckle arm, passes the lug bore (0.3 radial) and is clamped to the arm by an M3x12 whose head seats on the bush end, so tightening can never clamp the lug: float 0.2 (flange to lug underside) + 0.2 (head to counterbore floor) = 0.4 total, the vertical load goes up through the flange on a printed thrust face (not through a screw head), the screw is fixed in the knuckle and turns with it, nothing can tighten up with steering, a loose screw cannot unthread past the 0.2 float. Thread: 6.0 mm in the arm (pilot dia 2.8, tip 1.2 below the arm). Head to counterbore 0.85 radial, tips and heads 0.8 or more off the joint parts (measured).
# Wheel: WHEEL_D 110 tyre diameter, 26 wide, printed dished wheel: hub boss and flat plate (dia 72) with the kit hex socket (8.5 on 8.0 AF, 0.25 per side, M3x16 cross screw along Y through an access hole in the dish, spot face for the head), a 50 degree cone web (prints with no support) up to a flange and a 2.4 thick rim with a 0.7 inboard bead that the tyre snaps over (matching relief groove in the tyre); the Tyre is a plain TPU band (ID 102 on rim OD 104, 2 percent stretch) that butts against the rim flange (locating lip). The wheel centre plane is 11.7 outboard of the kingpin (scrub), the hub plate sits 13.1 beyond the tyre face (width over hubs 212.4 against 186.1 over tyres on a 160.1 track (inboard joint centre at 49.98); a larger plate radius closes the gap but pushes the wheel outboard, the 50 degree cone and the 8 mm stub engagement outboard of the knuckle limit it); the knuckle, arms and steering arm are inside the cavity with 5.0 or more to the dish.
# Steering: stops on the HubCarrier (a block on the strut for one direction, the arm corner for the other) at 27.97 degrees each way, so the joint stays at or under 28; with the stops removed the wheel, knuckle, arm and screws are clear of the carrier to 30 (measured, wheel and tyre 10.5 or more); the joint itself is clear of every part at 0, 10, 20, 25 degrees at every 15 degrees of shaft rotation, with the DoubleFork also inclined 10 degrees in four directions; first contact is the kit joint limit (34.7 worst phase). Lock option: one extra M3x12 from below through the lower lug (clear dia 3.6, counterbore) into a pilot in the lower knuckle arm fixes the knuckle straight ahead (toe play +-2 degrees from the 0.3 radial in the clear hole).
# Hardware per wheel: 2 x M3x12 pivot screws, 1 x M3x12 lock screw (optional), 1 x M3x16 hub screw, JointCross with 2 x M3x20 pins (inherited exception) for the joint, 2 PTFE liners 12 x 10 x 8 (Sleeve_1 and Sleeve_2 are printed placeholders), 2 PivotBush. Only M3x12 and M3x16 are new.
# Assembly (each step is a straight slide with zero overlap in verify): 1 CrossJoint onto the stub fork, pin A with a dia 6 driver from the side, DoubleFork onto the cross, pin B from above with a dia 6 driver; 2 Sleeves into the Knuckle; 3 Knuckle over the stub hex tip from outboard; 4 bushes on the arms, the unit slides in from the rear (-Y) through the lug slots into the carrier; 5 pivot screws from above and below; 6 optional lock screw from below; 7 wheel onto the stub tip, 8 hub screw through the access hole, 9 tyre over the rim from inboard.
# Print (PLA, supports OFF): HubCarrier on its strut face (-Y up, 935 mm2 on the bed), Knuckle on the flat of the octagon (-Y up), StubYoke lying on its hex flat (+Z up), Wheel plate down (dia 87 plate) (+X up), Tyre on its inboard face (-X up), PivotBush flange down, Sleeves on end. Fork departure: the ear bottoms are cut flat at the hex flat (z -4.0) so the stub lies on one plane, which leaves 1.0 (not 1.2) of wall under the dia 6 head counterbore.
# Unverified: printed fit and wear of the thrust faces (the wheel tilt couple is assumed to be carried by the hub boss face on the knuckle end face, see strength), the tie rod and a single rod for both sides, TPU stretch of the tyre, the lug slot strength after use, the far (diff side) joint beside the carrier strut when the DoubleFork is inclined 10 degrees.
import FreeCAD as App, Part, math
from shapely.geometry import Polygon, Point, LineString
from shapely.ops import unary_union
from shapely.prepared import prep

S = {"NO_RUN": True, "__name__": "drive_shaft"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/drive_shaft.py").read(), "drive_shaft.py", "exec"), S)
V, O, cyl, box, hexprism, rot = (S[k] for k in ("V", "O", "cyl", "box", "hexprism", "rot"))
AX, SH, EAR_T, GAP, EAR_OUT, EAR_W, R_TIP, PIN_HOLE, HEAD_CB, HEAD_CB_D, SPHERE_R = (S[k] for k in (
    "AX", "SH", "EAR_T", "GAP", "EAR_OUT", "EAR_W", "R_TIP", "PIN_HOLE", "HEAD_CB", "HEAD_CB_D", "SPHERE_R"))
SHAFT_AF = S["SHAFT_AF"]

DOC_NAME = "DriveHub"
OUT = "/home/mikhail/Documents/cad/RC Car/DriveHub.FCStd"
X, Y, Z = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)

BOT = -SHAFT_AF / 2
ROOT_X1 = -(AX + SH)
BLOCK_T = 3.2
BLOCK_X1 = ROOT_X1 - BLOCK_T
G = 0.2
LINER_BORE, LINER_OD, LINER_ID, LINER_L = 12.2, 12.0, 10.0, 8.0
LIP_T, LIP_BORE, LINER_REC, LEAD = 1.6, 10.6, 0.1, 0.7
KN_HALF = LIP_T / 2 + LINER_L + LINER_REC
KN_X1 = BLOCK_X1 - G
KN_XC = KN_X1 - KN_HALF
KN_X0 = KN_X1 - 2 * KN_HALF
HUB_X0 = KN_X0 - G
HUB_BOSS_L, PLATE_T0 = 5.6, 2.8
HEX_END = HUB_X0 - HUB_BOSS_L - PLATE_T0 + 1.2 + 0.4
SH_X = HUB_X0 - 3.65
SH_HOLE = 2.8


def mv(s, x=0.0, y=0.0, z=0.0):
    c = s.copy()
    c.translate(V(x, y, z))
    return c


def xz_prism(pts, y0, y1):
    p = [V(x, y0, z) for x, z in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).extrude(V(0, y1 - y0, 0))


def ycyl(r, y0, y1, x=0.0, z=0.0):
    return Part.makeCylinder(r, y1 - y0, V(x, y0, z), Y)


def build_stub():
    px, R = -AX, R_TIP
    t = R * math.tan(math.pi / 8)
    pts = [(ROOT_X1, BOT), (px + t + (R + BOT), BOT), (px + R, -t), (px + R, t), (px + t, R), (ROOT_X1, R)]
    sph = Part.makeSphere(SPHERE_R, O)
    ears = None
    for s in (-1, 1):
        y0 = GAP / 2 if s > 0 else -EAR_OUT
        e = xz_prism(pts, y0, y0 + EAR_T).common(sph)
        ears = e if ears is None else ears.fuse(e)
    blk = box(BLOCK_X1, ROOT_X1, -EAR_OUT, EAR_OUT, BOT, R)
    s = ears.fuse(blk).fuse(hexprism(SHAFT_AF, HEX_END, BLOCK_X1 + 0.01)).removeSplitter()
    s = s.cut(ycyl(PIN_HOLE / 2, -15, 15, px))
    for sg in (-1, 1):
        s = s.cut(ycyl(HEAD_CB_D / 2, *sorted((sg * (EAR_OUT - HEAD_CB), sg * (EAR_OUT + 1))), px))
    s = s.cut(ycyl(SH_HOLE / 2, -10, 10, SH_X))
    return s.removeSplitter()


R_H = LINER_BORE / 2 + 2.55
TAN50 = math.tan(math.radians(50.0))
LEADX = LEAD / TAN50
ROOF_Z, LIP_ROOF_Z = 7.2, 6.0
ARM_Z0, ARM_Z1 = 14.5, 20.5
RISER_X1, RISER_X0 = KN_X1, KN_X1 - 8.0
ARM_YB, ARM_YF = -5.5, R_H
PIL_D, CLR_D = 2.8, 3.6
SARM_Z0, SARM_X, SARM_HOLES, SARM_END_R, SARM_HOLE = 14.5, (RISER_X0 + RISER_X1) / 2, (20.0, 27.0, 34.0), 4.5, 3.6


def revx(pts):
    p = [V(x, r, 0) for x, r in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).revolve(O, X, 360)


def tear(r, zr, x0, x1):
    t, hw = r / math.sqrt(2), r * math.sqrt(2) - zr
    p = [V(x0, -v, u) for u, v in ((-t, 0), (t, 0), (t, t), (hw, zr), (-hw, zr), (-t, t))]
    return Part.Face(Part.makePolygon(p + p[:1])).extrude(V(x1 - x0, 0, 0))


def bore_void():
    r, h, c = LINER_BORE / 2, LIP_T / 2, KN_HALF
    v = revx([(-c - 1, 0), (-c - 1, r + LEAD + TAN50), (-c, r + LEAD), (-c + LEADX, r), (-h, r), (-h, LIP_BORE / 2), (h, LIP_BORE / 2), (h, r), (c - LEADX, r), (c, r + LEAD), (c + 1, r + LEAD + TAN50), (c + 1, 0)])
    for r_, z_, x0, x1 in ((r, ROOF_Z, -c, -h), (r, ROOF_Z, h, c), (LIP_BORE / 2, LIP_ROOF_Z, -h, h)):
        v = v.fuse(tear(r_, z_, x0, x1))
    return v.removeSplitter()


def build_knuckle():
    a = R_H
    oct_ = [(a - 3.0, a), (-(a - 3.0), a), (-a, a - 3.0), (-a, -(a - 3.0)), (-(a - 3.0), -a), (a - 3.0, -a), (a, -(a - 3.0)), (a, a - 3.0)]
    pts = [V(KN_X0, y, z) for z, y in oct_]
    k = Part.Face(Part.makePolygon(pts + pts[:1])).extrude(V(2 * KN_HALF, 0, 0))
    k = k.fuse(box(RISER_X0, RISER_X1, ARM_YB, ARM_YF, -ARM_Z1, ARM_Z1))
    ap = [V(x, y, 0) for x, y in ((RISER_X0, ARM_YF), (ARM_EX, ARM_YF), (ARM_EX, ARM_YB + 2.5), (ARM_EX - 2.5, ARM_YB), (RISER_X0, ARM_YB))]
    arm = Part.Face(Part.makePolygon(ap + ap[:1])).extrude(V(0, 0, ARM_Z1 - ARM_Z0))
    k = k.fuse(mv(arm, 0, 0, ARM_Z0)).fuse(mv(arm, 0, 0, -ARM_Z1))
    e = SARM_HOLES[-1]
    sp = [V(SARM_X - 4.0, -3.0, 0), V(SARM_X + 4.0, -3.0, 0), V(SARM_X + SARM_END_R, -e, 0), V(SARM_X - SARM_END_R, -e, 0)]
    sa = Part.Face(Part.makePolygon(sp + sp[:1])).extrude(V(0, 0, ARM_Z1 - SARM_Z0))
    k = k.fuse(mv(sa, 0, 0, SARM_Z0)).fuse(Part.makeCylinder(SARM_END_R, ARM_Z1 - SARM_Z0, V(SARM_X, -e, SARM_Z0)))
    k = k.cut(mv(bore_void(), KN_XC))
    k = k.cut(Part.makeCylinder(PIL_D / 2, 2 * ARM_Z1 + 2, V(0, 0, -ARM_Z1 - 1)))
    k = k.cut(Part.makeCylinder(PIL_D / 2, 12, V(LOCK_X, LOCK_Y, -ARM_Z1 - 1)))
    for h in SARM_HOLES:
        k = k.cut(Part.makeCylinder(SARM_HOLE / 2, 10, V(SARM_X, -h, SARM_Z0 - 1)))
    return k.removeSplitter()


PAD_X0, PAD_X1, PAD_Y, PAD_T, AXIS_DEPTH = -11.0, 29.0, 16.5, 2.6, 29.0
PAD_Z0 = AXIS_DEPTH - PAD_T
GLUES = [(18.0, 10.0), (18.0, -10.0), (7.2, 12.5), (7.2, -12.5)]
GLUE_D = 5.0
FL_T, FL_D, BUSH_OD, BUSH_ID, BORE_D, CB_D = 1.2, 10.0, 5.6, 3.2, 6.2, 7.7
Z_FL1 = ARM_Z1 + FL_T
LUG_Z0 = Z_FL1 + 0.2
Z_HEAD = 25.3
LUG_CB = Z_HEAD - 0.2
BLK_HW, STRUT_Y0, STRUT_X0 = 5.2, 13.8, -3.2
LUG_Y0 = -8.0
SCREW_D, HEAD_D, HEAD_H = 3.0, 6.0, 3.2
PIV_L = 12.0
STOP_HW, STOP_Y, STOP_Z0, ARM_EX = 3.0, 11.39, 14.9, 8.0
TRIM_Z, TRIM_DX, TRIM_DY = 13.0, 4.0, 1.0
STRUT_PTS = [(STRUT_X0, -29.0), (5.2, -29.0), (5.2, -23.5), (12.5, 14.5), (29.0, 29.0), (STRUT_X0, 29.0)]
LOCK_X, LOCK_Y, LOCK_CB = -8.5, 1.55, 6.6
HUB_ACC_R, HUB_ACC_ROOF = 3.5, 4.1


def screw(p, d, length, dia=SCREW_D):
    return Part.makeCylinder(dia / 2, length, p, d).fuse(Part.makeCylinder(HEAD_D / 2, HEAD_H, p - d * HEAD_H, d))


def tear_z(r, zr, z0, z1):
    t, hw = r / math.sqrt(2), r * math.sqrt(2) - zr
    p = [V(u, -v, z0) for u, v in ((-t, 0), (t, 0), (t, t), (hw, zr), (-hw, zr), (-t, t))]
    return Part.Face(Part.makePolygon(p + p[:1])).extrude(V(0, 0, z1 - z0)).fuse(Part.makeCylinder(r, z1 - z0, V(0, 0, z0))).removeSplitter()


def build_carrier(stops=True):
    ch = 6.0
    pp = [V(x, y, PAD_Z0) for x, y in ((PAD_X0 + ch, -PAD_Y), (PAD_X1 - ch, -PAD_Y), (PAD_X1, -PAD_Y + ch), (PAD_X1, PAD_Y - ch), (PAD_X1 - ch, PAD_Y), (PAD_X0 + ch, PAD_Y), (PAD_X0, PAD_Y - ch), (PAD_X0, -PAD_Y + ch))]
    c = Part.Face(Part.makePolygon(pp + pp[:1])).extrude(V(0, 0, PAD_T))
    c = c.fuse(box(-BLK_HW, BLK_HW, LUG_Y0, PAD_Y, LUG_Z0, AXIS_DEPTH)).fuse(box(LOCK_X - LOCK_CB / 2 - 1.2, BLK_HW, LUG_Y0, PAD_Y, -AXIS_DEPTH, -LUG_Z0))
    if stops:
        c = c.fuse(box(-STOP_HW, STOP_HW, STOP_Y, STRUT_Y0 + 1.2, STOP_Z0, LUG_Z0 + 0.1)).fuse(box(-STOP_HW, STOP_HW, STOP_Y, STRUT_Y0 + 1.2, -LUG_Z0 - 0.1, -STOP_Z0))
    c = c.fuse(xz_prism([(x, z) for x, z in STRUT_PTS], STRUT_Y0, PAD_Y))
    tri = [V(STRUT_X0 - 0.1, STRUT_Y0 - 0.1, -TRIM_Z), V(STRUT_X0 + TRIM_DX, STRUT_Y0 - 0.1, -TRIM_Z), V(STRUT_X0 - 0.1, STRUT_Y0 + TRIM_DY, -TRIM_Z)]
    c = c.cut(Part.Face(Part.makePolygon(tri + tri[:1])).extrude(V(0, 0, 2 * TRIM_Z)))
    c = c.cut(Part.makeCylinder(BORE_D / 2, 2 * AXIS_DEPTH + 2, V(0, 0, -AXIS_DEPTH - 1)))
    cbr, cbz = CB_D / 2, 4.2
    c = c.cut(tear_z(cbr, cbz, LUG_CB, AXIS_DEPTH + 1)).cut(tear_z(cbr, cbz, -AXIS_DEPTH - 1, -LUG_CB))
    c = c.cut(Part.makeCylinder(CLR_D / 2, 12, V(LOCK_X, LOCK_Y, -AXIS_DEPTH - 1))).cut(mv(tear_z(LOCK_CB / 2, 3.7, -AXIS_DEPTH - 1, -LUG_CB), LOCK_X, LOCK_Y, 0))
    c = c.cut(box(-BORE_D / 2, BORE_D / 2, LUG_Y0 - 1, 0, LUG_Z0 - 1, Z_HEAD + 0.1)).cut(box(-BORE_D / 2, BORE_D / 2, LUG_Y0 - 1, 0, -Z_HEAD - 0.1, -LUG_Z0 + 1))
    for x, y in GLUES:
        c = c.cut(Part.makeCylinder(GLUE_D / 2, PAD_T + 2, V(x, y, PAD_Z0)))
    return c.removeSplitter()


def build_sleeve(x0, x1):
    return cyl(LINER_OD / 2, x0, x1).cut(cyl(LINER_ID / 2, x0 - 1, x1 + 1))


def build_bush():
    b = Part.makeCylinder(FL_D / 2, FL_T, V(0, 0, ARM_Z1)).fuse(Part.makeCylinder(BUSH_OD / 2, Z_HEAD - ARM_Z1, V(0, 0, ARM_Z1)))
    return b.cut(Part.makeCylinder(BUSH_ID / 2, 10, V(0, 0, ARM_Z1 - 1)))


def rp(s, base, axis, deg):
    s = s.copy()
    s.rotate(base, axis, deg)
    return s


def vol(a, b):
    return a.common(b).Volume if a.BoundBox.intersect(b.BoundBox) else 0.0


def jkit():
    return dict(Cr=S["build_cross"](), A=S["screw"](V(-AX, -(EAR_OUT - HEAD_CB), 0), Y, 20.0), B=S["screw"](V(AX, 0, EAR_OUT - HEAD_CB), -Z, 20.0), DF=S["build_dfork"]())


def pose_s(kit, d):
    be, al = math.degrees(math.asin(max(-1, min(1, d.y)))), math.degrees(math.atan2(-d.z, d.x))
    ta = lambda s: rp(s, V(-AX, 0, 0), Y, al)
    return dict(Cr=ta(kit["Cr"]), A=kit["A"], B=ta(kit["B"]), DF=ta(rp(kit["DF"], V(AX, 0, 0), Z, be)))


def unit(deg, ph):
    t, p = math.radians(deg), math.radians(ph)
    return V(math.cos(t), math.sin(t) * math.cos(p), math.sin(t) * math.sin(p))


def joint_pose(kit, stub, st, psi, inc=(0.0, 0.0)):
    w = unit(*inc)
    dk = App.Rotation(Z, -st).multVec(w)
    ds = App.Rotation(X, -psi).multVec(dk)
    ds.normalize()
    ps = pose_s(kit, ds)
    out = {n: rp(sh, O, X, psi) for n, sh in dict(ps, Stub=stub).items()}
    return out


def joint_hits(kit, stub, fixed, st, psi, inc=(0.0, 0.0)):
    j = joint_pose(kit, stub, st, psi, inc)
    car = rp(fixed["Carrier"], O, Z, -st)
    others = dict(fixed, Carrier=car)
    th = {("A", "Cr"), ("B", "Cr")}
    h = [(a, b) for a in j for b in others if vol(j[a], others[b]) > 1e-3]
    ks = list(j)
    h += [(a, b) for i, a in enumerate(ks) for b in ks[i + 1:] if (a, b) not in th and (b, a) not in th and vol(j[a], j[b]) > 1e-3]
    return h


WHEEL_D, WHEEL_W, TYRE_T, RIM_T = 110.0, 26.0, 3.0, 2.4
RIM_R = WHEEL_D / 2 - TYRE_T
PLATE_R, PLATE_T, BOSS_R, CONE_DEG, WEB_T = 43.5, PLATE_T0, 9.0, 50.0, 2.4
P0 = HUB_X0 - HUB_BOSS_L - PLATE_T
P1 = P0 + PLATE_T
SOCK_AF, SOCK_BOT = 8.5, P0 + 1.2
WH_NEAR, WH_FAR = 3.4, 2.8
TAN_C = math.tan(math.radians(CONE_DEG))
FLANGE_R = WHEEL_D / 2 - 0.5
RF = P0 + (FLANGE_R - PLATE_R) * TAN_C
RIM_X1 = RF + WHEEL_W
TYRE_ID = 2 * RIM_R - 2.0
BEAD_H, GROOVE_R = 0.7, 0.2
XW = RF + WHEEL_W / 2


def revxp(pts):
    p = [V(x, r, 0) for x, r in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).revolve(O, X, 360)


def build_wheel():
    ro, ri = RIM_R, RIM_R - RIM_T
    dr_in = WEB_T / math.sin(math.radians(CONE_DEG))
    xq = P0 + (ri + dr_in - PLATE_R) * TAN_C
    x1 = P1
    r1 = PLATE_R + (x1 - P0) / TAN_C - dr_in
    w = revxp([(P0, 0), (P0, PLATE_R), (RF, FLANGE_R), (RF, ro), (RIM_X1 - BEAD_H * TAN_C - 0.4, ro), (RIM_X1 - 0.4, ro + BEAD_H), (RIM_X1, ro + BEAD_H), (RIM_X1, ri), (xq, ri), (x1, r1), (x1, 0)])
    w = w.fuse(revxp([(P1 - 0.5, 0), (P1 - 0.5, BOSS_R), (HUB_X0, BOSS_R), (HUB_X0, 0)]))
    w = w.removeSplitter()
    w = w.cut(hexprism(SOCK_AF, SOCK_BOT, HUB_X0 + 1)).cut(Part.makeCone(6.2, SOCK_AF / math.sqrt(3), 1.5, V(HUB_X0, 0, 0), -X))
    w = w.cut(box(SH_X - 3.2, HUB_X0 + 1.0, -12, -8, -3.3, 3.3))
    w = w.cut(ycyl(WH_NEAR / 2, -12, 0, SH_X)).cut(ycyl(WH_FAR / 2, 0, 12, SH_X))
    t, hw = HUB_ACC_R / math.sqrt(2), HUB_ACC_R * math.sqrt(2) - HUB_ACC_ROOF
    pp = [V(SH_X + v, -60, u) for u, v in ((-t, 0), (t, 0), (t, t), (hw, HUB_ACC_ROOF), (-hw, HUB_ACC_ROOF), (-t, t))]
    acc = Part.Face(Part.makePolygon(pp + pp[:1])).extrude(V(0, 52, 0)).fuse(ycyl(HUB_ACC_R, -60, -8, SH_X)).removeSplitter()
    return w.cut(acc).removeSplitter()


def build_tyre():
    ri, rg = TYRE_ID / 2, RIM_R + BEAD_H + GROOVE_R
    return revxp([(RF, ri), (RF, WHEEL_D / 2), (RIM_X1, WHEEL_D / 2), (RIM_X1, rg), (RIM_X1 - 0.6, rg), (RIM_X1 - 0.6 - (rg - ri) * TAN_C, ri)])


LAYER, OVER, SPAN_MAX, ARCH_R, CHORD = 0.2, 0.3, 10.0, 3.0, 0.25


def region(wires):
    r = Polygon()
    for w in wires:
        q = [(v.x, v.y) for v in w.discretize(Deflection=0.02)]
        if len(q) > 3:
            r = r.symmetric_difference(Polygon(q).buffer(0))
    return r


def bridged(c, below, tol):
    ok, x0, y0, x1, y1 = prep(below.buffer(tol)), *c.bounds
    big, cx, cy = math.hypot(x1 - x0, y1 - y0) + 1.0, (x0 + x1) / 2, (y0 + y1) / 2
    good = []
    for deg in range(0, 180, 15):
        a = math.radians(deg)
        d, n = (math.cos(a), math.sin(a)), (-math.sin(a), math.cos(a))
        for i in range(-int(big / CHORD / 2) - 1, int(big / CHORD / 2) + 2):
            o = (cx + n[0] * i * CHORD, cy + n[1] * i * CHORD)
            seg = c.intersection(LineString([(o[0] - d[0] * big, o[1] - d[1] * big), (o[0] + d[0] * big, o[1] + d[1] * big)]))
            for g in getattr(seg, "geoms", [seg]):
                if g.geom_type == "LineString" and 1e-6 < g.length <= SPAN_MAX and all(ok.covers(Point(q)) for q in (g.coords[0], g.coords[-1])):
                    good.append(g.buffer(CHORD))
    return c.difference(unary_union(good)).area < 0.15


def print_check(s, up):
    sign, axis = up
    u = V(*[(1 if sign == "+" else -1) if a == axis else 0 for a in "XYZ"])
    s = s.copy()
    s.transformShape(App.Placement(V(), App.Rotation(u, Z)).toMatrix())
    s.translate(V(0, 0, -s.optimalBoundingBox(False, False).ZMin))
    h = s.optimalBoundingBox(False, False).ZMax
    floor, p1, p2, p5 = 0.0, [], [], []
    lim = -math.sin(math.radians(45.0))
    for f in s.Faces:
        pl = isinstance(f.Surface, Part.Plane)
        if pl and f.BoundBox.ZMax < 1e-4:
            floor += f.Area
            continue
        if pl and f.BoundBox.ZMax - f.BoundBox.ZMin < 1e-6 and f.normalAt(*f.Surface.parameter(f.CenterOfMass)).z < -0.999:
            if f.Area > 0.05:
                F = region(f.Wires)
                below = region(s.slice(Z, max(f.BoundBox.ZMin - 0.1, 0.05)))
                if any(p.interiors for p in getattr(F, "geoms", [F])) or not all(bridged(p, below, 0.15) for p in getattr(F, "geoms", [F])):
                    p2.append((round(f.BoundBox.ZMin, 2), round(f.Area, 1)))
            continue
        pts, tris = f.tessellate(0.1)
        area, hole = 0.0, True
        for i, j, k in tris:
            n = (pts[j] - pts[i]).cross(pts[k] - pts[i])
            if n.Length and n.z / n.Length < lim + 0.05:
                u2, v2 = f.Surface.parameter((pts[i] + pts[j] + pts[k]) * (1 / 3))
                nn = f.normalAt(u2, v2)
                if nn.z < lim - 1e-3:
                    area += n.Length / 2
                    if isinstance(f.Surface, Part.Cylinder):
                        r = (pts[i] + pts[j] + pts[k]) * (1 / 3) - f.Surface.Center
                        hole = hole and nn.dot(r - f.Surface.Axis * r.dot(f.Surface.Axis)) < 0 and f.Surface.Radius <= ARCH_R + 1e-6 and abs(f.Surface.Axis.z) < 0.5
                    else:
                        hole = False
        if area > 0.05 and not hole:
            p1.append((type(f.Surface).__name__, round(getattr(f.Surface, "Radius", 0.0), 2), round(area, 1)))
    prev, first = None, None
    for k in range(int(math.ceil(h / LAYER - 1e-6))):
        cur = region(s.slice(Z, LAYER * (k + 0.5)))
        if prev is None:
            first = cur
        else:
            r = cur.difference(prev.buffer(OVER)).buffer(-0.04).buffer(0.04)
            raw = [c for c in getattr(r, "geoms", [r]) if c.area > 0.05]
            if raw:
                arch = unary_union(raw).buffer(ARCH_R).buffer(-ARCH_R)
                for c in getattr(arch, "geoms", [arch]):
                    own = [q for q in raw if c.buffer(0.01).contains(q)]
                    if any(q.interiors for q in own) or not bridged(c, prev, OVER + 0.15):
                        p5.append((round(LAYER * (k + 0.5), 2), round(sum(q.area for q in own), 2), tuple(round(v, 1) for v in c.bounds)))
        prev = cur
    x0, y0, x1, y1 = first.bounds
    thin = first.difference(first.buffer(-0.4, join_style=2).buffer(0.4, join_style=2)).area
    return dict(floor=round(floor, 1), height=round(h, 2), bed_dim=round(min(x1 - x0, y1 - y0), 2), thin_mm2=round(thin, 2), p1=p1, p2=p2, p5=p5)


SLV_A = (KN_XC + LIP_T / 2, KN_XC + LIP_T / 2 + LINER_L)
SLV_B = (KN_XC - LIP_T / 2 - LINER_L, KN_XC - LIP_T / 2)
STD_L = (8.0, 12.0, 16.0)
COLORS = dict(HubCarrier=(0.5, 0.5, 0.55), Knuckle=(0.2, 0.5, 0.9), HubCarrier_L=(0.5, 0.5, 0.55), Knuckle_L=(0.2, 0.5, 0.9), StubYoke=(0.7, 0.3, 0.8), Wheel=(0.9, 0.4, 0.6), Tyre=(0.15, 0.15, 0.15),
              PivotBush_1=(0.9, 0.9, 0.2), PivotBush_2=(0.9, 0.9, 0.2), Sleeve_1=(0.95, 0.95, 0.95), Sleeve_2=(0.95, 0.95, 0.95))
PRINT_UP = dict(HubCarrier="-Y", Knuckle="-Y", HubCarrier_L="-Y", Knuckle_L="-Y", StubYoke="+Z", Wheel="+X", Tyre="-X", PivotBush_1="+Z", PivotBush_2="-Z", Sleeve_1="+X", Sleeve_2="+X")
NO_BED = ("Sleeve_1", "Sleeve_2")


def build_parts():
    P = dict(HubCarrier=build_carrier(), Knuckle=build_knuckle(), StubYoke=build_stub(), Wheel=build_wheel(), Tyre=build_tyre(),
             PivotBush_1=build_bush(), PivotBush_2=build_bush().mirror(O, Z), HubCarrier_L=build_carrier().mirror(O, X), Knuckle_L=build_knuckle().mirror(O, X), Sleeve_1=build_sleeve(*SLV_A), Sleeve_2=build_sleeve(*SLV_B))
    return P


def build_refs():
    kit = jkit()
    return dict(Ref_PivotScrew_U=screw(V(0, 0, Z_HEAD), -Z, PIV_L), Ref_PivotScrew_L=screw(V(0, 0, -Z_HEAD), Z, PIV_L),
                Ref_LockScrew=screw(V(LOCK_X, LOCK_Y, -LUG_CB), Z, PIV_L), Ref_HubScrew=screw(V(SH_X, -8.0, 0), Y, 16.0),
                Ref_JointCross=kit["Cr"], Ref_PinA=kit["A"], Ref_PinB=kit["B"], Ref_DoubleFork=kit["DF"])


def moved(s, v, t):
    c = s.copy()
    c.translate(v * t)
    return c


def sweep(mov, fixed, v, length=60.0, step=1.0):
    worst = 0.0
    for i in range(int(round(length / step)) + 1):
        for a in mov.values():
            m = moved(a, v, length - i * step)
            worst = max(worst, max(vol(m, b) for b in fixed.values()))
    return round(worst, 4)


def driver(p, d, length=60.0):
    return Part.makeCylinder(3.0, length, p, d)


def core(p, d, length, head_d=HEAD_D, head_h=HEAD_H):
    return Part.makeCylinder(1.3, length, p, d).fuse(Part.makeCylinder(head_d / 2, head_h, p - d * head_h, d))


def cores():
    return dict(A=core(V(-AX, -(EAR_OUT - HEAD_CB), 0), Y, 20.0, 5.5, 3.0), B=core(V(AX, 0, EAR_OUT - HEAD_CB), -Z, 20.0, 5.5, 3.0),
                PU=core(V(0, 0, Z_HEAD), -Z, PIV_L), PL=core(V(0, 0, -Z_HEAD), Z, PIV_L), LK=core(V(LOCK_X, LOCK_Y, -LUG_CB), Z, PIV_L), HS=core(V(SH_X, -8.0, 0), Y, 16.0))


def assembly(P, R):
    K, St, W, Ca = (P[n] for n in ("Knuckle", "StubYoke", "Wheel", "HubCarrier"))
    S1, S2, B1, B2 = P["Sleeve_1"], P["Sleeve_2"], P["PivotBush_1"], P["PivotBush_2"]
    Cr, DF = R["Ref_JointCross"], R["Ref_DoubleFork"]
    C = cores()
    A, B, PU, PL, LK, HS = (C[n] for n in ("A", "B", "PU", "PL", "LK", "HS"))
    r = {}
    r["1_cross_into_fork"] = sweep(dict(c=Cr), dict(S=St), X, 40.0)
    r["2_pinA_and_driver"] = sweep(dict(a=A, d=driver(V(-AX, -(EAR_OUT - HEAD_CB) - 3.0, 0), -Y)), dict(S=St), -Y, 40.0)
    r["3_doublefork_onto_cross"] = sweep(dict(f=DF), dict(S=St, c=Cr, a=A), X, 40.0)
    r["3b_pinB_and_driver"] = sweep(dict(b=B, d=driver(V(AX, 0, EAR_OUT - HEAD_CB + 3.0), Z)), dict(S=St, f=DF, a=A), Z, 40.0)
    r["4_sleeves_into_knuckle"] = max(sweep(dict(s=S1), dict(K=K), X, 40.0), sweep(dict(s=S2), dict(K=K, a=S1), -X, 40.0))
    joint = dict(S=St, c=Cr, a=A, f=DF, b=B)
    r["5_knuckle_over_stub_tip"] = sweep(dict(k=K, a=S1, b=S2), joint, -X, 60.0)
    unit = dict(K=K, a=S1, b=S2, S=St, c=Cr, p=A, f=DF, q=B, u=B1, l=B2)
    r["6_unit_into_carrier_from_rear"] = sweep(unit, dict(C=Ca), -Y, 70.0)
    allfix = dict(unit, C=Ca)
    r["7_pivot_screws_and_drivers"] = max(sweep(dict(s=PU, d=driver(V(0, 0, Z_HEAD + HEAD_H), Z)), allfix, Z, 40.0), sweep(dict(s=PL, d=driver(V(0, 0, -Z_HEAD - HEAD_H), -Z)), dict(allfix, u2=PU), -Z, 40.0))
    allfix.update(u2=PU, l2=PL)
    r["8_lock_screw_and_driver"] = sweep(dict(s=LK, d=driver(V(LOCK_X, LOCK_Y, -LUG_CB - HEAD_H), -Z)), allfix, -Z, 40.0)
    r["9_wheel_onto_stub_tip"] = sweep(dict(w=W), allfix, -X, 60.0)
    allfix["w"] = W
    r["10_hub_screw_and_driver"] = sweep(dict(s=HS, d=driver(V(SH_X, -8.0 - HEAD_H, 0), -Y)), allfix, -Y, 60.0)
    own = dict(A="p", B="q", PU="u2", PL="l2")
    r["final_core_overlaps"] = {n: round(max(vol(c, b) for k, b in allfix.items() if k != own.get(n)), 4) for n, c in C.items() if n != "LK"}
    return r


def tyre_sweep(P, R):
    ri = RIM_R + BEAD_H + 0.1
    stretched = revxp([(RF, ri), (RF, WHEEL_D / 2), (RIM_X1, WHEEL_D / 2), (RIM_X1, ri)])
    fix = {n: P[n] for n in ("HubCarrier", "Knuckle", "Wheel", "StubYoke")}
    return sweep(dict(t=stretched), fix, X, 60.0)


def kfix(P, R):
    return dict(Knuckle=P["Knuckle"], Sleeve_1=P["Sleeve_1"], Sleeve_2=P["Sleeve_2"], PivotBush_1=P["PivotBush_1"], PivotBush_2=P["PivotBush_2"],
                Ref_PivotScrew_U=R["Ref_PivotScrew_U"], Ref_PivotScrew_L=R["Ref_PivotScrew_L"])


def joint_ring(P, R, levels=(0, 10, 20, 25), pstep=15):
    kit = dict(Cr=R["Ref_JointCross"], A=R["Ref_PinA"], B=R["Ref_PinB"], DF=R["Ref_DoubleFork"])
    fixed = dict(kfix(P, R), Carrier=P["HubCarrier"])
    bad = {}
    for lv in levels:
        for st in sorted({lv, -lv}):
            for psi in range(0, 360, pstep):
                for h in joint_hits(kit, P["StubYoke"], fixed, st, psi):
                    bad.setdefault(h, []).append((st, psi))
            if lv:
                for inc in ((10.0, 0.0), (10.0, 90.0), (10.0, 180.0), (10.0, 270.0)):
                    for psi in range(0, 360, 2 * pstep):
                        for h in joint_hits(kit, P["StubYoke"], fixed, st, psi, inc):
                            bad.setdefault(("inc",) + h, []).append((st, psi, inc))
    return bad


def joint_first(P, R, pstep=45, top=60.0):
    kit = dict(Cr=R["Ref_JointCross"], A=R["Ref_PinA"], B=R["Ref_PinB"], DF=R["Ref_DoubleFork"])
    fixed = dict(kfix(P, R), Carrier=P["HubCarrier"])
    out = {}
    for sg in (1, -1):
        for psi in range(0, 360, pstep):
            f = lambda a: bool(joint_hits(kit, P["StubYoke"], fixed, sg * a, psi))
            a = 30.0
            while a <= top and not f(a):
                a += 5.0
            if a > top:
                out[(sg, psi)] = top
                continue
            lo, hi = a - 5.0, a
            for _ in range(5):
                mid = (lo + hi) / 2
                lo, hi = (lo, mid) if f(mid) else (mid, hi)
            out[(sg, psi)] = round(hi, 2)
    return out


def rk(s, deg):
    return rp(s, O, Z, deg)


def stop_angle(P, R, sg):
    mov = [P["Knuckle"], P["PivotBush_1"], P["PivotBush_2"], R["Ref_PivotScrew_U"], R["Ref_PivotScrew_L"], P["Wheel"], P["Tyre"], P["StubYoke"]]
    lo, hi = 0.0, 45.0
    for _ in range(11):
        mid = (lo + hi) / 2
        c = rk(P["HubCarrier"], -sg * mid)
        lo, hi = (lo, mid) if any(m.distToShape(c)[0] < 1e-6 for m in mov) else (mid, hi)
    return round(lo, 2)


def clearances(P, R, top=30):
    nostop = build_carrier(stops=False)
    pk = {n: P[n] for n in ("Knuckle", "PivotBush_1", "PivotBush_2", "StubYoke", "Wheel", "Tyre")}
    pk["PivotScrew_U"], pk["PivotScrew_L"] = R["Ref_PivotScrew_U"], R["Ref_PivotScrew_L"]
    hub = Part.makeCylinder(BOSS_R + 3.0, 40, V(P0 - 3, 0, 0), X)
    dish = P["Wheel"].cut(hub)
    out = dict(steer_free={}, steer_stops=stop_angle(P, R, 1), steer_stops_neg=stop_angle(P, R, -1))
    for a in range(0, top + 1, 5):
        for sg in (1, -1):
            c = rk(nostop, -sg * a)
            out["steer_free"][sg * a] = {n: round(s_.distToShape(c)[0], 2) for n, s_ in pk.items()}
    st = {n: round(dish.distToShape(P[n])[0], 2) for n in ("Knuckle", "PivotBush_1", "PivotBush_2")}
    st.update({n: round(dish.distToShape(R[n])[0], 2) for n in ("Ref_PivotScrew_U", "Ref_PivotScrew_L")})
    st.update({"Tyre_" + n: round(P["Tyre"].distToShape(P[n])[0], 2) for n in ("Knuckle", "StubYoke")})
    out["head_radial"] = round(nostop.distToShape(moved(R["Ref_PivotScrew_U"], Z, 0.6))[0], 3)
    out["dish_static"] = st
    return out


def screw_clear(P, R):
    kit = dict(Cr=R["Ref_JointCross"], A=R["Ref_PinA"], B=R["Ref_PinB"], DF=R["Ref_DoubleFork"])
    car = P["HubCarrier"]
    res = dict(PU_joint=1e9, PL_joint=1e9, PU_carrier=1e9, PL_carrier=1e9, HS_knuckle=1e9, HS_carrier=1e9, HS_joint=1e9)
    for st in (0, 28, -28):
        for psi in range(0, 360, 45):
            j = joint_pose(kit, P["StubYoke"], st, psi)
            for nm, sc in (("PU", R["Ref_PivotScrew_U"]), ("PL", R["Ref_PivotScrew_L"])):
                res[nm + "_joint"] = min([res[nm + "_joint"]] + [sc.distToShape(j[k])[0] for k in ("Cr", "DF", "A", "B", "Stub")])
        c = rk(car, -st)
        for nm, sc in (("PU", R["Ref_PivotScrew_U"]), ("PL", R["Ref_PivotScrew_L"])):
            res[nm + "_carrier"] = min(res[nm + "_carrier"], sc.distToShape(c)[0])
        for rev in range(0, 360, 30):
            h = rp(R["Ref_HubScrew"], O, X, rev)
            res["HS_knuckle"] = min(res["HS_knuckle"], h.distToShape(P["Knuckle"])[0])
            res["HS_carrier"] = min(res["HS_carrier"], h.distToShape(c)[0])
    return {k: round(v, 2) for k, v in res.items()}


def orient(s, up):
    sign, axis = up
    u = V(*[(1 if sign == "+" else -1) if a == axis else 0 for a in "XYZ"])
    s = s.copy()
    s.transformShape(App.Placement(V(), App.Rotation(u, Z)).toMatrix())
    s.translate(V(0, 0, -s.optimalBoundingBox(False, False).ZMin))
    return s


def thin_layers(s, up, w=1.2, step=0.2):
    o = orient(s, up)
    h = o.optimalBoundingBox(False, False).ZMax
    run, worst = 0, (0.0, 0.0)
    for k in range(int(h / step)):
        z = step * (k + 0.5) + 0.013
        r = region(o.slice(Z, z))
        a = 0.0
        if not r.is_empty:
            try:
                a = r.difference(r.buffer(-w / 2, join_style=2).buffer(w / 2, join_style=2)).area
            except Exception:
                r = r.buffer(1e-4)
                a = r.difference(r.buffer(-w / 2, join_style=2).buffer(w / 2, join_style=2)).area
        run = run + 1 if a > 0.3 else 0
        if run >= 3 and a > worst[0]:
            worst = (round(a, 3), round(z, 2))
    return worst


LOAD_V, LOAD_S, BUMP_G, DRIVE_T, ALLOW = 15.0, 15.0, 3.0, 500.0, 10.0
INBOARD_JOINT_X = 49.98
LC_DF = S["LC_D"]
OLD_JOINT_TO_WHEEL = 68.0


def axis_of(s, r):
    f = [f for f in s.Faces if isinstance(f.Surface, Part.Cylinder) and abs(f.Surface.Radius - r) < 1e-6]
    return f[0].Surface.Center, f[0].Surface.Axis


def strength(P):
    z_p = -(LUG_Z0 + LUG_CB) / 2
    rl = LOAD_S * (WHEEL_D / 2 + abs(z_p)) / (2 * abs(z_p))
    ru = rl - LOAD_S
    t = PAD_Y - STRUT_Y0
    xs = {}
    pts = STRUT_PTS
    def width(z):
        for (xa, za), (xb, zb) in zip(pts[1:], pts[2:]):
            if za <= z <= zb and zb > za:
                return xa + (xb - xa) * (z - za) / (zb - za) - STRUT_X0
        return pts[1][0] - STRUT_X0
    worst = (0.0, 0.0)
    z = z_p
    while z < AXIS_DEPTH - PAD_T:
        sg = 6 * rl * (z - z_p) / (t * width(z) ** 2)
        if sg > worst[0]:
            worst = (sg, z)
        z += 0.5
    lug_net = 2 * BLK_HW - BORE_D
    lug_sig = rl * STRUT_Y0 / (( AXIS_DEPTH - LUG_Z0) * ((2 * BLK_HW) ** 3 - BORE_D ** 3) / (6 * 2 * BLK_HW))
    z_stub = 5 * math.sqrt(3) / 16 * (SHAFT_AF / math.sqrt(3)) ** 4 / (SHAFT_AF / 2)
    hub_lever = abs(SH_X) - abs(SLV_B[0])
    m_bump = LOAD_V * BUMP_G * abs(hub_lever)
    stub_shear_bend = m_bump / z_stub * 1.1
    m_tilt = LOAD_S * WHEEL_D / 2 + LOAD_V * BUMP_G * (abs(SH_X) - abs(XW))
    face_in, face_out = 6.8, R_H
    z_face = math.pi / (4 * face_out) * (face_out ** 4 - face_in ** 4)
    z_boss = math.pi / (4 * BOSS_R) * (BOSS_R ** 4 - 4.4 ** 4)
    tors = 16 * DRIVE_T / (math.pi * SHAFT_AF ** 3) / (1 - 2.8 / SHAFT_AF)
    bush_len = LUG_CB - LUG_Z0
    flange_area = math.pi * ((FL_D / 2) ** 2 - (BORE_D / 2) ** 2) - BORE_D * (FL_D / 2 - BORE_D / 2)
    glue_area = sum(f.Area for f in P["HubCarrier"].Faces if isinstance(f.Surface, Part.Plane) and abs(f.BoundBox.ZMin - AXIS_DEPTH) < 1e-6 and abs(f.BoundBox.ZMax - AXIS_DEPTH) < 1e-6)
    m_pad = rl * (AXIS_DEPTH - PAD_T - z_p)
    sarm = 10.0 * (max(SARM_HOLES) - abs(ARM_YB)) * 6 / ((ARM_Z1 - SARM_Z0) * (2 * 4.0) ** 2)
    return dict(sarm_root_MPa=round(sarm, 2), reaction_lower_N=round(rl, 1), reaction_upper_N=round(ru, 1), strut_max_MPa=round(worst[0], 2), strut_max_at_z=round(worst[1], 1),
                lug_bend_MPa=round(lug_sig, 2), stub_bend_bump_MPa=round(stub_shear_bend, 2), stub_if_couple_on_hex_MPa=round(m_tilt / z_stub, 1),
                tilt_moment_Nmm=round(m_tilt, 0), thrust_face_bearing_MPa=round(m_tilt / z_face, 2), hub_boss_bend_MPa=round(m_tilt / z_boss, 2),
                stub_torsion_MPa=round(tors, 2), bush_bearing_MPa=round(rl / (BUSH_OD * bush_len), 2), flange_bearing_MPa=round(LOAD_V * BUMP_G / flange_area, 2),
                pad_hole_N=round(m_pad / (18.0 - 7.2) / 2, 1), pad_glue_mm2=round(glue_area, 0), pad_glue_MPa=round(rl / glue_area, 3))


def fits(P, R):
    K, St, W, Ca = (P[n] for n in ("Knuckle", "StubYoke", "Wheel", "HubCarrier"))
    hexpart = St.common(box(HEX_END - 1, BLOCK_X1 - 0.01, -20, 20, -20, 20))
    ob = lambda s_: s_.optimalBoundingBox(False, False)
    PU = R["Ref_PivotScrew_U"]
    flange = P["PivotBush_1"].common(box(-20, 20, -20, 20, ARM_Z1 - 0.01, Z_FL1 + 0.01))
    bodyp = P["PivotBush_1"].common(box(-20, 20, -20, 20, Z_FL1 + 0.01, 40))
    head = PU.common(box(-20, 20, -20, 20, Z_HEAD - 0.01, 40))
    ba, pa = axis_of(K, LINER_BORE / 2), axis_of(Ca, BORE_D / 2)
    ln = lambda c, a: Part.makeLine(c - a * 90, c + a * 90)
    jc = Part.Vertex(O)
    return dict(
        stub_in_liner=round(hexpart.distToShape(P["Sleeve_1"])[0], 3), stub_in_lip=round(hexpart.distToShape(K)[0], 3),
        sleeve_pocket=round(K.distToShape(moved(P["Sleeve_1"], X, 1.0))[0], 3),
        thrust_in=round(St.distToShape(K)[0], 3), thrust_out=round(W.distToShape(K)[0], 3),
        bush_bore_radial=round(bodyp.distToShape(Ca)[0], 3), flange_gap=round(flange.distToShape(Ca)[0], 3), head_floor_gap=round(head.distToShape(Ca)[0], 3),
        axle_axis=(round(abs(ba[1].x), 4), round(ln(*ba).distToShape(jc)[0], 5)), kingpin_axis=(round(abs(pa[1].z), 4), round(ln(*pa).distToShape(jc)[0], 5)),
        hub_socket_radial=round(hexpart.distToShape(W)[0], 3),
        thrust_in_mm2=round(sum(f.Area for f in St.Faces if isinstance(f.Surface, Part.Plane) and abs(f.BoundBox.XMin - BLOCK_X1) < 1e-6 and abs(f.BoundBox.XMax - BLOCK_X1) < 1e-6), 1),
        lock_play_deg=round(math.degrees(0.3 / math.hypot(LOCK_X, LOCK_Y)), 2))


def tracks():
    kp = INBOARD_JOINT_X + LC_DF
    wc, tyre = kp + abs(XW), kp + abs(RF)
    old = kp + OLD_JOINT_TO_WHEEL
    return dict(kingpin_x=round(kp, 2), scrub_mm=round(abs(XW), 2), wheel_centre_x=round(wc, 2), track=round(2 * wc, 1), over_tyres=round(2 * tyre, 1),
                over_hubs=round(2 * (kp + abs(P0)), 1), hub_beyond_tyre=round(abs(P0) - abs(RF), 1), old_track=round(2 * old, 1), saved_track=round(2 * (old - wc), 1))


def run_len(s_, p, d, length, step=0.02):
    tot, started = 0.0, False
    for i in range(int(length / step)):
        if s_.isInside(p + d * (i * step), 1e-7, True):
            tot, started = tot + step, True
        elif started:
            break
    return round(tot, 2)


def wall_probe(P):
    W = P["Wheel"]
    out = []
    for y in (-10.0, -20.0, -30.0, -40.0):
        for z in (0.0, 2.0):
            out.append(run_len(W, V(SH_X, y, z - 0.0) + V(-math.sqrt(max(HUB_ACC_R ** 2 - z ** 2, 0.0)) - 0.005, 0, 0), -X, 6.0))
    for y in (-9.0, -10.0):
        out.append(run_len(W, V(SH_X - 3.2 - 0.005, y, 0.0), -X, 6.0))
    return round(min(out), 2)


def joint_dist(P, R, pstep=10):
    kit = dict(Cr=R["Ref_JointCross"], A=R["Ref_PinA"], B=R["Ref_PinB"], DF=R["Ref_DoubleFork"])
    sa = (stop_angle(P, R, 1), stop_angle(P, R, -1))
    angs = [sa[0], -sa[1], 26.0, -26.0, 25.0, -25.0]
    worst = 1e9
    for a in angs:
        c = rk(P["HubCarrier"], -a)
        for psi in range(0, 360, pstep):
            j = joint_pose(kit, P["StubYoke"], a, psi)
            for n, s_ in j.items():
                if s_.BoundBox.intersect(c.BoundBox) or True:
                    worst = min(worst, s_.distToShape(c)[0])
    return round(worst, 3), angs


def verify(P, R):
    rep = {}
    rep["valid"] = {n: (s_.isValid(), len(s_.Solids), round(s_.Volume, 1)) for n, s_ in P.items()}
    ob = lambda s_: s_.optimalBoundingBox(False, False)
    rep["size"] = {n: tuple(round(v, 1) for v in (ob(s_).XLength, ob(s_).YLength, ob(s_).ZLength)) for n, s_ in P.items()}
    rep["asm"] = assembly(P, R)
    rep["asm"]["11_tyre_over_rim"] = tyre_sweep(P, R)
    rep["fits"] = fits(P, R)
    rep["ring"] = joint_ring(P, R)
    rep["first"] = joint_first(P, R)
    rep["joint_dist"] = joint_dist(P, R)
    rep["wall_probe"] = wall_probe(P)
    rep["clear"] = clearances(P, R)
    rep["screws"] = screw_clear(P, R)
    rep["strength"] = strength(P)
    rep["track"] = tracks()
    rep["thin"] = {n: thin_layers(s_, PRINT_UP[n]) for n, s_ in P.items()}
    rep["print"] = {n: print_check(s_, PRINT_UP[n]) for n, s_ in P.items()}
    rep["stub_cb_wall"] = round(-BOT - HEAD_CB_D / 2, 3)
    return rep


def check(rep):
    assert all(v[0] and v[1] == 1 for v in rep["valid"].values()), rep["valid"]
    assert all(v < 1e-3 for k, v in rep["asm"].items() if k[0].isdigit()) and not any(rep["asm"]["final_core_overlaps"].values()), rep["asm"]
    f = rep["fits"]
    assert f["stub_in_liner"] >= 0.3 and f["stub_in_lip"] >= 0.3 and f["sleeve_pocket"] >= 0.1 - 1e-6 and 0.25 - 1e-3 <= f["hub_socket_radial"] <= 0.5, f
    assert abs(f["thrust_in"] - G) < 1e-3 and abs(f["thrust_out"] - G) < 1e-3 and f["thrust_in_mm2"] >= 20.0, f
    assert f["bush_bore_radial"] >= 0.3 - 1e-6 and abs(f["flange_gap"] - 0.2) < 1e-3 and 0.2 - 1e-3 <= f["head_floor_gap"] <= 0.25, f
    assert f["axle_axis"][0] == 1.0 and f["axle_axis"][1] < 1e-4 and f["kingpin_axis"][0] == 1.0 and f["kingpin_axis"][1] < 1e-4, f
    assert not rep["ring"], rep["ring"]
    assert min(rep["first"].values()) >= 30.0, rep["first"]
    assert rep["joint_dist"][0] >= 0.8 and rep["wall_probe"] >= 1.2 - 1e-3, (rep["joint_dist"], rep["wall_probe"])
    c = rep["clear"]
    assert 27.8 <= c["steer_stops"] <= 28.02 and 27.8 <= c["steer_stops_neg"] <= 28.02, c
    for a, d in c["steer_free"].items():
        assert min(d["Wheel"], d["Tyre"]) >= 2.0 and min(d.values()) >= 0.15, (a, d)
    assert min(v for k, v in c["dish_static"].items()) >= 2.0 and c["head_radial"] >= 0.8 - 1e-3, c
    sc = rep["screws"]
    assert sc["PU_joint"] >= 0.8 and sc["PL_joint"] >= 0.8 and sc["HS_knuckle"] >= 0.8 and sc["HS_carrier"] >= 0.8, sc
    st = rep["strength"]
    assert st["sarm_root_MPa"] <= 5.0, st
    for k in ("strut_max_MPa", "lug_bend_MPa", "stub_bend_bump_MPa", "thrust_face_bearing_MPa", "hub_boss_bend_MPa", "stub_torsion_MPa", "bush_bearing_MPa", "flange_bearing_MPa"):
        assert st[k] <= ALLOW, (k, st)
    assert rep["track"]["scrub_mm"] <= 12.0 and rep["track"]["track"] < rep["track"]["old_track"], rep["track"]
    assert abs(rep["stub_cb_wall"] - 1.0) < 1e-6
    walls = (BOSS_R - SOCK_AF / math.sqrt(3), -ARM_YB - PIL_D / 2, ARM_YF - PIL_D / 2, ARM_EX - PIL_D / 2, LOCK_Y - ARM_YB - PIL_D / 2, ARM_YF - LOCK_Y - PIL_D / 2, (BUSH_OD - BUSH_ID) / 2, SARM_END_R - SARM_HOLE / 2)
    assert min(walls) >= 1.2 - 1e-9 and min(walls[1:6]) >= 2.0, walls
    assert ARM_Z1 - ARM_Z0 >= 5.0 and all(L in STD_L for L in (PIV_L, 16.0)), (ARM_Z1 - ARM_Z0, PIV_L)
    for n, r in rep["thin"].items():
        assert r[0] <= 0.3 or n in NO_BED, (n, r)
    for n, r in rep["print"].items():
        assert not r["p1"] and not r["p2"] and not r["p5"], (n, r)
        assert (r["floor"] >= 60.0 or n in NO_BED) and r["height"] <= 4 * r["bed_dim"] and r["thin_mm2"] < 0.5, (n, r)


def put(doc, name, shape):
    assert shape.isValid() and len(shape.Solids) == 1, name
    o = doc.addObject("Part::Feature", name)
    o.Shape = shape
    key = name.replace("Shown_", "")
    if App.GuiUp and key in COLORS:
        o.ViewObject.ShapeColor = COLORS[key]
    return o


def display(doc, P, R):
    kit = dict(Cr=R["Ref_JointCross"], A=R["Ref_PinA"], B=R["Ref_PinB"], DF=R["Ref_DoubleFork"])
    for n in ("HubCarrier", "Knuckle", "StubYoke", "Wheel", "Tyre", "PivotBush_1", "PivotBush_2", "Sleeve_1", "Sleeve_2"):
        put(doc, n, P[n])
    for n, s_ in R.items():
        if n not in ("Ref_JointCross", "Ref_PinA", "Ref_PinB", "Ref_DoubleFork"):
            put(doc, n, s_)
    put(doc, "Ref_JointCross", kit["Cr"])
    put(doc, "Ref_PinA", kit["A"])
    put(doc, "Ref_PinB", kit["B"])
    put(doc, "Ref_DoubleFork", kit["DF"])
    j = joint_pose(kit, P["StubYoke"], SHOW_DEG, 0)
    sh = lambda s_: mv(rk(s_, SHOW_DEG), 0, SHOW_DY, 0)
    put(doc, "Shown_HubCarrier", mv(P["HubCarrier"], 0, SHOW_DY, 0))
    for n in ("Knuckle", "Wheel", "Tyre", "PivotBush_1", "PivotBush_2", "Sleeve_1", "Sleeve_2"):
        put(doc, "Shown_" + n, sh(P[n]))
    for n, k in (("PivotScrew_U", "Ref_PivotScrew_U"), ("PivotScrew_L", "Ref_PivotScrew_L"), ("HubScrew", "Ref_HubScrew")):
        put(doc, "Shown_" + n, sh(R[k]))
    for n, k in (("StubYoke", "Stub"), ("JointCross", "Cr"), ("PinA", "A"), ("PinB", "B"), ("DoubleFork", "DF")):
        put(doc, "Shown_" + n, mv(rk(j[k], SHOW_DEG), 0, SHOW_DY, 0))
    put(doc, "HubCarrier_L", mv(P["HubCarrier_L"], 0, 0, -120.0))
    put(doc, "Knuckle_L", mv(P["Knuckle_L"], 0, 0, -120.0))
    put(doc, "Ref_Floor", box(PAD_X0 - 10, PAD_X1 + 20, -60, 60, AXIS_DEPTH, AXIS_DEPTH + 4.0))


SHOW_DEG, SHOW_DY = 25.0, 170.0


def main():
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    P, R = build_parts(), build_refs()
    rep = verify(P, R)
    print("report", rep, flush=True)
    check(rep)
    display(doc, P, R)
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
