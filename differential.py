# Axle module, no motor: closed bevel differential in a two-piece clamshell case (CaseTop glue face z 29 hangs under the floor, all shaft axes 29 mm below it). Ratio 36:22 (1.64), input pinion A at +y, output B at -y.
# Both pinions sit between the 36T carrier ring and a free-spinning 36T IdlerRing that turns opposite, so tooth side loads cancel. Every shaft leaves the case as a 16 mm plain 8.0 AF hex port with a dia 2.8 cross pilot 5.9 from the tip for universal joint yokes.
# Chaining: the output pinion turns opposite to the input, so mount the next axle in a chain turned 180 degrees about Z.
# Hardware: 4 x M3x16 pan head (dia 6 x 3.2) from below for the case (dia 3.6 pass holes), 25 mm deep wells: use a long driver. 4 x M3x12 pan head (dia 6 x 3.2) for the Cap into the Carrier pilots (dia 2.8, 9 deep). 4 x M3x16 pan head bolts with 4 nuts and 4 washers for the CaseTop ears. 4 PTFE liners 12 x 10 x 8 (later, see below).
# Liners (A2): PTFE tube 10 ID x 12 OD to be used as plain bearings, 4 liners of LINER_L 8.0 where a shaft turns in the case: Sleeve_1 (HalfShaft_L, x -38.88..-30.88), Sleeve_2 (HalfShaft_R, x 30.88..38.88), Sleeve_3 (PinionShaftA, y 32.65..40.65), Sleeve_4 (PinionShaftB, y -40.65..-32.65), all on the axis. Printed placeholders named Sleeve_1..4, exactly LINER_OD x LINER_ID x LINER_L, one print group (4 copies), standing on end; real PTFE replaces them and nothing else is reprinted. Pocket bore LINER_BORE 12.2 (tune after measuring the tube). The print plate also holds the OutputPlug and the B pinion set although they are alternatives.
# Each pocket is two half saddles (one in CaseTop, one in CaseBottom) between two lips 1.2 thick with a 10.9 bore (0.83 radial to the hex corners) and a pocket 8.3 long: the liner (8.0) has 0.3 total end play (0.15 each way), is held both ways by the two lips and only by friction against turning. Every lip face has a 0.5 x 45 degree lead-in notch on the split plane. Pocket wall 2.0 or more on the closed case (asserted on a ray scan at 3 axial stations, 2.3 on the x pockets and the y pockets). The liners are slid onto the four port tips BEFORE the bundle goes into CaseTop (step 8) and set by feel: a plain straight Z sweep passes only within 0.15 of the nominal place, with the lead-in notches the sleeve end is caught up to 0.6 off (sweep guided along the notch, asserted); a closed tube cannot be laid in from the side over a shaft, so nothing larger than the 8.0 AF hex sits outboard of a liner. The OutputPlug takes the place of PinionB, PinionShaftB and Sleeve_4 (Sleeve_4 is simply not used when the plug is).
# Shafts: every shaft is a plain 8.0 AF hex straight through its liner (0.38 radial), no round journals any more (the old dia 9.3 pinion journal and the printed bushing tails are gone). PinionShaft keeps its 11.0 AF head in the pinion hex pocket (head now 2.4 thick, flush with the pinion front, so the PinionA/B shape is untouched). The Bushings only carry the Carrier and the IdlerRing now (journal dia 14.0 in the 14.6 bores, idler hub dia 14.0 in the 14.6 bore, 0.3 radial) and do not touch the shafts (10.9 bore, 0.83 radial to the hex corners).
# Axial location (all faces modelled with the floats shown, asserted): Bushing_L and Bushing_R are held in the case by a V pad of the case (an arc of 40 degrees either side of the crown, not a full ring: a full ring gives no capture near the split plane where the lowering runs tangent to it) sitting in a V groove ring of the bushing (groove 0.35 deep, 0.6 wide at the bottom, 2.0 wide at the mouth, flanks 26 degrees off the axis; the bushing end stops 0.5 short of the wall). Modelled axial play is zero on purpose, the carrier and idler floats plus the pinion floats already use the whole 0.15 to 0.5 mesh gap window (0.016 of margin), so a flat 0.5 per side clearance cannot be used: the carrier or idler would be free to slide into collision with the pinions. Instead the wedge makes the bundle self-centering: the pad tip (1.0 wide, 0.1 above the groove bottom) is caught within 0.5 of the seat on each side and the bundle is walked into place by the flanks as it is lowered (guided sweep asserted at 0.45 plus the plain sweeps), the seat itself is the printed fit (radial slack 0.1 at the tip). Carrier plus Cap float 0.30 between the Bushing_L flange and the Bushing_R flange; IdlerRing floats 0.30 between the Bushing_R flange and the case wall; each pinion with its shaft floats 0.30 (back of the pinion to the inner lip, head flush on the cavity end wall so inward travel is 0); PinionShaft total float 0.30. Half shafts: inward 0.15 (flange to SpiderPin), outward 0.10 (flange to SideGear front) plus 0.25 (SideGear back to the Bushing journal end, Bushing_L journal reaches x -11.5 like the Bushing_R one), total 0.50 each side. Mesh gaps are checked over these floats. Side gear to spider mesh is asserted at the carrier float extremes: the side gears have no inward stop except the spiders, so at the far carrier extreme the spiders push the free side gear outward (needed push is asserted to stay inside its 0.25 outward float, gap 0 or more, no overlap).
# Assembly order (verify() sweeps each step as a straight slide in 0.5 mm steps from 60 mm clear, then the bundle every 0.5 mm from 30 mm clear and every 0.1 mm for the last 3 mm into CaseTop): 1 SideGear_L onto HalfShaft_L from the port tip end, that into the Carrier; 2 Bushing_L; 3 SpiderGear_1 and 2 onto SpiderPin, pin with spiders into the Carrier (it collides if SideGear_R is already in);
# 4 SideGear_R on HalfShaft_R into the Carrier; 5 Cap, then its 4 M3x12 screws (before the IdlerRing, which covers the heads); 6 Bushing_R, IdlerRing; 7 Pinions onto their PinionShafts from the tips and into mesh (they drop in only at the drawn mesh phase: turn the carrier and idler until each pinion drops into mesh, other phases collide); 8 Sleeve_1..4 slid over the four port tips to their pockets, then the bundle straight along Z into CaseTop (OutputPlug is laid in here if used instead of PinionB, PinionShaftB and Sleeve_4); 9 CaseBottom, 4 case screws.
# Sizes: CaseTop body 80.46 x 84.0 mm (was 62.82 x 86.8); with the bolt ears the flat glue face is 100.46 x 84.0 mm. Both case ends are the same slim tube boss (radius about 12 at the end face, the big drum only behind it). Ports (the 16 mm stick-out) reference the case end faces (x +-40.23) and y faces (+-42.0). A universal joint yoke seats fully on a 16 mm port (socket 10 deep), so its mouth sits 6 mm off the case face and never touches the case.
# Optional OutputPlug (parked 40 mm out along -y in the FCStd) replaces PinionB and PinionShaftB when the axle is not chained: a dia 11.5 barrel 8.0 long lies in the same -y pocket between the two lips (0.15 axial each way, 0.35 radial, better than the old 0.45 axial per side), its dia 10.2 necks pass the lip bores, and it closes the case.
# Four bolt ears on CaseTop (4 mm thick, flush with the glue face, fully round outer end, 1.0 chamfer on the underside rim and two 1.8 wide 2 mm 45 degree webs under each ear set 1.0 in from the chamfered rim so no flat ledge hangs over it, where it meets the case end wall (clear of the dia 6 head and driver), dia 3.6 holes for M3x16 pan head bolts from below through the cardboard to a nut and washer on top): holes at x = +-45.23, y = +-36 from the axle centre (90.46 x 72 pattern).
# Phases drawn: ring 0, iring 0, pinion 0; the bundle never moves relative to itself, so the mesh cannot block it. Inherited, not changed here: Carrier pilot wall 1.4 (asserted 1.2) and Cap clear hole dia 3.2. Lowest point 30.6 mm below the axle axis: wheels need radius over 31. Print (PLA, 0.4 nozzle, 0.2 layers, supports must stay OFF), measured on the shapes by print_report for every unique printed part in its print orientation (twins are tested once) and asserted in check(): P1 no down-facing face under 45 degrees from horizontal (faces sampled on a grid and along their edges; a horizontal round hole of dia 6 or less may stay round, a larger one would fail), CaseTop and CaseBottom ramps and domes sit at exactly 45.0 (no margin, left), HalfShaft flange flanks 48.2 (the 8.0 AF flat they lie on cannot move), OutputPlug 51.1; P2, P3, P5 every 0.2 layer is sliced (0.1 mm raster) and no pixel of a layer may lie more than 0.3 plus half a pixel (0.35) from the layer below (exact distance transform, no erosion), except a true bridge (simply connected, straight, 10 mm or less across, 80 percent of its rim on the layer below: the 3 mm glue grooves in CaseTop and the 6.6 mm roofs of the CaseBottom screw wells); P6 bed contact 60 mm2 or more, first layer wall 0.8 or more, height at most 4 x the smallest bed dimension. Changes: each CaseBottom screw well (dia 6.6) has a sacrificial 0.2 mm skin (SKIN, modelled as solid) across its dia 3.6 pass hole, so the roof is a 6.6 mm round bridge; assembly step: punch the skin with a 3.5 drill or the screw tip before fitting each M3x16. The slicer still puts about 1.7 g of auto support in these wells if supports are on, so keep supports off (with them off the roofs are legal bridges). CaseTop glue grooves sit at x -18, -8, 8, 18 (no cross grooves at y +-36) so none crosses another or runs half under a screw rib: all are straight 3 mm bridges. CaseBottom hollow cells in the y arms have their floor at print height HOLLOW_Z 9.4 so the 45 degree ramp never opens them (the old 0.1 mm skin across a 12 mm cell mouth at z 9.1 is gone). OutputPlug flat is 3.2 below the axis (neck flank 51 degrees). Exemptions by name (EXEMPT, each asserted at its measured value, nothing else is relaxed): SpiderPin P1 (lies on its 0.6 flat, flank 40.5 degrees, printed by the user and unchanged); Bushing_R P5 (1.2 wide flat ring under the flange, measured 1.22: both orientations have it because the tail sits on the other side of the flange, and a chamfer there would hit the Cap bore or the IdlerRing web, which stay as printed); PinionA and PinionB P5 (hex pocket roof 0.8 to 1.45 wide pierced by the bore, measured 1.5, printed by the user); SpiderGear_1 and 2 P5 (0.4 wide flat ledge at the hub, hub r 7.1 to 7.5, measured 0.42 at 12 tooth roots, toothed part printed by the user); CaseBottom P5 (the 45 degree ramp skin meets the round rim of each screw well and leaves 2 mm crescent bridges over the rim, measured 1.02, each anchored at both tips); Sleeve_1 to 4 P6 (bed 34.6 mm2: a placeholder tube of the exact PTFE size, 1.0 wall, 8 tall on 12 dia, brim it if it lifts). IdlerRing has a 0.28 step (r 19.62 to 19.9), under the 0.35 limit, so it needs no exemption. Everything else passes.
import FreeCAD as App, Part, math
import numpy as np
from scipy import ndimage as ndi
import freecad.gears.commands as gc

