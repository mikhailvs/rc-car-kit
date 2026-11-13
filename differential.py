# Axle module, no motor: closed bevel differential in a two-piece clamshell case (CaseTop glue face z 29 hangs under the floor, all shaft axes 29 mm below it). Ratio 36:22 (1.64), input pinion A at +y, output B at -y.
# Both pinions sit between the 36T carrier ring and a free-spinning 36T IdlerRing that turns opposite, so tooth side loads cancel. Every shaft leaves the case as a 16 mm hex port with a dia 2.8 cross pilot for universal joint yokes.
# Chaining: the output pinion turns opposite to the input, so mount the next axle in a chain turned 180 degrees about Z. Hardware: 4 x M3x16 pan head (dia 6 x 3.2) from below, 25 mm deep wells: use a long driver.
# Assembly (verify() sweeps it every 0.1 mm near the end): build ONE bundle (diff with bushings and IdlerRing, both Pinions on their PinionShafts pushed inward along Y into mesh), lower it straight along Z into CaseTop (glue face down tray), set CaseBottom on, 4 screws.
# Ports (the 16 mm stick-out) reference the bushing tail ends and the case y faces; the glue face is under 62.5 x 86.5 mm. Seat each universal joint yoke about 1 mm off the case face: the case is stationary and a yoke on a port touching it would rub.
# Phases drawn: ring 0, iring 0, pinion 0; the bundle never moves relative to itself, so the mesh cannot block it. Lowest point 30.6 mm below the axle axis: wheels need radius over 31.
import FreeCAD as App, Part, math
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
SHAFT_AF, SHAFT_X0 = 8.0, 2.9
FLANGE_D, FLANGE_X1 = 12.0, 5.1
SHAFT_HOLE_D, SHAFT_HOLE_X = 2.8, 67.0
JOURNAL_D, BORE_BUSH, PORT_LEN, PORT_HOLE = 9.3, 9.9, 16.0, 5.9
PS_FLANGE_T, PS_FL_IN, HEAD_AF, POCKET_AF, PIN_BORE_D = 2.2, 0.2, 11.0, 11.4, 9.8
PS_CB_DEEP = PS_FL_IN + PS_FLANGE_T
WH_FD, WH_FT, WH_BD, WH_X0, WH_X1 = 44.0, 3.0, 16.0, 58.0, 73.0
WH_SOCKET, WH_GLUE_D, WH_GLUE_R = 8.2, 4.0, 15.0
WH_SCREW_NEAR, WH_SCREW_FAR = 3.4, 2.8

HS_EXT = 0.0
RING_DX, CARRIER_FLOAT, IDLER_FLOAT, PIN_FLOAT, RING_TRIM_R = 0.03, 0.28, 0.28, 0.2, 26.8
BUSH_OD, BUSH_J, BUSH_FL_R, BUSH_FT_L, BUSH_FT_R = 14.0, 5.0, 8.2, 3.5, 3.7
IDL_BORE_R, IDL_COLLAR_R, IDL_COLLAR_IN, IDL_COLLAR_X0, IDL_RECESS_R = 7.3, 10.0, 8.5, 16.9, 19.62
IDL_HEAD_R, IDL_TOE_X = 19.9, 14.0
SADDLE_R, WALL_T = 7.1, 5.0
GROOVE_W, GROOVE_M, GROOVE_R, RIB_R = 2.4, 1.3, 6.15, 6.25
PS_GROOVE_R, PS_RIB_R, PS_RIB_SIDE = 3.8, 4.1, 0.15
PIN_BORE_R, PIN_BORE_LEN, HUB_EXT, SHELL_T = BORE_BUSH / 2, 12.4, 3.6, 2.4
CAV_M, DRUM_CAV_R, CAV_JOIN = 0.8, HOUSE_R + 0.62, 12.4
POCKET_R, WALL_CLR = 10.6, 0.4
CASE_Z, SPLIT_GAP, FILLET_R, CHAMFER_TOP, CHAMFER_BOT = 29.0, 0.05, 3.0, 1.0, 1.5
SCREW_X, SCREW_Y, SEAT_Z, PILOT_LEN, WELL_R, HOLE_R = (-24.8, 23.2), 37.5, -6.0, 11.0, 3.3, 1.7
KEY_W, KEY_D = 3.0, 0.6
KEY_X, KEY_Y = (-24.0, -8.0, 8.0, 24.0), (-36.0, -14.0, 14.0, 36.0)

