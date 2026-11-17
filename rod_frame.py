# Rod frame module for the RC car kit: parallelogram suspension, two 8 mm carbon rods (495 long) carrying two identical AxleFrames and the GearboxCradle.
# Per wheel: two Links (44.88 pivot to pivot, H shape, 4 pivots each, one part used 8 times), one Upright bolted to the HubCarrier pad (3 screws plus a Dowel trapped between a recess in the Upright plate and the pad hole of the blocked strut side), pivots on M3x16 through PivotBush (the bush takes the clamp load, the lug floats 0.3 radial, 0.2 axial; every pivot nut snaps into a hex pocket with a retaining lip),
# one spring on a 24 mm guide pin under the lower Link tail (seat pocket on the AxleFrame floor holds the spring at least 2 mm with 4 shims, 0 to 4 Shim spacers change the preload), bump and droop stops are flush faces in a window of the AxleFrame block (window roof 5 thick, tail 7.6 x 17). Links are fitted at a drooped attitude (THETA_A) so the spring clears.
# ASSEMBLY: hub pad screws can only be driven on the bench, so the Upright is bolted to the hub unit first (HubCarrier, Knuckle, StubYoke) and the driver sweep for those three screws is asserted against that bench set (driver_step). Then in the car: plug shafts in, frame down, rods, springs, links, Upright unit, pivot screws, wheel.
# Geometry: pivot rows ZL and ZU above the axle (above the steered tyre ring), kingpin 98.16 from the car centre, rods at x 57, z 56 under the pivot posts. Printed parts (PLA, supports OFF, 0.2 layers): AxleFrame (+Z), Link (+Z), Upright_R and Upright_L (+Z), PivotBush (-Y), Dowel (-Z), Shim (+Z), GearboxCradle (+Z). Print check thresholds as gearbox_module.py (SAG 0.3, LOST 1.0, ignored area 0.03), bridge() measures the true span including the 0.3 buffer.
# Strength is checked for the COMBINED case on one wheel (15 N sideways + 10 N fore and aft at the ground, 55 below the axle, + the whole 3 g car 29.4 N): sections are cut from the solids at many heights; the M3 steel screw carries the bush bending (under 200 MPa), PLA bearing under 10 MPa in plane, vertical members 5 MPa across layers.
# UNVERIFIED assumptions (constants above): spring wire 1.04 and rate 2.2, rod diameter and wall, PLA stiffness, pad hole and dowel fits. check() asserts every rule; the report printed by main() lists every measured value. Ref_* and Shown_* objects are display only. Hub pad nuts are loose under the pad (no nut trap possible there).
import FreeCAD as App, Part, math, os
import numpy as np
from shapely.geometry import MultiLineString, Point, Polygon, LineString, box as _sbox
from shapely.ops import linemerge, unary_union
from shapely import affinity

FAST = bool(os.environ.get("RF_FAST"))
ONLY = os.environ.get("RF_ONLY", "")
V = App.Vector
O = V(0, 0, 0)
X, Y, Z = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
DOC_NAME = "RodFrame"
HERE = "/home/mikhail/Documents/cad/RC Car/"
OUT = HERE + "RodFrame.FCStd"

# ---- constants (section 1)

JCX, FORK = 53.28, 18.4
KPX = JCX + FORK
WHEEL_D, WHEEL_W, STEER_DEG = 110.0, 26.0, 28.0
PAD_TOP = 29.0
TH_D, TH_B = -22.4, -4.9
STATIC_N = 2.45
ROD_D, ROD_BORE, ROD_L = 8.0, 8.4, 495.0
ROD_X, ROD_Z = 61.0, 61.0
BOSS_WALL = 2.5
R_BORE = ROD_BORE / 2
R_B = R_BORE + BOSS_WALL
BOSS_L = 14.0
ROOF_Z, FLAT_DEG = 4.6, 50.0
NUT_AF, NUT_POCKET_AF, NUT_T, NUT_SLOT_T = 5.5, 5.8, 2.4, 2.6
SLOT_Z0 = ROOF_Z + 1.6
SLOT_Z1 = SLOT_Z0 + NUT_SLOT_T
Z_TOP = SLOT_Z1 + 1.6
PASS_D, HEAD_D, HEAD_H, WASHER_D, WASHER_ID, WASHER_T, SCREW_D = 3.6, 6.0, 3.2, 7.0, 3.2, 0.5, 3.0
LEAD_R, LEAD_L, SKIN = 0.9, 0.7, 0.2
KIT_L = (8.0, 12.0, 16.0)
CLAMP_L, CLAMP_H0 = 8.0, 1.6
EAR_X, EAR_Y = 45.23, 36.0
FR_BY = 36.0
PX, LAYER, BRIDGE_MAX = 0.1, 0.2, 10.0
SPRING_OD, SPRING_ID, SPRING_FREE, SPRING_SOLID, SPRING_RATE = 4.5, 3.6, 22.0, 8.0, 2.5
CUT = (-32.0, 32.0, -89.4, 13.2)
GB_EARS = [(-38.0, 12.0), (38.0, 12.0), (-38.0, 56.0), (38.0, 56.0)]
CR_ROWS = (47.0, -70.0)
PRINT_UP = dict(AxleFrame="-Z", SwingArm="-Z", PivotBush="-Y", GearboxCradle="+Z")
UPV = {"+X": X, "-X": V(-1, 0, 0), "+Y": Y, "-Y": V(0, -1, 0), "+Z": Z, "-Z": V(0, 0, -1)}

def box(x0, x1, y0, y1, z0, z1):
    x0, x1 = sorted((x0, x1))
    y0, y1 = sorted((y0, y1))
    return Part.makeBox(x1 - x0, y1 - y0, z1 - z0, V(x0, y0, z0))


def cylz(r, x, y, z0, z1):
    return Part.makeCylinder(r, z1 - z0, V(x, y, z0), Z)


def cylx(r, x0, x1, y, z):
    return Part.makeCylinder(r, x1 - x0, V(x0, y, z), X)


def cyly(r, y0, y1, x, z):
    return Part.makeCylinder(r, y1 - y0, V(x, y0, z), Y)


def fuse(*ss):
    r = ss[0]
    for s in ss[1:]:
        r = r.fuse(s)
    q = r.removeSplitter()
    return q if q.isValid() else r


def ring_face(ring, z):
    return Part.Face(Part.makePolygon([V(x, y, z) for x, y in ring.coords]))


def prism_xy(g, z0, z1):
    out = None
    for p in getattr(g, "geoms", [g]):
        s = ring_face(p.exterior, z0).extrude(V(0, 0, z1 - z0))
        for h in p.interiors:
            s = s.cut(ring_face(h, z0 - 1).extrude(V(0, 0, z1 - z0 + 2)))
        out = s if out is None else out.fuse(s)
    return out.removeSplitter()


def prism_xz(pts, y0, y1):
    f = Part.Face(Part.makePolygon([V(x, y0, z) for x, z in pts] + [V(pts[0][0], y0, pts[0][1])]))
    return f.extrude(V(0, y1 - y0, 0))


def hexz(af, x, y, z0, z1, rot=0.0):
    r = af / math.sqrt(3)
    pts = [V(x + r * math.cos(math.radians(a + rot)), y + r * math.sin(math.radians(a + rot)), z0) for a in range(0, 361, 60)]
    return Part.Face(Part.makePolygon(pts)).extrude(V(0, 0, z1 - z0))


def mirror_y(s):
    return s.mirror(O, Y)


def mirror_x(s):
    return s.mirror(O, X)


def rotz(s, deg, c=O):
    s = s.copy()
    s.rotate(c, Z, deg)
    return s


def moved(s, x=0.0, y=0.0, z=0.0):
    s = s.copy()
    s.translate(V(x, y, z))
    return s


def sbox(x0, x1, y0, y1):
    return _sbox(x0, y0, x1, y1)


def rrect(x0, x1, y0, y1, r):
    return sbox(x0, x1, y0, y1).buffer(-r, quad_segs=8).buffer(r, quad_segs=8)


# ---- constants. UNVERIFIED: spring wire, rate, rod diameter and wall, PLA stiffness
JCX, FORK = 53.28, 44.88
KPX = JCX + FORK
WHEEL_OFF = 11.69
WHEEL_D, WHEEL_W, STEER_DEG = 110.0, 26.0, 28.0
PAD_TOP, PAD_T = 29.0, 2.6
THETA = 16.2
STATIC_N = 2.45
SP, LH = 32.0, 12.0
HH = LH / 2
SPRING_OD, SPRING_WIRE, SPRING_FREE, SPRING_RATE, SPRING_SOLID = 9.13, 1.04, 34.9, 2.2, 13.0
SPRING_ID = SPRING_OD - 2 * SPRING_WIRE
E_S = 22.0
X_S = JCX - E_S
SHIM_T, NSHIM = 1.0, 2
PIN_D, PIN_H = 6.2, 24.0
POCKET_D, POCKET_DEPTH, PED_D, PED_H = 11.7, 6.5, 14.2, 8.0
NSHIM_MAX = 4
TPOCKET_D, TPOCKET_DEPTH = 11.6, 0.0
TFLOOR_D = 9.3
FL_Z0, FL_T = 29.2, 2.4
FL_Z1 = FL_Z0 + FL_T
PK_Z = FL_Z1 + PED_H - POCKET_DEPTH
SPR_BOT = PK_Z + NSHIM * SHIM_T
F_RIDE = STATIC_N * FORK / E_S
L_RIDE = SPRING_FREE - F_RIDE / SPRING_RATE
Z_TB = SPR_BOT + L_RIDE - TPOCKET_DEPTH
ZL = Z_TB + HH
ZU = ZL + SP
ROD_D, ROD_BORE, ROD_L = 8.0, 8.4, 495.0
ROD_X, ROD_Z, ROD_Y = 57.0, 56.0, 23.3
BOSS_WALL = 2.5
R_BORE = ROD_BORE / 2
R_B = R_BORE + BOSS_WALL
BOSS_L = 14.4
ROOF_Z, FLAT_DEG = 4.6, 50.0
NUT_AF, NUT_POCKET_AF, NUT_T, NUT_SLOT_T = 5.5, 5.8, 2.4, 2.6
SLOT_Z0 = ROOF_Z + 1.6
SLOT_Z1 = SLOT_Z0 + NUT_SLOT_T
Z_TOP = SLOT_Z1 + 1.6
PASS_D, HEAD_D, HEAD_H, WASHER_D, WASHER_ID, WASHER_T, SCREW_D = 3.6, 6.0, 3.2, 7.0, 3.2, 0.5, 3.0
LEAD_R, LEAD_L, SKIN = 0.9, 0.7, 0.2
KIT_L = (8.0, 12.0, 16.0)
CLAMP_L, CLAMP_H0 = 8.0, 1.6
EAR_X, EAR_Y = 45.23, 36.0
PX, LAYER, BRIDGE_MAX = 0.1, 0.2, 10.0
Y_IC0, Y_IC1 = 16.1, 21.3
LIP_T = 1.2
NUT_LIP_AF = 5.4
Y_LUG0, Y_LUG1 = 21.5, 26.3
Y_OC0, Y_OC1 = 26.5, 30.5
Y_FL1 = 31.7
LUG_BORE, BUSH_OD, BUSH_ID, FLANGE_D, FLANGE_T = 6.2, 5.6, 3.2, 10.0, 1.2
NUT_PD = 3.8
CHEEK_HOLE = 6.1
GB_EARS = [(-38.0, 12.0), (38.0, 12.0), (-38.0, 56.0), (38.0, 56.0)]
CR_ROWS = (47.0, -97.5)
PRINT_UP = dict(AxleFrame="+Z", Link="+Z", Upright_R="+Z", Upright_L="+Z", PivotBush="-Y", Dowel="-Z", Shim="+Z", GearboxCradle="+Z")
UPV = {"+X": X, "-X": V(-1, 0, 0), "+Y": Y, "-Y": V(0, -1, 0), "+Z": Z, "-Z": V(0, 0, -1)}
# hub pad holes in car x offsets from the kingpin (inboard positive) and y; the strut side hole (7.2, +12.5) is blocked below the pad
HOLES = [(18.0, 10.0), (18.0, -10.0), (7.2, -12.5)]
DOWEL_AT = (7.2, 12.5)
DOWEL_D, DOWEL_L = 4.5, 2.6
UP_T0, UP_T1 = PAD_TOP, PAD_TOP + 2.4
PAD_W = 14.0
PAD_Z = 5.5
THETA_A = -10.0
WIDE_HW = 7.8
X_CB0, X_CB1 = 68.0, 74.0
TAIL_W = 7.6
TAIL_H = 17.0
ROOF_T = 5.0
WIN_X0, WIN_X1 = 40.0, 46.0
X_W = (WIN_X0 + WIN_X1) / 2
WIN_HW = TAIL_W / 2 + 0.8
STOP_PADH = 2.3
OCT = HH * math.tan(math.radians(22.5))
LEG_HX0, LEG_HX1 = 18.8, 29.0
PL_HX0 = 1.0
UP_WEB_T, UP_WEB_Z = 8.0, 57.0
UP_WEB2_HX = 12.4
UP_BAND_W = 21.0
UP_BAR_HW = 12.0
UP_TIE_T = 2.4
LEG_T = 2.8
LEG_X0, LEG_X1 = 44.5, ROD_X + R_B
BOSS_TOP = ZL - 10.5
BOSS_BOT = ROD_Z - Z_TOP
POST_X0, POST_X1 = JCX - 8.0, ROD_X + R_B
WALL_X0, WALL_X1 = WIN_X1 - 3.0, WIN_X1
COLLAR_HW = 11.0
PED_PLATE = (X_S - 7.5, WIN_X1, -8.5, 8.5)
BAR_Y0, BAR_Y1 = 31.5, 40.5
SHIM_OD, SHIM_ID = 11.2, 6.7
DOWEL_FL_D, DOWEL_FL_T = 9.0, 1.2
DOWEL_REC_D = 9.4