V = App.Vector
O = V(0, 0, 0)
DOC_NAME = "Differential"
OUT = "/home/mikhail/Documents/cad/RC Car/Differential.FCStd"

M = 1.5
PA = 20.0
CONE_R = 15.0
BACKLASH = 0.42
CLEARANCE = 0.25
HEX_SOCKET = 8.3
SPIDER_BORE = 5.6
RING_N, PINION_N, FACE_W = 36, 22, 7.0
SIDE_N, SPIDER_N = 16, 12
RING_R, PINION_R = M * RING_N / 2, M * PINION_N / 2
APEX_R = math.hypot(RING_R, PINION_R)
SIDE = dict(cone=CONE_R, n=SIDE_N, front=5.4, back=11.25, boss=10.9)
SPIDER = dict(cone=CONE_R, n=SPIDER_N, front=7.7, back=13.9, boss=7.5)
RING = dict(cone=APEX_R, n=RING_N, front=(APEX_R - FACE_W) * PINION_R / APEX_R, back=PINION_R + 6.0, boss=0)
PINION = dict(cone=APEX_R, n=PINION_N, front=(APEX_R - FACE_W) * RING_R / APEX_R, back=RING_R + 4.0, boss=0)

FACE_IN, HOUSE_R = 11.5, 19.0
CAV_R, CAV_Y, PAD_HZ = 16.6, 14.2, 5.5
SLOT_Y1, SLOT_W = 17.8, 5.3
BORE_D, CB_D, CB_DEEP = 14.6, 22.4, 2.0
PILOT_D, PILOT_DEEP, BOSS_D, BOSS_Y, BOSS_Z = 2.8, 9.0, 5.2, 6.835, 14.69
CAP_T = 5.0
FINGER_CLR = 0.15
CLEAR_D = 3.2
HEAD_D, HEAD_H = 6.0, 3.2
PIN_D, PIN_LEN, PIN_FLAT = 5.0, 35.2, 0.6
SHAFT_AF, SHAFT_X0 = 8.0, 2.65
FLANGE_D, FLANGE_X1 = 12.0, 5.3
SHAFT_HOLE_D, SHAFT_HOLE_X = 2.8, 67.0
PORT_LEN, PORT_HOLE = 16.0, 5.9
PS_FLANGE_T, HEAD_AF, POCKET_AF, PIN_BORE_D = 2.4, 11.0, 11.4, 9.8
PS_CB_DEEP = PS_FLANGE_T
WH_FD, WH_FT, WH_BD, WH_X0, WH_X1 = 44.0, 3.0, 16.0, 58.0, 73.0
WH_SOCKET, WH_GLUE_D, WH_GLUE_R = 8.2, 4.0, 15.0
WH_SCREW_NEAR, WH_SCREW_FAR = 3.4, 2.8

RING_DX, CARRIER_FLOAT, IDLER_FLOAT, PIN_FLOAT, RING_TRIM_R = 0.03, 0.3, 0.3, 0.3, 26.8
LINER_BORE, LINER_OD, LINER_ID, LINER_L = 12.2, 12.0, 10.0, 8.0
LIP_T, LIP_BORE, LINER_PLAY, LIP_LEAD, LEAD_OFF = 1.2, 10.9, 0.3, 0.5, 0.6
GRV_B, GRV_D, GRV_LEAD, GRV_OFF, END_GAP, RIB_CLR, RIB_OFF, RIB_ARC = 0.6, 0.35, 0.7, 0.3, 0.5, 0.1, 0.45, 40.0
SLOPE = GRV_LEAD / GRV_D
MOUTH = GRV_B + 2 * GRV_LEAD
CEN = END_GAP + GRV_OFF + MOUTH / 2
BUSH_CB = CEN + GRV_B / 2 + SLOPE * (GRV_D + 0.1) + 0.1
BUSH_OD, BUSH_J, BUSH_FL_R, BUSH_FT_R = 14.0, 5.0, 8.2, 3.7
IDL_BORE_R, IDL_COLLAR_R, IDL_COLLAR_IN, IDL_COLLAR_X0, IDL_RECESS_R = 7.3, 10.0, 8.5, 16.9, 19.62
IDL_HEAD_R, IDL_TOE_X = 19.9, 14.0
PK_L = LINER_L + LINER_PLAY
WALL_T = 2 * LIP_T + PK_L
LIP_R, PK_R, PLUG_NECK_R, PLUG_PLAY = LIP_BORE / 2, LINER_BORE / 2, LIP_BORE / 2 - 0.35, 0.3
HUB_EXT, SHELL_T = 3.6, 2.4
CAV_M, DRUM_CAV_R, CAV_JOIN = 0.8, HOUSE_R + 0.62, 12.4
POCKET_R, WALL_CLR = BUSH_FL_R + 0.1, 0.4
CASE_Z, SPLIT_GAP, FILLET_R, CHAMFER_TOP, CHAMFER_BOT = 29.0, 0.05, 3.0, 1.0, 1.5
SCREW_X, SCREW_Y, SEAT_Z, PILOT_LEN, WELL_R, HOLE_R = (-24.8, 23.2), 37.5, -6.0, 11.0, 3.3, 1.8
KEY_W, KEY_D = 3.0, 0.6
HOLLOW_Z = 9.4
KEY_X, KEY_Y = (-18.0, -8.0, 8.0, 18.0), (-14.0, 14.0)

RING_BACK = RING["back"] + RING_DX
BL_X1 = -RING_BACK - CARRIER_FLOAT
XC = FACE_IN + CAP_T
BR_X1 = XC + BUSH_FT_R
TR = RING_BACK + HUB_EXT + IDLER_FLOAT
TRF = TR + BUSH_CB
XR = TRF + WALL_T
TL, XL = -TRF, -XR
RIB_END_L = -(RING_BACK + WALL_CLR)
BL_X0 = TL + END_GAP
BUSH_JL = -FACE_IN - BL_X1
YT = PINION["back"]
YL0 = YT + PIN_FLOAT
YP0 = YL0 + LIP_T
YP1 = YP0 + PK_L
YC = YP1 + LIP_T
HB = 30.6
EAR_T, EAR_HOLE_D, EAR_R, EAR_DX, EAR_Y, EAR_TUCK, EAR_CH, EAR_WEB, EAR_WEB_W = 4.0, 3.6, 5.0, 5.0, 36.0, 0.8, 1.0, 2.0, 1.8
BOLT_L, BOLT_D, BOLT_HEAD_D, BOLT_HEAD_H, DRIVER_D, DRIVER_L = 16.0, 3.0, 6.0, 3.2, 6.0, 60.0
PLUG_R, PLUG_Y0, PLUG_OUT, PLUG_CH, PLUG_FLAT = PK_R - 0.35, YL0 - 0.5, 0.6, 0.5, 3.2

PX, LAYER, OVER, BRIDGE_MAX, HOLE_MAX, TILT_MIN, SKIN = 0.1, 0.2, 0.3, 10.0, 3.0, 45.0, 0.2
GAP = 2 * OVER + PX
NEAR = np.add.outer(np.arange(-5, 6) ** 2, np.arange(-5, 6) ** 2) <= 25
CROSS = ndi.generate_binary_structure(2, 1)

EXEMPT = dict(SpiderPin=("P1",), Bushing_R=("P5", 1.3), PinionA=("P5", 1.6), SpiderGear_1=("P5", 0.45), CaseBottom=("P5", 1.1), Sleeve_1=("P6",))

PH = dict(spider=15.0, sideL=0.0, ring=0.0, pinion=0.0, iring=0.0)

COLORS = dict(Carrier=(0.2, 0.5, 0.9), Cap=(0.9, 0.5, 0.1), Bushing_L=(0.9, 0.9, 0.2), Bushing_R=(0.9, 0.9, 0.2),
              SideGear_L=(0.8, 0.2, 0.2), SideGear_R=(0.8, 0.2, 0.2), SpiderGear_1=(0.2, 0.8, 0.3), SpiderGear_2=(0.2, 0.8, 0.3),
              SpiderPin=(0.6, 0.6, 0.6), HalfShaft_L=(0.7, 0.3, 0.8), HalfShaft_R=(0.7, 0.3, 0.8), PinionA=(0.1, 0.8, 0.8),
              PinionB=(0.1, 0.8, 0.8), PinionShaftA=(0.7, 0.3, 0.8), PinionShaftB=(0.7, 0.3, 0.8), OutputPlug=(0.9, 0.7, 0.2), IdlerRing=(0.9, 0.4, 0.6),
              CaseTop=(0.5, 0.5, 0.55), CaseBottom=(0.4, 0.4, 0.45), Sleeve_1=(0.95, 0.95, 0.95), Sleeve_2=(0.95, 0.95, 0.95), Sleeve_3=(0.95, 0.95, 0.95), Sleeve_4=(0.95, 0.95, 0.95))
PRINT_UP = dict(Carrier="+X", Cap="-X", Bushing_L="+X", Bushing_R="+X", SideGear_L="+X", SideGear_R="-X", SpiderGear_1="+Y",
                SpiderGear_2="-Y", SpiderPin="-Z", HalfShaft_L="+Z", HalfShaft_R="+Z", PinionA="+Y", PinionB="-Y",
                PinionShaftA="+Z", PinionShaftB="+Z", OutputPlug="+Z", IdlerRing="-X", CaseTop="-Z", CaseBottom="+Z",
                Sleeve_1="+X", Sleeve_2="+X", Sleeve_3="+Y", Sleeve_4="+Y")


def lib_shape(doc, cls, **props):
    o = doc.addObject("Part::FeaturePython", "tmp")
    cls(o)
    for k, v in props.items():
        setattr(o, k, v)
    doc.recompute()
    s = o.Shape.copy()
    doc.removeObject(o.Name)
    return s