RING_BACK = RING["back"] + RING_DX
BL_X1 = -RING_BACK - CARRIER_FLOAT
BL_X0 = BL_X1 - BUSH_FT_L
XC = FACE_IN + CAP_T
BR_X1 = XC + BUSH_FT_R
TL = BL_X0 - 0.1
XL = TL - WALL_T
TR = RING_BACK + HUB_EXT + IDLER_FLOAT
XR = TR + WALL_T
YT = PINION["back"]
YC = YT + PIN_BORE_LEN
PS_GROOVE_Y = YT + 1.0
HB = 30.6

PH = dict(spider=15.0, sideL=0.0, ring=0.0, pinion=0.0, iring=0.0)

COLORS = dict(Carrier=(0.2, 0.5, 0.9), Cap=(0.9, 0.5, 0.1), Bushing_L=(0.9, 0.9, 0.2), Bushing_R=(0.9, 0.9, 0.2),
              SideGear_L=(0.8, 0.2, 0.2), SideGear_R=(0.8, 0.2, 0.2), SpiderGear_1=(0.2, 0.8, 0.3), SpiderGear_2=(0.2, 0.8, 0.3),
              SpiderPin=(0.6, 0.6, 0.6), HalfShaft_L=(0.7, 0.3, 0.8), HalfShaft_R=(0.7, 0.3, 0.8), PinionA=(0.1, 0.8, 0.8),
              PinionB=(0.1, 0.8, 0.8), PinionShaftA=(0.7, 0.3, 0.8), PinionShaftB=(0.7, 0.3, 0.8), IdlerRing=(0.9, 0.4, 0.6),
              CaseTop=(0.5, 0.5, 0.55), CaseBottom=(0.4, 0.4, 0.45))
PRINT_UP = dict(Carrier="+X", Cap="-X", Bushing_L="+X", Bushing_R="+X", SideGear_L="+X", SideGear_R="-X", SpiderGear_1="+Y",
                SpiderGear_2="-Y", SpiderPin="-Z", HalfShaft_L="+Z", HalfShaft_R="+Z", PinionA="+Y", PinionB="-Y",
                PinionShaftA="+Z", PinionShaftB="+Z", IdlerRing="-X", CaseTop="-Z", CaseBottom="+Z")


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


def grooves(t0, sg):
    return t0 + sg * GROOVE_M, t0 + sg * (GROOVE_M + GROOVE_W)


def build_bushing(side):
    r, f, rb = BUSH_OD / 2, BUSH_FL_R, BORE_BUSH / 2
    if side < 0:
        g0, g1 = sorted(grooves(TL, -1))
        pts = [(XL, 0), (XL, r), (g0, r), (g0, GROOVE_R), (g1, GROOVE_R), (g1, r), (BL_X0, r), (BL_X0 + f - r, f),
               (BL_X1, f), (BL_X1, r), (BL_X1 + BUSH_J, r), (BL_X1 + BUSH_J, 0)]
    else:
        g0, g1 = grooves(TR, 1)
        pts = [(XC - BUSH_J, 0), (XC - BUSH_J, r), (XC, r), (XC, f), (BR_X1, f), (BR_X1, r), (g0, r), (g0, GROOVE_R),
               (g1, GROOVE_R), (g1, r), (XR, r), (XR, 0)]
    return rev(pts).cut(cyl(rb, XL - 1, XR + 1)).removeSplitter()


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
    tip = ref + PORT_LEN + HS_EXT
    s = hexprism(SHAFT_AF, SHAFT_X0, SIDE["back"]).fuse(cyl(FLANGE_D / 2, SHAFT_X0, FLANGE_X1))
    s = s.fuse(cyl(JOURNAL_D / 2, SIDE["back"], ref)).fuse(hexprism(SHAFT_AF, ref, tip))
    s = port_cut(s, SHAFT_X0, tip).cut(Part.makeCylinder(SHAFT_HOLE_D / 2, 20, V(tip - PORT_HOLE, 0, -10), V(0, 0, 1)))
    return (s if sign > 0 else mirror_x(s)).removeSplitter()