# ---- reference modules, loaded from their saved FCStd files
def load_refs():
    R = {}
    for f in ("DriveHub", "Differential", "Gearbox3", "DriveShaft"):
        d = App.openDocument(HERE + f + ".FCStd")
        R[f] = {o.Name: o.Shape.copy() for o in d.Objects if hasattr(o, "Shape") and o.Shape.Solids}
        App.closeDocument(d.Name)
    return R


HUBF = {}


def hub_funcs():
    if not HUBF:
        HUBF.update({"NO_RUN": True, "__name__": "drive_hub"})
        exec(compile(open(HERE + "drive_hub.py").read(), "drive_hub.py", "exec"), HUBF)
    return HUBF


def c2_car(th):
    return V(JCX + FORK * math.cos(math.radians(th)), 0, FORK * math.sin(math.radians(th)))


def to_car(s, th=0.0, side=1):
    """hub document frame (kingpin at origin, outboard -X) to the car frame at suspension angle th (bump positive), right side; side -1 mirrors"""
    t = mirror_x(s)
    t = moved(t, c2_car(th).x, 0, c2_car(th).z)
    return t if side > 0 else mirror_x(t)


def rot_link(s, theta, z=None):
    s = s.copy()
    s.rotate(V(JCX, 0, ZL if z is None else z), Y, -theta)
    return s


def rotv(s, p, axis, deg):
    s = s.copy()
    s.rotate(p, axis, deg)
    return s


def basis_place(s, cols, origin=O):
    m = App.Matrix(cols[0].x, cols[1].x, cols[2].x, origin.x, cols[0].y, cols[1].y, cols[2].y, origin.y, cols[0].z, cols[1].z, cols[2].z, origin.z, 0, 0, 0, 1)
    s = s.copy()
    s.transformShape(m)
    return s


def unit_v(v):
    v = V(v.x, v.y, v.z)
    v.normalize()
    return v


class Kit:
    """joint parts of the side shaft chain in the car frame: PlugShaft fork - cross - ShortLink assembly - cross - StubYoke fork"""

    def __init__(self, R):
        H, D, S_ = R["DriveHub"], R["Differential"], R["DriveShaft"]
        z0 = 120.0
        g = lambda n: moved(S_[n], 0, 0, z0)
        self.cross = g("Shown_JointCross_S1")
        self.crossB = moved(self.cross, FORK, 0, 0)
        self.shaft = [g("Shown_JointYoke_S2"), g("Shown_ShortLink"), g("Shown_JointYoke_S3")]
        self.plug = moved(D["PlugShaft_R"], 0, 0, -45.0)
        self.pinY, self.pinZ = H["Ref_PinA"], H["Ref_PinB"]
        self.stub = H["StubYoke"]

    def pose(self, th, st=0.0, chi=0.0):
        """parts dict for suspension angle th, steering st, stub spin chi (all degrees); right side"""
        t, c = math.radians(th), math.radians(chi)
        c1 = V(JCX, 0, 0)
        c2 = c2_car(th)
        u = V(math.cos(t), 0, math.sin(t))
        p2 = App.Rotation(Z, -st).multVec(V(0, math.cos(c), math.sin(c)))
        q = unit_v(u.cross(p2))
        p1 = unit_v(X.cross(q))
        if p1.cross(q).dot(u) < 0:
            p1 = p1 * -1
        pB = p2 * -1 if p2.cross(q).dot(u) > 0 else p2
        out = {}
        sh = lambda s, cols, o: basis_place(s, cols, o)
        sg = [sh(s, [u, q.cross(u), q], c1) for s in self.shaft]
        out["YokeS2"], out["ShortLink"], out["YokeS3"] = sg
        out["CrossA"] = sh(self.cross, [p1.cross(q), p1, q], c1)
        out["CrossB"] = sh(self.cross, [pB.cross(q), pB, q], c2)
        out["PinA"] = sh(self.pinY, [p1.cross(q), p1, q], c1)
        out["PinB"] = sh(self.pinZ, [p1.cross(q), p1, q], c1)
        out["PinC"] = sh(self.pinY, [pB.cross(q), pB, q], c2)
        out["PinD"] = sh(self.pinZ, [pB.cross(q), pB, q], c2)
        phi = math.degrees(math.atan2(p1.z, p1.y))
        out["PlugShaft"] = rotv(self.plug, O, X, phi)
        stub = rotv(self.stub, O, X, chi)
        stub = rotv(stub, O, Z, st)
        out["StubYoke"] = to_car(stub, th)
        return out


def hub_parts(R, th, st):
    """steering group and carrier of one DriveHub unit in the car frame (right side)"""
    H = R["DriveHub"]
    hf = hub_funcs()
    out = {"HubCarrier": to_car(H["HubCarrier"], th)}
    for n in ("Knuckle", "Wheel", "Tyre", "PivotBush_1", "PivotBush_2", "Sleeve_1", "Sleeve_2", "Ref_PivotScrew_U", "Ref_PivotScrew_L", "Ref_HubScrew"):
        out[n] = to_car(hf["rp"](H[n], O, Z, st), th)
    return out


def layout_y(R):
    gb, ds, D = R["Gearbox3"], R["DriveShaft"], R["Differential"]
    joff = -ds["DummyPort_1"].BoundBox.XMax
    depth = ds["DummyPort_1"].BoundBox.XMax - ds["JointYoke_1"].BoundBox.XMin
    lcs = (ds["Shown_JointCross_S2"].BoundBox.XMin + ds["Shown_JointCross_S2"].BoundBox.XMax) / 2 - (ds["Shown_JointCross_S1"].BoundBox.XMin + ds["Shown_JointCross_S1"].BoundBox.XMax) / 2
    pa = D["PinionShaftA"].BoundBox.YMax
    t = gb["ThroughShaft"].BoundBox
    yr = (t.YMin - joff) - lcs - (pa + joff)
    yf = (t.YMax + joff) + lcs + (pa + joff)
    return dict(joff=joff, depth=depth, lcs=lcs, pa=pa, yr=yr, yf=yf, m_r=t.YMin + depth, m_f=t.YMax - depth)


def short_shaft(R, m1, sign):
    ds = R["DriveShaft"]
    x0 = ds["Shown_JointYoke_S1"].BoundBox.XMin
    names = ("Shown_JointYoke_S1", "Shown_JointYoke_S2", "Shown_JointCross_S1", "Shown_ShortLink", "Shown_JointYoke_S3", "Shown_JointYoke_S4", "Shown_JointCross_S2")
    return [moved(rotz(moved(ds[n], -x0, 0, 120.0), 90 * sign), 0, m1, 0) for n in names]


def diff_parts(R, front):
    D = R["Differential"]
    parts = {n: s for n, s in D.items() if n not in ("OutputPlug", "HalfShaft_L", "HalfShaft_R", "PlugShaft_L", "PlugShaft_R")}
    parts.update({n: moved(D[n], 0, 0, -45.0) for n in ("PlugShaft_L", "PlugShaft_R")})
    if front:
        parts = {n: rotz(s, 180.0) for n, s in parts.items()}
    return parts


def port_axis(s, y):
    b = Part.makeCompound(s.slice(Y, y)).BoundBox
    return ((b.XMin + b.XMax) / 2, (b.ZMin + b.ZMax) / 2)



# ---- link kinematics helpers (link local frame is the car frame at ride, pivot axis through (JCX, y, ZL))
def rot_pt(x, z, theta, cx=JCX, cz=None):
    cz = ZL if cz is None else cz
    t = math.radians(theta)
    dx, dz = x - cx, z - cz
    return cx + dx * math.cos(t) - dz * math.sin(t), cz + dx * math.sin(t) + dz * math.cos(t)


STOP_Q = (X_W, Z_TB + TAIL_H + STOP_PADH)
Z_ROOF = rot_pt(*STOP_Q, -THETA)[1]
STOP_M = math.tan(math.radians(THETA))


def pad_poly():
    xs = (X_W - 3.5, X_W + 3.5)
    ztop = lambda x: STOP_Q[1] + (x - STOP_Q[0]) * STOP_M
    xc = X_W + 2.0
    return [(xs[0], Z_TB + TAIL_H - 0.01), (xs[1], Z_TB + TAIL_H - 0.01), (xs[1], ztop(xc)), (xc, ztop(xc)), (xs[0], ztop(xs[0]))]


def tear_roof_y(r, y0, y1, x, z, up=1):
    """round hole along Y whose roof is a 45 degree point at car +Z (up=1) or -Z (up=-1)"""
    k = math.sqrt(2) * r
    rng = range(135, 406, 9) if up > 0 else range(-45, 226, 9)
    pts = [(x + r * math.cos(math.radians(d)), z + r * math.sin(math.radians(d))) for d in rng] + [(x, z + up * k)]
    return prism_xz(pts, y0, y1)


def arm_poly():
    a, o = HH, OCT
    return [(JCX - o, ZL + a), (KPX + o, ZL + a), (KPX + a, ZL + o), (KPX + a, ZL - o), (KPX + o, ZL - a), (JCX - o, ZL - a), (JCX - a, ZL - o), (JCX - a, ZL + o)]


def build_link():
    parts = []
    for sg in (1, -1):
        y0, y1 = sorted((sg * Y_LUG0, sg * Y_LUG1))
        parts.append(prism_xz(arm_poly(), y0, y1))
    parts.append(box(X_CB0, X_CB1, -Y_LUG0 - 0.01, Y_LUG0 + 0.01, Z_TB, ZL + HH))
    parts.append(box(X_S, X_CB0 + 0.01, -TAIL_W / 2, TAIL_W / 2, Z_TB, Z_TB + TAIL_H))
    parts.append(box(X_S - PAD_W / 2, X_S + PAD_W / 2, -PAD_W / 2, PAD_W / 2, Z_TB, Z_TB + PAD_Z))
    parts.append(prism_xz(pad_poly(), -TAIL_W / 2, TAIL_W / 2))
    s = fuse(*parts)
    for sg in (1, -1):
        y0, y1 = sorted((sg * Y_LUG0, sg * Y_LUG1))
        for x in (JCX, KPX):
            s = s.cut(tear_roof_y(LUG_BORE / 2, y0 - 1, y1 + 1, x, ZL, 1))
    return s.removeSplitter()


def build_bush():
    """print flange down, car -Y up: tube through the lug and the outer cheek, flange outside"""
    L = Y_OC1 - Y_IC1
    b = Part.makeCylinder(FLANGE_D / 2, FLANGE_T, V(0, Y_OC1, 0), Y).fuse(Part.makeCylinder(BUSH_OD / 2, L + 0.01, V(0, Y_IC1, 0), Y))
    return b.cut(Part.makeCylinder(BUSH_ID / 2, L + FLANGE_T + 2, V(0, Y_IC1 - 1, 0), Y)).removeSplitter()


Z_WIDE = max(rot_pt(x, Z_TB + PAD_Z, THETA_A)[1] for x in (X_S - PAD_W / 2, X_S + PAD_W / 2)) + 0.8


# ---- cheek profiles (xz) shared by Upright and AxleFrame posts: octagon lug zones at both rows, joined by a vertical bar
def octagon(cx, cz):
    a, o = HH, OCT
    return Polygon([(cx - o, cz + a), (cx + o, cz + a), (cx + a, cz + o), (cx + a, cz - o), (cx + o, cz - a), (cx - o, cz - a), (cx - a, cz - o), (cx - a, cz + o)])


def rect(x0, x1, z0, z1):
    return sbox(x0, x1, z0, z1)


def sx_pts(g):
    return list(g.exterior.coords)[:-1]


def prism_g(g, y0, y1):
    out = None
    for p in getattr(g, "geoms", [g]):
        s = prism_xz(sx_pts(p), y0, y1)
        for h in p.interiors:
            s = s.cut(prism_xz(list(h.coords)[:-1], y0 - 1, y1 + 1))
        out = s if out is None else out.fuse(s)
    return out.removeSplitter()