def cyl(r, x0, x1, y=0, z=0):
    return Part.makeCylinder(r, x1 - x0, V(x0, y, z), V(1, 0, 0))


def ycyl(r, y0, y1):
    return Part.makeCylinder(r, y1 - y0, V(0, y0, 0), V(0, 1, 0))


def vcyl(r, x, y, z0, z1):
    return Part.makeCylinder(r, z1 - z0, V(x, y, z0))


def box(x0, x1, y0, y1, z0, z1):
    x0, x1 = sorted((x0, x1))
    y0, y1 = sorted((y0, y1))
    return Part.makeBox(x1 - x0, y1 - y0, z1 - z0, V(x0, y0, z0))


def prism(pts, d):
    return Part.Face(Part.makePolygon(pts + [pts[0]])).extrude(d)


def hexprism(af, x0, x1):
    r = af / math.sqrt(3)
    pts = [V(x0, r * math.cos(math.radians(a)), r * math.sin(math.radians(a))) for a in range(0, 361, 60)]
    return Part.Face(Part.makePolygon(pts)).extrude(V(x1 - x0, 0, 0))


def rot(s, axis, deg):
    s = s.copy()
    s.rotate(O, axis, deg)
    return s


def yhex(af, y0, y1):
    return rot(hexprism(af, y0, y1), V(0, 0, 1), 90)


def mirror_z(s):
    return s.mirror(O, V(0, 0, 1))


def mirror_x(s):
    return s.mirror(O, V(1, 0, 0))


def rev(pts, axis="x"):
    P = [V(a, b, 0) for a, b in pts]
    return Part.Face(Part.makePolygon(P + [P[0]])).revolve(O, V(1, 0, 0) if axis == "x" else V(0, 1, 0), 360)


def bevel_body(doc, g, phase):
    n, cone_r, front, back, boss = g["n"], g["cone"], g["front"], g["back"], g["boss"]
    pa = math.asin(n * M / 2 / cone_r)
    s, c = math.sin(pa), math.cos(pa)
    ah, rh = cone_r * c, cone_r * s
    scale = M * n / 2 / math.tan(pa)
    t = lib_shape(doc, gc.BevelGear, num_teeth=n, module="%g mm" % M, pitch_angle="%f deg" % math.degrees(pa),
                  height="1 mm", pressure_angle="%g deg" % PA, backlash="%g mm" % BACKLASH,
                  clearance=CLEARANCE, reset_origin=False)
    face = [f for f in t.Faces if abs(f.BoundBox.ZMin - scale) < 1e-3 and abs(f.BoundBox.ZMax - scale) < 1e-3][0]
    wires = []
    for z in ((front - 0.5) / scale, (back + 1) / scale):
        w = face.OuterWire.copy()
        m = App.Matrix()
        m.scale(z, z, z)
        wires.append(w.transformGeometry(m))
    loft = Part.makeLoft(wires, True, True)

    def line_r(a):
        return rh - (a - ah) * c / s
    poly = [V(0, 0, front), V(line_r(front), 0, front), V(line_r(back), 0, back), V(0, 0, back), V(0, 0, front)]
    env = Part.Face(Part.makePolygon(poly)).revolve(O, V(0, 0, 1), 360)
    body = loft.common(env)
    if boss:
        body = body.fuse(Part.makeCylinder(boss, back - (ah + 2.5 * s), V(0, 0, ah + 2.5 * s)))
    body = body.removeSplitter()
    body.rotate(O, V(0, 0, 1), phase)
    return body


def silhouette(body, g):
    pa = math.asin(g["n"] * M / 2 / g["cone"])
    s, c = math.sin(pa), math.cos(pa)
    ah, rh = g["cone"] * c, g["cone"] * s
    rf = max(math.hypot(v.X, v.Y) for v in body.Vertexes if abs(v.Z - g["front"]) < 1e-3)
    k = rf / g["front"]
    ap = (rh + ah * c / s) / (k + c / s)
    return [(g["front"], rf), (ap, k * ap), (g["back"], rh - (g["back"] - ah) * c / s)]


def build_gears(doc, ph):
    side = bevel_body(doc, SIDE, 0.0)
    sideL = bevel_body(doc, SIDE, ph["sideL"])
    spider = bevel_body(doc, SPIDER, ph["spider"])
    hexcut = hexprism(HEX_SOCKET, -30, 30)
    gR = rot(side, V(0, 1, 0), 90).cut(hexcut)
    gL = rot(sideL, V(0, 1, 0), -90).cut(hexcut)
    s1 = rot(spider, V(1, 0, 0), -90).cut(Part.makeCylinder(SPIDER_BORE / 2, 60, V(0, -30, 0), V(0, 1, 0)))
    s2 = rot(s1, V(1, 0, 0), 180)
    return gR, gL, s1, s2


def build_pinion(body):
    return rot(body, V(1, 0, 0), -90).cut(ycyl(PIN_BORE_D / 2, 0, 60)).cut(yhex(POCKET_AF, 0, PINION["front"] + PS_CB_DEEP))


def ring_x(body, phase, sign):
    r = rot(rot(body, V(0, 0, 1), phase), V(0, 1, 0), -90).common(cyl(RING_TRIM_R, -40, 40))
    r.translate(V(-RING_DX, 0, 0))
    return r if sign < 0 else mirror_x(r)


def build_carrier(ring):
    c = ring.fuse(cyl(HOUSE_R, -RING_BACK, FACE_IN))
    c = c.cut(cyl(BORE_D / 2, -RING_BACK - 1, -FACE_IN + 1)).cut(cyl(CB_D / 2, -FACE_IN - CB_DEEP, -FACE_IN))
    cav = cyl(CAV_R, -FACE_IN, FACE_IN + 1)
    for sg in (1, -1):
        cav = cav.cut(box(-FACE_IN, FACE_IN + 1, *sorted((sg * CAV_Y, sg * (CAV_R + 1))), -PAD_HZ, PAD_HZ))
        for zz in (1, -1):
            cav = cav.cut(cyl(BOSS_D / 2, -FACE_IN, FACE_IN + 1, sg * BOSS_Y, zz * BOSS_Z))
    c = c.cut(cav)
    for sg in (1, -1):
        s0, s1 = sorted((sg * (CAV_Y - 0.2), sg * SLOT_Y1))
        slot = box(0, FACE_IN + 1, s0, s1, -SLOT_W / 2, SLOT_W / 2).fuse(
            Part.makeCylinder(SLOT_W / 2, s1 - s0, V(0, s0, 0), V(0, 1, 0)))
        c = c.cut(slot)
        for zz in (1, -1):
            c = c.cut(cyl(PILOT_D / 2, FACE_IN - PILOT_DEEP, FACE_IN + 1, sg * BOSS_Y, zz * BOSS_Z))
    return c.removeSplitter()


def build_cap():
    c = cyl(HOUSE_R, FACE_IN, XC)
    fz = SLOT_W / 2 - FINGER_CLR
    for sg in (1, -1):
        y0, y1 = sorted((sg * (CAV_Y + FINGER_CLR), sg * (SLOT_Y1 - FINGER_CLR)))
        c = c.fuse(box(PIN_D / 2 + 0.3, FACE_IN, y0, y1, -fz, fz))
        for zz in (1, -1):
            c = c.cut(cyl(CLEAR_D / 2, FACE_IN - 1, XC + 1, sg * BOSS_Y, zz * BOSS_Z))
    return c.cut(cyl(BORE_D / 2, FACE_IN - 1, XC + 1)).removeSplitter()


def build_bushing(side):
    r, f, rb = BUSH_OD / 2, BUSH_FL_R, LIP_BORE / 2
    if side < 0:
        s = rev([(BL_X0, 0), (BL_X0, f), (BL_X1, f), (BL_X1, r), (BL_X1 + BUSH_JL, r), (BL_X1 + BUSH_JL, 0)])
        cx, rg, rr = TL + CEN, f - GRV_D, f
    else:
        e = TRF - END_GAP
        s = rev([(XC - BUSH_J, 0), (XC - BUSH_J, r), (XC, r), (XC, f), (BR_X1, f), (BR_X1, r), (e, r), (e, 0)])
        cx, rg, rr = TRF - CEN, r - GRV_D, r
    m, b = MOUTH / 2, GRV_B / 2
    s = s.cut(rev([(cx - m - SLOPE, rr + 1), (cx - m, rr), (cx - b, rg), (cx + b, rg), (cx + m, rr), (cx + m + SLOPE, rr + 1)]))
    return s.cut(cyl(rb, TL - 1, TRF + 1)).removeSplitter()


def build_idler(ring):
    r = ring_x(ring, PH["iring"], 1)
    r = r.cut(cyl(IDL_RECESS_R, 12.0, XC - 1.5)).cut(cyl(IDL_HEAD_R, XC - 1.5, BR_X1)).cut(cyl(40, 12.0, IDL_TOE_X))
    r = r.fuse(cyl(IDL_COLLAR_R, IDL_COLLAR_X0, BR_X1)).cut(cyl(IDL_COLLAR_IN, IDL_COLLAR_X0 - 1, BR_X1))
    r = r.fuse(cyl(bb(r.common(box(RING_BACK - 0.3, RING_BACK, -40, 40, -40, 40))).ZMax - 0.05, RING_BACK - 0.5, RING_BACK + HUB_EXT))
    return r.cut(cyl(IDL_BORE_R, BR_X1 - 1, RING_BACK + HUB_EXT + 1)).removeSplitter()


def build_pin():
    p = Part.makeCylinder(PIN_D / 2, PIN_LEN, V(0, -PIN_LEN / 2, 0), V(0, 1, 0))
    return p.cut(box(-5, 5, -30, 30, PIN_D / 2 - PIN_FLAT, 5))


def port_cut(s, x0, x1, ax="x"):
    return s.cut(box(x0 - 1, x1 + 1, -10, 10, -10, -SHAFT_AF / 2) if ax == "x" else box(-10, 10, x0 - 1, x1 + 1, -10, -SHAFT_AF / 2))


def build_half_shaft(sign):
    ref = XR if sign > 0 else -XL
    tip = ref + PORT_LEN
    s = hexprism(SHAFT_AF, SHAFT_X0, tip).fuse(cyl(FLANGE_D / 2, SHAFT_X0, FLANGE_X1))
    s = port_cut(s, SHAFT_X0, tip).cut(Part.makeCylinder(SHAFT_HOLE_D / 2, 20, V(tip - PORT_HOLE, 0, -10), V(0, 0, 1)))
    return (s if sign > 0 else mirror_x(s)).removeSplitter()