def build_pinion_shaft(front):
    y0, tip = front + PS_FL_IN, YC + PORT_LEN
    s = yhex(HEAD_AF, y0, y0 + PS_FLANGE_T).fuse(ycyl(JOURNAL_D / 2, y0, YC)).fuse(yhex(SHAFT_AF, YC, tip))
    s = s.cut(ycyl(JOURNAL_D / 2 + 1, PS_GROOVE_Y, PS_GROOVE_Y + GROOVE_W).cut(ycyl(PS_GROOVE_R, PS_GROOVE_Y - 1, PS_GROOVE_Y + GROOVE_W + 1)))
    s = port_cut(s, y0, tip, "y").cut(vcyl(SHAFT_HOLE_D / 2, 0, tip - PORT_HOLE, -10, 10))
    return s.removeSplitter()


def build_wheel_hub():
    h = cyl(WH_FD / 2, WH_X1 - WH_FT, WH_X1).fuse(cyl(WH_BD / 2, WH_X0, WH_X1 - WH_FT))
    h = h.cut(hexprism(WH_SOCKET, WH_X0 - 1, WH_X1 + 1))
    for k in range(6):
        a = math.radians(60 * k)
        h = h.cut(cyl(WH_GLUE_D / 2, WH_X1 - WH_FT - 1, WH_X1 + 1, WH_GLUE_R * math.cos(a), WH_GLUE_R * math.sin(a)))
    h = h.cut(Part.makeCylinder(WH_SCREW_NEAR / 2, 10, V(SHAFT_HOLE_X, 0, 0), V(0, 0, 1)))
    return h.cut(Part.makeCylinder(WH_SCREW_FAR / 2, 10, V(SHAFT_HOLE_X, 0, -10), V(0, 0, 1))).removeSplitter()


def case_cavity(sr, sp):
    m = CAV_M
    (af, rf), (ap, rp), (ab, rb) = sr
    x0, x1 = (v + 0.1 * k for v, k in zip(sorted(grooves(TL, -1)), (1, -1)))
    r0, r1 = (v + 0.1 * k for v, k in zip(grooves(TR, 1), (1, -1)))
    L = RING_DX
    xt = af + (RING_TRIM_R - rf) / (rp - rf) * (ap - af)
    x2 = ap + (rp - RING_TRIM_R) / (rp - rb) * (ab - ap)
    left = [(-CAV_JOIN, 0), (-CAV_JOIN, rf + m), (-(xt + L), RING_TRIM_R + m), (-(x2 + L), RING_TRIM_R + m), (-(ab + L) - WALL_CLR, rb + m), (-(ab + L) - WALL_CLR, 0)]
    right = [(CAV_JOIN, 0), (CAV_JOIN, rf + m), (xt + L, RING_TRIM_R + m), (x2 + L, RING_TRIM_R + m), (ab + L, rb + m), (TR, rb + m), (TR, 0)]
    saddle_l = [(XL - 1, 0), (XL - 1, SADDLE_R), (x0, SADDLE_R), (x0, RIB_R), (x1, RIB_R), (x1, SADDLE_R), (TL + 1, SADDLE_R), (TL + 1, 0)]
    saddle_r = [(TR - 1, 0), (TR - 1, SADDLE_R), (r0, SADDLE_R), (r0, RIB_R), (r1, RIB_R), (r1, SADDLE_R), (XR + 1, SADDLE_R), (XR + 1, 0)]
    xs = [rev(left), rev(right), rev(saddle_l), rev(saddle_r),
          rev([(TL, 0), (TL, POCKET_R), (-(ab + L) - WALL_CLR, POCKET_R), (-(ab + L) - WALL_CLR, 0)]),
          rev([(-CAV_JOIN, 0), (-CAV_JOIN, DRUM_CAV_R), (CAV_JOIN, DRUM_CAV_R), (CAV_JOIN, 0)])]
    (yf, rpf), (yp, rpp), (yb, rpb) = sp
    pin = [(0, yf - 0.2), (rpf + m, yf - 0.2), (rpp + m, yp), (rpb + m, yb), (rpb + m, yb + PIN_FLOAT), (0, yb + PIN_FLOAT)]
    g0 = PS_GROOVE_Y
    bore = [(0, yb), (PIN_BORE_R, yb), (PIN_BORE_R, g0 + PS_RIB_SIDE), (PS_RIB_R, g0 + PS_RIB_SIDE), (PS_RIB_R, g0 + GROOVE_W - PS_RIB_SIDE), (PIN_BORE_R, g0 + GROOVE_W - PS_RIB_SIDE), (PIN_BORE_R, YC + 1), (0, YC + 1)]
    ya = rev(pin, "y").fuse(rev(bore, "y"))
    return xs, [ya, rot(ya, V(0, 0, 1), 180)]