def hex_y(y0, y1, x, z, af=None):
    r = (af or NUT_POCKET_AF) / math.sqrt(3)
    return prism_xz([(x + r * math.cos(math.radians(60 * k)), z + r * math.sin(math.radians(60 * k))) for k in range(6)], y0, y1)


def cheek_cuts(x, zs, y_in, sg):
    """nut pocket (inner cheek) and bush hole with a 45 degree roof (outer cheek), at pivot x and rows zs, side sg"""
    cuts = []
    for z in zs:
        a0, a1 = sorted((sg * (Y_IC0 + LIP_T), sg * (Y_IC0 + NUT_PD)))
        cuts.append(hex_y(a0, a1, x, z))
        a0, a1 = sorted((sg * (Y_IC0 - 1), sg * (Y_IC0 + LIP_T + 0.01)))
        cuts.append(hex_y(a0, a1, x, z, NUT_LIP_AF))
        b0, b1 = sorted((sg * (Y_IC0 - 1), sg * (Y_IC1 + 1)))
        cuts.append(cyly(PASS_D / 2, b0, b1, x, z))
        c0, c1 = sorted((sg * (Y_OC0 - 1), sg * (Y_OC1 + 1)))
        cuts.append(tear_roof_y(CHEEK_HOLE / 2, c0, c1, x, z, 1))
    return cuts


UC0 = (KPX + OCT) - (ZL - HH)
UP_ZTOP = ZU + 7.5 + UP_TIE_T


def upright_cheek():
    xr = KPX - LEG_HX0 + 0.0
    xl = KPX - LEG_HX1
    xr = KPX - 14.0 if False else KPX - LEG_HX0
    za = xr - UC0 + 0.0
    leg = Polygon([(xl, UP_T0), (xr, UP_T0), (xr, za + UP_BAND_W), (xl, za + UP_BAND_W - (xr - xl))])
    diag = Polygon([(xr, za), (KPX + OCT, ZL - HH), (KPX + OCT, ZL - HH + UP_BAND_W), (xr, za + UP_BAND_W)])
    zb = ZL - 4.0
    bar = Polygon([(KPX - 4.0, zb), (KPX + 4.0, zb), (KPX + UP_BAR_HW, zb + UP_BAR_HW - 4.0), (KPX + UP_BAR_HW, UP_ZTOP), (KPX - UP_BAR_HW, UP_ZTOP), (KPX - UP_BAR_HW, zb + UP_BAR_HW - 4.0)])
    g = unary_union([leg, diag, octagon(KPX, ZL), octagon(KPX, ZU), bar])
    cb = sbox(X_CB0, X_CB1, Z_TB, ZL + HH)
    notch = unary_union([affinity.rotate(cb, a_, origin=(KPX, ZL)) for a_ in np.linspace(-THETA, THETA, 9)] + [affinity.rotate(sbox(X_CB0, X_CB1, Z_TB + SP, ZL + HH + SP), a_, origin=(KPX, ZU)) for a_ in np.linspace(-THETA, THETA, 9)]).buffer(0.9, join_style=2)
    return g.difference(notch).simplify(0.001)


def hx_box(a, b, y0, y1):
    return KPX - b, KPX - a, y0, y1


def upright_plate():
    g = unary_union([sbox(*hx_box(PL_HX0, LEG_HX1, -16.5, 16.5)), sbox(*hx_box(PL_HX0, 12.5, -18.6, 18.6)), sbox(KPX - LEG_HX1, KPX - LEG_HX0, -Y_OC1, Y_OC1)])
    return g.difference(Point(KPX, 0).buffer(3.9, quad_segs=8))


def build_upright():
    ch = upright_cheek()
    parts = [prism_xy(upright_plate(), UP_T0, UP_T1)]
    for sg in (1, -1):
        for a, b in ((Y_IC0, Y_IC1), (Y_OC0, Y_OC1)):
            y0, y1 = sorted((sg * a, sg * b))
            parts.append(prism_g(ch, y0, y1))
        for z0, z1 in ((ZU + 7.5, ZU + 7.5 + UP_TIE_T), ((ZL + ZU) / 2 - 1.2, (ZL + ZU) / 2 + 1.2)):
            xa = KPX - 1.0 if z0 > ZU else KPX - 3.0
            y0, y1 = sorted((sg * (Y_IC1 - 0.01), sg * (Y_OC0 + 0.01)))
            parts.append(box(xa, KPX + HH, y0, y1, z0, z1))
    parts.append(box(KPX - LEG_HX1, KPX - LEG_HX1 + UP_WEB_T, -Y_OC1, Y_OC1, UP_T0, UP_WEB_Z))
    s = fuse(*parts)
    for sg in (1, -1):
        for c in cheek_cuts(KPX, (ZL, ZU), None, sg):
            s = s.cut(c)
    for hx_, hy in HOLES:
        s = s.cut(cylz(PASS_D / 2, KPX - hx_, hy, UP_T0 - 1, UP_T1 + 1))
    s = s.cut(cylz(DOWEL_REC_D / 2, KPX - DOWEL_AT[0], DOWEL_AT[1], UP_T0 - 1, UP_T0 + DOWEL_FL_T + 0.2))
    return s.removeSplitter()


# ---- AxleFrame (print +Z up, floor on the bed). Right half built, left half is its mirror.
def bump_floor(x):
    return _bump_floor(x) - 0.03


def _bump_floor(x):
    (x1, z1), (x2, z2) = rot_pt(JCX - 20, Z_TB, THETA), rot_pt(JCX + 20, Z_TB, THETA)
    return z1 + (x - x1) * (z2 - z1) / (x2 - x1)


Z_WALL_TOP = Z_ROOF + ROOF_T


def boss_up_add():
    return box(LEG_X0 - ROD_X, R_B + 7.0, -BOSS_L / 2, BOSS_L / 2, -Z_TOP, BOSS_TOP - ROD_Z)


def boss_up_cut(y0, y1):
    """rod bore with a 45 degree roof point up, lead-ins, M3 clamp from below through a nut slot (flat roof, 0.2 skin above it)"""
    c = [tear_roof_y(R_BORE, y0 - 1, y1 + 1, 0, 0, 1)]
    for sgn, yy in ((1, y1), (-1, y0)):
        c.append(Part.makeCone(R_BORE + LEAD_R + 0.02, R_BORE, LEAD_L + 0.02, V(0, yy + sgn * 0.02, 0), V(0, -sgn, 0)))
    ymid = (y0 + y1) / 2
    c.append(cylz(PASS_D / 2, 0, ymid, -SLOT_Z0 + SKIN, 0))
    c.append(cylz(PASS_D / 2, 0, ymid, -(Z_TOP - SKIN), -SLOT_Z1))
    c.append(box(-3.5, R_B + 8.0, ymid - NUT_POCKET_AF / 2, ymid + NUT_POCKET_AF / 2, -SLOT_Z1, -SLOT_Z0))
    return c


def post_cheek():
    zb, zt = BOSS_TOP, ZU + 7.5 + UP_TIE_T
    return Polygon([(POST_X0, zb), (POST_X1, zb), (POST_X1, zt), (POST_X0, zt)])


def prism_yz(pts, x0, x1):
    f = Part.Face(Part.makePolygon([V(x0, y, z) for y, z in pts] + [V(x0, pts[0][0], pts[0][1])]))
    return f.extrude(V(x1 - x0, 0, 0))


def build_frame_half():
    """right half: two posts (y signs), floor, wall, collar, pedestal, ear columns; returns (solid, cuts list)"""
    parts, cuts = [], []
    for sg in (1, -1):
        for a, b in ((Y_IC0, Y_IC0 + LEG_T), (Y_OC1 - LEG_T, Y_OC1)):
            y0, y1 = sorted((sg * a, sg * b))
            parts.append(box(LEG_X0, LEG_X1, y0, y1, FL_Z0, BOSS_TOP))
        yb0, yb1 = sorted((sg * Y_IC0, sg * Y_OC1))
        parts.append(box(LEG_X0, ROD_X + R_B, yb0, yb1, BOSS_BOT, BOSS_TOP))
        for a, b in ((Y_IC0, Y_IC1), (Y_OC0, Y_OC1)):
            y0, y1 = sorted((sg * a, sg * b))
            parts.append(prism_g(post_cheek(), y0, y1))
        for z0, z1, xa, xb in ((ZU + 7.5, ZU + 7.5 + UP_TIE_T, JCX - 8.0, JCX + 1.0), ((ZL + ZU) / 2 - 1.2, (ZL + ZU) / 2 + 1.2, JCX - 8.0, JCX + 6.0)):
            y0, y1 = sorted((sg * (Y_IC1 - 0.01), sg * (Y_OC0 + 0.01)))
            parts.append(box(xa, xb, y0, y1, z0, z1))
        for a, b in ((Y_IC0, Y_IC0 + LEG_T), (Y_OC1 - LEG_T, BAR_Y0 + 0.5)):
            y0, y1 = sorted((sg * a, sg * b))
            parts.append(box(LEG_X0, LEG_X1, y0, y1, FL_Z0, FL_Z1))
        ym = sg * ROD_Y
        yy0, yy1 = sorted((sg * Y_IC0, sg * Y_OC1))
        for c in boss_up_cut(yy0, yy1):
            cuts.append(moved(c, ROD_X, 0, ROD_Z))
        for z in (ZL, ZU):
            pass
        for c in cheek_cuts(JCX, (ZL, ZU), None, sg):
            cuts.append(c)
        ear = prism_xy(rrect(EAR_X - 4.3, EAR_X + 3.4, sg * EAR_Y - 4.5, sg * EAR_Y + 4.5, 1.2), FL_Z0, FL_Z0 + 8.5)
        parts.append(ear)
        cuts.append(Part.makeCylinder(1.4, 8.0, V(EAR_X, sg * EAR_Y, FL_Z0 - 0.1), Z))
        parts.append(box(-EAR_X - 4.3 if False else 0.0, EAR_X + 3.4, sg * BAR_Y0 if sg > 0 else -BAR_Y1, sg * BAR_Y1 if sg > 0 else -BAR_Y0, FL_Z0, FL_Z1))
    parts.append(box(PED_PLATE[0], PED_PLATE[1], PED_PLATE[2], PED_PLATE[3], FL_Z0, FL_Z1))
    parts.append(box(WALL_X0, WALL_X1, -Y_IC0 - 0.05, Y_IC0 + 0.05, FL_Z0, Z_WALL_TOP))
    parts.append(box(WIN_X0, WIN_X1, -COLLAR_HW, COLLAR_HW, FL_Z0, Z_WALL_TOP))
    zf0, zf1 = bump_floor(WIN_X0), bump_floor(WIN_X1)
    parts.append(cylz(PED_D / 2, X_S, 0, FL_Z0, FL_Z1 + PED_H))
    parts.append(cylz(PIN_D / 2, X_S, 0, PK_Z, PK_Z + PIN_H))
    xc = WIN_X1 - 1.2
    zfl = bump_floor(xc)
    win = Polygon([(WIN_X0 - 0.01, zf0), (xc, zfl), (WIN_X1 + 0.01, zfl), (WIN_X1 + 0.01, Z_WIDE), (WIN_X0 - 0.01, Z_WIDE)])
    cuts.append(prism_xz(sx_pts(win), -WIDE_HW, WIDE_HW))
    fun = Polygon([(-WIDE_HW, Z_WIDE - 0.01), (WIDE_HW, Z_WIDE - 0.01), (WIN_HW, Z_WIDE + WIDE_HW - WIN_HW), (WIN_HW, Z_ROOF + 0.03), (-WIN_HW, Z_ROOF + 0.03), (-WIN_HW, Z_WIDE + WIDE_HW - WIN_HW)])
    cuts.append(prism_yz(sx_pts(fun), WIN_X0 - 0.01, WIN_X1 + 0.01))
    win = Polygon([(WIN_X0 - 0.01, Z_WIDE - 0.01), (WIN_X1 + 0.01, Z_WIDE - 0.01), (WIN_X1 + 0.01, Z_ROOF + 0.03), (WIN_X0 - 0.01, Z_ROOF + 0.03)])
    cuts.append(prism_xz(sx_pts(win), -WIN_HW, WIN_HW))
    cuts.append(cylz(POCKET_D / 2, X_S, 0, PK_Z, FL_Z1 + PED_H + 1))
    return parts, cuts


def build_frame():
    parts, cuts = build_frame_half()
    left = [mirror_x(p) for p in parts]
    s = fuse(*(parts + left))
    for c in cuts:
        s = s.cut(c).cut(mirror_x(c))
    pin = fuse(cylz(PIN_D / 2, X_S, 0, PK_Z, PK_Z + PIN_H))
    for p in (cylz(PIN_D / 2, X_S, 0, PK_Z - 0.01, PK_Z + PIN_H), cylz(PIN_D / 2, -X_S, 0, PK_Z - 0.01, PK_Z + PIN_H)):
        s = s.fuse(p)
    return s.removeSplitter()