def build_plug(y_in=PLUG_Y0):
    r, n, yo = PLUG_R, PLUG_NECK_R, YC + PLUG_OUT
    b0, b1 = YP0 + PLUG_PLAY / 2, YP1 - PLUG_PLAY / 2
    s = rev([(0, y_in), (n, y_in), (n, b0), (r, b0), (r, b1), (n, b1), (n, yo - PLUG_CH), (n - PLUG_CH, yo), (0, yo)], "y")
    return rot(s.cut(box(-10, 10, 0, 99, -10, -PLUG_FLAT)), V(0, 0, 1), 180).removeSplitter()


def build_pinion_shaft(front):
    y0, tip = front, YC + PORT_LEN
    s = yhex(HEAD_AF, y0, y0 + PS_FLANGE_T).fuse(yhex(SHAFT_AF, y0, tip))
    s = port_cut(s, y0, tip, "y").cut(vcyl(SHAFT_HOLE_D / 2, 0, tip - PORT_HOLE, -10, 10))
    return s.removeSplitter()


def build_sleeve(ax, c0):
    s = Part.makeCylinder(LINER_OD / 2, LINER_L, V(0, 0, 0), V(0, 0, 1)).cut(Part.makeCylinder(LINER_ID / 2, LINER_L + 2, V(0, 0, -1), V(0, 0, 1)))
    s = rot(s, V(0, 1, 0), 90) if ax == "x" else rot(s, V(-1, 0, 0), 90)
    s.translate(V(c0, 0, 0) if ax == "x" else V(0, c0, 0))
    return s


def build_wheel_hub():
    h = cyl(WH_FD / 2, WH_X1 - WH_FT, WH_X1).fuse(cyl(WH_BD / 2, WH_X0, WH_X1 - WH_FT))
    h = h.cut(hexprism(WH_SOCKET, WH_X0 - 1, WH_X1 + 1))
    for k in range(6):
        a = math.radians(60 * k)
        h = h.cut(cyl(WH_GLUE_D / 2, WH_X1 - WH_FT - 1, WH_X1 + 1, WH_GLUE_R * math.cos(a), WH_GLUE_R * math.sin(a)))
    h = h.cut(Part.makeCylinder(WH_SCREW_NEAR / 2, 10, V(SHAFT_HOLE_X, 0, 0), V(0, 0, 1)))
    return h.cut(Part.makeCylinder(WH_SCREW_FAR / 2, 10, V(SHAFT_HOLE_X, 0, -10), V(0, 0, 1))).removeSplitter()


def pocket_x(a, b, sg):
    p0, p1 = (a + sg * LIP_T, a + sg * (LIP_T + PK_L))
    return rev([(a - sg, 0), (a - sg, LIP_R), (p0, LIP_R), (p0, PK_R), (p1, PK_R), (p1, LIP_R), (b, LIP_R), (b, 0)])


def lip_lead(ax, u, d):
    tri = [(u, LIP_LEAD), (u + d * LIP_LEAD, 0), (u, -LIP_LEAD)]
    if ax == "x":
        return prism([V(a, -PK_R, z) for a, z in tri], V(0, 2 * PK_R, 0))
    return prism([V(-PK_R, a, z) for a, z in tri], V(2 * PK_R, 0, 0))


def pocket_leads(ax, a, sg):
    p0, p1 = a + sg * LIP_T, a + sg * (LIP_T + PK_L)
    return [lip_lead(ax, p0, -sg), lip_lead(ax, p1, sg)]


def rib_void(side):
    r, rg, cx = (POCKET_R, BUSH_FL_R - GRV_D, TL + CEN) if side < 0 else (BUSH_OD / 2 + 0.1, BUSH_OD / 2 - GRV_D, TRF - CEN)
    ht, hx = GRV_B / 2 + SLOPE * RIB_CLR, GRV_B / 2 + SLOPE * (r + 0.5 - rg)
    a, b = (TL, RIB_END_L) if side < 0 else (TR - 1, TRF)
    tooth = rev([(cx - hx, r + 0.5), (cx - ht, rg + RIB_CLR), (cx + ht, rg + RIB_CLR), (cx + hx, r + 0.5)])
    t, c = 40.0 * math.sin(math.radians(RIB_ARC)), 40.0 * math.cos(math.radians(RIB_ARC))
    pad = prism([V(-60, 0, 0), V(-60, -t, c), V(-60, t, c)], V(120, 0, 0))
    return rev([(a, 0), (a, r), (b, r), (b, 0)]).cut(tooth.common(pad))


def case_cavity(sr, sp):
    m = CAV_M
    (af, rf), (ap, rp), (ab, rb) = sr
    L = RING_DX
    xt = af + (RING_TRIM_R - rf) / (rp - rf) * (ap - af)
    x2 = ap + (rp - RING_TRIM_R) / (rp - rb) * (ab - ap)
    left = [(-CAV_JOIN, 0), (-CAV_JOIN, rf + m), (-(xt + L), RING_TRIM_R + m), (-(x2 + L), RING_TRIM_R + m), (-(ab + L) - WALL_CLR, rb + m), (-(ab + L) - WALL_CLR, 0)]
    right = [(CAV_JOIN, 0), (CAV_JOIN, rf + m), (xt + L, RING_TRIM_R + m), (x2 + L, RING_TRIM_R + m), (ab + L, rb + m), (TR, rb + m), (TR, 0)]
    xs = [rev(left), rev(right), pocket_x(XL, TL + 1, 1), pocket_x(XR, TR - 1, -1), rib_void(-1), rib_void(1),
          rev([(-CAV_JOIN, 0), (-CAV_JOIN, DRUM_CAV_R), (CAV_JOIN, DRUM_CAV_R), (CAV_JOIN, 0)])]
    xs += pocket_leads("x", XL, 1) + pocket_leads("x", XR, -1) + pocket_leads("y", YL0, 1) + pocket_leads("y", -YL0, -1)
    (yf, rpf), (yp, rpp), (yb, rpb) = sp
    pin = [(0, yf), (rpf + m, yf), (rpp + m, yp), (rpb + m, yb), (rpb + m, YL0), (0, YL0)]
    bore = [(0, yb), (LIP_R, yb), (LIP_R, YP0), (PK_R, YP0), (PK_R, YP1), (LIP_R, YP1), (LIP_R, YC + 1), (0, YC + 1)]
    ya = rev(pin, "y").fuse(rev(bore, "y"))
    return xs, [ya, rot(ya, V(0, 0, 1), 180)]


def outer_block(z0, z1):
    b = box(XL, XR, -YC, YC, z0, z1)
    return b.makeFillet(FILLET_R, [e for e in b.Edges if abs(e.Vertexes[0].Z - e.Vertexes[1].Z) > 1e-6])


def shell(cav, ys, h, boss_r):
    n = 12
    w = (XR - XL) / n
    R = [bb(cav.common(box(XL + i * w, XL + (i + 1) * w, -40, 40, -40, 40))).ZMax + SHELL_T for i in range(n)]
    R = [R[i] if i in (0, n - 1) else max(R[i - 1:i + 2]) for i in range(n)]
    k, top = SHELL_T * math.sqrt(2), h - SHELL_T

    def ext(q, ax, a, b):
        pts = [V(a, u, v) for u, v in q] if ax == "x" else [V(u, a, v) for u, v in q]
        return prism(pts, V(b - a, 0, 0) if ax == "x" else V(0, b - a, 0))

    def wedge(r, ax, a, b, a2, b2, top=top):
        t = min(r / math.sqrt(2), h)
        s = ext([(0, 0), (-t, t), (-h, h), (h, h), (t, t)], ax, a, b)
        u0 = r / math.sqrt(2)
        for sg in (1, -1):
            if top - k - u0 > 2:
                s = s.cut(ext([(sg * u0, u0 + k), (sg * u0, top), (sg * (top - k), top)], ax, a2, b2))
        c = min(u0 - SHELL_T, top - r)
        if c > 1:
            s = s.cut(ext([(0, r), (c, r + c), (c, top), (-c, top), (-c, r + c)], ax, a2, b2))
        return s.fuse(cyl(r, a, b) if ax == "x" else ycyl(r, a, b))
    parts = [wedge(R[i], "x", XL + i * w, XL + (i + 1) * w, XL + i * w + SHELL_T * (i == 0), XL + (i + 1) * w - SHELL_T * (i == n - 1)) for i in range(n)]
    rp = bb(ys[0]).XLength / 2 + SHELL_T
    arm = [wedge(rp, "y", 0, YT + SHELL_T, 0, YT), wedge(PK_R + SHELL_T, "y", YT, YC, YT + SHELL_T, YC - SHELL_T, h - (HOLLOW_Z if h == HB else SHELL_T))]
    parts += arm + [rot(a, V(0, 0, 1), 180) for a in arm]
    for sx in SCREW_X:
        parts.append(box(sx - 1.2, sx + 1.2, -SCREW_Y, SCREW_Y, 0, h))
        parts += [vcyl(boss_r, sx, sy, 0, h) for sy in (SCREW_Y, -SCREW_Y)]
    return parts[0].fuse(parts[1:]).removeSplitter()


def build_case(sr, sp):
    xs, ys = case_cavity(sr, sp)
    cav = xs[0].fuse(xs[1:])
    top = outer_block(0, CASE_Z)
    top = top.makeChamfer(CHAMFER_TOP, [e for e in top.Edges if all(abs(v.Z - CASE_Z) < 1e-6 for v in e.Vertexes)]).common(shell(cav, ys, CASE_Z, 3.4))
    bot = outer_block(-HB, -SPLIT_GAP)
    bot = bot.makeChamfer(CHAMFER_BOT, [e for e in bot.Edges if all(abs(v.Z + HB) < 1e-6 for v in e.Vertexes)]).common(mirror_z(shell(cav, ys, HB, 5.0)))
    yf = 30.6
    for sg in (1, -1):
        ramp = [V(XL - 1, sg * yf, -HB), V(XL - 1, sg * (YC + 1), -HB + YC + 1 - yf), V(XL - 1, sg * (YC + 1), -HB - 1), V(XL - 1, sg * yf, -HB - 1)]
        bot = bot.cut(prism(ramp, V(XR - XL + 2, 0, 0)))
    cut_all = xs + ys
    for sx in SCREW_X:
        for sy in (SCREW_Y, -SCREW_Y):
            top = top.cut(vcyl(PILOT_D / 2, sx, sy, -1, PILOT_LEN))
            bot = bot.cut(vcyl(HOLE_R, sx, sy, SEAT_Z + SKIN, 1)).cut(vcyl(WELL_R, sx, sy, -HB - 1, SEAT_Z))
    keys = [box(x - KEY_W / 2, x + KEY_W / 2, y0, y1, CASE_Z - KEY_D, CASE_Z + 1) for x in KEY_X for y0, y1 in ((-YC - 1, -29.0), (29.0, YC + 1))]
    keys += [box(XL - 1, XR + 1, y - KEY_W / 2, y + KEY_W / 2, CASE_Z - KEY_D, CASE_Z + 1) for y in KEY_Y]
    top = top.cut(keys[0].fuse(keys[1:]).removeSplitter())
    for c in cut_all:
        top, bot = top.cut(c), bot.cut(c)
    return max(top.removeSplitter().Solids, key=lambda x: x.Volume), bot.removeSplitter()