def outer_block(z0, z1):
    b = box(XL, XR, -YC, YC, z0, z1)
    return b.makeFillet(FILLET_R, [e for e in b.Edges if abs(e.Vertexes[0].Z - e.Vertexes[1].Z) > 1e-6])


def shell(cav, ys, h, boss_r):
    n = 12
    w = (XR - XL) / n
    R = [bb(cav.common(box(XL + i * w, XL + (i + 1) * w, -40, 40, -40, 40))).ZMax + SHELL_T for i in range(n)]
    R = [max(R[max(i - 1, 0):i + 2]) for i in range(n)]
    k, top = SHELL_T * math.sqrt(2), h - SHELL_T

    def ext(q, ax, a, b):
        pts = [V(a, u, v) for u, v in q] if ax == "x" else [V(u, a, v) for u, v in q]
        return prism(pts, V(b - a, 0, 0) if ax == "x" else V(0, b - a, 0))

    def wedge(r, ax, a, b, a2, b2):
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
    arm = [wedge(rp, "y", 0, YT + SHELL_T, 0, YT), wedge(PIN_BORE_R + SHELL_T, "y", YT, YC, YT + SHELL_T, YC - SHELL_T)]
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
            bot = bot.cut(vcyl(HOLE_R, sx, sy, SEAT_Z - 1, 1)).cut(vcyl(WELL_R, sx, sy, -HB - 1, SEAT_Z))
    keys = [box(x - KEY_W / 2, x + KEY_W / 2, y0, y1, CASE_Z - KEY_D, CASE_Z + 1) for x in KEY_X for y0, y1 in ((-YC - 1, -29.0), (29.0, YC + 1))]
    keys += [box(XL - 1, XR + 1, y - KEY_W / 2, y + KEY_W / 2, CASE_Z - KEY_D, CASE_Z + 1) for y in KEY_Y]
    top = top.cut(keys[0].fuse(keys[1:]).removeSplitter())
    for c in cut_all:
        top, bot = top.cut(c), bot.cut(c)
    return max(top.removeSplitter().Solids, key=lambda x: x.Volume), bot.removeSplitter()


def build_parts(doc, ph=PH):
    gR, gL, s1, s2 = build_gears(doc, ph)
    rb, pb = bevel_body(doc, RING, 0.0), bevel_body(doc, PINION, ph["pinion"])
    pin = build_pinion(pb)
    top, bot = build_case(silhouette(rb, RING), silhouette(pb, PINION))
    return dict(Carrier=build_carrier(ring_x(rb, ph["ring"], -1)), Cap=build_cap(), Bushing_L=build_bushing(-1), Bushing_R=build_bushing(1),
                SideGear_L=gL, SideGear_R=gR, SpiderGear_1=s1, SpiderGear_2=s2, SpiderPin=build_pin(),
                HalfShaft_L=build_half_shaft(-1), HalfShaft_R=build_half_shaft(1), PinionA=pin, PinionB=rot(pin, V(1, 0, 0), 180),
                PinionShaftA=build_pinion_shaft(PINION["front"]), PinionShaftB=rot(build_pinion_shaft(PINION["front"]), V(0, 0, 1), 180),
                IdlerRing=build_idler(rb), CaseTop=top, CaseBottom=bot)