# ---- small parts
def build_dowel():
    s = Part.makeCylinder(DOWEL_D / 2, DOWEL_L + 0.01, V(0, 0, 0), Z).fuse(Part.makeCylinder(DOWEL_FL_D / 2, DOWEL_FL_T, V(0, 0, DOWEL_L), Z))
    return s.removeSplitter()


def build_shim():
    return Part.makeCylinder(SHIM_OD / 2, SHIM_T, O, Z).cut(Part.makeCylinder(SHIM_ID / 2, SHIM_T + 2, V(0, 0, -1), Z))

# ---- rod boss for the cradle (old closed block, screw from above)
# ---- rod boss: closed rigid block, bore with teardrop roof pointing down (car), one M3x8 clamp screw from below through a captive nut
PHI = math.radians(FLAT_DEG)
TX, TZ = R_BORE * math.sin(PHI), R_BORE * math.cos(PHI)
XR = TX - (ROOF_Z - TZ) / math.tan(PHI)


def boss_add():
    b = box(-R_B, R_B, -BOSS_L / 2, BOSS_L / 2, -Z_TOP, R_B)
    return b.makeFillet(2.5, [e for e in b.Edges if abs(e.BoundBox.ZLength - (R_B + Z_TOP)) < 1e-6])


def boss_cut():
    c = [prism_xz([(-TX, -TZ), (-XR, -ROOF_Z), (XR, -ROOF_Z), (TX, -TZ)], -BOSS_L / 2 - 1, BOSS_L / 2 + 1), cyly(R_BORE, -BOSS_L / 2 - 1, BOSS_L / 2 + 1, 0, 0)]
    for sg in (1, -1):
        c.append(Part.makeCone(R_BORE + LEAD_R + 0.02, R_BORE, LEAD_L + 0.02, V(0, sg * (BOSS_L / 2 + 0.02), 0), V(0, -sg, 0)))
    c.append(cylz(PASS_D / 2, 0, 0, -SLOT_Z0, -(ROOF_Z + SKIN)))
    c.append(cylz(PASS_D / 2, 0, 0, -(Z_TOP + 1), -(SLOT_Z1 + SKIN)))
    c.append(box(-3.5, R_B + 1, -NUT_POCKET_AF / 2, NUT_POCKET_AF / 2, -SLOT_Z1, -SLOT_Z0))
    return fuse(*c)


def boss_at(y, sxs=(1, -1)):
    a, c = boss_add(), boss_cut()
    A, C = [], []
    for sgx in sxs:
        A.append(moved(a if sgx > 0 else mirror_x(a), sgx * ROD_X, y, ROD_Z))
        C.append(moved(c if sgx > 0 else mirror_x(c), sgx * ROD_X, y, ROD_Z))
    return A, C

# ---- gearbox cradle: plate on the bed (print +Z up), two ribs per boss, the boss turned over (clamp screw from above)
def mirror_z(s):
    return s.mirror(O, Z)


def boss_flip_at(y):
    a, c = mirror_z(boss_add()), mirror_z(boss_cut())
    A, C = [], []
    for sgx in (1, -1):
        A.append(moved(a if sgx > 0 else mirror_x(a), sgx * ROD_X, y, ROD_Z))
        C.append(moved(c if sgx > 0 else mirror_x(c), sgx * ROD_X, y, ROD_Z))
    return A, C


def cradle_plate():
    g = [rrect(32, 50, -98, 66.5, 3), rrect(-40, -32, -98, -48, 3), rrect(-43.5, -32, 0, 66.5, 3), rrect(-43.5, 50, -95, -89.4, 2), rrect(-43.5, 50, CUT[3], 20.5, 2), rrect(-43.5, 50, 59, 66.5, 2)]
    for yb in CR_ROWS:
        g += [rrect(48, ROD_X + R_B, yb - 7, yb + 7, 2), rrect(-ROD_X - R_B, -42, yb - 7, yb + 7, 2)]
    p = unary_union(g).buffer(3, quad_segs=8).buffer(-3, quad_segs=8)
    p = p.difference(sbox(*CUT)).difference(rrect(37.5, 44.5, -83, -58, 3)).difference(rrect(37.5, 44.5, -52, -6, 3)).difference(rrect(-33.5, 33.5, 20.5, 59, 8))
    return p.simplify(0.01)


def build_cradle():
    plate = cradle_plate()
    adds, cuts = [], []
    for yb in CR_ROWS:
        a, c = boss_flip_at(yb)
        adds += a
        cuts += c
        for sgx in (1, -1):
            for xr in (ROD_X - R_B, ROD_X + R_B - 2.4):
                x0, x1 = sorted((sgx * xr, sgx * (xr + 2.4)))
                adds.append(prism_xy(plate.intersection(sbox(x0, x1, yb - BOSS_L / 2, yb + BOSS_L / 2)), Z1 - 0.5, ROD_Z - R_B + 0.5))
    s = fuse(prism_xy(plate, Z0, Z1), *adds)
    for c in cuts:
        s = s.cut(c)
    for x, y in GB_EARS:
        s = s.cut(hexz(NUT_POCKET_AF, x, y, Z0 - 1, Z0 + NUT_SLOT_T, 90)).cut(cylz(PASS_D / 2, x, y, Z0 + NUT_SLOT_T + SKIN, Z1 + 1))
    return s.removeSplitter()


Z0, FLOOR_T = 29.0, 4.0
Z1 = Z0 + FLOOR_T
# ---- print rules P1 to P6 on the solids, same method as gearbox_module.py
P1_COS, FLAT_COS = math.cos(math.radians(45.0)) + 1e-4, 0.9999
SAG_MAX, HOLE_R_MAX = 0.3, 3.0
BED_MIN, TALL_MAX, FIRST_WALL, LOST_MAX = 60.0, 4.0, 0.8, 1.0


def convex(f):
    c = f.Surface
    u0, u1, v0, v1 = f.ParameterRange
    um, vm = (u0 + u1) / 2, (v0 + v1) / 2
    r = f.valueAt(um, vm) - c.Center
    return f.normalAt(um, vm).dot(r - c.Axis * r.dot(c.Axis)) > 0


def to_print(name, s):
    up = UPV[PRINT_UP[name]]
    s = s.copy()
    s.transformShape(App.Placement(V(0, 0, 0), App.Rotation(up, Z)).toMatrix())
    s.transformShape(App.Placement(V(0, 0, -min(v.Z for v in s.Vertexes)), App.Rotation()).toMatrix())
    return s


def slopes(s):
    """P1 and P4: every face of the part in print orientation; flat down faces are judged by the layer test"""
    bad, holes = [], []
    for f in s.Faces:
        sf = f.Surface
        if isinstance(sf, Part.Plane):
            worst = -f.normalAt(0, 0).z
        else:
            if isinstance(sf, Part.Cylinder) and abs(sf.Axis.z) < 1e-6 and sf.Radius <= HOLE_R_MAX and not convex(f):
                d = V(sf.Axis.x, sf.Axis.y, 0)
                ts = [v.X * d.x + v.Y * d.y for v in f.Vertexes]
                holes.append((sf.Center, d, sf.Radius, min(ts) - 0.05, max(ts) + 0.05))
                continue
            u0, u1, v0, v1 = f.ParameterRange
            worst = max(-f.normalAt(u0 + (u1 - u0) * i / 8, v0 + (v1 - v0) * j / 8).z for i in range(9) for j in range(9))
        if P1_COS < worst < FLAT_COS or (worst >= FLAT_COS and not isinstance(sf, Part.Plane)):
            bad.append((round(math.degrees(math.acos(min(worst, 1.0))), 1), [round(c, 1) for c in f.CenterOfMass]))
    return bad, holes


def mesh(s):
    v, f = s.tessellate(0.02)
    return np.array([(p.x, p.y, p.z) for p in v])[np.array(f)]


def region(tri, z):
    """cross section of the triangle mesh at height z as a shapely region (even odd over the closed outlines)"""
    zs = tri[:, :, 2]
    t = tri[(zs.min(1) < z) & (zs.max(1) > z)]
    segs = []
    for i, j in ((0, 1), (1, 2), (2, 0)):
        a, b = t[:, i], t[:, j]
        c = (a[:, 2] - z) * (b[:, 2] - z) < 0
        k = ((z - a[c, 2]) / (b[c, 2] - a[c, 2]))[:, None]
        segs.append((np.nonzero(c)[0], (a[c] + k * (b[c] - a[c]))[:, :2]))
    pts = np.full((len(t), 2, 2), np.nan)
    cnt = np.zeros(len(t), int)
    for idx, p in segs:
        pts[idx, cnt[idx]] = p
        cnt[idx] += 1
    ls = linemerge(MultiLineString([[tuple(np.round(q[0], 5)), tuple(np.round(q[1], 5))] for q in pts if q[0, 0] == q[0, 0] and q[1, 0] == q[1, 0]]))
    g = Polygon()
    for r in getattr(ls, "geoms", [ls]):
        if not r.is_ring:
            return None
        g = g.symmetric_difference(Polygon(r).buffer(0))
    return g


def roof(h, z):
    """footprint at height z of a round horizontal hole of dia 6 or less (P4 lets its roof stay round)"""
    c, d, r, t0, t1 = h
    if abs(z - c.z) >= r:
        return Polygon()
    w, n = math.sqrt(r * r - (z - c.z) ** 2) + 0.02, V(-d.y, d.x, 0)
    s0 = c.x * n.x + c.y * n.y
    return Polygon([(d.x * t + n.x * (s0 + sg * w), d.y * t + n.y * (s0 + sg * w)) for t, sg in ((t0, -1), (t1, -1), (t1, 1), (t0, 1))])


def bridge(c, low):
    """P2: a convex region with a straight span of 10 or less and solid under both ends of it"""
    if c.interiors or c.area < 0.95 * c.convex_hull.area:
        return False
    p = list(c.minimum_rotated_rectangle.exterior.coords)
    e = [(p[i + 1][0] - p[i][0], p[i + 1][1] - p[i][1]) for i in range(2)]
    cx, cy = c.centroid.x, c.centroid.y
    for a, b in ((e[0], e[1]), (e[1], e[0])):
        la, lb = math.hypot(*a), math.hypot(*b)
        if la + 2 * SAG_MAX > BRIDGE_MAX or la < 1e-9 or lb < 1e-9:
            continue
        ax, ay, bx, by = a[0] / la, a[1] / la, b[0] / lb, b[1] / lb
        pts = [Point(cx + bx * k * lb * 0.3 + ax * sg * (la / 2 + 0.7), cy + by * k * lb * 0.3 + ay * sg * (la / 2 + 0.7)) for sg in (-1, 1) for k in (-1, 0, 1)]
        if all(low.contains(q) for q in pts):
            return True
    return False


def layers(s, holes):
    """P5 and P6: slice every 0.2 at mid layer; no region may lie more than 0.3 outside the layer below unless it is a bridge"""
    tri = mesh(s)
    h = tri[:, :, 2].max()
    prev, sig0, bad, first = None, None, [], None
    for k in range(int(math.ceil(h / LAYER - 1e-6))):
        z = min(LAYER * k + LAYER / 2, (LAYER * k + h) / 2) + 1e-3
        g = region(tri, z)
        for dz in (0.0137, 0.0271, 0.0413):
            if g is None:
                g = region(tri, z + dz)
        assert g is not None, (z, "section does not close")
        sig = (round(g.area, 3), round(g.length, 3), tuple(round(c, 3) for c in g.bounds), tuple(round(c, 3) for c in g.centroid.coords[0]) if not g.is_empty else 0)
        if sig == sig0:
            continue
        if k == 0:
            first = g
        elif not g.is_empty:
            res = g.difference(prev.buffer(SAG_MAX)).buffer(-0.05).buffer(0.05)
            roofs = unary_union([roof(h, z - LAYER) for h in holes] + [Polygon()])
            for c in getattr(res, "geoms", [res]):
                if c.area > 0.03 and not c.within(roofs) and not bridge(c, prev):
                    bad.append((round(z, 1), round(c.area, 2), [round(c.centroid.x, 1), round(c.centroid.y, 1)]))
        prev, sig0 = g, sig
    b = first.bounds
    lost = first.difference(first.buffer(-FIRST_WALL / 2, join_style=2).buffer(FIRST_WALL / 2, join_style=2)).area
    return dict(bed=round(first.area, 1), tall=round(h / min(b[2] - b[0], b[3] - b[1]), 2), thin=round(lost, 2), layers=bad[:6], nlayers=len(bad))


def printable(name, s):
    p = to_print(name, s)
    r = dict(slopes=None)
    r["slopes"], holes = slopes(p)
    r.update(layers(p, holes))
    return r



def near(a, b, m=30.0):
    p, q = a.BoundBox, b.BoundBox
    return not (p.XMax + m < q.XMin or q.XMax + m < p.XMin or p.YMax + m < q.YMin or q.YMax + m < p.YMin or p.ZMax + m < q.ZMin or q.ZMax + m < p.ZMin)


def vol(a, b):
    return a.common(b).Volume if a.BoundBox.intersect(b.BoundBox) else 0.0