def ear_pos():
    return [(xh, sy * EAR_Y) for xh in (XL - EAR_DX, XR + EAR_DX) for sy in (1, -1)]


def add_ears(top):
    z0 = CASE_Z - EAR_T
    for xh, yh in ear_pos():
        sg = 1 if xh > 0 else -1
        xw = sg * (XR if sg > 0 else -XL)
        tab = box(xh, SCREW_X[0] + EAR_TUCK, yh - EAR_R, yh + EAR_R, z0, CASE_Z) if sg < 0 else box(SCREW_X[1] - EAR_TUCK, xh, yh - EAR_R, yh + EAR_R, z0, CASE_Z)
        ear = tab.fuse(vcyl(EAR_R, xh, yh, z0, CASE_Z)).removeSplitter()
        ear = ear.makeChamfer(EAR_CH, [e for e in ear.Edges if all(abs(v.Z - z0) < 1e-6 for v in e.Vertexes) and min(abs(v.X - xw) for v in e.Vertexes) > 1.0])
        tri = [V(xw - sg * 1.0, 0, z0), V(xw + sg * EAR_WEB, 0, z0), V(xw - sg * 1.0, 0, z0 - EAR_WEB - 1.0)]
        for ya in (yh - EAR_R + EAR_CH, yh + EAR_R - EAR_CH - EAR_WEB_W):
            ear = ear.fuse(prism([V(p.x, ya, p.z) for p in tri], V(0, EAR_WEB_W, 0)))
        top = top.fuse(ear.cut(vcyl(EAR_HOLE_D / 2, xh, yh, z0 - 1, CASE_Z + 1)))
    return top.removeSplitter()


def build_bolt(x, y):
    zh = CASE_Z - EAR_T
    b = vcyl(BOLT_D / 2, x, y, zh, zh + BOLT_L).fuse(vcyl(BOLT_HEAD_D / 2, x, y, zh - BOLT_HEAD_H, zh))
    return b.removeSplitter(), vcyl(DRIVER_D / 2, x, y, zh - BOLT_HEAD_H - DRIVER_L, zh - BOLT_HEAD_H)


def build_parts(doc, ph=PH):
    gR, gL, s1, s2 = build_gears(doc, ph)
    rb, pb = bevel_body(doc, RING, 0.0), bevel_body(doc, PINION, ph["pinion"])
    pin = build_pinion(pb)
    top, bot = build_case(silhouette(rb, RING), silhouette(pb, PINION))
    return dict(Carrier=build_carrier(ring_x(rb, ph["ring"], -1)), Cap=build_cap(), Bushing_L=build_bushing(-1), Bushing_R=build_bushing(1),
                SideGear_L=gL, SideGear_R=gR, SpiderGear_1=s1, SpiderGear_2=s2, SpiderPin=build_pin(),
                HalfShaft_L=build_half_shaft(-1), HalfShaft_R=build_half_shaft(1), PinionA=pin, PinionB=rot(pin, V(1, 0, 0), 180),
                PinionShaftA=build_pinion_shaft(PINION["front"]), PinionShaftB=rot(build_pinion_shaft(PINION["front"]), V(0, 0, 1), 180),
                IdlerRing=build_idler(rb), CaseTop=add_ears(top), CaseBottom=bot,
                Sleeve_1=build_sleeve("x", XL + LIP_T + LINER_PLAY / 2), Sleeve_2=build_sleeve("x", XR - LIP_T - PK_L + LINER_PLAY / 2),
                Sleeve_3=build_sleeve("y", YP0 + LINER_PLAY / 2), Sleeve_4=build_sleeve("y", -YP1 + LINER_PLAY / 2))


def bb(s):
    return s.optimalBoundingBox(False, False)


def vol(a, b):
    return a.common(b).Volume if a.BoundBox.intersect(b.BoundBox) else 0.0


def dist(a, b):
    return a.distToShape(b)[0]


def travel(s, ax, blockers, hi=1.0):
    def hit(d):
        t = s.copy()
        t.translate(ax * d)
        return any(vol(t, b) > 1e-3 for b in blockers)
    out = []
    for sg in (1, -1):
        lo, up = 0.0, hi
        for _ in range(14):
            mid = (lo + up) / 2
            lo, up = (lo, mid) if hit(sg * mid) else (mid, up)
        out.append(round(lo, 3))
    return out


def mesh_run(P, rng):
    pitch = 360.0 / PINION_N
    rep = dict(gaps={}, dirs={})
    for nm in ("Carrier", "IdlerRing"):
        ring = P[nm]
        ok = [sg for sg in (1, -1) if vol(rot(P["PinionA"], V(0, 1, 0), pitch / 4), rot(ring, V(1, 0, 0), sg * pitch / 4 * PINION_N / RING_N)) < 1e-3]
        assert len(ok) == 1, (nm, ok)
        rep["dirs"][nm] = ok[0]
        for pn, sp in (("PinionA", 1), ("PinionB", -1)):
            res = []
            for k in range(4):
                th = pitch * k / 4
                for tr in rng[nm]:
                    for tp in rng[pn]:
                        r, p = rot(ring, V(1, 0, 0), ok[0] * th * PINION_N / RING_N), rot(P[pn], V(0, 1, 0), sp * th)
                        r.translate(V(tr, 0, 0))
                        p.translate(V(0, tp, 0))
                        res.append((round(vol(r, p), 4), round(dist(r, p), 3)))
            rep["gaps"][(nm, pn)] = res
    return rep


def side_mesh(P, rng, outs):
    pitch = 360.0 / SPIDER_N
    s1, s2, res = P["SpiderGear_1"], P["SpiderGear_2"], {}
    for n in "LR":
        g, out = P["SideGear_" + n], (-1 if n == "L" else 1)
        ok = [k for k in (1, -1) if vol(rot(s1, V(0, 1, 0), pitch / 4), rot(g, V(1, 0, 0), k * pitch / 4 * SPIDER_N / SIDE_N)) < 1e-3]
        assert len(ok) == 1, (n, ok)
        rep = dict(nominal=99.0, nominal_push=0.0, push=0.0, gap=99.0, overlap=0.0)
        for k in range(4):
            th = pitch * k / 4
            ga = rot(g, V(1, 0, 0), ok[0] * th * SPIDER_N / SIDE_N)
            for sh in (0.0, rng[0], rng[1]):
                sp = [rot(s1, V(0, 1, 0), th), rot(s2, V(0, 1, 0), -th)]
                for q in sp:
                    q.translate(V(sh, 0, 0))
                push = 0.0
                while True:
                    t = ga.copy()
                    t.translate(V(out * push, 0, 0))
                    if max(vol(t, q) for q in sp) < 1e-3 or push > outs[n] + 0.1:
                        break
                    push += 0.05
                gap = min(dist(t, q) for q in sp)
                if sh == 0.0:
                    rep["nominal"] = min(rep["nominal"], gap)
                    rep["nominal_push"] = max(rep["nominal_push"], push)
                rep["push"] = max(rep["push"], push)
                rep["gap"] = min(rep["gap"], gap)
                rep["overlap"] = max(rep["overlap"], *(vol(t, q) for q in sp))
        res[n] = {k: round(v, 4) for k, v in rep.items()}
    return res


def assembly(P):
    bundle = [n for n in P if n not in ("CaseTop", "CaseBottom")]
    out = dict(lower=0.0, close=0.0)
    for dz in [-30 + 0.5 * i for i in range(55)] + [round(-3 + 0.1 * i, 1) for i in range(31)]:
        b = P["CaseBottom"].copy()
        b.translate(V(0, 0, dz))
        for n in bundle:
            t = P[n].copy()
            t.translate(V(0, 0, dz))
            out["lower"] = max(out["lower"], vol(t, P["CaseTop"]))
            out["close"] = max(out["close"], vol(b, P[n]))
    return {k: round(v, 4) for k, v in out.items()}


def oriented(s, up):
    sign, axis = PRINT_UP[up][0], PRINT_UP[up][1]
    v = V(*[(1 if sign == "+" else -1) if a == axis else 0 for a in "XYZ"])
    t = s.copy()
    t.transformShape(App.Placement(O, App.Rotation(v, V(0, 0, 1))).toMatrix())
    t.translate(V(0, 0, -bb(t).ZMin))
    return t


def fill(polys, org, shape):
    e = np.concatenate([np.stack([p[:-1], p[1:]], 1) for p in polys])
    x1, y1, x2, y2 = e[:, 0, 0], e[:, 0, 1], e[:, 1, 0], e[:, 1, 1]
    j0 = np.ceil((np.minimum(y1, y2) - org[1]) / PX - .5).astype(int)
    n = np.maximum(np.ceil((np.maximum(y1, y2) - org[1]) / PX - .5).astype(int) - j0, 0)
    idx = np.repeat(np.arange(len(e)), n)
    j = j0[idx] + np.arange(n.sum()) - np.repeat(np.cumsum(n) - n, n)
    x = x1[idx] + (org[1] + (j + .5) * PX - y1[idx]) * (x2[idx] - x1[idx]) / (y2[idx] - y1[idx])
    i = np.clip(np.ceil((x - org[0]) / PX - .5).astype(int), 0, shape[1])
    c = np.bincount(j * (shape[1] + 1) + i, minlength=shape[0] * (shape[1] + 1)).reshape(shape[0], shape[1] + 1)
    return np.cumsum(c, 1)[:, :shape[1]] % 2 == 1


def bridge(m, pv):
    ys, xs = np.nonzero(m)
    pts = np.c_[xs, ys] * PX
    edge = m & ~ndi.binary_erosion(m, CROSS)
    ext = np.ptp(pts @ np.linalg.eigh(np.cov(pts.T))[1], axis=0) + PX if len(xs) > 2 else np.array([PX, PX])
    held = (edge & ndi.binary_dilation(pv, NEAR)).sum() / max(edge.sum(), 1)
    ok = not (ndi.binary_fill_holes(m) & ~m).any() and held >= 0.8 and ext.min() + GAP <= BRIDGE_MAX and m.sum() * PX * PX >= 0.7 * ext[0] * ext[1]
    return ok, round(float(ext.min() + GAP), 1), round(float(ext.max() + GAP), 1)


