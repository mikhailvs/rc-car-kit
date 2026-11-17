# Drive shaft: two double-hinge joints and a telescoping hex slide, replaces the wheel_mount.py DriveCoupler + ball-hex Stub; 4 x JointYoke, 2 x JointCross, SlideRod, SlideTube, every end clamps on a kit port.
# Hardware per shaft, 9 screws: per joint 2 x M3x20 (each through ear, cross block, ear; 12 mm thread in the block, head sunk 0.8 into the ear). Hinge: tighten only until the head seats, then back off a quarter turn; the ear gap is 0.25 per side, so driving further clamps the ear on the block (no geometric stop, M3x20 runs through the block), per yoke 1 x M3x12 port clamp screw, 1 x M3x4 stop screw in the tube wall.
# Pins: the two pin axes are 2 x AX = 4 mm apart along the shaft (no intersection), so the joint is a double hinge, not a true cardan: output axis runs out 1.0 to 1.07 mm sideways at 30 degrees. Joint centre is the block centre, 12.03 mm from the port tip.
# Assembly: 1 yoke over a cross, M3x20 in; 2 other yoke over the cross at 90 degrees, M3x20 in; 3 repeat; 4 yokes onto rod and tube ports, then rod into tube, M3x4 through the tube wall into the rod groove; 5 shaft onto the ports, M3x12 through each yoke and port pilot.
# Max angle: first contact 36.3 degrees at the worst phase (30 required, clear at 10/20/30/35 at every 15 degrees of phase). Stroke: joint centre to joint centre LC_LO to LC_HI, set by the stop screw in the rod groove, 15.5 mm of hex engaged at full extension, swing sphere radius 12.5 measured to the yoke ears (pin screw heads and tips 12.4, clamp screw heads 9.9 off the axis).
# Short variant: same 4 yokes and 2 crosses, SlideRod and SlideTube replaced by a rigid ShortLink (8 AF hex bar, 20.83 long, the wall beside the vertical pilot is 0.91 in the first and last 0.5 mm of height like SlideRod, 2.8 pilot 5.9 from each tip, M3x12 clamp at each end), so the two inner yoke mouths sit LINK_GAP 0.5 apart. Fixed LC 44.88 (joint centre to joint centre), overall yoke mouth to yoke mouth 89.27 (the 5.5 in long dimension is that overall length, 140.76 at LC_MIN, 141.26 at LC_LO); no stroke. Cannot go below this with unchanged yokes (inner yoke bodies meet); a telescope cannot get under about 124 overall. Print ShortLink on a hex flat (+Y up), 83.9 mm2 on the bed, 8 high, no overhangs; shown straight in Shown_*_S* and alone below.
# Shortest variant: DoubleFork, one printed piece replacing JointYoke_2, JointYoke_3 and the link; the 2 outer JointYokes and both JointCrosses are unchanged. A fork at each end (same ear, gap, pin hole and head counterbore as a JointYoke, M3x20 pins as before) with the pin axes parallel, which is how the long shaft already phases its inner yokes (both inner pins along Z, outer pins along Y). Web 2.4 long along X between the fork roots (section 18.5 x 8.8, narrowing to 14.4 at mid length where the swing cylinders meet; two 1.2 walls), so LC_D = 2 x (AX + SH) + DF_WEB = 18.4 joint centre to joint centre and 62.78 overall yoke mouth to mouth (long shaft 140.76 at LC_MIN), no stroke. The kinematic limit is the 36.3 degree joint first contact, unchanged from the yokes; a zero web (LC 16, 60.4 overall) still clears but would split the part, so the web wall sets the minimum. Max angle 36.3 per joint, whole shaft both bent clear at 30. Ear tips are a half octagon about each pin (flat plus two 45 degree chamfers tangent to R_TIP 4.4), leaving 1.4 round the dia 6 counterbores like a yoke, and the web and ears are trimmed to a swing radius of 12.5 about each joint centre (vertical cylinders), so it prints unsupported: lying with +Y up (ears vertical walls, pin holes horizontal), flat bottom 130.7 mm2, 8.8 high, no overhang beyond the horizontal pin holes. Display: Shown_*_D* straight shaft, DoubleFork alone below.
# Prints: yoke standing on its socket mouth (ears up), cross on its 12 x 12 face, rod on the flat opposite the groove (groove on top), tube standing port up. Document: the angled shaft (Shown_*) and the same shaft straight below it (print parts).
import FreeCAD as App, Part, math