def dist(a, b):
    return a.distToShape(b)[0] if near(a, b) else 99.0


def mind(a, bs):
    return min(dist(a, b) for b in bs)


def comp(ss):
    return Part.makeCompound(list(ss))




def ring_pts(p, d, r, n=8):
    u = d.cross(X if abs(d.x) < 0.9 else Y)
    u.normalize()
    w = d.cross(u)
    return [p + u * (r * math.cos(2 * math.pi * i / n)) + w * (r * math.sin(2 * math.pi * i / n)) for i in range(n)]


def seat(host, p, d, r):
    pts = ring_pts(p, d, r)
    inn = sum(1 for q in pts if host.isInside(q + d * 0.05, 1e-6, True)) / len(pts)
    out = sum(1 for q in pts if host.isInside(q - d * 0.05, 1e-6, True)) / len(pts)
    return inn, out





def place(s, p, d):
    s = s.copy()
    s.transformShape(App.Placement(p, App.Rotation(Z, d)).toMatrix())
    return s


def m3_bolt(p, d, L):
    return Part.makeCylinder(HEAD_D / 2, HEAD_H, p - d * HEAD_H, d).fuse(Part.makeCylinder(SCREW_D / 2, L, p, d))


def m3_washer(p, d):
    return Part.makeCylinder(WASHER_D / 2, WASHER_T, p, d).cut(Part.makeCylinder(WASHER_ID / 2, WASHER_T + 2, p - d, d))


def m3_nut(p, d, rot=0.0):
    n = hexz(NUT_AF, 0, 0, 0, NUT_T, rot).cut(cylz(SCREW_D / 2, 0, 0, -1, NUT_T + 1))
    return place(n, p, d)


def fastener(kind, p, d, L, washers=(), nut=None, rot=0.0, hosts=()):
    core = Part.makeCylinder(1.3, L, p, d).fuse(Part.makeCylinder(HEAD_D / 2, HEAD_H, p - d * HEAD_H, d))
    drv = Part.makeCylinder(3.0, 60.0, p - d * HEAD_H, -d)
    return dict(kind=kind, p=p, d=d, L=L, bolt=m3_bolt(p, d, L), core=core, driver=drv, washers=[m3_washer(q, e) for q, e in washers],
                nut=m3_nut(nut[0], nut[1], rot) if nut else None, nut_p=nut[0] if nut else None, nut_d=nut[1] if nut else None, hosts=hosts)


def thin_walls(name, s, w=1.2):
    p = to_print(name, s)
    tri = mesh(p)
    h = tri[:, :, 2].max()
    bad, sig0 = [], None
    for k in range(int(math.ceil(h / LAYER - 1e-6))):
        z = min(LAYER * k + LAYER / 2, (LAYER * k + h) / 2) + 1e-3
        g = region(tri, z)
        for dz in (0.0137, 0.0271, 0.0413):
            if g is None:
                g = region(tri, z + dz)
        if g is None or g.is_empty:
            continue
        sig = (round(g.area, 3), round(g.length, 3))
        if sig == sig0:
            continue
        sig0 = sig
        res = g.difference(g.buffer(-(w / 2 - 0.01)).buffer(w / 2 - 0.01)).buffer(-0.16)
        for c in getattr(res, "geoms", [res]):
            if c.area > 0.05:
                bad.append((round(z, 1), round(c.area, 2), [round(c.centroid.x, 1), round(c.centroid.y, 1)]))
    return bad[:6], len(bad)


# ---- assembly pose of one axle (right side, axle at y 0). Left side is the mirror in x.
def tail_z(th, x=None):
    x = X_S if x is None else x
    zs = Z_TB + TPOCKET_DEPTH
    (x1, z1), (x2, z2) = rot_pt(x - 5, zs, th), rot_pt(x + 5, zs, th)
    return z1 + (x - x1) * (z2 - z1) / (x2 - x1)


def spring_len(th):
    return tail_z(th) - SPR_BOT


def spring_force(th):
    return max(0.0, SPRING_RATE * (SPRING_FREE - spring_len(th)))


def ride_theta():
    lo, hi = -THETA, THETA
    for _ in range(60):
        m = (lo + hi) / 2
        d = 1e-3
        dL = (spring_len(m + d) - spring_len(m - d)) / (2 * math.radians(d))
        g = spring_force(m) * (-dL) - STATIC_N * FORK * math.cos(math.radians(m))
        if g > 0:
            hi = m
        else:
            lo = m
    return (lo + hi) / 2


def spring_tube(th, top_off=0.02):
    """spring as a tube OD 9.13 ID 7.05 from the seat floor, upper end cut along the tilted seat plane of the Link"""
    t = Part.makeCylinder(SPRING_OD / 2, 80.0, V(X_S, 0, SPR_BOT), Z)
    cap = rot_link(box(X_S - 30, X_S + 30, -30, 30, Z_TB + TPOCKET_DEPTH - top_off, Z_TB + 200), th)
    return t.cut(cap).cut(Part.makeCylinder(SPRING_ID / 2, 90.0, V(X_S, 0, SPR_BOT - 1), Z))


def right_set(R, K, B, th, st=0.0, chi=0.0, kit=True):
    """every fitted part of the right side except the frame and the fixed hardware; B holds the printed parts"""
    dx, dz = FORK * (math.cos(math.radians(th)) - 1), FORK * math.sin(math.radians(th))
    S = {}
    S["Link_L"] = rot_link(B["Link"], th)
    S["Link_U"] = rot_link(moved(B["Link"], 0, 0, SP), th, ZU)
    S["Upright"] = moved(B["Upright"], dx, 0, dz)
    for k, (x, z) in enumerate(((KPX, ZL), (KPX, ZU))):
        for sg in (1, -1):
            b = B["PivotBush"] if sg > 0 else mirror_y(B["PivotBush"])
            S["BushU%d%d" % (k, sg > 0)] = moved(b, x + dx, 0, z + dz)
    for n, s in hub_parts(R, th, st).items():
        S["Hub_" + n] = s
    if kit:
        for n, s in K.pose(th, st, chi).items():
            S["Kit_" + n] = s
    S["Spring"] = spring_tube(th)
    return S


def fixed_set(R, B, FR, rods=True):
    D = R["Differential"]
    F = {"Frame": FR, "CaseTop": D["CaseTop"], "CaseBottom": D["CaseBottom"]}
    for k, (x, z) in enumerate(((JCX, ZL), (JCX, ZU))):
        for sg in (1, -1):
            b = B["PivotBush"] if sg > 0 else mirror_y(B["PivotBush"])
            F["BushF%d%d" % (k, sg > 0)] = moved(b, x, 0, z)
    if rods:
        for k, sg in enumerate((1, -1)):
            F["Rod%d" % k] = cyly(ROD_D / 2, -90, 90, ROD_X, ROD_Z)
    return F


def gap(a, b, thr):
    ba, bb = a.BoundBox, b.BoundBox
    if (ba.XMin - thr > bb.XMax or bb.XMin - thr > ba.XMax or ba.YMin - thr > bb.YMax or bb.YMin - thr > ba.YMax or ba.ZMin - thr > bb.ZMax or bb.ZMin - thr > ba.ZMax):
        return 99.0
    return a.distToShape(b)[0]


KIT_ADJ = {("Kit_CrossA", "Kit_PlugShaft"), ("Kit_CrossA", "Kit_YokeS2"), ("Kit_CrossB", "Kit_YokeS3"), ("Kit_CrossB", "Kit_StubYoke"), ("Kit_YokeS2", "Kit_ShortLink"), ("Kit_ShortLink", "Kit_YokeS3"),
           ("Kit_PinA", "Kit_CrossA"), ("Kit_PinA", "Kit_PlugShaft"), ("Kit_PinB", "Kit_CrossA"), ("Kit_PinB", "Kit_YokeS2"), ("Kit_PinC", "Kit_CrossB"), ("Kit_PinC", "Kit_StubYoke"), ("Kit_PinD", "Kit_CrossB"), ("Kit_PinD", "Kit_YokeS3"),
           ("Kit_PinA", "Kit_YokeS2"), ("Kit_PinB", "Kit_PlugShaft"), ("Kit_PinC", "Kit_YokeS3"), ("Kit_PinD", "Kit_StubYoke")}
HUB_SELF = {"Hub_Knuckle", "Hub_Wheel", "Hub_Tyre", "Hub_PivotBush_1", "Hub_PivotBush_2", "Hub_Sleeve_1", "Hub_Sleeve_2", "Hub_Ref_PivotScrew_U", "Hub_Ref_PivotScrew_L", "Hub_Ref_HubScrew", "Hub_HubCarrier", "Kit_StubYoke"}


def adjacent(a, b):
    return (a, b) in KIT_ADJ or (b, a) in KIT_ADJ or (a in HUB_SELF and b in HUB_SELF)


def pose_report(R, K, B, FR, th, st, chi, thr_mov=0.8, thr_kit=0.3, only_kit=False):
    """overlap volumes and minimum gaps of one pose: returns list of (a, b, volume or gap) violations"""
    S = right_set(R, K, B, th, st, chi)
    F = fixed_set(R, B, FR)
    bad = []
    names = list(S)
    for i, a in enumerate(names):
        sa = S[a]
        for f, sf in (F.items() if (not only_kit or a.startswith("Kit_")) else []):
            if a == "Kit_PlugShaft" and f in ("CaseTop", "CaseBottom"):
                continue
            if a.startswith("Bush") and (f.startswith("BushF") or f == "Frame"):
                continue
            v = vol(sa, sf)
            if v > 1e-4:
                bad.append((a, f, "vol", round(v, 4)))
                continue
            need = 2.0 if f.startswith("Rod") else (0.19 if a.startswith("Link") or a.startswith("Upright") or a.startswith("Bush") else thr_mov)
            if a.startswith("Link") and f == "Frame":
                need = 0.19 if abs(abs(th) - THETA) > 0.01 else -1.0
            if a == "Spring" or a.startswith("Hub_Ref") or a.startswith("Hub_PivotBush") and f.startswith("Bush"):
                continue
            if f.startswith("BushF") and not (a.startswith("Link")):
                need = thr_mov if not a.startswith("Hub") else thr_mov
            if need < 0:
                continue
            g = gap(sa, sf, need)
            if g < need - 1e-6:
                bad.append((a, f, "gap", round(g, 3), need))
        for b in names[i + 1:]:
            sb = S[b]
            if adjacent(a, b) or (only_kit and not (a.startswith("Kit_") or b.startswith("Kit_"))):
                continue
            ka, kb = a.startswith("Kit_"), b.startswith("Kit_")
            if (a.startswith("Bush") and b.startswith("Link")) or (b.startswith("Bush") and a.startswith("Link")) or (a == "Upright" and b.startswith("Hub_HubCarrier")) or (b == "Upright" and a.startswith("Hub_HubCarrier")):
                continue
            if (a.startswith("Bush") and b == "Upright") or (b.startswith("Bush") and a == "Upright"):
                continue
            v = vol(sa, sb)
            if v > 1e-4:
                bad.append((a, b, "vol", round(v, 4)))
                continue
            if a == "Spring" or b == "Spring":
                continue
            need = thr_kit if (ka and kb) else thr_mov
            if a.startswith("Link") and b.startswith("Upright") or b.startswith("Link") and a.startswith("Upright"):
                need = 0.19
            if (a.startswith("Link") and b.startswith("Link")):
                need = 0.8
            g = gap(sa, sb, need)
            if g < need - 1e-6:
                bad.append((a, b, "gap", round(g, 3), need))
    return bad


# ---- strength: hand statics with sections taken from the CAD where it matters. PLA limits 10 MPa in plane, 5 MPa across layers (UNVERIFIED stiffness not needed here)
LIM_IN, LIM_ACROSS = 10.0, 5.0


def ring_I(pts):
    a = ix = iy = cx = cy = 0.0
    n = len(pts)
    for i in range(n):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % n]
        c = x0 * y1 - x1 * y0
        a += c
        cx += (x0 + x1) * c
        cy += (y0 + y1) * c
        ix += (y0 * y0 + y0 * y1 + y1 * y1) * c
        iy += (x0 * x0 + x0 * x1 + x1 * x1) * c
    return a / 2, cx / 6, cy / 6, ix / 12, iy / 12


def section(shape, z, clip=None):
    """area, Ix (about the x axis through the centroid), Iy, ymax distance, xmax distance of the horizontal cross section at height z"""
    tri = mesh(shape)
    g = None
    for dz in (0.0, 0.0137, 0.0271, 0.0413, -0.0137):
        g = region(tri, z + dz)
        if g is not None:
            break
    if clip is not None:
        g = g.intersection(sbox(*clip))
    A = Sx = Sy = Ixx = Iyy = 0.0
    polys = list(getattr(g, "geoms", [g]))
    rings = []
    for p in polys:
        rings.append((list(p.exterior.coords)[:-1], 1))
        for h in p.interiors:
            rings.append((list(h.coords)[:-1], -1))
    for pts, sgn in rings:
        a, cx, cy, ix, iy = ring_I(pts)
        if a < 0:
            a, cx, cy, ix, iy = -a, -cx, -cy, -ix, -iy
        A += sgn * a
        Sx += sgn * cx
        Sy += sgn * cy
        Ixx += sgn * ix
        Iyy += sgn * iy
    xc, yc = Sx / A, Sy / A
    Ixc, Iyc = Ixx - A * yc * yc, Iyy - A * xc * xc
    b = g.bounds
    return dict(A=A, Ix=Ixc, Iy=Iyc, ymax=max(b[3] - yc, yc - b[1]), xmax=max(b[2] - xc, xc - b[0]))