def layers(t):
    b = bb(t)
    org, shape = (b.XMin - 1, b.YMin - 1), (int((b.YLength + 2) / PX) + 1, int((b.XLength + 2) / PX) + 1)
    prev, out = None, dict(bad=[], bridges=[])
    for k in range(int(math.ceil(b.ZLength / LAYER - 1e-6))):
        z = min((k + .5) * LAYER + 0.017, (k * LAYER + b.ZLength) / 2)
        polys = [np.array([(v.x, v.y) for v in e.discretize(Number=max(int(e.Length / 0.05), 2) + 1)]) for w in t.slice(V(0, 0, 1), z) for e in w.Edges]
        cur = fill(polys, org, shape) if polys else np.zeros(shape, bool)
        if prev is not None:
            dist = ndi.distance_transform_edt(~prev) * PX
            lab, _ = ndi.label(cur & (dist > OVER + PX / 2), np.ones((3, 3)))
            for c, s in enumerate(ndi.find_objects(lab), 1):
                s = tuple(slice(max(q.start - 8, 0), q.stop + 8) for q in s)
                m = lab[s] == c
                ok, span, length = bridge(m, prev[s])
                cy, cx = ndi.center_of_mass(m)
                at = (round(org[0] + (cx + s[1].start + .5) * PX, 1), round(org[1] + (cy + s[0].start + .5) * PX, 1))
                out["bridges" if ok else "bad"].append((round(z, 1), span, length, at) if ok else (round(z, 1), round(float(dist[s][m].max()), 2), at))
        prev = cur
    return out


def min_tilt(t):
    worst = (90.0, None)
    for f in t.Faces:
        k = f.Surface
        u0, u1, v0, v1 = f.ParameterRange
        uv = [(u0, v0)] if isinstance(k, Part.Plane) else [(u0 + (u1 - u0) * (i + .5) / 10, v0 + (v1 - v0) * (j + .5) / 10) for i in range(10) for j in range(10)]
        uv = [q for q in uv if isinstance(k, Part.Plane) or f.isPartOfDomain(*q)]
        if not isinstance(k, Part.Plane):
            uv += [k.parameter(p) for e in f.Edges for p in e.discretize(Number=9)]
        for u, v in uv:
            n = f.normalAt(u, v)
            if n.z >= 0 or (isinstance(k, Part.Plane) and n.z < -0.9999):
                continue
            p = f.valueAt(u, v)
            if isinstance(k, Part.Cylinder) and abs(k.Axis.z) < 1e-3 and k.Radius <= HOLE_MAX:
                d = p - k.Center
                if n.dot(d - k.Axis * d.dot(k.Axis)) < 0:
                    continue
            a = math.degrees(math.acos(min(1.0, -n.z)))
            if a < worst[0]:
                worst = (round(a, 1), (round(p.x, 1), round(p.y, 1), round(p.z, 1)))
    return worst


def print_report(name, s):
    t = oriented(s, name)
    fl = [f for f in t.Faces if f.BoundBox.ZMax < 1e-4 and isinstance(f.Surface, Part.Plane)]
    fb = bb(Part.makeCompound(fl))
    L = layers(t)
    return dict(floor=round(sum(f.Area for f in fl), 1), wall=round(min(2 * f.Area / f.Length for f in fl), 2), bed_min=round(min(fb.XLength, fb.YLength), 1),
                height=round(bb(t).ZLength, 1), tilt=min_tilt(t), bad=L["bad"], bridges=L["bridges"])


def print_reports(P):
    groups, out = [], {}
    for n, s in P.items():
        t = oriented(s, n)
        key = (round(s.Volume, 1), tuple(sorted(round(d, 1) for d in (bb(t).XLength, bb(t).YLength, bb(t).ZLength))))
        for g in groups:
            if g[0] == key:
                g[1].append(n)
                break
        else:
            groups.append((key, [n]))
    for _, ms in groups:
        out[ms[0]] = dict(print_report(ms[0], P[ms[0]]), twins=ms[1:])
    return out


def port(sh, ref, ax, sg):
    b = bb(sh)
    tip = (b.XMax if sg > 0 else b.XMin) if ax == "x" else (b.YMax if sg > 0 else b.YMin)
    u = V(1, 0, 0) if ax == "x" else V(0, 1, 0)
    probe = lambda off: sh.isInside(u * (tip - sg * PORT_HOLE + off), 1e-6, True)
    z = box(tip - sg * PORT_LEN, tip, -9, 9, -9, 9) if ax == "x" else box(-9, 9, tip - sg * PORT_LEN, tip, -9, 9)
    c = bb(sh.common(z))
    return dict(stick=round(abs(tip - ref), 3), hole_open=not probe(0) and not probe(1.3) and not probe(-1.3) and probe(1.5) and probe(-1.5),
                af=round(c.ZLength, 3), corners=round(c.YLength if ax == "x" else c.XLength, 3))


def insert(items, d, blockers, near=60.0):
    c = Part.makeCompound(items)
    worst = 0.0
    for o in [near - 0.5 * k for k in range(int(near / 0.5) + 1)]:
        t = c.copy()
        t.translate(d * o)
        worst = max(worst, max(vol(t, b) for b in blockers))
    return round(worst, 4)


def ear_wall(top):
    w = 99.0
    for xh, yh in ear_pos():
        loc = top.common(box(xh - 9, xh + 9, yh - 9, yh + 9, CASE_Z - EAR_T / 2 - 0.5, CASE_Z - EAR_T / 2 + 0.5))
        for a in range(0, 360, 10):
            u = V(math.cos(math.radians(a)), math.sin(math.radians(a)), 0)
            r = EAR_HOLE_D / 2 + 0.02
            while r < 9 and loc.isInside(V(xh, yh, CASE_Z - EAR_T / 2) + u * r, 1e-6, True):
                r += 0.05
            w = min(w, r - EAR_HOLE_D / 2)
    return round(w, 2)


def slide(sh, sg, step=0.5):
    b, g = bb(sh), bb(sg)
    sign = 1 if (b.XMax + b.XMin) > 0 else -1
    span = (b.XMax - g.XMin) if sign > 0 else (g.XMax - b.XMin)
    worst = 0.0
    for k in range(int(span / step) + 2):
        t = sg.copy()
        t.translate(V(sign * k * step, 0, 0))
        worst = max(worst, vol(t, sh))
    return round(worst, 4)


def pocket_wall(top, bot, ax, c):
    inside = lambda p: top.isInside(p, 1e-6, True) or bot.isInside(p, 1e-6, True)
    w = 99.0
    for k in range(36):
        a = math.radians(10 * k + 5)
        q = (lambda r: V(c, r * math.cos(a), r * math.sin(a))) if ax == "x" else (lambda r: V(r * math.cos(a), c, r * math.sin(a)))
        r = PK_R + 0.02
        while r < 14 and r - PK_R - 0.1 < w and inside(q(r)):
            r += 0.1
        w = min(w, r - 0.1 - PK_R)
    return round(w, 2)


def lead_sweep(P, top):
    worst, zs = 0.0, [-LINER_OD / 2 - 0.5 + 0.1 * i for i in range(16)] + [-LINER_OD / 2 + 1.5 + 0.5 * i for i in range(10)]
    for k, ax in ((1, V(1, 0, 0)), (2, V(1, 0, 0)), (3, V(0, 1, 0)), (4, V(0, 1, 0))):
        for sg in (1, -1):
            for dz in zs:
                off = sg * min(LEAD_OFF, LINER_PLAY / 2 + max(0.0, LIP_LEAD - max(dz + LINER_OD / 2, 0.0)))
                t = P["Sleeve_%d" % k].copy()
                t.translate(ax * off + V(0, 0, dz))
                worst = max(worst, vol(t, top))
    return round(worst, 4)


def rib_sweep(P, top):
    worst = 0.0
    for n in "LR":
        for sg in (1, -1):
            for i in range(21):
                dz = -2.0 + 0.1 * i
                t = P["Bushing_" + n].copy()
                t.translate(V(sg * min(RIB_OFF, SLOPE * math.cos(math.radians(RIB_ARC)) * -dz), 0, dz))
                worst = max(worst, vol(t, top))
    return round(worst, 4)


def lip_runs(top, ax, c0, c1, step=0.02):
    q = (lambda t: V(t, 0, (LIP_R + PK_R) / 2)) if ax == "x" else (lambda t: V(0, t, (LIP_R + PK_R) / 2))
    runs, cur = [], 0.0
    for k in range(int((c1 - c0) / step)):
        if top.isInside(q(c0 + k * step), 1e-6, True):
            cur += step
        elif cur:
            runs.append(round(cur, 2))
            cur = 0.0
    return runs + ([round(cur, 2)] if cur else [])