def bb(s):
    return s.optimalBoundingBox(False, False)


def vol(a, b):
    return a.common(b).Volume if a.BoundBox.intersect(b.BoundBox) else 0.0


def dist(a, b):
    return max(a.distToShape(b)[0] for _ in range(2))


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


def assembly(P):
    bundle = [n for n in P if n not in ("CaseTop", "CaseBottom")]
    out = dict(lower=0.0, close=0.0)
    for dz in [-30, -12, -4] + [round(-3 + 0.1 * i, 1) for i in range(31)]:
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


def print_report(name, s):
    t = oriented(s, name)
    floor = sum(f.Area for f in t.Faces if f.BoundBox.ZMax < 1e-4 and isinstance(f.Surface, Part.Plane))
    bad = []
    for f in t.Faces:
        u0, u1, v0, v1 = f.ParameterRange
        hit = [1 for i in range(6) for j in range(6) if f.isPartOfDomain(u0 + (u1 - u0) * (i + .5) / 6, v0 + (v1 - v0) * (j + .5) / 6)
               and f.valueAt(u0 + (u1 - u0) * (i + .5) / 6, v0 + (v1 - v0) * (j + .5) / 6).z > 0.8
               and f.normalAt(u0 + (u1 - u0) * (i + .5) / 6, v0 + (v1 - v0) * (j + .5) / 6).z < -0.7072]
        if not hit:
            continue
        k = f.Surface
        if getattr(k, "Radius", 99) <= 3.5 or 2 * f.Area / f.Length <= 3.5:
            continue
        bad.append((type(k).__name__, round(f.Area, 1), round(f.CenterOfMass.z, 1)))
    return round(floor, 1), bad


def port(sh, ref, ax, sg):
    b = bb(sh)
    tip = (b.XMax if sg > 0 else b.XMin) if ax == "x" else (b.YMax if sg > 0 else b.YMin)
    u = V(1, 0, 0) if ax == "x" else V(0, 1, 0)
    probe = lambda off: sh.isInside(u * (tip - sg * PORT_HOLE + off), 1e-6, True)
    z = box(tip - sg * PORT_LEN, tip, -9, 9, -9, 9) if ax == "x" else box(-9, 9, tip - sg * PORT_LEN, tip, -9, 9)
    c = bb(sh.common(z))
    return dict(stick=round(abs(tip - ref), 3), hole_open=not probe(0) and not probe(1.3) and not probe(-1.3) and probe(1.5) and probe(-1.5),
                af=round(c.ZLength, 3), corners=round(c.YLength if ax == "x" else c.XLength, 3))