def tube_Z(od, idd):
    return math.pi * (od ** 4 - idd ** 4) / (32 * od)


def strength(FR, UR, th0):
    """COMBINED case on one wheel: 15 N sideways + 10 N fore and aft at the ground (55 below the axle) + the whole 3 g car (29.4 N) on that wheel.
    Model: ground loads act below both pivot rows, so the lower row reaction is NU + F; sections are cut from the real solids; the M3 steel screw carries the bush bending (screw bending under 200 MPa, PLA bearing under 10 MPa in plane)."""
    ZC = -WHEEL_D / 2
    FV = 3 * 9.81
    FS, FA = 15.0, 10.0
    NU = FS * (ZL - ZC) / SP
    NL = NU + FS
    YU = FA * (ZL - ZC) / SP
    YL = YU + FA
    e_stop = JCX - X_W
    Mlink = FV * FORK * math.cos(math.radians(THETA))
    Fsp = spring_force(THETA)
    Fstop = Mlink / e_stop
    Vi = Fstop + FV
    out = []
    add = lambda n, s, lim, note="": out.append((n, round(s, 2), lim, note))
    arm_yaw = YL * FORK / (Y_LUG0 + Y_LUG1)
    arm_x = NL / 2 + arm_yaw
    lug = math.hypot(arm_x, Vi / 2)
    L_t = Y_OC0 - Y_IC1
    d_s = 2.5e0
    add("M3 screw bending in the bush gap, lug load %.0f N (steel)" % lug, lug * L_t / 4 / (math.pi * d_s ** 3 / 32), 200.0, "screw carries the bending, tube is clamped on it")
    add("PLA bearing, bush tube on lug", lug / (BUSH_OD * (Y_LUG1 - Y_LUG0)), LIM_IN, "in plane")
    add("PLA bearing, bush tube in cheek", lug / (BUSH_OD * (Y_OC1 - Y_OC0)), LIM_IN, "in plane")
    Za = (Y_LUG1 - Y_LUG0) * LH ** 2 / 6
    add("link arm bending + axial, combined", (Mlink / 2) / Za + (NL / 2 + arm_yaw) / ((Y_LUG1 - Y_LUG0) * LH), LIM_IN, "in plane along x, per arm")
    Zt = TAIL_W * TAIL_H ** 2 / 6
    Mtail = Fstop * (X_CB0 - X_W)
    add("tail web bending at the cross bar, whole 3 g car on the stop (%.0f N)" % Fstop, Mtail / Zt, LIM_IN, "spring %.0f N" % Fsp)
    padb = (WIN_X1 - 1.2 - WIN_X0) * TAIL_W
    padd = (WIN_X1 - WIN_X0) * TAIL_W
    add("stop face compression, bump (%.0f mm2)" % padb, Fstop / padb, LIM_IN)
    add("stop face compression, droop (%.0f mm2)" % padd, Fstop / padd, LIM_IN)
    span = 2 * WIN_HW
    add("window roof bending (%.1f thick over %.1f)" % (ROOF_T, span), (Fstop * span / 8) / ((WIN_X1 - WIN_X0) * ROOF_T ** 2 / 6), LIM_IN, "bridge stress runs along the layers (y)")
    def Mz(z, amp, ZLrow):
        return amp * (z - ZC) if z <= ZLrow else amp * (ZLrow - ZC) / SP * (ZU - z)
    worst = {}
    for nm, shape, zs, clipb in (("upright", UR, [UP_T1 + 2 + 4 * k for k in range(int((ZU - UP_T1) / 4))], (60.0, 110.0, 10.0, 35.0)), ("frame post", FR, [BOSS_TOP + 1 + 3 * k for k in range(int((ZU - BOSS_TOP) / 3))], (40.0, 70.0, 10.0, 35.0))):
        best = (0.0, 0.0)
        for z in zs:
            if z > ZU - 1:
                continue
            sb = section(shape, z, None if nm == "upright" else clipb)
            sl = section(shape, z, clipb)
            share = 1.0 if nm == "upright" else 0.5
            My = Mz(z, FS, ZL) + (FV * 24.0 if z <= ZL and nm == "upright" else (Vi * 8.0 if nm != "upright" and z <= ZL else 0.0))
            Mx = Mz(z, FA, ZL)
            if nm == "upright":
                sy = My / (sb["Iy"] / sb["xmax"])
                sx = (Mx / 2) / (sl["Ix"] / sl["ymax"])
                ax = FV / sb["A"]
            else:
                sy = (My * share) / (sl["Iy"] / sl["xmax"])
                sx = (Mx * share) / (sl["Ix"] / sl["ymax"])
                ax = 0.0
            tot = sy + sx + ax
            if tot > best[0]:
                best = (tot, z)
        add("%s worst section, combined (z %.0f)" % (nm, best[1]), best[0], LIM_ACROSS, "bending about both axes plus axial, vertical members on the bed: across layers")
    M_pad = FS * (UP_T1 + 55) + FV * 26.0
    Fscrew = M_pad * 21.8 / (2 * 11.0 ** 2 + 21.8 ** 2)
    add("pad screw plate bearing under washer, outboard screw (%.0f N)" % Fscrew, Fscrew / (math.pi / 4 * (WASHER_D ** 2 - WASHER_ID ** 2)), LIM_ACROSS, "plate flat on bed: across layers")
    add("pad screw steel tension, outboard screw", Fscrew / (math.pi / 4 * 2.5 ** 2), 200.0)
    add("spring seat ring compression at full bump (%.0f N)" % Fsp, Fsp / (math.pi / 4 * (PED_D ** 2 - POCKET_D ** 2)), LIM_IN)
    loads = dict(FV=round(FV, 2), NU=round(NU, 1), NL=round(NL, 1), YU=round(YU, 1), YL=round(YL, 1), Mlink=round(Mlink, 0), Fsp=round(Fsp, 1), Fstop=round(Fstop, 1), Vi=round(Vi, 1), lug=round(lug, 1))
    return out, loads


# ---- fasteners at their seated positions, right side of one axle (the left side is the mirror in x)
def xf(f, fn):
    return dict(f, bolt=fn(f["bolt"]), core=fn(f["core"]), driver=fn(f["driver"]), washers=[fn(w) for w in f["washers"]], nut=fn(f["nut"]) if f["nut"] else None)


def pivot_screws(dx=0.0, dz=0.0, upright=False):
    out = []
    x = (KPX if upright else JCX) + dx
    for z in (ZL, ZU):
        for sg in (1, -1):
            f = fastener("pivotU" if upright else "pivotF", V(x, sg * Y_FL1, z + dz), V(0, -sg, 0), 16.0, nut=(V(x, sg * (Y_IC0 + LIP_T), z + dz), V(0, sg, 0)))
            out.append(f)
    return out


def hub_screws(dx=0.0, dz=0.0):
    out = []
    for hx, hy in HOLES:
        x = KPX - hx + dx
        out.append(fastener("hub", V(x, hy, UP_T1 + WASHER_T + dz), -Z, 12.0, washers=[(V(x, hy, UP_T1 + dz), Z), (V(x, hy, UP_T0 - PAD_T - WASHER_T + dz), Z)], nut=(V(x, hy, UP_T0 - PAD_T - WASHER_T - NUT_T + dz), Z)))
    return out


def ear_screws():
    out = []
    for sg in (1, -1):
        out.append(fastener("ear", V(EAR_X, sg * EAR_Y, 25.0 - WASHER_T), Z, 12.0, washers=[(V(EAR_X, sg * EAR_Y, 25.0 - WASHER_T), Z)]))
    return out


def clamp_screws():
    return [fastener("clamp", V(ROD_X, sg * ROD_Y, ROD_Z - Z_TOP - CLAMP_H0), Z, CLAMP_L, nut=(V(ROD_X, sg * ROD_Y, ROD_Z - SLOT_Z1), Z)) for sg in (1, -1)]


def cradle_clamps():
    out = []
    for y in CR_ROWS:
        for sgx in (1, -1):
            out.append(fastener("cclamp", V(sgx * ROD_X, y, ROD_Z + Z_TOP + CLAMP_H0), -Z, CLAMP_L, nut=(V(sgx * ROD_X, y, ROD_Z + SLOT_Z1), -Z)))
    return out


def cradle_fasteners():
    out = []
    for x, y in GB_EARS:
        tie = (x, y) == (38.0, 12.0)
        out.append(fastener("gear", V(x, y, 41.0 if tie else 37.0), -Z, 16.0 if tie else 12.0, nut=(V(x, y, Z0 + NUT_SLOT_T), -Z), rot=90.0))
    return out


def allsh(F):
    return [s for f in F for s in [f["bolt"]] + f["washers"] + ([f["nut"]] if f["nut"] else [])]


def dowels(dx=0.0, dz=0.0):
    return [moved(Part.makeCylinder(DOWEL_D / 2, DOWEL_L, V(KPX - DOWEL_AT[0] + dx, DOWEL_AT[1], UP_T0 - DOWEL_L + dz), Z).fuse(Part.makeCylinder(DOWEL_FL_D / 2, DOWEL_FL_T, V(KPX - DOWEL_AT[0] + dx, DOWEL_AT[1], UP_T0 + dz), Z)), 0, 0, 0)]


def axle_fasteners(th):
    dx, dz = FORK * (math.cos(math.radians(th)) - 1), FORK * math.sin(math.radians(th))
    return pivot_screws() + pivot_screws(dx, dz, True) + hub_screws(dx, dz) + ear_screws() + clamp_screws()


def seat_report(R, K, B, FR, th=0.0, st=0.0):
    """interference, 0.8 clearance, thread and driver sweep of every right side screw at pose th (steering straight)"""
    S = right_set(R, K, B, th, st, 0.0)
    Fx = fixed_set(R, B, FR)
    Fs = axle_fasteners(th)
    world = dict(Fx, **S)
    hosts = dict(pivotF=("Frame", "BushF"), pivotU=("Upright", "BushU", "Hub_Ref"), hub=("Upright", "Hub_HubCarrier", "Dowel"), ear=("Frame", "CaseTop"), clamp=("Frame", "Rod"))
    rep = []
    for f in Fs:
        k = f["kind"]
        sh = [f["bolt"]] + f["washers"] + ([f["nut"]] if f["nut"] else [])
        r = dict(kind=k, L=f["L"])
        r["interference"] = round(sum(vol(q, o) for q in sh for n, o in world.items() if not n.startswith("Kit_Plug") and not any(n.startswith(h) for h in hosts[k]) for _ in [0]), 4)
        r["host_overlap"] = round(sum(vol(f["core"], o) for n, o in world.items() if any(n.startswith(h) for h in hosts[k]) and not n.startswith("Hub_Ref")), 4)
        r["driver_hit"] = round(sum(vol(f["driver"], o) for n, o in world.items() if not n.startswith("Spring")), 4)
        if k == "hub":
            bench = ("Upright", "Hub_HubCarrier", "Hub_Knuckle", "Kit_StubYoke", "Hub_PivotBush", "Hub_Sleeve", "Hub_Ref_Pivot")
            r["driver_step"] = round(sum(vol(f["driver"], o) for n, o in world.items() if any(n.startswith(b) for b in bench)), 4)
        g = min([gap(q, o, 0.8) for q in sh for n, o in world.items() if not any(n.startswith(h) for h in hosts[k])] + [99.0])
        r["min_gap"] = round(g, 3)
        if f["nut"]:
            sa = (f["nut_p"] - f["p"]).dot(f["d"])
            sb = sa + NUT_T * f["nut_d"].dot(f["d"])
            near, far = min(sa, sb), max(sa, sb)
            r["thread_in_nut"] = round(max(0.0, min(f["L"], far) - near), 2)
            r["tip_beyond_nut"] = round(f["L"] - far, 2)
        else:
            r["thread_in_plastic"] = round(24.5 + f["L"] - FL_Z0, 2) if k == "ear" else 0.0
        rep.append(r)
    return rep


# ---- verification
THS = (-THETA, -THETA / 2, 0.0, THETA / 2, THETA)
STS = (0.0, STEER_DEG, -STEER_DEG)


def rod_cyls(y0=-420.0, y1=420.0):
    return [cyly(ROD_D / 2, y0, y1, sg * ROD_X, ROD_Z) for sg in (1, -1)]


def kit_pose_report(R, K, B, FR, th, st, chi):
    return pose_report(R, K, B, FR, th, st, chi, only_kit=True)