def verify(P):
    names = list(P)
    rep = {}
    rep["bbox"] = {n: tuple(round(v, 2) for v in (bb(s).XLength, bb(s).YLength, bb(s).ZLength)) for n, s in P.items()}
    rep["overlap"] = {(a, b): round(vol(P[a], P[b]), 4) for i, a in enumerate(names) for b in names[i + 1:] if vol(P[a], P[b]) > 1e-3}
    X, Y = V(1, 0, 0), V(0, 1, 0)
    cs = dict(CaseTop=P["CaseTop"], CaseBottom=P["CaseBottom"])
    rep["carrier_float"] = travel(Part.makeCompound([P["Carrier"], P["Cap"]]), X, [P["Bushing_L"], P["Bushing_R"]])
    rep["idler_float"] = travel(P["IdlerRing"], X, [P["Bushing_R"], P["CaseTop"], P["CaseBottom"], P["Cap"]])
    rep["pinion_float"] = {n: travel(P["Pinion" + n], Y, [P["PinionShaft" + n], P["CaseTop"], P["CaseBottom"]]) for n in "AB"}
    rep["pinion_shaft_float"] = {n: travel(Part.makeCompound([P["PinionShaft" + n], P["Pinion" + n]]), Y, list(cs.values())) for n in "AB"}
    rng = dict(Carrier=rep["carrier_float"], IdlerRing=rep["idler_float"], PinionA=rep["pinion_float"]["A"], PinionB=rep["pinion_float"]["B"])
    mr = {k: (-v[1], v[0]) for k, v in rng.items()}
    rep["mesh_ranges"] = mr
    rep["mesh"] = mesh_run(P, mr)
    rep["assembly"] = assembly(P)
    heads = [Part.makeCylinder(HEAD_D / 2, HEAD_H, V(XC, sy * BOSS_Y, sz * BOSS_Z), V(1, 0, 0)) for sy in (1, -1) for sz in (1, -1)]
    rep["idler_heads"] = round(min(dist(P["IdlerRing"].common(box(-99, XC + HEAD_H, -99, 99, -99, 99)), h) for h in heads), 3)
    rep["sg_carrier"] = round(min(dist(P["Carrier"].common(box(-FACE_IN + 0.1, FACE_IN - 0.1, -99, 99, -99, 99)), P["SideGear_" + n]) for n in "LR"), 3)
    rep["idler_clear"] = {n: round(dist(P["IdlerRing"], P[n].common(box(-99, XC - 1, -99, 99, -99, 99)) if n == "Cap" else P[n]), 3) for n in ("Carrier", "Cap")}
    rep["heads_case"] = round(min(dist(c, h) for c in cs.values() for h in heads), 3)
    rep["case_clear"] = {(c, n): round(dist(cs[c], P[n]), 3) for c in cs for n in ("Carrier", "Cap", "IdlerRing", "SideGear_L", "SideGear_R", "SpiderGear_1", "SpiderGear_2")}
    rep["pinion_case"] = {(c, n): round(dist(cs[c], P[n]), 3) for c in cs for n in ("PinionA", "PinionB")}
    rep["split_gap"] = round(dist(P["CaseTop"], P["CaseBottom"]), 3)
    rep["bushing_play"] = {n: travel(P["Bushing_" + n], X, list(cs.values()), 0.5) for n in "LR"}
    rep["tail_clear"] = {(n, c): round(dist(P["Bushing_" + n], cs[c]), 3) for n in "LR" for c in cs}
    pil = vcyl(PILOT_D / 2, SCREW_X[0], SCREW_Y, 0, PILOT_LEN)
    others = [f for f in P["CaseTop"].Faces if not (f.BoundBox.XMax - f.BoundBox.XMin < 3.0 and f.BoundBox.YMax - f.BoundBox.YMin < 3.0 and abs(f.BoundBox.XMin - SCREW_X[0]) < 1.6) and f.BoundBox.ZMax > 1e-6]
    rep["pass_hole"] = round(2 * min(f.Surface.Radius for f in P["CaseBottom"].Faces if isinstance(f.Surface, Part.Cylinder) and f.Surface.Radius < 2.6), 3)
    rep["pilot_wall"] = round(min(dist(f, pil) for f in others if f.BoundBox.ZMin < PILOT_LEN + 1), 3)
    col = [vcyl(WELL_R - 0.05, sx, sy, -HB - 1, SEAT_Z - HEAD_H) for sx in SCREW_X for sy in (SCREW_Y, -SCREW_Y)]
    hd = [vcyl(HEAD_D / 2, sx, sy, SEAT_Z - HEAD_H, SEAT_Z) for sx in SCREW_X for sy in (SCREW_Y, -SCREW_Y)]
    rep["heads_free"] = max(vol(c, P[n]) for c in col + hd for n in names)
    top = P["CaseTop"]
    glue = [f for f in top.Faces if isinstance(f.Surface, Part.Plane) and abs(f.BoundBox.ZMin - CASE_Z) < 1e-6 and abs(f.BoundBox.ZMax - CASE_Z) < 1e-6]
    bt, bo = bb(top.common(box(-99, 99, -99, 99, CASE_Z - EAR_T - EAR_WEB - 2.5, CASE_Z - EAR_T - EAR_WEB - 1.5))), bb(top)
    rep["glue"] = dict(body=(round(bt.XLength, 2), round(bt.YLength, 2)), overall=(round(bo.XLength, 2), round(bo.YLength, 2)), area=round(sum(f.Area for f in glue), 1), zmax=round(bo.ZMax, 3))
    cb = bb(Part.makeCompound([top, P["CaseBottom"]]))
    rep["case_size"] = (round(cb.XLength, 2), round(cb.YLength, 2), round(cb.ZLength, 2))
    rep["ground"] = round(-bb(P["CaseBottom"]).ZMin, 3)
    rep["top_wall"] = round(CASE_Z - bb(P["Carrier"]).ZMax - CAV_M, 3)
    circ = []
    spots = [("x", XL + LIP_T / 2, LIP_R), ("x", XL + LIP_T + PK_L / 2, PK_R), ("x", TL - LIP_T / 2, LIP_R), ("x", TL + 0.1, POCKET_R), ("x", TL + CEN + MOUTH, POCKET_R),
             ("x", XR - LIP_T / 2, LIP_R), ("x", XR - LIP_T - PK_L / 2, PK_R), ("x", TRF + LIP_T / 2, LIP_R), ("x", TRF - 0.2, BUSH_OD / 2 + 0.1)]
    spots += [("y", sg * y, r) for sg in (1, -1) for y, r in ((YL0 + LIP_T / 2, LIP_R), (YP0 + PK_L / 2, PK_R), (YC - LIP_T / 2, LIP_R))]
    for ax, pos, r in spots:
        for k in range(24):
            a = math.radians(7.5 * k + 3.75)
            d = lambda rr: V(pos, rr * math.cos(a), rr * math.sin(a)) if ax == "x" else V(rr * math.cos(a), pos, rr * math.sin(a))
            inside = lambda p: top.isInside(p, 1e-6, True) or P["CaseBottom"].isInside(p, 1e-6, True)
            circ.append(inside(d(r + 0.05)) and not inside(d(r - 0.05)))
    rep["bores_closed"] = all(circ)
    ends = [bb(top.common(box(-99, 99, -9, 9, -9, 9)))]
    rep["ports"] = dict(HalfShaft_L=port(P["HalfShaft_L"], ends[0].XMin, "x", -1), HalfShaft_R=port(P["HalfShaft_R"], ends[0].XMax, "x", 1),
                        PinionShaftA=port(P["PinionShaftA"], bb(top).YMax, "y", 1), PinionShaftB=port(P["PinionShaftB"], bb(top).YMin, "y", -1))
    lin = {}
    for k, ax, c0, shn in ((1, "x", XL, "HalfShaft_L"), (2, "x", XR - WALL_T, "HalfShaft_R"), (3, "y", YL0, "PinionShaftA"), (4, "y", -YC, "PinionShaftB")):
        sl, u = P["Sleeve_%d" % k], (X if ax == "x" else Y)
        mid = c0 + LIP_T + PK_L / 2
        lat = (bb(sl).YLength, bb(sl).ZLength) if ax == "x" else (bb(sl).XLength, bb(sl).ZLength)
        lin[k] = dict(vol=round(sl.Volume, 1), od=round(max(lat), 3), length=round(bb(sl).XLength if ax == "x" else bb(sl).YLength, 3), play=travel(sl, u, list(cs.values()), 0.5),
                      hex=round(dist(P[shn], sl), 3), pocket=round(min(dist(sl, c) for c in cs.values()), 3), wall=min(pocket_wall(top, P["CaseBottom"], ax, mid + d) for d in (-3.0, 0.0, 3.0)),
                      lips=lip_runs(top, ax, c0 - 1, c0 + WALL_T + 1))
    rep["liner"] = lin
    rep["lead"] = lead_sweep(P, top)
    rep["rib_lead"] = rib_sweep(P, top)
    rep["slide"] = {n: slide(P["HalfShaft_" + n], P["SideGear_" + n]) for n in "LR"}
    hf = {}
    for n in "LR":
        sh, gr = P["HalfShaft_" + n], P["SideGear_" + n]
        rest = [P[m] for m in names if m not in ("HalfShaft_" + n, "SideGear_" + n, "OutputPlug") and not m.startswith("Sleeve")]
        tin = travel(sh, X, rest + [gr], 0.5)
        ggo = travel(gr, X, rest, 0.5)
        sg = -1 if n == "L" else 1
        inward, gap = (tin[0], tin[1]) if n == "L" else (tin[1], tin[0])
        gear_out = ggo[1] if n == "L" else ggo[0]
        hf[n] = dict(inward=inward, flange_gap=gap, gear_out=gear_out, total=round(inward + gap + gear_out, 3))
    rep["half_float"] = hf
    rep["side_mesh"] = side_mesh(P, mr["Carrier"], {n: hf[n]["gear_out"] for n in "LR"})
    c, sgl, hsl, sgr, hsr = (P[n] for n in ("Carrier", "SideGear_L", "HalfShaft_L", "SideGear_R", "HalfShaft_R"))
    sp = [P["SpiderGear_1"], P["SpiderGear_2"], P["SpiderPin"]]
    screws = [cyl(1.35, XC - 12, XC, sg * BOSS_Y, zz * BOSS_Z).fuse(cyl(HEAD_D / 2, XC, XC + HEAD_H, sg * BOSS_Y, zz * BOSS_Z)) for sg in (1, -1) for zz in (1, -1)]
    od = {"L_in": insert([sgl, hsl], X, [c])}
    cum = [c, sgl, hsl]
    od["bushing_L"] = insert([P["Bushing_L"]], -X, cum)
    cum.append(P["Bushing_L"])
    od["spiders_with_R"] = insert(sp, X, cum + [sgr, hsr])
    od["spiders"] = insert(sp, X, cum)
    cum += sp
    od["R_in"] = insert([sgr, hsr], X, cum)
    cum += [sgr, hsr]
    od["cap"] = insert([P["Cap"]], X, cum)
    cum.append(P["Cap"])
    od["cap_screws"] = insert(screws, X, cum)
    cum += screws
    od["bushing_R"] = insert([P["Bushing_R"]], X, cum)
    cum.append(P["Bushing_R"])
    od["idler"] = insert([P["IdlerRing"]], X, cum)
    for n, d in (("A", Y), ("B", -Y)):
        od["pinion_" + n] = insert([P["Pinion" + n]], d, [P["PinionShaft" + n]])
    fixed_b = [P[n] for n in names if n not in ("CaseTop", "CaseBottom") and not n.startswith("Sleeve")]
    for k, d in ((1, -X), (2, X), (3, Y), (4, -Y)):
        od["sleeve_%d" % k] = insert([P["Sleeve_%d" % k]], d, fixed_b)
    rep["order"] = od
    pl = build_plug()
    spin = [P[n] for n in names if n not in ("CaseTop", "CaseBottom", "PinionB", "PinionShaftB", "Sleeve_4")]
    zs = 0.0
    for k in range(int(60 / 0.5) + 1):
        t = pl.copy()
        t.translate(V(0, 0, 0.5 * k - 60))
        zs = max(zs, vol(t, P["CaseTop"]), *(vol(t, b) for b in spin))
    rep["plug"] = dict(vol=round(pl.Volume, 1), case=round(min(dist(pl, cs[c]) for c in cs), 3), spin=round(min(dist(pl, b) for b in spin), 3), overlap=round(max(vol(pl, b) for b in spin + list(cs.values())), 4),
                       play=travel(pl, V(0, 1, 0), list(cs.values()), 1.0), zsweep=round(zs, 4), out=round(-bb(pl).YMin - YC, 3), inner=round(-bb(pl).YMax, 3))
    S = {"NO_RUN": True, "__name__": "drive_shaft"}
    exec(compile(open("/home/mikhail/Documents/cad/RC Car/drive_shaft.py").read(), "drive_shaft.py", "exec"), S)
    yk0, yokes = S["build_yoke"](), []
    sock = S["XB"] - bb(yk0).XMin
    off = PORT_LEN - sock
    for roll in (0, 90):
        yk = rot(yk0, V(1, 0, 0), roll)
        for a, tgt in ((0, XR + off), (180, XL - off), (90, YC + off), (-90, -YC - off)):
            y = rot(yk, V(0, 0, 1), a)
            b = bb(y)
            lead = {0: b.XMin, 180: b.XMax, 90: b.YMin, -90: b.YMax}[a]
            y.translate(V(tgt - lead, 0, 0) if a in (0, 180) else V(0, tgt - lead, 0))
            yokes.append(y)
    fixed = list(P.values()) + yokes
    bolts = [build_bolt(x, y) for x, y in ear_pos()]
    sw, gap = 0.0, 99.0
    for bolt, drv in bolts:
        full = bolt.fuse(drv)
        gap = min(gap, min(dist(full, o) for o in fixed if o is not top))
        for k in range(int(70 / 0.5) + 1):
            t = full.copy()
            t.translate(V(0, 0, 0.5 * k - 70))
            sw = max(sw, *(vol(t, o) for o in fixed))
    rep["ears"] = dict(holes=[(round(x, 2), round(y, 2)) for x, y in ear_pos()], sweep=round(sw, 4), gap=round(gap, 3), yoke_face=round(min(dist(top, y) for y in yokes), 3),
                       wall=ear_wall(top), yoke_off=round(off, 3), size=(round(bb(top).XLength, 2), round(bb(top).YLength, 2)), top_vol=round(top.Volume, 1))
    rep["print"] = print_reports(dict(P, OutputPlug=pl))
    rep["plastic_cm3"] = round(sum(s.Volume for s in P.values()) / 1000, 1)
    rep["volumes"] = {n: round(s.Volume, 1) for n, s in P.items()}
    rep["volumes"]["OutputPlug"] = round(pl.Volume, 1)
    return rep