def verify(P):
    names = list(P)
    rep = {}
    rep["bbox"] = {n: tuple(round(v, 2) for v in (bb(s).XLength, bb(s).YLength, bb(s).ZLength)) for n, s in P.items()}
    rep["overlap"] = {(a, b): round(vol(P[a], P[b]), 4) for i, a in enumerate(names) for b in names[i + 1:] if vol(P[a], P[b]) > 1e-3}
    rep["carrier_float"] = travel(Part.makeCompound([P["Carrier"], P["Cap"]]), V(1, 0, 0), [P["Bushing_L"], P["Bushing_R"]])
    rep["idler_float"] = travel(P["IdlerRing"], V(1, 0, 0), [P["Bushing_R"], P["CaseTop"], P["CaseBottom"], P["Cap"]])
    rep["pinion_float"] = {n: travel(P["Pinion" + n], V(0, 1, 0), [P["PinionShaft" + n], P["CaseTop"], P["CaseBottom"]]) for n in "AB"}
    rng = dict(Carrier=rep["carrier_float"], IdlerRing=rep["idler_float"], PinionA=rep["pinion_float"]["A"], PinionB=rep["pinion_float"]["B"])
    rep["mesh"] = mesh_run(P, {k: (-v[1], v[0]) for k, v in rng.items()})
    rep["assembly"] = assembly(P)
    heads = [Part.makeCylinder(HEAD_D / 2, HEAD_H, V(XC, sy * BOSS_Y, sz * BOSS_Z), V(1, 0, 0)) for sy in (1, -1) for sz in (1, -1)]
    rep["idler_heads"] = round(min(dist(P["IdlerRing"].common(box(-99, XC + HEAD_H, -99, 99, -99, 99)), h) for h in heads), 3)
    rep["sg_carrier"] = round(min(dist(P["Carrier"].common(box(-FACE_IN + 0.1, FACE_IN - 0.1, -99, 99, -99, 99)), P["SideGear_" + n]) for n in "LR"), 3)
    rep["idler_clear"] = {n: round(dist(P["IdlerRing"], P[n].common(box(-99, XC - 1, -99, 99, -99, 99)) if n == "Cap" else P[n]), 3) for n in ("Carrier", "Cap")}
    cs = dict(CaseTop=P["CaseTop"], CaseBottom=P["CaseBottom"])
    rep["heads_case"] = round(min(dist(c, h) for c in cs.values() for h in heads), 3)
    rep["case_clear"] = {(c, n): round(dist(cs[c], P[n].common(box(-99, TR - 1, -99, 99, -99, 99)) if n == "IdlerRing" else P[n]), 3) for c in cs for n in ("Carrier", "Cap", "IdlerRing", "SideGear_L", "SideGear_R", "SpiderGear_1", "SpiderGear_2")}
    rep["pinion_case"] = {(c, n): round(dist(cs[c], P[n]), 3) for c in cs for n in ("PinionA", "PinionB")}
    rep["shaft_play"] = {n: travel(P["PinionShaft" + n], V(0, 1, 0), [P["CaseTop"], P["CaseBottom"]], 0.5) for n in "AB"}
    rep["bushing_play"] = {n: travel(P["Bushing_" + n], V(1, 0, 0), [P["CaseTop"], P["CaseBottom"]], 0.5) for n in "LR"}
    rep["split_gap"] = round(dist(P["CaseTop"], P["CaseBottom"]), 3)
    rep["tail_clear"] = {(n, c): round(dist(P["Bushing_" + n], cs[c]), 3) for n in "LR" for c in cs}
    pil = vcyl(PILOT_D / 2, SCREW_X[0], SCREW_Y, 0, PILOT_LEN)
    others = [f for f in P["CaseTop"].Faces if not (f.BoundBox.XMax - f.BoundBox.XMin < 3.0 and f.BoundBox.YMax - f.BoundBox.YMin < 3.0 and abs(f.BoundBox.XMin - SCREW_X[0]) < 1.6) and f.BoundBox.ZMax > 1e-6]
    rep["pilot_wall"] = round(min(dist(f, pil) for f in others if f.BoundBox.ZMin < PILOT_LEN + 1), 3)
    col = [vcyl(WELL_R - 0.05, sx, sy, -HB - 1, SEAT_Z - HEAD_H) for sx in SCREW_X for sy in (SCREW_Y, -SCREW_Y)]
    hd = [vcyl(HEAD_D / 2, sx, sy, SEAT_Z - HEAD_H, SEAT_Z) for sx in SCREW_X for sy in (SCREW_Y, -SCREW_Y)]
    rep["heads_free"] = max(vol(c, P[n]) for c in col + hd for n in names)
    top = P["CaseTop"]
    glue = [f for f in top.Faces if isinstance(f.Surface, Part.Plane) and abs(f.BoundBox.ZMin - CASE_Z) < 1e-6 and abs(f.BoundBox.ZMax - CASE_Z) < 1e-6]
    gb = bb(Part.makeCompound(glue))
    rep["glue"] = dict(x=round(gb.XLength, 2), y=round(gb.YLength, 2), area=round(sum(f.Area for f in glue), 1), zmax=round(bb(top).ZMax, 3))
    cb = bb(Part.makeCompound([top, P["CaseBottom"]]))
    rep["case_size"] = (round(cb.XLength, 2), round(cb.YLength, 2), round(cb.ZLength, 2))
    rep["ground"] = round(-bb(P["CaseBottom"]).ZMin, 3)
    rep["top_wall"] = round(CASE_Z - bb(P["Carrier"]).ZMax - CAV_M, 3)
    circ = []
    for ax, pos, r in [("x", (XL + min(grooves(TL, -1))) / 2, SADDLE_R), ("x", (TR + XR) / 2 - 1.5, SADDLE_R), ("x", sum(grooves(TL, -1)) / 2, RIB_R), ("x", sum(grooves(TR, 1)) / 2, RIB_R)] + [("y", sg * y, PIN_BORE_R) for sg in (1, -1) for y in (YT + 0.4, YC - 1)]:
        for k in range(24):
            a = math.radians(7.5 * k + 3.75)
            d = lambda rr: V(pos, rr * math.cos(a), rr * math.sin(a)) if ax == "x" else V(rr * math.cos(a), pos, rr * math.sin(a))
            inside = lambda p: top.isInside(p, 1e-6, True) or P["CaseBottom"].isInside(p, 1e-6, True)
            circ.append(inside(d(r + 0.05)) and not inside(d(r - 0.05)))
    rep["bores_closed"] = all(circ)
    rep["ports"] = dict(HalfShaft_L=port(P["HalfShaft_L"], bb(P["Bushing_L"]).XMin, "x", -1), HalfShaft_R=port(P["HalfShaft_R"], bb(P["Bushing_R"]).XMax, "x", 1),
                        PinionShaftA=port(P["PinionShaftA"], bb(top).YMax, "y", 1), PinionShaftB=port(P["PinionShaftB"], bb(top).YMin, "y", -1))
    rep["print"] = {n: print_report(n, P[n]) for n in names}
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
    assert min((BORE_D - BUSH_OD) / 2, IDL_BORE_R - BUSH_OD / 2, IDL_COLLAR_IN - BUSH_FL_R, (BORE_BUSH - JOURNAL_D) / 2, (SPIDER_BORE - PIN_D) / 2, PS_RIB_R - PS_GROOVE_R) >= 0.25 - 1e-9
    assert IDL_RECESS_R - HOUSE_R >= 0.6 and DRUM_CAV_R - HOUSE_R >= 0.55 and rep["idler_clear"]["Cap"] >= 0.6 and rep["sg_carrier"] >= 0.7, rep
    assert all(v >= 0.4 for v in rep["case_clear"].values()), rep["case_clear"]
    assert 0.25 <= sum(rep["carrier_float"]) <= 0.35, rep["carrier_float"]
    assert 0.2 <= sum(rep["idler_float"]) <= 0.4, rep["idler_float"]
    assert all(0.2 <= sum(v) <= 0.5 for v in rep["pinion_float"].values()), rep["pinion_float"]
    assert 0 <= rep["split_gap"] <= 0.1, rep["split_gap"]
    assert all(0 < v <= 0.2 for v in rep["tail_clear"].values()), rep["tail_clear"]
    assert rep["pilot_wall"] >= 1.2 and rep["heads_free"] < 1e-3 and rep["bores_closed"], rep
    g = rep["glue"]
    assert g["zmax"] == CASE_Z and g["x"] <= 62.5 and g["y"] <= 86.5, g
    assert all(p["stick"] == PORT_LEN and p["hole_open"] and abs(p["af"] - SHAFT_AF) < 1e-3 and abs(p["corners"] - SHAFT_AF * 2 / math.sqrt(3)) < 1e-3 for p in rep["ports"].values()), rep["ports"]
    assert all(f >= 5.0 and not b for f, b in rep["print"].values()), {k: v for k, v in rep["print"].items() if v[0] < 5.0 or v[1]}


def main():
    old = App.listDocuments().get(DOC_NAME)
    if old:
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    P = build_parts(doc)
    for name, shp in P.items():
        assert shp.isValid() and len(shp.Solids) == 1, name
        o = doc.addObject("Part::Feature", name)
        o.Shape = shp
        if App.GuiUp:
            o.ViewObject.ShapeColor = COLORS[name]
    rep = verify(P)
    print("report", rep, flush=True)
    check(rep)
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