def kin_report(B, FR):
    out = {"rows": {}}
    for th in THS:
        ox, oz = rot_pt(KPX, ZL, th)
        c2 = c2_car(th)
        err = math.hypot(ox - c2.x, oz - (ZL + c2.z))
        dist = math.hypot(c2.x - JCX, c2.z)
        ang_in = abs(th)
        out["rows"][round(th, 2)] = dict(parallelogram_error=round(err, 9), joint_distance=round(dist, 6), inner_angle=round(ang_in, 2), wheel_z=round(c2.z, 3), wheel_x_shift=round(c2.x - KPX, 3))
    v = lambda t: vol(rot_link(B["Link"], t), FR)
    out["stop_bump"] = (round(v(THETA), 6), round(v(THETA + 0.6), 4))
    out["stop_droop"] = (round(v(-THETA), 6), round(v(-THETA - 0.6), 4))
    out["pivot_play_radial"] = (LUG_BORE - BUSH_OD) / 2
    jmax = 0.0
    for th in THS:
        for st in STS:
            u = V(math.cos(math.radians(th)), 0, math.sin(math.radians(th)))
            a = App.Rotation(Z, -st).multVec(X)
            jmax = max(jmax, math.degrees(math.acos(max(-1, min(1, u.dot(a))))))
    out["outer_joint_max"] = round(jmax, 2)
    return out


def spring_report():
    global SPRING_RATE
    k0 = SPRING_RATE
    th0 = ride_theta()
    out = dict(ride_deg=round(th0, 3), ride_wheel_mm=round(FORK * math.sin(math.radians(th0)), 3), ride_len=round(spring_len(th0), 2), ride_force=round(spring_force(th0), 2), preload_level_force=round(spring_force(0.0), 2),
               len_bump=round(spring_len(THETA), 2), len_droop=round(spring_len(-THETA), 2), force_bump=round(spring_force(THETA), 2), force_droop=round(spring_force(-THETA), 2), solid=SPRING_SOLID, k=k0, shims=NSHIM)
    for f in (0.5, 2.0):
        SPRING_RATE = k0 * f
        out["ride_mm_k_x%.1f" % f] = round(FORK * math.sin(math.radians(ride_theta())), 2)
    SPRING_RATE = k0
    out["droop_contact_lost_mm"] = round(max(0.0, spring_len(-THETA) - SPRING_FREE), 2)
    for ns in (0, 1, 3, 4):
        pass
    return out


def slide_steps(R, K, B, FR):
    D = R["Differential"]
    case = [D["CaseTop"], D["CaseBottom"]]
    out = {}

    def slide(movers, fixed, v, length, step=4.0):
        worst = 0.0
        for i in range(int(length / step) + 1):
            d = length - i * step
            for m in movers:
                mm = moved(m, -v.x * d, -v.y * d, -v.z * d)
                worst = max(worst, max(vol(mm, o) for o in fixed))
        return round(worst, 4)

    plug = moved(D["PlugShaft_R"], 0, 0, -45.0)
    plugL = moved(D["PlugShaft_L"], 0, 0, -45.0)
    out["1_plug_shafts_in_from_outboard"] = slide([plug], case, -X, 60.0, 3.0) + slide([plugL], case, X, 60.0, 3.0)
    out["2_frame_down_onto_case"] = slide([FR], case + [plug, plugL], -Z, 70.0)
    rods = rod_cyls(-90, 90)
    out["3_rods_through_frame"] = slide(rods, [FR], Y, 200.0, 10.0)
    sp = spring_tube(THETA_A)
    sp = Part.makeCylinder(SPRING_OD / 2, SPRING_FREE, V(X_S, 0, SPR_BOT), Z).cut(Part.makeCylinder(SPRING_ID / 2, SPRING_FREE + 2, V(X_S, 0, SPR_BOT - 1), Z))
    out["4_spring_down_onto_pin"] = slide([sp], [FR], -Z, 40.0, 2.0)
    la = rot_link(B["Link"], THETA_A)
    lu = rot_link(moved(B["Link"], 0, 0, SP), THETA_A, ZU)
    out["5_links_in_from_outboard"] = slide([la, lu], [FR, sp] + rods + case, -X, 70.0, 3.0)
    S = right_set(R, K, B, THETA_A, 0.0, 0.0)
    names = [n for n in S if n == "Upright" or (n.startswith("Hub_") and n not in ("Hub_Wheel", "Hub_Tyre", "Hub_Ref_HubScrew")) or (n.startswith("Kit_") and n not in ("Kit_PlugShaft", "Kit_PinA", "Kit_PinB"))]
    unit = [S[n] for n in names]
    fixed = [FR, la, lu, sp, plug] + case + rods
    out["6_upright_unit_in_from_outboard"] = slide(unit, fixed, -X, 40.0, 3.0)
    wheel = [S["Hub_Wheel"], S["Hub_Tyre"]]
    others = unit + fixed
    out["7_wheel_onto_stub_from_outboard"] = slide(wheel, others, -X, 60.0, 3.0)
    return out


def layout_checks(R, lay, CR):
    rods = rod_cyls()
    iv = [(lay["yr"] + sg * ROD_Y - BOSS_L / 2, lay["yr"] + sg * ROD_Y + BOSS_L / 2) for sg in (1, -1)] + [(lay["yf"] + sg * ROD_Y - BOSS_L / 2, lay["yf"] + sg * ROD_Y + BOSS_L / 2) for sg in (1, -1)] + [(y - BOSS_L / 2, y + BOSS_L / 2) for y in CR_ROWS]
    iv.sort()
    out = {"boss_gaps": [round(iv[i + 1][0] - iv[i][1], 2) for i in range(len(iv) - 1)], "rod_span": round(iv[-1][1] - iv[0][0], 2)}
    out["spare_each_end"] = round((ROD_L - out["rod_span"]) / 2, 2)
    out["rod_y0"], out["rod_y1"] = round(iv[0][0] - out["spare_each_end"], 2), round(iv[-1][1] + out["spare_each_end"], 2)
    out["wheelbase"] = round(lay["yf"] - lay["yr"], 2)
    return out


def tie_rod_report(R, FR, B):
    """straight tie rod (dia 3) between the same arm hole of the two front knuckles at ride, steering straight: where it runs and what it meets"""
    H = R["DriveHub"]
    holes = []
    for f in H["Knuckle"].Faces:
        s = f.Surface
        if isinstance(s, Part.Cylinder) and abs(abs(s.Axis.z) - 1) < 1e-6 and abs(s.Radius - 1.8) < 0.05 and s.Center.y < -15:
            holes.append((round(s.Center.x, 2), round(s.Center.y, 2), round((f.BoundBox.ZMin + f.BoundBox.ZMax) / 2, 2)))
    out = dict(holes=sorted(set(holes), key=lambda h: h[1]), hits={})
    D = diff_parts(R, True)
    others = dict(CaseTop=D["CaseTop"], CaseBottom=D["CaseBottom"], Frame=FR, PlugR=D["PlugShaft_R"], PlugL=D["PlugShaft_L"])
    for h in out["holes"]:
        xr = KPX - h[0]
        rod = Part.makeCylinder(1.5, 2 * xr, V(-xr, h[1], h[2]), X)
        out["hits"][h[1]] = {n: round(vol(rod, s), 1) for n, s in others.items() if vol(rod, s) > 1e-3}
    xr = KPX - out["holes"][0][0]
    y0 = out["holes"][0][1]
    p0, p1 = V(xr, y0, out["holes"][0][2]), V(0, y0, 60.0)
    rise = Part.makeCylinder(1.5, (p1 - p0).Length, p0, p1 - p0)
    out["raised_to_z60"] = {n: round(vol(rise, s), 1) for n, s in others.items()}
    out["raised_gap"] = {n: round(gap(rise, s, 3.0), 2) for n, s in others.items()}
    return out


def drag_link_report(R, K, B, FR, Pb=None, quick=False):
    """raised drag link: front right knuckle arm hole to a bellcrank point above the front differential, through travel and steering"""
    H = R["DriveHub"]
    hole = None
    for f in H["Knuckle"].Faces:
        s = f.Surface
        if isinstance(s, Part.Cylinder) and abs(abs(s.Axis.z) - 1) < 1e-6 and abs(s.Radius - 1.8) < 0.05 and abs(s.Center.y + 34.0) < 0.01:
            hole = V(s.Center.x, s.Center.y, (f.BoundBox.ZMin + f.BoundBox.ZMax) / 2)
    D = diff_parts(R, True)
    fixed = dict(Frame=FR, CaseTop=D["CaseTop"], CaseBottom=D["CaseBottom"])
    def arm(th, st):
        p = App.Rotation(Z, st).multVec(hole)
        c2 = c2_car(th)
        return V(-p.x + c2.x, p.y, p.z + c2.z)
    out = dict(hole_hub=(round(hole.x, 2), round(hole.y, 2), round(hole.z, 2)), min_gap=99.0, worst=None, length={})
    Pb = Pb or V(30.0, -34.0, 62.0)
    for th in ((-THETA, THETA) if quick else THS):
        for st in STS:
            a = arm(th, st)
            L = (a - Pb).Length
            out["length"][(round(th, 1), st)] = round(L, 2)
            S = right_set(R, K, B, th, st, 0.0, kit=False)
            rod = Part.makeCylinder(1.5, L, a, Pb - a)
            for n, s in list(fixed.items()) + [(n, s) for n, s in S.items() if n != "Spring"]:
                if n.startswith("Hub_Ref") or n == "Hub_Knuckle":
                    continue
                g = vol(rod, s)
                g = -1.0 if g > 1e-4 else (99.0 if quick else gap(rod, s, 3.0))
                if g < out["min_gap"]:
                    out["min_gap"], out["worst"] = round(g, 2), (n, th, st)
    if quick:
        return out
    L0 = out["length"][(0.0, 0.0)]
    out["bump_steer_mm"] = (round(out["length"][(round(-THETA, 1), 0.0)] - L0, 2), round(out["length"][(round(THETA, 1), 0.0)] - L0, 2))
    out["steer_range_mm"] = (round(out["length"][(0.0, STEER_DEG)] - L0, 2), round(out["length"][(0.0, -STEER_DEG)] - L0, 2))
    out["bellcrank_point"] = (Pb.x, Pb.y, Pb.z)
    return out


# ---- whole car display, report, checks
def part_report(B, CR):
    parts = {"AxleFrame": B["Frame"], "Link": B["Link"], "Upright_R": B["Upright"], "Upright_L": mirror_x(B["Upright"]), "PivotBush": B["PivotBush"], "Dowel": B["Dowel"], "Shim": B["Shim"], "GearboxCradle": CR}
    return parts


COPIES_CAR = dict(AxleFrame=2, Link=8, Upright_R=2, Upright_L=2, PivotBush=32, Dowel=4, Shim=4 * NSHIM, GearboxCradle=1)