def check(rep):
    assert RING_N * PINION_R == PINION_N * RING_R and abs(RING_N / PINION_N - 36 / 22) < 1e-9
    assert not rep["overlap"], rep["overlap"]
    m = rep["mesh"]
    assert m["dirs"]["Carrier"] == -m["dirs"]["IdlerRing"], m["dirs"]
    for k, res in m["gaps"].items():
        assert all(v < 1e-3 and 0.15 <= g <= 0.5 for v, g in res), (k, res)
    assert not any(rep["assembly"].values()) and KEY_W <= 3.5 and rep["top_wall"] >= 1.2, (rep["assembly"], rep["top_wall"])
    assert rep["idler_heads"] >= 0.65 and BR_X1 - XC - HEAD_H >= 0.4 and rep["heads_case"] >= 0.55 and HOUSE_R - math.hypot(BOSS_Y, BOSS_Z) - CLEAR_D / 2 >= 1.15 and HOUSE_R - math.hypot(BOSS_Y, BOSS_Z) - PILOT_D / 2 >= 1.2 and all(v >= 0.3 for v in rep["idler_clear"].values()), rep
    assert min((SPIDER_BORE - PIN_D) / 2, (PIN_BORE_D - SHAFT_AF * 2 / math.sqrt(3)) / 2) >= 0.25 - 1e-9
    assert min((BORE_D - BUSH_OD) / 2, IDL_BORE_R - BUSH_OD / 2, IDL_COLLAR_IN - BUSH_FL_R) >= 0.3 - 1e-9 and LIP_BORE / 2 - SHAFT_AF / math.sqrt(3) >= 0.8 and LINER_ID / 2 - SHAFT_AF / math.sqrt(3) >= 0.3 and (LINER_BORE - LINER_OD) / 2 >= 0.1 - 1e-9 and BUSH_OD / 2 - GRV_D - LIP_BORE / 2 >= 1.2 - 1e-9 and GRV_LEAD - SLOPE * RIB_CLR >= 0.5 - 1e-9 and END_GAP >= RIB_OFF and CEN - MOUTH / 2 >= GRV_OFF
    assert IDL_RECESS_R - HOUSE_R >= 0.6 and DRUM_CAV_R - HOUSE_R >= 0.55 and rep["idler_clear"]["Cap"] >= 0.6 and rep["sg_carrier"] >= 0.7, rep
    assert all(v >= (IDLER_FLOAT - 1e-3 if n == "IdlerRing" else 0.4) for (c, n), v in rep["case_clear"].items()), rep["case_clear"]
    fl = lambda v: 0.3 - 1e-3 <= sum(v) <= 0.5
    assert fl(rep["carrier_float"]) and fl(rep["idler_float"]) and all(fl(v) for v in rep["pinion_float"].values()) and all(fl(v) for v in rep["pinion_shaft_float"].values()), rep
    assert all(0.3 - 1e-3 <= v["total"] <= 0.6 for v in rep["half_float"].values()), rep["half_float"]
    for k, l in rep["liner"].items():
        assert abs(l["od"] - LINER_OD) < 1e-3 and abs(l["length"] - LINER_L) < 1e-3 and 8.0 <= LINER_L <= 10.0 and abs(l["vol"] - math.pi * (LINER_OD ** 2 - LINER_ID ** 2) / 4 * LINER_L) < 0.2, l
        assert 0.2 - 1e-3 <= sum(l["play"]) <= 0.4 and l["hex"] >= 0.3 and l["pocket"] >= 0.1 - 1e-3 and l["wall"] >= 2.0 and len(l["lips"]) == 2 and min(l["lips"]) >= LIP_T, (k, l)
    assert rep["lead"] < 1e-3 and rep["rib_lead"] < 1e-3 and RIB_OFF <= GRV_LEAD - SLOPE * RIB_CLR and LEAD_OFF <= LINER_PLAY / 2 + LIP_LEAD and LIP_LEAD >= 0.5, rep["lead"]
    assert 0 <= rep["split_gap"] <= 0.1, rep["split_gap"]
    assert all(0 <= v <= 0.2 for v in rep["tail_clear"].values()) and all(sum(v) < 5e-3 for v in rep["bushing_play"].values()), (rep["tail_clear"], rep["bushing_play"])
    assert rep["pilot_wall"] >= 2.0 and rep["pass_hole"] >= 3.6 and EAR_HOLE_D >= 3.6 and rep["heads_free"] < 1e-3 and rep["bores_closed"], rep
    g = rep["glue"]
    assert g["zmax"] == CASE_Z and g["body"][0] <= XR - XL + 0.01 and g["body"][1] <= 2 * YC + 0.01 and g["overall"][0] <= 2 * (XR + EAR_DX + EAR_R) + 0.01 and g["overall"][1] <= 2 * YC + 0.01, g
    assert all(p["stick"] == PORT_LEN and p["hole_open"] and abs(p["af"] - SHAFT_AF) < 1e-3 and abs(p["corners"] - SHAFT_AF * 2 / math.sqrt(3)) < 1e-3 for p in rep["ports"].values()), rep["ports"]
    assert all(v < 1e-3 for v in rep["slide"].values()), rep["slide"]
    for n, sm in rep["side_mesh"].items():
        assert sm["nominal"] >= 0.15 and sm["nominal_push"] == 0.0 and sm["push"] <= rep["half_float"][n]["gear_out"] + 1e-6 and sm["gap"] >= 0.0 and sm["overlap"] < 1e-3, (n, sm)
    od = rep["order"]
    assert all(v < 1e-3 for k, v in od.items() if k != "spiders_with_R") and od["spiders_with_R"] > 1e-3, od
    ea = rep["ears"]
    assert ea["sweep"] < 1e-3 and ea["gap"] >= 2.0 and ea["wall"] >= 3.0 and ea["yoke_face"] >= ea["yoke_off"] - 0.1, ea
    pg = rep["plug"]
    assert pg["case"] >= LINER_PLAY / 2 - 1e-3 and pg["spin"] >= 0.8 and pg["overlap"] < 1e-3 and pg["zsweep"] < 1e-3 and 0.2 <= sum(pg["play"]) <= 0.4, pg
    for n, r in rep["print"].items():
        ex = [EXEMPT[m] for m in [n] + r["twins"] if m in EXEMPT]
        ex = ex[0] if ex else ()
        assert "P1" in ex or r["tilt"][0] >= TILT_MIN - 0.01, (n, "P1 P4", r["tilt"])
        assert "P5" in ex and max([o for _, o, _ in r["bad"]] + [0]) <= ex[ex.index("P5") + 1] or not r["bad"], (n, "P2 P3 P5", r["bad"])
        assert "P6" in ex or (r["floor"] >= 60.0 and r["wall"] >= 0.8 and r["height"] <= 4 * r["bed_min"]), (n, "P6", r["floor"], r["wall"], r["bed_min"], r["height"])
        assert all(sp <= BRIDGE_MAX for _, sp, _, _ in r["bridges"]), (n, r["bridges"])


def main():
    old = App.listDocuments().get(DOC_NAME)
    if old:
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    P = build_parts(doc)
    plug = build_plug()
    assert plug.isValid() and len(plug.Solids) == 1
    for name, shp in P.items():
        assert shp.isValid() and len(shp.Solids) == 1, name
        o = doc.addObject("Part::Feature", name)
        o.Shape = shp
        if App.GuiUp:
            o.ViewObject.ShapeColor = COLORS[name]
    o = doc.addObject("Part::Feature", "OutputPlug")
    o.Shape = plug.translated(V(0, -40, 0))
    if App.GuiUp:
        o.ViewObject.ShapeColor = COLORS["OutputPlug"]
    rep = verify(P)
    print("report", rep, flush=True)
    check(rep)
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