D = {"NO_RUN": True, "__name__": "differential"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/differential.py").read(), "differential.py", "exec"), D)
V, O, cyl, box, hexprism, rot = (D[k] for k in ("V", "O", "cyl", "box", "hexprism", "rot"))
SHAFT_AF = D["SHAFT_AF"]

DOC_NAME = "DriveShaft"
OUT = "/home/mikhail/Documents/cad/RC Car/DriveShaft.FCStd"
X, Y, Z = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
R3 = math.sqrt(3)

SOCKET, BORE, PILOT, PS_OUT, PS_PILOT = 8.3, 8.4, 2.8, 16.0, 5.9
SOCK_D, BODY_R, SH, SPHERE_R = 10.0, 7.5, 6.0, 12.5
EAR_T, GAP, PIN_HOLE, EAR_W = 3.0, 12.5, 3.4, 4.4
CLAMP_HOLE, CB_D, CB_Z = 3.4, 6.0, 6.5
BLK_X, BLK, AX = 12.0, 12.0, 2.0
HEAD_CB, HEAD_CB_D, CROSS_CH = 0.8, 6.0, 1.3
STOP_W, STOP_D, STOP_S, STOP_L, SLACK = 3.4, 1.2, 8.0, 4.0, 0.5
CONE_TOP, ROOF_WALL = 2.0, 1.4
TUBE_R, ROD_L, TUBE_L, ENG_MIN, END_GAP = 7.0, 52.0, 44.0, 15.0, 0.3
SCREW_D, HEAD_D, HEAD_H = 3.0, 5.5, 3.0
A_LEN, C_LEN = 20.0, 12.0
OVERHANG_DEG = 45.0
TORQUE = 500.0
DISPLAY_DEG = 15.0
EXP_DY, EXP_DZ = 0.0, -60.0
SHORT_DZ = -120.0
DF_DZ = -180.0

RC_S, RC_B, HEX_R = SOCKET / R3, BORE / R3, SHAFT_AF / R3
CONE_H_S, CONE_H_B = RC_S - CONE_TOP, RC_B - CONE_TOP
EAR_OUT = GAP / 2 + EAR_T
FORK_R = math.sqrt(SPHERE_R ** 2 - (SH + AX) ** 2) - 0.01
CONE_H = FORK_R - BODY_R
XB = -(SH + CONE_H_S + ROOF_WALL)
TIP_D = -XB - (RC_S - HEX_R - 0.01)
XC = -(TIP_D + PS_PILOT)
X_CB = -(PS_OUT + ROOF_WALL + CONE_H_B)
X_STOP = X_CB + RC_B - HEX_R
YOKE_L = SOCK_D - XB
TIP_J = TIP_D + AX
TUBE_FULL = PS_OUT + TUBE_L
LC_MIN = max(2 * TIP_J + ROD_L - X_STOP + END_GAP, AX + YOKE_L + TIP_J + TUBE_FULL + 1.0)
LC_MAX = 2 * TIP_J + ROD_L + TUBE_FULL - ENG_MIN
LC_LO, LC_HI = LC_MIN + SLACK, LC_MAX - SLACK
LC_MID = (LC_LO + LC_HI) / 2
END_OUT = AX + YOKE_L
LINK_GAP = SLACK
LC_S = 2 * END_OUT + LINK_GAP
LINK_L = LC_S - 2 * TIP_J
DF_WEB, R_TIP = 2.4, 4.4
LC_D = 2 * (AX + SH) + DF_WEB
OA_D = LC_D + 2 * END_OUT
LAYER, MAX_STEP = 0.2, 0.3
XS_T = -TUBE_FULL + STOP_S


def stop_x(lc):
    return lc - 2 * TIP_J - TUBE_FULL + STOP_S


G0, G1 = stop_x(LC_LO) - SCREW_D / 2, stop_x(LC_HI) + SCREW_D / 2

PARTS_S = ("ShortLink", "DoubleFork")
PARTS = ("JointYoke_1", "JointYoke_2", "JointYoke_3", "JointYoke_4", "JointCross_1", "JointCross_2", "SlideRod", "SlideTube")
PRINT_UP = dict(JointYoke_1="+X", JointYoke_2="-X", JointYoke_3="+X", JointYoke_4="-X", JointCross_1="+X", JointCross_2="-X", SlideRod="+Y", SlideTube="+X", ShortLink="+Y", DoubleFork="+Y")
COLORS = dict(JointYoke=(0.9, 0.6, 0.2), JointCross=(0.2, 0.5, 0.9), SlideRod=(0.2, 0.7, 0.4), SlideTube=(0.7, 0.3, 0.8), ShortLink=(0.9, 0.8, 0.2), DoubleFork=(0.9, 0.4, 0.4), DummyPort=(0.7, 0.7, 0.72))


def mv(s, x=0.0, y=0.0, z=0.0):
    c = s.copy()
    c.translate(V(x, y, z))
    return c


def yc(r, y0, y1, x=0.0, z=0.0):
    return Part.makeCylinder(r, y1 - y0, V(x, y0, z), Y)


def rhex(af, x0, x1):
    return rot(hexprism(af, x0, x1), X, 90)


def roofed(rc, af, x0, xb, h, hexf):
    cav = hexf(af, x0, xb).fuse(hexf(af, xb - 0.01, xb + h + 0.01).common(Part.makeCone(rc, CONE_TOP, h, V(xb, 0, 0), X)))
    return cav.removeSplitter()


def build_yoke():
    mouth = XB - SOCK_D
    flare = Part.makeCone(BODY_R, FORK_R, CONE_H, V(-(SH + CONE_H), 0, 0), X).common(box(-SH - CONE_H - 1, -SH + 1, -15, 15, -EAR_W, EAR_W))
    body = cyl(BODY_R, mouth, -(SH + CONE_H)).fuse(flare)
    fork = Part.makeCylinder(0.01, 0.01)
    for s in (-1, 1):
        y0 = min(s * GAP / 2, s * EAR_OUT)
        ear = box(-SH, 0, y0, y0 + EAR_T, -EAR_W, EAR_W).fuse(yc(EAR_W, y0, y0 + EAR_T))
        fork = ear if s == -1 else fork.fuse(ear)
    y = body.fuse(fork.common(Part.makeSphere(SPHERE_R, V(AX, 0, 0)))).removeSplitter()
    y = y.cut(yc(PIN_HOLE / 2, -15, 15))
    for sg in (-1, 1):
        y = y.cut(yc(HEAD_CB_D / 2, *sorted((sg * (EAR_OUT - HEAD_CB), sg * (EAR_OUT + 1)))))
    y = y.cut(roofed(RC_S, SOCKET, mouth - 1, XB, CONE_H_S, hexprism))
    y = y.cut(Part.makeCylinder(CLAMP_HOLE / 2, 30, V(XC, 0, -15), Z))
    for z0 in (CB_Z, -CB_Z - 6):
        y = y.cut(Part.makeCylinder(CB_D / 2, 6, V(XC, 0, z0), Z))
    return y.removeSplitter()


def cross_blank():
    b = box(-BLK_X / 2, BLK_X / 2, -BLK / 2, BLK / 2, -BLK / 2, BLK / 2)
    return b.makeChamfer(CROSS_CH, [e for e in b.Edges if abs(e.BoundBox.XLength) < 1e-6 and abs(e.BoundBox.Center.x) > BLK_X / 2 - 1e-6])


def build_cross():
    b = cross_blank()
    return b.cut(yc(PILOT / 2, -10, 10, -AX)).cut(Part.makeCylinder(PILOT / 2, 20, V(AX, 0, -10), Z))


def build_rod():
    r = rhex(SHAFT_AF, 0, ROD_L).cut(yc(PILOT / 2, -10, 10, PS_PILOT))
    return r.cut(box(G0, G1, SHAFT_AF / 2 - STOP_D, SHAFT_AF / 2 + 1, -STOP_W / 2, STOP_W / 2)).removeSplitter()


def build_tube():
    xo = -TUBE_FULL
    t = cyl(TUBE_R, xo, -PS_OUT).fuse(rhex(SHAFT_AF, -PS_OUT, 0))
    t = t.cut(roofed(RC_B, BORE, xo - 1, X_CB, CONE_H_B, rhex))
    t = t.cut(yc(PILOT / 2, -10, 10, -PS_PILOT))
    return t.cut(Part.makeCylinder(PILOT / 2, 10, V(XS_T, 0, 0), Y)).removeSplitter()


def build_link():
    r = rhex(SHAFT_AF, 0, LINK_L)
    for x in (PS_PILOT, LINK_L - PS_PILOT):
        r = r.cut(yc(PILOT / 2, -10, 10, x))
    return r.removeSplitter()


def build_dfork():
    pa, pb = AX, LC_D - AX
    t = R_TIP * math.tan(math.pi / 8)
    x0, x1 = pa - R_TIP, pb + R_TIP
    s = box(x0, x1, -EAR_W, EAR_W, -EAR_OUT, EAR_OUT)
    s = s.cut(box(x0 - 1, pa + SH, -EAR_W - 1, EAR_W + 1, -GAP / 2, GAP / 2)).cut(box(pb - SH, x1 + 1, -EAR_W - 1, EAR_W + 1, -GAP / 2, GAP / 2))
    pts = [V(x0, t, -15), V(pa - t, R_TIP, -15), V(pb + t, R_TIP, -15), V(x1, t, -15), V(x1, -t, -15), V(pb + t, -R_TIP, -15), V(pa - t, -R_TIP, -15), V(x0, -t, -15)]
    s = s.common(Part.Face(Part.makePolygon(pts + pts[:1])).extrude(V(0, 0, 30)))
    rr = math.sqrt(SPHERE_R ** 2 - EAR_W ** 2)
    s = s.common(Part.makeCylinder(rr, 30, V(0, -15, 0), Y).fuse(Part.makeCylinder(rr, 30, V(LC_D, -15, 0), Y)))
    return s.cut(df_holes()).removeSplitter()


def df_holes():
    h = None
    for p in (AX, LC_D - AX):
        c = Part.makeCylinder(PIN_HOLE / 2, 30, V(p, 0, -15), Z)
        for sg in (-1, 1):
            z0 = sg * (EAR_OUT - HEAD_CB) if sg > 0 else -EAR_OUT - 1
            c = c.fuse(Part.makeCylinder(HEAD_CB_D / 2, EAR_OUT + 1 - (EAR_OUT - HEAD_CB), V(p, 0, z0), Z))
        h = c if h is None else h.fuse(c)
    return h.removeSplitter()


def port(tip_x, d):
    p = hexprism(SHAFT_AF, tip_x, tip_x + d * 30)
    return p.cut(Part.makeCylinder(PILOT / 2, 20, V(tip_x + d * PS_PILOT, 0, -10), Z))


def screw(p, d, length):
    return Part.makeCylinder(SCREW_D / 2, length, p, d).fuse(Part.makeCylinder(HEAD_D / 2, HEAD_H, p - d * HEAD_H, d))


def qxf(s):
    return rot(rot(s, Z, 180), X, 90)


def rp(s, base, axis, deg):
    s = s.copy()
    s.rotate(base, axis, deg)
    return s


def chain(lc, g=0.0, shift=(0.0, 0.0, 0.0), short=False):
    y1, cr = build_yoke(), build_cross()
    pb, gr, d = V(AX, 0, 0), math.radians(g), lc - 2 * AX
    sh = lambda s: mv(s, *shift)
    mid = lambda s: sh(rp(s, pb, Z, g))
    j2 = (2 * AX + d * math.cos(gr) + shift[0], d * math.sin(gr) + shift[1], shift[2])
    at2 = lambda s: mv(s, *j2)
    mids = {"ShortLink": mid(mv(build_link(), TIP_J))} if short else {"SlideRod": mid(mv(build_rod(), TIP_J)), "SlideTube": mid(mv(build_tube(), lc - TIP_J))}
    return {
        "JointYoke_1": sh(mv(y1, -AX)), "JointYoke_2": mid(mv(qxf(y1), AX)), "JointYoke_3": mid(mv(rot(y1, X, 90), lc - AX)),
        "JointYoke_4": at2(mv(rot(y1, Z, 180), AX)), "JointCross_1": sh(cr), "JointCross_2": at2(rot(cr, Z, 180)),
        **mids,
        "DummyPort_1": sh(port(-TIP_J, -1)), "DummyPort_2": at2(port(TIP_J, 1))}


def vol(a, b):
    return a.common(b).Volume if a.BoundBox.intersect(b.BoundBox) else 0.0


def joint_kit():
    P, Cr, Cp = build_yoke(), build_cross(), screw(V(XC, 0, CB_Z), -Z, C_LEN)
    return dict(P=mv(P, -AX), Cr=Cr, Q=mv(qxf(P), AX), A=screw(V(-AX, -(EAR_OUT - HEAD_CB), 0), Y, A_LEN),
                B=screw(V(AX, 0, EAR_OUT - HEAD_CB), -Z, A_LEN), Cp=mv(Cp, -AX), Cq=mv(qxf(Cp), AX))


def tilt_ab(th, ph):
    t, p = math.radians(th), math.radians(ph)
    return math.degrees(math.atan2(-math.sin(t) * math.sin(p), math.cos(t))), math.degrees(math.asin(math.sin(t) * math.cos(p)))


def posed(kit, th, ph):
    al, be = tilt_ab(th, ph)
    ta = lambda s: rp(s, V(-AX, 0, 0), Y, al)
    tq = lambda s: ta(rp(s, V(AX, 0, 0), Z, be))
    return dict(P=kit["P"], A=kit["A"], Cp=kit["Cp"], Cr=ta(kit["Cr"]), Q=tq(kit["Q"]), B=ta(kit["B"]), Cq=tq(kit["Cq"]))


THREADED = {("A", "Cr"), ("B", "Cr")}


def hits(pose):
    ks = list(pose)
    return [(a, b) for i, a in enumerate(ks) for b in ks[i + 1:] if (a, b) not in THREADED and (b, a) not in THREADED and vol(pose[a], pose[b]) > 1e-3]


def first_contact(kit, ph, top=60.0):
    a = 0.0
    while a <= top and not hits(posed(kit, a, ph)):
        a += 5.0
    if a > top:
        return top, []
    lo, hi = max(a - 5.0, 0.0), a
    for _ in range(6):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if hits(posed(kit, mid, ph)) else (mid, hi)
    return round(hi, 2), hits(posed(kit, hi, ph))


def articulation(kit):
    rep = {"table": {}, "first": {}}
    for ph in (0, 90, 45):
        for th in (10, 20, 30, 35):
            rep["table"][(ph, th)] = hits(posed(kit, th, ph))
    for ph in range(0, 360, 45):
        rep["first"][ph] = first_contact(kit, ph)
    rep["ring30"] = {ph: hits(posed(kit, 30, ph)) for ph in range(0, 360, 15)}
    return rep


def captured(kit):
    dirs = [V(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1) if (a, b, c) != (0, 0, 0)]
    out = {}
    for name, yk, partners in (("P", kit["P"], ("Cr", "A")), ("Q", kit["Q"], ("Cr", "B"))):
        free = []
        for d in dirs:
            d = V(d.x, d.y, d.z)
            d.normalize()
            m = mv(yk, d.x, d.y, d.z)
            if all(vol(m, kit[p]) < 1e-3 for p in partners):
                free.append((round(d.x, 2), round(d.y, 2), round(d.z, 2)))
        out[name] = free
    return out


def clamp(kit):
    p = mv(port(-TIP_D, -1), -AX)
    slide = {}
    for dx in (-0.5, 0.5):
        slide[dx] = round(vol(mv(kit["P"], dx), kit["Cp"]), 4)
    axis = [V(XC - AX, 0, z) for z in (-3.9, -2.0, 0.0, 2.0, 3.9)]
    return dict(thread_overlap=round(vol(p, kit["Cp"]), 3), axis_in_pilot=all(not p.isInside(a, 1e-6, True) for a in axis),
                pilot_x_error=round(abs(XC - AX - (-TIP_D - AX - PS_PILOT)), 4), yoke_vs_screw=round(vol(kit["P"], kit["Cp"]), 4),
                slide_pull_out=slide, port_vs_yoke=round(vol(p, kit["P"]), 4), port_to_yoke_min=round(p.distToShape(kit["P"])[0], 3))


def telescope(lc_list):
    rod, tube = build_rod(), build_tube()
    out = []
    for lc in lc_list:
        r, t = mv(rod, TIP_J), mv(tube, lc - TIP_J)
        engaged = r.BoundBox.XMax - (t.BoundBox.XMin)
        out.append((round(lc, 2), round(vol(r, t), 4), round(r.distToShape(t)[0], 3), round(engaged, 2)))
    return out


def runout(kit):
    out = {}
    for ph in range(0, 360, 15):
        al, be = tilt_ab(30, ph)
        d = App.Rotation(Y, al).multVec(App.Rotation(Z, be).multVec(X))
        c = V(-AX, 0, 0) + App.Rotation(Y, al).multVec(V(2 * AX, 0, 0))
        out[ph] = round((c - d * c.dot(d)).Length, 3)
    return out


def swing(kit):
    zone = kit["P"].common(box(-AX - SH - 0.01, 20, -20, 20, -20, 20))
    pts = [v for s in (zone, kit["Cr"], kit["A"], kit["B"]) for v in s.tessellate(0.05)[0]]
    r = max(p.Length for p in pts)
    heads = max(v.Length for s in (kit["A"], kit["B"]) for v in s.tessellate(0.05)[0])
    clampr = max(math.hypot(v.y, v.z) for v in kit["Cp"].tessellate(0.05)[0])
    bare = max(p.Length for s in (zone, kit["Cr"]) for p in s.tessellate(0.05)[0])
    return dict(sphere_with_heads=round(r, 2), sphere_no_screws=round(bare, 2), screw_extreme=round(heads, 2), clamp_head_radial=round(clampr, 2))


def stress():
    arm = GAP + EAR_T
    f = TORQUE / arm
    a_min = math.pi / 4 * 2.39 ** 2
    return dict(pin_force_N=round(f, 1), pin_shear_MPa=round(f / a_min, 1), ear_bearing_MPa=round(f / (SCREW_D * EAR_T), 1),
                ear_root_bend_MPa=round(6 * f * SH / (EAR_T * (2 * EAR_W) ** 2), 1))


def thin(kit):
    pa, pb = yc(PILOT / 2, -10, 10, -AX), Part.makeCylinder(PILOT / 2, 20, V(AX, 0, -10), Z)
    ch = [f for f in cross_blank().Faces if abs(f.normalAt(0, 0).x) > 1e-6 and abs(f.normalAt(0, 0).x) < 1 - 1e-6]
    pil = pa.fuse(pb)
    return dict(ear_wall_round_hole=round(EAR_W - PIN_HOLE / 2, 2), ear_cb_wall=round(EAR_W - HEAD_CB_D / 2, 2),
                cross_ch_wall=round(min(f.distToShape(pil)[0] for f in ch), 3), clamp_far=round(C_LEN - CB_Z - SHAFT_AF / 2, 2), ear_t=EAR_T, ear_under_head=round(EAR_T - HEAD_CB, 2),
                cross_B_to_A=round(pa.distToShape(pb)[0], 3), cross_x_wall=round(BLK_X / 2 - AX - PILOT / 2, 2),
                tube_wall_corner=round(TUBE_R - RC_B, 2), tube_wall_flat=round(TUBE_R - BORE / 2, 2),
                yoke_socket_wall=round(BODY_R - RC_S, 2), clamp_cb_to_flat=round(CB_Z - SOCKET / 2, 2), roof_yoke=ROOF_WALL)


def stop():
    rod, tube = mv(build_rod(), TIP_J), build_tube()
    sc = screw(V(XS_T, TUBE_R, 0), -Y, STOP_L)
    at = lambda lc: mv(sc, lc - TIP_J)
    sec = build_rod().slice(X, (G0 + G1) / 2)
    ds = lambda lc: round(rod.distToShape(at(lc))[0], 3)
    return dict(G0=round(G0, 2), G1=round(G1, 2), port_gap=round(G0 - PS_PILOT - PILOT / 2, 2), free_end=round(ROD_L - G1, 2),
                core_r=round(min(Part.Vertex(V((G0 + G1) / 2, 0, 0)).distToShape(w)[0] for w in sec), 3),
                tip_to_floor=round(TUBE_R - STOP_L - (SHAFT_AF / 2 - STOP_D), 3), mid_dist=ds(LC_MID), end_dist=(ds(LC_LO), ds(LC_HI)),
                blocked=(round(vol(rod, at(LC_LO - 0.3)), 3), round(vol(rod, at(LC_HI + 0.3)), 3)),
                free_vol=[round(vol(rod, at(lc)), 4) for lc in (LC_LO, LC_MID, LC_HI)],
                tube_vs_screw=round(vol(mv(tube, 0), sc), 3), stroke=round(LC_HI - LC_LO, 2))


def overhangs(s, up):
    sign, axis = up
    u = V(*[(1 if sign == "+" else -1) if a == axis else 0 for a in "XYZ"])
    s = s.copy()
    s.transformShape(App.Placement(V(), App.Rotation(u, Z)).toMatrix())
    s.translate(V(0, 0, -s.optimalBoundingBox(False, False).ZMin))
    floor, bad = 0.0, []
    for f in s.Faces:
        if f.BoundBox.ZMax < 1e-4 and isinstance(f.Surface, Part.Plane):
            floor += f.Area
            continue
        pts, tris = f.tessellate(0.1)
        area = 0.0
        for i, j, k in tris:
            n = (pts[j] - pts[i]).cross(pts[k] - pts[i])
            if n.Length and n.z / n.Length < -math.sin(math.radians(OVERHANG_DEG)) + 0.05:
                u, v = f.Surface.parameter((pts[i] + pts[j] + pts[k]) * (1 / 3))
                if f.normalAt(u, v).z < -math.sin(math.radians(OVERHANG_DEG)) - 1e-3:
                    area += n.Length / 2
        if area > 0.05:
            st = f.Surface
            bad.append((type(st).__name__, round(getattr(st, "Radius", 0.0), 2), round(area, 1), round(f.BoundBox.ZMin, 1)))
    return round(floor, 1), bad


def short_check(link, kit):
    out = {}
    ov, clear = {}, {}
    for g in (0, 30, -30):
        c = chain(LC_S, g, short=True)
        ks = list(c)
        ov[g] = [(a, b) for i, a in enumerate(ks) for b in ks[i + 1:] if vol(c[a], c[b]) > 1e-3]
        clear[g] = round(c["JointYoke_2"].distToShape(c["JointYoke_3"])[0], 3)
    c = chain(LC_S, 0, short=True)
    cp = screw(V(XC, 0, CB_Z), -Z, C_LEN)
    scr = {2: mv(qxf(cp), AX), 3: mv(rot(cp, X, 90), LC_S - AX)}
    ref = clamp(kit)
    out["overlap"], out["yoke_gap"] = ov, clear
    out["fit"] = {k: (round(vol(c["ShortLink"], c["JointYoke_%d" % k]), 4), round(c["ShortLink"].distToShape(c["JointYoke_%d" % k])[0], 3), round(vol(c["ShortLink"], scr[k]), 3)) for k in (2, 3)}
    out["ref_fit"] = (ref["port_to_yoke_min"], ref["thread_overlap"])
    bb = link.BoundBox
    out["bed"] = dict(height=round(bb.YLength, 2), foot=(round(bb.XLength, 2), round(bb.ZLength, 2)))
    f = 16 * TORQUE / (math.pi * SHAFT_AF ** 3) / (1 - PILOT / SHAFT_AF)
    out["stress_MPa"] = round(f, 1)
    out["thin"] = dict(pilot_end=round(PS_PILOT - PILOT / 2, 2), pilot_between=round(LINK_L - 2 * PS_PILOT - PILOT, 2), wall_flat=round(SHAFT_AF / 2 - PILOT / 2, 2), wall_corner=round(SHAFT_AF / R3 - PILOT / 2, 2))
    out["len"] = dict(LC_S=round(LC_S, 2), LINK_L=round(LINK_L, 2), OA_S=round(LC_S + 2 * END_OUT, 2), OA_LONG=round(LC_MIN + 2 * END_OUT, 2), OA_LONG_LO=round(LC_LO + 2 * END_OUT, 2), OA_LONG_HI=round(LC_HI + 2 * END_OUT, 2))
    return out


def short_kit():
    return dict(Y=mv(build_yoke(), -AX), Cr=build_cross(), A=screw(V(-AX, -(EAR_OUT - HEAD_CB), 0), Y, A_LEN),
                B=screw(V(AX, 0, EAR_OUT - HEAD_CB), -Z, A_LEN), Cp=mv(screw(V(XC, 0, CB_Z), -Z, C_LEN), -AX))


def df_frame(k, th, ph):
    al, be = tilt_ab(th, ph)
    inv = lambda s: rp(rp(s, V(-AX, 0, 0), Y, -al), V(AX, 0, 0), Z, -be)
    rz = lambda s: rp(s, V(AX, 0, 0), Z, -be)
    d = App.Rotation(Z, -be).multVec(App.Rotation(Y, -al).multVec(V(-1, 0, 0)))
    return dict(Y=inv(k["Y"]), Cr=rz(k["Cr"]), A=inv(k["A"]), B=rz(k["B"]), Cp=inv(k["Cp"])), d


def df_pose(k, df, th1, ph1, th2, ph2):
    rc = lambda s: rp(s, V(LC_D / 2, 0, 0), Z, 180)
    a, da = df_frame(k, th1, ph1)
    b, db = df_frame(k, th2, ph2)
    out = dict(DF=df, Y1=a["Y"], X1=a["Cr"], A1=a["A"], B1=a["B"], C1=a["Cp"], Y4=rc(b["Y"]), X2=rc(b["Cr"]), A2=rc(b["A"]), B2=rc(b["B"]), C4=rc(b["Cp"]))
    return out, math.degrees((-da).getAngle(App.Rotation(Z, 180).multVec(db)))


DF_THREADED = {("A1", "X1"), ("B1", "X1"), ("A2", "X2"), ("B2", "X2")}


def df_hits(k, df, *a):
    pose = df_pose(k, df, *a)[0]
    ks = list(pose)
    return [(x, y) for i, x in enumerate(ks) for y in ks[i + 1:] if (x, y) not in DF_THREADED and (y, x) not in DF_THREADED and vol(pose[x], pose[y]) > 1e-3]


def df_first(k, df, ph1, ph2, both, start=30.0, top=60.0):
    f = lambda t: df_hits(k, df, t, ph1, t if both else 0.0, ph2)
    a = start
    while a <= top and not f(a):
        a += 5.0
    if a > top:
        return top
    if a == start:
        a, start = 5.0, 0.0
        while not f(a):
            a += 5.0
    lo, hi = max(a - 5.0, 0.0), a
    for _ in range(6):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if f(mid) else (mid, hi)
    return round(hi, 2)


def df_articulation(k, df):
    rep = dict(joint1={}, joint2={}, clear30={"j1": [], "j2": [], "C": [], "S": []}, ends={})
    for ph in range(0, 360, 15):
        for th in (10, 20, 30, 35):
            rep["clear30"]["j1"] += [(ph, th, h) for h in df_hits(k, df, th, ph, 0, 0)]
            rep["clear30"]["j2"] += [(ph, th, h) for h in df_hits(k, df, 0, 0, th, ph)]
    for ph in range(0, 360, 15):
        rep["joint1"][ph] = df_first(k, df, ph, 0, False)
    for ph in range(0, 360, 45):
        rep["joint2"][ph] = df_first(k, df, 0, ph, False) if False else df_first_j2(k, df, ph)
    for name, off in (("same", 0), ("opp", 180)):
        rep["ends"][name] = round(df_pose(k, df, 30, 0, 30, off)[1], 1)
    rep["first"] = {}
    for name, off in (("same", 0), ("opp", 180)):
        rep["first"][name] = {ph: df_first(k, df, ph, (ph + off) % 360, True) for ph in range(0, 360, 15)}
    for name, off in (("same", 0), ("opp", 180), ("off45", 45), ("off90", 90)):
        rep["clear30"][name] = [(ph, h) for ph in range(0, 360, 15) for h in df_hits(k, df, 30, ph, 30, (ph + off) % 360)]
    return rep


def df_first_j2(k, df, ph):
    f = lambda t: df_hits(k, df, 0.0, 0, t, ph)
    a = 30.0
    while a <= 60.0 and not f(a):
        a += 5.0
    if a > 60.0:
        return 60.0
    lo, hi = a - 5.0, a
    for _ in range(6):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if f(mid) else (mid, hi)
    return round(hi, 2)


def df_assembly(k, df):
    p = df_pose(k, df, 0, 0, 0, 0)[0]
    out = {}
    plan = ((1, ("Y1", "X1", "A1"), ("DF", "Y4", "X2", "A2", "B2"), V(1, 0, 0), "B1", V(AX, 0, 0)), (2, ("Y4", "X2", "A2"), ("DF", "Y1", "X1", "A1", "B1"), V(-1, 0, 0), "B2", V(LC_D - AX, 0, 0)))
    for j, sub, fixed, d, scr, px in plan:
        worst = 0.0
        for i in range(61):
            sh = d * (-0.5 * i)
            worst = max([worst] + [vol(mv(p[n], sh.x, sh.y, sh.z), p[f]) for n in sub for f in fixed])
        rest = [n for n in p if n not in ("C1", "C4", scr, "X1" if j == 1 else "X2")]
        w2 = 0.0
        for i in range(81):
            w2 = max([w2] + [vol(mv(p[scr], 0, 0, 0.5 * i), p[n]) for n in rest])
        drv = Part.makeCylinder(3.0, 40, V(px.x, 0, EAR_OUT - HEAD_CB + HEAD_H), Z)
        w3 = max(vol(drv, p[n]) for n in rest)
        out[j] = dict(cross_slide=round(worst, 4), screw_slide=round(w2, 4), driver=round(w3, 4))
    return out


def df_orient(s, up, dz=None):
    sign, axis = up
    u = V(*[(1 if sign == "+" else -1) if a == axis else 0 for a in "XYZ"])
    s = s.copy()
    s.transformShape(App.Placement(V(), App.Rotation(u, Z)).toMatrix())
    dz = -s.optimalBoundingBox(False, False).ZMin if dz is None else dz
    s.translate(V(0, 0, dz))
    return s, dz


def faces_at(s, z):
    ws = s.slice(Z, z)
    fs = list(Part.makeFace(ws, "Part::FaceMakerBullseye").Faces) if ws else []
    return [mv(f, 0, 0, -z) for f in fs]


def grow(f, d):
    return Part.Face(f.makeOffset2D(d).Wires[0])


def layer_check(s, up, exempt):
    o, dz = df_orient(s, up)
    ex = df_orient(exempt, up, dz)[0]
    top = o.BoundBox.ZMax
    worst, n = 0.0, int(top / LAYER)
    prev = faces_at(o, LAYER / 2)
    for i in range(1, n):
        cur = faces_at(o, LAYER * (i + 0.5))
        u = Part.makeCompound(cur)
        for f in prev + faces_at(ex, LAYER * (i - 0.5)):
            try:
                u = u.cut(grow(f, MAX_STEP if f in prev else 0.05))
            except ValueError:
                u = None
                break
        worst = max(worst, sum(f.Area for f in u.Faces) if u else 0.0)
        prev = cur
    bb = o.BoundBox
    return dict(layers=n, unsupported_mm2=round(worst, 3), height=round(top, 2), foot=(round(bb.XLength, 2), round(bb.YLength, 2)))


def df_strength():
    a, b = 2 * math.sqrt(SPHERE_R ** 2 - EAR_W ** 2 - (LC_D / 2) ** 2), 2 * EAR_W
    al = (1 - 0.63 * b / a) / 3
    return dict(web_torsion_MPa=round(TORQUE / (al * a * b * b), 1), web_bend_MPa=round(6 * TORQUE / (a * b * b), 1), ear=stress())


def ear_walls(df):
    out = {}
    for nm, z in (("cb", EAR_OUT - HEAD_CB / 2), ("pin", EAR_OUT - HEAD_CB - 1.0)):
        ds = []
        for fc in Part.makeFace(df.slice(Z, z), "Part::FaceMakerBullseye").Faces:
            ow = fc.OuterWire
            inner = [w for w in fc.Wires if not w.isSame(ow)]
            ds += [w.distToShape(ow)[0] for w in inner] + [a.distToShape(b)[0] for i, a in enumerate(inner) for b in inner[i + 1:]]
        out[nm] = round(min(ds), 3)
    return out


def df_thin(df):
    w = ear_walls(df)
    return dict(cb_wall_measured=w["cb"], pin_wall_measured=w["pin"], tip_flat=round(2 * R_TIP * math.tan(math.pi / 8), 2),
                ear_t=EAR_T, ear_under_head=round(EAR_T - HEAD_CB, 2), root_to_pin=SH - PIN_HOLE / 2)


def df_swing(df):
    c1, c2 = V(0, 0, 0), V(LC_D, 0, 0)
    return round(max(min((p - c1).Length, (p - c2).Length) for p in df.tessellate(0.05)[0]), 2)


def df_check(df):
    k = short_kit()
    rep = dict(art=df_articulation(k, df), asm=df_assembly(k, df), strength=df_strength(), thin=df_thin(df), swing=df_swing(df), layers=layer_check(df, PRINT_UP["DoubleFork"], df_holes()))
    rep["len"] = dict(LC_D=round(LC_D, 2), OA_D=round(OA_D, 2), OA_LONG=round(LC_MIN + 2 * END_OUT, 2), DF_WEB=DF_WEB)
    rep["valid"] = (df.isValid(), len(df.Solids), round(df.Volume, 1))
    return rep


def verify(parts, kit):
    rep = dict(consts=dict(LC_MIN=round(LC_MIN, 2), LC_MAX=round(LC_MAX, 2), LC_LO=round(LC_LO, 2), LC_HI=round(LC_HI, 2), TIP_D=round(TIP_D, 3), TIP_J=round(TIP_J, 3), X_STOP=round(X_STOP, 3)))
    rep["valid"] = {n: (s.isValid(), len(s.Solids), round(s.Volume, 1)) for n, s in parts.items()}
    ov = {}
    for lc, g in ((LC_LO, 0), (LC_MID, 0), (LC_HI, 0), (LC_MID, DISPLAY_DEG)):
        c = chain(lc, g)
        ks = list(c)
        ov[(round(lc, 1), g)] = [(a, b) for i, a in enumerate(ks) for b in ks[i + 1:] if vol(c[a], c[b]) > 1e-3]
    rep["overlap"] = ov
    rep["artic"] = articulation(kit)
    rep["captured"] = captured(kit)
    rep["clamp"] = clamp(kit)
    rep["tele"] = telescope([LC_LO, LC_MID, LC_HI])
    rep["swing"] = swing(kit)
    rep["stop"] = stop()
    rep["runout"] = runout(kit)
    rep["stress"] = stress()
    rep["thin"] = thin(kit)
    rep["print"] = {n: overhangs(parts[n], PRINT_UP[n]) for n in PARTS + PARTS_S}
    rep["short"] = short_check(parts["ShortLink"], kit)
    rep["df"] = df_check(parts["DoubleFork"])
    return rep


def check(rep):
    assert all(v[0] and v[1] == 1 for v in rep["valid"].values()), rep["valid"]
    assert not any(rep["overlap"].values()), rep["overlap"]
    assert min(r[0] for r in rep["artic"]["first"].values()) >= 30.0, rep["artic"]["first"]
    assert not any(rep["artic"]["ring30"].values()), rep["artic"]["ring30"]
    assert not rep["captured"]["P"] and not rep["captured"]["Q"], rep["captured"]
    c = rep["clamp"]
    assert c["axis_in_pilot"] and c["pilot_x_error"] < 1e-3 and c["yoke_vs_screw"] < 1e-3 and c["port_vs_yoke"] < 1e-3, c
    assert all(v > 1e-3 for v in c["slide_pull_out"].values()), c
    assert all(r[1] < 1e-3 and 0.15 <= r[2] <= 0.25 and r[3] >= ENG_MIN - 1e-6 for r in rep["tele"]), rep["tele"]
    t = rep["thin"]
    p = rep["stop"]
    assert p["core_r"] >= 2.8 - 1e-3 and p["port_gap"] >= 3.0 and p["tip_to_floor"] >= 0.2 - 1e-3 and p["tube_vs_screw"] > 0, p
    assert p["mid_dist"] >= 0.2 - 1e-3 and all(v < 1e-3 for v in p["free_vol"]) and all(v > 1e-3 for v in p["blocked"]), p
    assert min(t["ear_wall_round_hole"], t["ear_cb_wall"], t["cross_ch_wall"], t["cross_B_to_A"], t["cross_x_wall"], t["tube_wall_corner"]) >= 1.2, t
    assert t["clamp_far"] >= 1.5 - 1e-3, t
    for n, (floor, bad) in rep["print"].items():
        assert floor >= 5.0, (n, floor)
        for kind, rad, area, z in bad:
            assert (kind == "Cylinder" and rad <= 3.1) or (kind == "Plane" and area <= 14.0), (n, bad)
    s = rep["short"]
    assert not any(s["overlap"].values()), s["overlap"]
    assert all(v >= LINK_GAP - 0.05 for v in s["yoke_gap"].values()), s["yoke_gap"]
    for k, (v, d, th) in s["fit"].items():
        assert v < 1e-3 and abs(d - s["ref_fit"][0]) < 0.01 and abs(th - s["ref_fit"][1]) < 0.05 and th > 0, (k, s["fit"], s["ref_fit"])
    assert s["thin"]["pilot_end"] >= 1.2 and s["thin"]["pilot_between"] >= 1.2 and s["thin"]["wall_flat"] >= 1.2 and s["thin"]["wall_corner"] >= 1.2, s["thin"]
    assert s["stress_MPa"] <= 10.0, s["stress_MPa"]
    floor, bad = rep["print"]["ShortLink"]
    assert floor >= 60.0 and not bad, rep["print"]["ShortLink"]
    assert s["bed"]["height"] <= 4 * min(s["bed"]["foot"]), s["bed"]
    assert s["len"]["OA_S"] < s["len"]["OA_LONG"] - 40, s["len"]
    d = rep["df"]
    assert d["valid"][0] and d["valid"][1] == 1, d["valid"]
    ar = d["art"]
    assert not ar["clear30"]["j1"] and not ar["clear30"]["j2"], ar["clear30"]
    assert not any(ar["clear30"].values()), ar["clear30"]
    assert min(ar["joint1"].values()) >= 30.0 and min(ar["joint2"].values()) >= 30.0, (ar["joint1"], ar["joint2"])
    assert all(min(v.values()) >= 30.0 for v in ar["first"].values()), ar["first"]
    assert all(v["cross_slide"] < 1e-3 and v["screw_slide"] < 1e-3 and v["driver"] < 1e-3 for v in d["asm"].values()), d["asm"]
    assert d["strength"]["web_torsion_MPa"] <= 10.0 and d["strength"]["web_bend_MPa"] <= 10.0, d["strength"]
    assert min(d["thin"]["cb_wall_measured"], d["thin"]["pin_wall_measured"], d["thin"]["tip_flat"], d["thin"]["root_to_pin"], d["thin"]["ear_under_head"]) >= 1.2, d["thin"]
    assert d["swing"] <= SPHERE_R + 0.01, d["swing"]
    floor, bad = rep["print"]["DoubleFork"]
    assert floor >= 60.0 and all(k == "Cylinder" and r <= 3.1 for k, r, a, z in bad), rep["print"]["DoubleFork"]
    ly = d["layers"]
    assert ly["unsupported_mm2"] <= 0.05 and ly["height"] <= 4 * min(ly["foot"]), ly
    assert d["len"]["OA_D"] <= 70.4 and DF_WEB >= 2 * 1.2, d["len"]


def main():
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    shown = chain(LC_MID, DISPLAY_DEG)
    plain = chain(LC_MID, 0.0, (0.0, EXP_DY, EXP_DZ))
    objs = [("Shown_" + n if n in PARTS else n, s) for n, s in shown.items() if n in PARTS or n.startswith("Dummy")]
    objs += [(n, plain[n]) for n in PARTS]
    sh_s = chain(LC_S, 0.0, (0.0, EXP_DY, SHORT_DZ), True)
    objs += [("Shown_" + n.replace("_", "_S") if n[-1].isdigit() else "Shown_" + n, s) for n, s in sh_s.items() if n in PARTS[:6] + PARTS_S]
    objs += [("ShortLink", chain(LC_S, 0.0, (0.0, EXP_DY, 2 * SHORT_DZ), True)["ShortLink"])]
    dfk, dfs = short_kit(), build_dfork()
    dp = df_pose(dfk, dfs, 0, 0, 0, 0)[0]
    names = dict(Y1="Shown_JointYoke_D1", Y4="Shown_JointYoke_D4", X1="Shown_JointCross_D1", X2="Shown_JointCross_D2", DF="Shown_DoubleFork")
    objs += [(names[n], mv(dp[n], 0, 0, DF_DZ)) for n in names]
    objs += [("DoubleFork", mv(dfs, 0, 0, 2 * DF_DZ))]
    for n, s in objs:
        assert s.isValid() and len(s.Solids) == 1, n
        o = doc.addObject("Part::Feature", n)
        o.Shape = s
        if App.GuiUp:
            o.ViewObject.ShapeColor = COLORS[n.replace("Shown_", "").split("_")[0]]
    kit = joint_kit()
    rep = verify({**{n: plain[n] for n in PARTS}, **{n: s for n, s in objs if n in PARTS_S}, "DoubleFork": dfs}, kit)
    print("report", rep)
    check(rep)
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