def verify(R, K, B, CR):
    rep = {}
    FR = B["Frame"]
    lay = layout_y(R)
    rep["lay"] = lay
    rep["kin"] = kin_report(B, FR)
    rep["spring"] = spring_report()
    th0 = ride_theta()
    print("kin/spring", rep["kin"], rep["spring"], flush=True)
    rep["strength"], rep["loads"] = strength(FR, B["Upright"], th0)
    print("strength", rep["loads"], flush=True)
    for r in rep["strength"]:
        print("  ", r, flush=True)
    parts = part_report(B, CR)
    rep["bbox"] = {n: tuple(round(v, 1) for v in (s.BoundBox.XLength, s.BoundBox.YLength, s.BoundBox.ZLength)) for n, s in parts.items()}
    rep["volumes"] = {n: round(s.Volume / 1000, 2) for n, s in parts.items()}
    rep["print"], rep["walls"] = {}, {}
    for n, s in parts.items():
        rep["print"][n] = printable(n, s)
        rep["walls"][n] = thin_walls(n, s)
    print("print", {n: (len(v["slopes"]), v["nlayers"], v["bed"], v["tall"], v["thin"]) for n, v in rep["print"].items()}, rep["walls"], flush=True)
    bad = []
    ths = (-THETA, 0.0, THETA) if FAST else THS
    sts = (0.0, STEER_DEG) if FAST else STS
    for th in ths:
        for st in sts:
            nb = [(th, st, 0.0) + b for b in pose_report(R, K, B, FR, th, st, 0.0)]
            bad += nb
            print("pose", th, st, len(bad), nb, flush=True)
    chis = (45.0, 90.0) if FAST else tuple(15.0 * i for i in range(1, 24))
    for th in (-THETA, 0.0, THETA):
        for st in sts:
            for chi in chis:
                bad += [(th, st, chi) + b for b in kit_pose_report(R, K, B, FR, th, st, chi)]
        print("kit phases", th, len(bad), flush=True)
    rep["sweep_bad"] = bad
    rep["seats"] = seat_report(R, K, B, FR, 0.0)
    print("seats", rep["seats"], flush=True)
    if not FAST:
        for nm, th, st in (("bump", THETA, 0.0), ("droop", -THETA, 0.0), ("steer_p", 0.0, STEER_DEG), ("steer_m", 0.0, -STEER_DEG), ("bump_steer", THETA, STEER_DEG), ("droop_steer", -THETA, -STEER_DEG)):
            rep["seats_" + nm] = seat_report(R, K, B, FR, th, st)
            print("seats", nm, min(r["min_gap"] for r in rep["seats_" + nm]), flush=True)
    rg = 99.0
    for th, st in ((THETA, 0.0), (-THETA, 0.0), (THETA, STEER_DEG), (-THETA, -STEER_DEG), (0.0, STEER_DEG)):
        Sx = right_set(R, K, B, th, st, 0.0)
        for n, s in Sx.items():
            if n == "Spring":
                continue
            for rd in rod_cyls(-90, 90):
                rg = min(rg, gap(s, rd, 6.0))
    rep["rod_min_gap"] = round(rg, 2)
    print("rod min gap", rep["rod_min_gap"], flush=True)
    rep["slides"] = slide_steps(R, K, B, FR)
    print("slides", rep["slides"], flush=True)
    rep["layout"] = layout_checks(R, lay, CR)
    gb = R["Gearbox3"]
    G_ = {n: s for n, s in gb.items() if n not in ("Ref_Floor", "Ref_Bolts", "Ref_Heads", "Ref_Grubs")}
    rep["cradle_in_gearbox"] = round(sum(vol(CR, s) for s in G_.values()), 4)
    bosses = []
    for y in CR_ROWS:
        bosses += boss_flip_at(y)[0]
    rep["rod_to_gearbox"] = round(min(gap(b, s, 5.0) for b in rod_cyls(-140, 90) + bosses for s in G_.values()), 3)
    t = gb["ThroughShaft"]
    rep["ports"] = dict(gearbox_rear=port_axis(t, t.BoundBox.YMin + 5), gearbox_front=port_axis(t, t.BoundBox.YMax - 5), diff=port_axis(R["Differential"]["PinionShaftA"], R["Differential"]["PinionShaftA"].BoundBox.YMax - 5))
    rep["drag"] = drag_link_report(R, K, B, FR)
    print("drag", rep["drag"], flush=True)
    sg = 99.0
    for th, st in ((THETA, 0.0), (-THETA, 0.0), (0.0, 0.0), (THETA, STEER_DEG), (-THETA, -STEER_DEG)):
        Sx = right_set(R, K, B, th, st, 0.0)
        sg = min(sg, gap(spring_tube(th, 0.6), Sx["Link_L"], 3.0))
    rep["spring_link_gap"] = round(sg, 3)
    rep["tie_rod"] = tie_rod_report(R, FR, B)
    print("tie rod", rep["tie_rod"], flush=True)
    return rep


DEPARTURES = []


def check(rep):
    k = rep["kin"]
    for r in k["rows"].values():
        assert r["parallelogram_error"] < 1e-6 and abs(r["joint_distance"] - FORK) < 1e-5, r
    assert k["stop_bump"][0] < 1e-4 and k["stop_bump"][1] > 1e-4 and k["stop_droop"][0] < 1e-4 and k["stop_droop"][1] > 1e-4, k
    assert k["outer_joint_max"] <= 33.0, k
    sp = rep["spring"]
    assert sp["len_bump"] > SPRING_SOLID + 5.0 and abs(sp["ride_wheel_mm"]) <= 3.0, sp
    for n, s_, lim, note in rep["strength"]:
        assert s_ <= lim, (n, s_, lim)
    for n, v in rep["print"].items():
        assert not v["slopes"] and not v["layers"] and v["nlayers"] == 0, (n, v)
        assert v["bed"] >= BED_MIN and v["tall"] <= TALL_MAX and v["thin"] <= LOST_MAX, (n, v)
    for n, w in rep["walls"].items():
        assert w[1] == 0, (n, w)
    for n, b in rep["bbox"].items():
        assert b[0] <= 236 and b[1] <= 236, (n, b)
    assert not rep["sweep_bad"], rep["sweep_bad"][:20]
    assert rep["rod_min_gap"] >= 2.0, rep["rod_min_gap"]
    assert FL_Z1 + PED_H - (PK_Z + NSHIM_MAX * SHIM_T) >= 2.0 and PK_Z + PIN_H - SPR_BOT >= 20.0, (PED_H, PIN_H)
    assert rep["spring_link_gap"] >= 0.5, rep["spring_link_gap"]
    for key in [k_ for k_ in rep if k_.startswith("seats")]:
        for r in rep.get(key, []):
            assert (r["driver_hit"] < 1e-4 or key != "seats" or r["kind"] == "hub") and r.get("driver_step", 0.0) < 1e-4 and r["interference"] < 1e-4 and r["host_overlap"] < (2.2 if r["kind"] == "clamp" else 1e-4) and r["min_gap"] >= 0.8 and r["L"] in KIT_L, (key, r)
            if "thread_in_nut" in r:
                assert r["thread_in_nut"] >= NUT_T - 1e-6 and r["tip_beyond_nut"] >= -0.01, r
            if "thread_in_plastic" in r and r["kind"] == "ear":
                assert r["thread_in_plastic"] >= 4.0, r
    for n, v in rep["slides"].items():
        assert v < 1e-3, (n, v)
    lc = rep["layout"]
    assert lc["spare_each_end"] >= 10.0 and min(lc["boss_gaps"]) >= 2.0, lc
    assert rep["cradle_in_gearbox"] < 1e-3 and rep["rod_to_gearbox"] >= 2.0, rep["cradle_in_gearbox"]
    pz = rep["ports"]
    assert all(abs(v[0]) < 0.05 for v in pz.values()) and abs(pz["gearbox_rear"][1] - pz["diff"][1]) < 0.05 and abs(pz["gearbox_front"][1] - pz["diff"][1]) < 0.05, pz


def car_numbers(R, K, B, lay, th0):
    S = right_set(R, K, B, th0, 0.0, 0.0)
    D = R["Differential"]
    tyre, wheel = S["Hub_Tyre"].BoundBox, S["Hub_Wheel"].BoundBox
    low = min([s.BoundBox.ZMin for n, s in S.items() if n not in ("Hub_Wheel", "Hub_Tyre")] + [D["CaseBottom"].BoundBox.ZMin])
    out = dict(track_level=round(2 * (KPX + WHEEL_OFF), 2), track_ride=round(2 * (c2_car(th0).x + WHEEL_OFF), 2), over_tyres=round(2 * tyre.XMax, 1), over_hub_plates=round(2 * wheel.XMax, 1),
               wheelbase=round(lay["yf"] - lay["yr"], 2), ground_clearance_ride=round(low - tyre.ZMin, 1))
    for nm, th in (("droop", -THETA), ("bump", THETA)):
        Sx = right_set(R, K, B, th, 0.0, 0.0)
        lo = min([s.BoundBox.ZMin for n, s in Sx.items() if n not in ("Hub_Wheel", "Hub_Tyre")] + [D["CaseBottom"].BoundBox.ZMin])
        out["ground_clearance_" + nm] = round(lo - Sx["Hub_Tyre"].BoundBox.ZMin, 1)
    out["height_top"] = round(B["Frame"].BoundBox.ZMax - tyre.ZMin, 1)
    out["volumes_cm3"] = {n: round(v, 2) for n, v in {k: B_.Volume / 1000 for k, B_ in (("AxleFrame", B["Frame"]), ("Link", B["Link"]), ("Upright", B["Upright"]), ("PivotBush", B["PivotBush"]), ("Dowel", B["Dowel"]), ("Shim", B["Shim"]))}.items()}
    return out


def build_display(R, K, B, CR, lay, th0):
    objs = {}
    yr, yf = lay["yr"], lay["yf"]
    gb = R["Gearbox3"]
    FR, LK, UR, BU = B["Frame"], B["Link"], B["Upright"], B["PivotBush"]
    objs["AxleFrame_1"] = moved(FR, 0, yr)
    objs["Shown_AxleFrame_2"] = moved(FR, 0, yf)
    objs["GearboxCradle"] = CR
    objs["Link_1"] = moved(LK, 0, yr)
    objs["Upright_R"] = moved(UR, 0, yr)
    objs["Upright_L"] = moved(mirror_x(UR), 0, yr)
    objs["PivotBush_1"] = moved(BU, JCX, yr, ZL)
    objs["Dowel_1"] = moved(B["Dowel"], KPX - DOWEL_AT[0], yr + DOWEL_AT[1], UP_T0 - DOWEL_L)
    objs["Shim_1"] = moved(B["Shim"], X_S, yr, PK_Z)
    objs["Ref_Gearbox"] = comp(s for n, s in gb.items() if n not in ("Ref_Floor", "Ref_Bolts", "Ref_Heads", "Ref_Grubs"))
    G = {k: [] for k in ("Hubs", "Wheels", "Kit", "Springs", "Links", "Uprights", "Bushes", "Dowels", "Shims", "Screws", "Washers", "Nuts")}
    for tag, y, front in (("R", yr, False), ("F", yf, True)):
        S = right_set(R, K, B, th0, 0.0, 0.0)
        F = fixed_set(R, B, FR, rods=False)
        objs["Ref_Diff_" + tag] = moved(comp(diff_parts(R, front).values()), 0, y)
        for side in ("R", "L"):
            sh = lambda s: moved(s if side == "R" else mirror_x(s), 0, y)
            for n, s in list(S.items()) + list(F.items()):
                if n.startswith("Hub_Wheel") or n.startswith("Hub_Tyre"):
                    G["Wheels"].append(sh(s))
                elif n.startswith("Hub_"):
                    G["Hubs"].append(sh(s))
                elif n.startswith("Kit_"):
                    G["Kit"].append(sh(s))
                elif n == "Spring":
                    G["Springs"].append(sh(s))
                elif n.startswith("Link"):
                    if not (tag == "R" and side == "R" and n == "Link_L"):
                        G["Links"].append(sh(s))
                elif n == "Upright":
                    if tag != "R":
                        G["Uprights"].append(sh(s))
                elif n.startswith("Bush"):
                    if not (tag == "R" and side == "R" and n == "BushF01"):
                        G["Bushes"].append(sh(s))
            if not (tag == "R" and side == "R"):
                G["Dowels"].append(sh(dowels_shape(0.0, 0.0)[0]))
            for k in range(NSHIM):
                if not (tag == "R" and side == "R" and k == 0):
                    G["Shims"].append(sh(moved(B["Shim"], X_S, 0, PK_Z + k * SHIM_T)))
            for f in axle_fasteners(th0):
                G["Screws"].append(sh(f["bolt"]))
                G["Washers"] += [sh(w) for w in f["washers"]]
                if f["nut"]:
                    G["Nuts"].append(sh(f["nut"]))
    for k, v in G.items():
        if v:
            objs["Ref_%s_All" % k] = comp(v)
    objs["Ref_Shaft_R"] = comp(short_shaft(R, lay["m_r"], -1))
    objs["Ref_Shaft_F"] = comp(short_shaft(R, lay["m_f"], 1))
    lc = layout_checks(R, lay, CR)
    objs["Ref_Rod_1"], objs["Ref_Rod_2"] = [cyly(ROD_D / 2, lc["rod_y0"], lc["rod_y1"], sg * ROD_X, ROD_Z) for sg in (1, -1)]
    objs["Ref_CradleScrews"] = comp(allsh(cradle_fasteners()) + allsh(cradle_clamps()))
    return objs


def dowels_shape(dx, dz):
    return [Part.makeCylinder(DOWEL_D / 2, DOWEL_L, V(KPX - DOWEL_AT[0] + dx, DOWEL_AT[1], UP_T0 - DOWEL_L + dz), Z).fuse(Part.makeCylinder(DOWEL_FL_D / 2, DOWEL_FL_T, V(KPX - DOWEL_AT[0] + dx, DOWEL_AT[1], UP_T0 + dz), Z))]


def main():
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    R = load_refs()
    K = Kit(R)
    th0 = ride_theta()
    B = dict(Frame=build_frame(), Link=build_link(), Upright=build_upright(), PivotBush=build_bush(), Dowel=build_dowel(), Shim=build_shim())
    CR = build_cradle()
    for n, s_ in list(B.items()) + [("Cradle", CR)]:
        assert s_.isValid() and len(s_.Solids) == 1, n
    lay = layout_y(R)
    rep = verify(R, K, B, CR)
    rep["numbers"] = car_numbers(R, K, B, lay, th0)
    print("numbers", rep["numbers"], flush=True)
    print("REPORT", rep, flush=True)
    check(rep)
    objs = build_display(R, K, B, CR, lay, th0)
    doc = App.newDocument(DOC_NAME)
    for n, s_ in objs.items():
        o = doc.addObject("Part::Feature", n)
        o.Shape = s_
    doc.recompute()
    doc.saveAs(OUT)
    print("saved", OUT, sorted(objs), flush=True)


if "NO_RUN" not in globals():
    main()
