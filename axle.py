# Axle: compact bevel differential centre section with BOLT-ON AXLE ARMS (Arm_N for the DoubleFork, kingpin 71.68 from the car centre, track 166.7; Arm_W for the ShortLink, kingpin 98.16, track 219.7).
# Axes: x lateral (axle), y fore-aft (input port toward +y), z up; origin = axle axis at the pinion axis = differential centre. Fast mode: set FAST = True before the exec (few phases, coarse sweeps, no print checks). Run: astocad -c "exec(open('axle.py').read())".
# Parts: HousingTop/HousingBottom (two open trays split at z = 0, 1.6 walls, 2.0 end walls, floor and ceiling flat at +-30.25, so the halves print on their outer flat with the cavity up; the cavity is the whole tray, beams (V keel plus web) carry the three shaft stacks, bulkhead plates carry the carrier thrust rings, screw columns), Carrier (ring gear 18T + carrier, bed face = ring big end), Cap, SideGear_L/R (10T), SpiderGear_1/2 (10T), SpiderPin, Pinion (11T), PinionShaft, PlugShaft_L/R (identical, 2 copies), Keeper_L/R/P, Sleeve_1..6 (printed placeholders of the 10 x 12 x 8 PTFE liners), JournalRing (front, hollow) and JournalStub (rear, cupped) printed standing so the journal OD 24.0 is truly round, Arm_N, Arm_W, Arm_N_L, Arm_W_L (mirrored pairs; Arm_N and Arm_W_L sit assembled, Arm_W and Arm_N_L are parked 100 and 160 above). Ref_* objects are screws, joint parts and hub kit parts in assembled position (narrow arm and DoubleFork on the -x side, wide arm and ShortLink with its two clamp screws on the +x side) and are never printed.
# Final drive: straight bevel, module 3, ring 18T pinion 11T, face 6, 20 degrees, profile shift +0.2 / -0.2, tip trim 0.5, own generator (Tredgold back cone involute, ruled to the apex, flat bed face, tips clipped to 28.0 ring / 19.14 pinion, the last 0.4 of height before the bed face tapers every tooth edge inward), flank gap 1.2 normal at the big end (0.97 at the toe), tip to root 1.4 at the big end. Differential gears: module 2.4 (not 3.0), 10T, 45 degree cones, face 4, trim 0.4, flat back (no counterbore: the carrier boss tube runs on the plug shaft), hex socket 8.5 AF from the bed face 8.15 deep. Spiders on a dia 5.0 pin 39 long (bore 5.6).
# Shaft stack per shaft (liner pockets 8.3, lips 1.2, two PTFE liners 8.0): lip, liner, lip, liner, lip. Plug shafts and the pinion shaft are lying round dia 9.1 journals with 45 degree flats on the bed plane, 8.0 AF hex where they drive. Retention: round neck groove dia 7.0 just outside the housing end face (pinion shaft: outside the JournalRing front face) and a printed Keeper (U slot, 2.0 thick, 0.15 float each way) held by one M3x8 (6.0 thread); it slides in from above through a gap in the arm spigot ring and is covered by the arm (take the arm off first, the differential stays closed).
# Pivot journals: JournalRing (front, root in a half pocket at the end of the front beam, V groove tongue and two flats, pinion shaft passes its dia 10.9 bore) and JournalStub (rear, root through the rear wall slot between two collars, flats). Each printed standing on its front collar, collars have a 45 degree cone on the journal side so no flat ledge starts in mid air (journal 12.4 long at OD 24.0 between the collar faces, collar OD 30.0 x 1.2 flat plus the cone).
# Carrier boss tube wall is 1.1 (closed ring, accepted departure from the 1.2 wall rule).
# Thrust: every spinning part has a 0.15 gap on both sides: Carrier and Cap against chamfered rings on the bulkhead plates, side gears against rings on the carrier / cap walls (front: against the pin), spiders against pads (front: against the side gear noses), plug shafts and the pinion unit between their groove flanks and Keeper.
# Arm joint: flange (5.0) lies on the housing end wall, located by the conical spigot ring on the wall into a cone recess in the arm (0.3 radial) and clamped by 6 M3x12 (4 on the rear side at y -24.3 / -12, 2 on the front side at y 13.5, driver access channels cut through the web and strut), 7.0 thread in dia 2.8 pilots 8.0 deep. The arm is the DriveHub HubCarrier lug unit (x < 5.2: bores, counterbores, bush seats, stops, lock screw hole) plus two bars and a front web.
# Bench steps (each swept as a straight slide, zero overlap, in verify): 1 SideGear_L into Carrier, 2 SpiderPin with both spiders, 3 SideGear_R, 4 Cap, 5 four M3x12 cap screws, 6 liners into HousingBottom, 7 carrier bundle with Pinion, PinionShaft, its two liners and the JournalRing slid over the shaft tip, plus the JournalStub, into HousingBottom at the drawn mesh phase, 8 HousingTop, 9 eight M3x16 closing screws from below (punch the 0.2 skin over each pass hole), 10 PlugShafts in from outside, 11 Keepers slid in from above, 12 M3x8 keeper screws, 13 arm sub-assembly (arm with Knuckle unit, StubYoke, cross, DoubleFork or yokes and ShortLink, far cross, built outside as in DriveHub) slid along x onto the plug fork and the end wall, 14 pin D from the rear, 15 arm screws with drivers (hub in place, wheel not yet fitted), 16 wheel, tyre.
# Departures and unverified items are listed in the final report of the build session.
import FreeCAD as App, Part, math, os, sys, time
import numpy as np

FAST = bool(globals().get("FAST", False))
D = {"NO_RUN": True, "__name__": "differential"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/differential.py").read(), "differential.py", "exec"), D)
H = {"NO_RUN": True, "__name__": "drive_hub"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/drive_hub.py").read(), "drive_hub.py", "exec"), H)
V, O, cyl, box, hexprism, rot, rev = (D[k] for k in ("V", "O", "cyl", "box", "hexprism", "rot", "rev"))
X, Y, Z = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
DOC_NAME = "Axle"
OUT = globals().get("OUT_OVERRIDE", "/home/mikhail/Documents/cad/RC Car/Axle.FCStd")
PA = math.radians(20.0)

# final drive (module 3, straight bevel, own tooth generator: Tredgold back cone involute with profile shift)
FM, RN, PN, FACE_F = 3.0, 18, 11, 6.0
RC = FM / 2 * math.hypot(RN, PN)
DR, DP = math.atan2(RN, PN) * 0, 0
DELTA_R, DELTA_P = math.atan2(RN, PN), math.atan2(PN, RN)
GAP_N, TRIM_F, X_P, X_R, CLR_TR = 0.9, 0.8, 0.2, -0.2, 1.4
# differential gears (module 2.4 instead of 3.0, see header)
SM, SN, FACE_S, TRIM_S = 3.0, 8, 6.5, 1.1
DELTA_S = math.radians(45.0)
RC_S = SM / 2 * SN / math.sin(DELTA_S)
GAP_S = 0.9


def mv(s, x=0.0, y=0.0, z=0.0):
    c = s.copy()
    c.translate(V(x, y, z))
    return c


def tooth_points(N, m, delta, xs, gap_n, ha, hf, Z0, npts=9):
    """closed outline (list of edges' point lists) of the toothed blank in plane z=Z0, apex at origin, axis +z"""
    cd = math.cos(delta)
    rho_p = m * N / cd / 2
    rb = rho_p * math.cos(PA)
    zb = (Z0 / cd) / cd if False else (Z0 / cd) / cd
    inv = lambda a: math.tan(a) - a
    thin = gap_n / math.cos(PA)
    s = m * (math.pi / 2 + 2 * xs * math.tan(PA)) - thin
    th_p = s / (2 * rho_p)
    rho_a, rho_f = rho_p + ha, rho_p - hf

    def half(rho):
        return th_p + inv(PA) - inv(math.acos(min(1.0, rb / rho)))

    r0 = max(rb, rho_f)
    rhos = [r0 + (rho_a - r0) * (i / (npts - 1)) ** 1.3 for i in range(npts)]
    zbk = Z0 / cd / cd * 1.0
    zb = (Z0 / math.cos(delta)) / math.cos(delta)

    def p3(rho, phi):
        r, z = rho * cd, zb - rho * math.sin(delta)
        f = Z0 / z
        psi = phi / cd
        return (f * r * math.cos(psi), f * r * math.sin(psi))

    tau = 2 * math.pi / (N / cd)
    edges = []
    for k in range(N):
        c = k * tau
        right = [p3(r, c - half(r)) for r in rhos]
        left = [p3(r, c + half(r)) for r in rhos]
        pre = [p3(rho_f, c - half(r0))] if rho_f < rb - 1e-9 else []
        pre_l = [p3(rho_f, c + half(r0))] if rho_f < rb - 1e-9 else []
        edges.append((pre + right, left[::-1] + pre_l[::-1], c, half(r0), rho_f))
    return edges, p3, tau


def spl(pts, z):
    pp = [V(x, y, z) for x, y in pts]
    c = Part.BSplineCurve()
    c.interpolate(pp)
    return c.toShape()


FILLET_R = 0.6


def fillet_corner(c, pts, tdir, r):
    """root fillet between the flank polyline pts (starting at the root corner c) and the root circle (unit tangent tdir leaving the tooth): returns (arc points from the root side to the flank, remaining flank points)"""
    cx, cy = c
    acc, prev, a_pt, k = 0.0, c, None, 1
    u1 = (pts[1][0] - cx, pts[1][1] - cy)
    n1 = math.hypot(*u1)
    u1 = (u1[0] / n1, u1[1] / n1)
    al = math.acos(max(-1.0, min(1.0, u1[0] * tdir[0] + u1[1] * tdir[1])))
    d = r / math.tan(al / 2)
    for k in range(1, len(pts)):
        seg = math.hypot(pts[k][0] - prev[0], pts[k][1] - prev[1])
        if acc + seg >= d:
            f = (d - acc) / seg
            a_pt = (prev[0] + f * (pts[k][0] - prev[0]), prev[1] + f * (pts[k][1] - prev[1]))
            break
        acc += seg
        prev = pts[k]
    b_pt = (cx + d * tdir[0], cy + d * tdir[1])
    bis = (u1[0] + tdir[0], u1[1] + tdir[1])
    nb = math.hypot(*bis)
    oc = (cx + bis[0] / nb * r / math.sin(al / 2), cy + bis[1] / nb * r / math.sin(al / 2))
    a0, a1 = math.atan2(b_pt[1] - oc[1], b_pt[0] - oc[0]), math.atan2(a_pt[1] - oc[1], a_pt[0] - oc[0])
    da = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
    arc = [(oc[0] + r * math.cos(a0 + da * i / 4), oc[1] + r * math.sin(a0 + da * i / 4)) for i in range(5)]
    return arc, pts[k:]


def bevel_wire(N, m, delta, xs, gap_n, ha, hf, Z0, lam):
    edges, p3, tau = tooth_points(N, m, delta, xs, gap_n, ha, hf, Z0)
    z = Z0 * lam
    fl = []
    for rt, lf, c, h0, rf in edges:
        cr, cl = rt[0], lf[-1]
        thr, thl = math.atan2(cr[1], cr[0]), math.atan2(cl[1], cl[0])
        arc_r, rt2 = fillet_corner(cr, rt, (math.sin(thr), -math.cos(thr)), FILLET_R)
        arc_l, lf2 = fillet_corner(cl, lf[::-1], (-math.sin(thl), math.cos(thl)), FILLET_R)
        fl.append((arc_r, rt2, arc_l, lf2))
    sc = lambda q: [(x * lam, y * lam) for x, y in q]
    es = []
    for k, (rt, lf, c, h0, rf) in enumerate(edges):
        arc_r, rt2, arc_l, lf2 = fl[k]
        nb = fl[(k + 1) % N][0][0]
        bl = arc_l[0]
        t1, t2 = math.atan2(bl[1], bl[0]), math.atan2(nb[1], nb[0])
        dt = (t2 - t1) % (2 * math.pi)
        r1, r2 = math.hypot(*bl), math.hypot(*nb)
        root = [bl] + [((r1 + (r2 - r1) * u) * math.cos(t1 + dt * u), (r1 + (r2 - r1) * u) * math.sin(t1 + dt * u)) for u in (0.2, 0.4, 0.6, 0.8)] + [nb]
        es.append(spl(sc(arc_r + rt2), z))
        es.append(Part.makeLine(V(rt[-1][0] * lam, rt[-1][1] * lam, z), V(lf[0][0] * lam, lf[0][1] * lam, z)))
        es.append(spl(sc(lf2[::-1] + arc_l[::-1]), z))
        es.append(spl(sc(root), z))
    return Part.Wire(es)


def chamfer_top(s, Z0, rmax, ch=0.4):
    pts = [V(rmax - ch, 0, Z0 + 0.01), V(rmax + 1.0, 0, Z0 + 0.01), V(rmax + 1.0, 0, Z0 - ch - 1.0 + 0.01)]
    return s.cut(Part.Face(Part.makePolygon(pts + pts[:1])).revolve(O, Z, 360)).removeSplitter()


def solid_loft(wa, wb):
    s = Part.makeLoft([wa, wb], True, True)
    if s.Volume < 0:
        s = Part.Solid(Part.Shell(s.Faces))
        if s.Volume < 0:
            s.reverse()
    return s


def bevel_blank(N, m, delta, xs, gap_n, ha, hf, face, phase=0.0, rclip=None, ch=0.4):
    """toothed solid between toe and big-end planes, apex at origin, axis +z, big end plane z=Rc cos(delta) is flat (bed). The last ch of height tapers every tooth edge inward (flank edges and tips), tips are clipped to rclip"""
    rc = m / 2 * N / math.sin(delta)
    Z0 = rc * math.cos(delta)
    w1 = bevel_wire(N, m, delta, xs, gap_n, ha, hf, Z0, (rc - face) / rc)
    if ch:
        lam_c = (Z0 - ch) / Z0
        wc = bevel_wire(N, m, delta, xs, gap_n, ha, hf, Z0, lam_c)
        s = None
        for rel in (ch, 0.3, 0.2):
            try:
                wt = bevel_wire(N, m, delta, xs, gap_n + rel, ha - rel, hf, Z0, 1.0)
                lam_t = (rc - face) / rc
                wtoe = bevel_wire(N, m, delta, xs, gap_n + rel, ha - rel, hf, Z0, lam_t)
                w1b = bevel_wire(N, m, delta, xs, gap_n, ha, hf, Z0, lam_t + ch / Z0)
                s = solid_loft(wtoe, w1b).fuse(solid_loft(w1b, wc)).fuse(solid_loft(wc, wt)).removeSplitter()
                if s.isValid():
                    break
            except Exception:
                s = None
        assert s is not None
    else:
        s = solid_loft(w1, bevel_wire(N, m, delta, xs, gap_n, ha, hf, Z0, 1.0))
    if rclip:
        s = s.common(Part.makeCylinder(rclip, 200, V(0, 0, -100)))
    if phase:
        s.rotate(O, Z, phase)
    return s


def prof_zone(delta, lo, hi, amax=60.0):
    """solid of revolution about +z of points with signed distance from the pitch cone in [lo, hi] (positive outside)"""
    s, c = math.sin(delta), math.cos(delta)
    line = lambda a, t: (a, (a * s + t) / c)
    pts = [line(0.0, hi), line(amax, hi), line(amax, lo), line(0.0, lo)]
    pts = [V(max(r, 0.0), 0, a) for a, r in pts]
    return Part.Face(Part.makePolygon(pts + pts[:1])).revolve(O, Z, 360)


def ring_place(s):
    return rot(s, Y, -90)


def pin_place(s):
    return rot(s, X, -90)


def rotx(s, a):
    return rot(s, X, a)


def roty(s, a):
    return rot(s, Y, a)


def vol(a, b):
    return a.common(b).Volume if a.BoundBox.intersect(b.BoundBox) else 0.0


def dist(a, b):
    return a.distToShape(b)[0]


class Pair:
    """two bevel blanks with tip and flank measurement zones, placed by two callables"""

    def __init__(self, ga, gb, pa_, pb_, zone_lo=1.0):
        self.ga, self.gb, self.pa, self.pb = ga, gb, pa_, pb_
        self.za = ga.common(prof_zone(pa_["delta"], zone_lo, 99.0))
        self.zb = gb.common(prof_zone(pb_["delta"], zone_lo, 99.0))
        self.fa = ga.common(prof_zone(pa_["delta"], -1.0, 1.0))
        self.fb = gb.common(prof_zone(pb_["delta"], -1.0, 1.0))


def pair_metrics(pr, place_a, place_b, rot_a, rot_b, ang, da=(0, 0, 0), db=(0, 0, 0)):
    """place_a/place_b: callables (solid, angle) -> solid in assembly frame"""
    a, b = [place_a(s, ang) for s in (pr.ga, pr.za, pr.fa)], [place_b(s, ang) for s in (pr.gb, pr.zb, pr.fb)]
    a = [mv(s, *da) for s in a]
    b = [mv(s, *db) for s in b]
    ov = vol(a[0], b[0])
    return dict(ov=round(ov, 4), whole=round(dist(a[0], b[0]), 3) if ov < 1e-4 else -1, flank=round(dist(a[2], b[2]), 3),
                tip_a=round(dist(a[1], b[0]), 3), tip_b=round(dist(b[1], a[0]), 3))


# ---------------------------------------------------------------- constants (A frame: origin = ring/pinion apex = differential centre)
GAP_F, GAP_S2 = 1.8, 1.9
CH_F = 1.0
RHO_P = FM * PN / math.cos(DELTA_P) / 2
HA_P, HA_R = FM * (1 + X_P) - TRIM_F, FM * (1 + X_R) - TRIM_F
HF_P, HF_R = HA_R + CLR_TR, HA_P + CLR_TR
Z_RING, Z_PIN = RC * math.cos(DELTA_R), RC * math.cos(DELTA_P)
Z_RING_TOE, Z_PIN_TOE = (RC - FACE_F) * math.cos(DELTA_R), (RC - FACE_F) * math.cos(DELTA_P)
R_RING_CLIP = 28.0
R_PIN_CLIP = (RHO_P + HA_P) * math.cos(DELTA_P)
HA_S, CLR_S = SM - TRIM_S, 1.4
HF_S = HA_S + CLR_S
RHO_S = SM * SN / math.cos(DELTA_S) / 2
R_S_CLIP = (RHO_S + HA_S) * math.cos(DELTA_S)
A_S = RC_S * math.cos(DELTA_S)
A_S_TOE = (RC_S - FACE_S) * math.cos(DELTA_S)
SIDE_NOSE_R, SIDE_NOSE_X, NOSE_OVER = 5.7, 2.55, 0.4
SPIDER_PH = 22.5
RING_R0, RING_R1 = 7.2, 8.4
HEX_SOCK = 8.55
SOCK_FLOOR = 3.85
SPI_BORE, SPI_NOSE_R, SPI_NOSE_Y = 5.5, 4.0, 5.85
PIN_D, PIN_HALF = 4.8, 19.2
XF, XW, XE = 16.5, 12.6, 14.3
PADY, RING_P = 14.3, 1.95
R_POCK, RING_H = 13.7, 2.15
R_CAV, R_CO = 19.4, 20.6
RING_BOSS_H, THRUST_GAP = 0.45, 0.15
BOSS_OD, BOSS_ID, BOSS_PROT = 12.4, 10.0, 1.4
PAD_HZ, SEAT_D, SEAT_Y1 = 5.5, 5.1, 19.4
CPB_Y, CPB_Z, CPB_R, CPB_DEEP = 7.0, 14.39, 2.6, 11.8
CAP_HEAD_H, CAP_CB_R, CAP_PAD_R, CAP_PAD_D, CAP_BUT_R = 3.2, 3.3, 3.4, 1.2, 4.5
CAP_SEAT_X = XF - CAP_HEAD_H
JOURNAL_D, LIP_BORE_D, POCK_D = 9.4, 10.9, 12.2
LIP_T2, PK_L2, LINER_L2 = 1.2, 8.3, 8.0
LIPSTK = LIP_T2 * 3 + PK_L2 * 2
XB_END = 17.3 + LIPSTK
KEEP_T, KEEP_GAP, GROOVE_D, FLANK_R = 2.0, 0.15, 7.0, 4.7
XJ = 53.28
YB_ZERO = 27.9
YE_END = YB_ZERO + LIPSTK
APO = 30.2


def build_pinion_blank(phase=0.0):
    return bevel_blank(PN, FM, DELTA_P, X_P, GAP_F, HA_P, HF_P, FACE_F, rclip=R_PIN_CLIP, ch=CH_F)


def build_ring_blank():
    return bevel_blank(RN, FM, DELTA_R, X_R, GAP_F, HA_R, HF_R, FACE_F, rclip=R_RING_CLIP, ch=CH_F)


def build_side_blank():
    return bevel_blank(SN, SM, DELTA_S, 0.0, GAP_S2, HA_S, HF_S, FACE_S, rclip=R_S_CLIP, ch=CH_F)


def zrev(pts):
    p = [V(r, 0, z) for r, z in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).revolve(O, Z, 360)


def hexz(af, z0, z1):
    r = af / math.sqrt(3)
    pts = [V(r * math.cos(math.radians(a)), r * math.sin(math.radians(a)), z0) for a in range(0, 361, 60)]
    return Part.Face(Part.makePolygon(pts)).extrude(V(0, 0, z1 - z0))


def build_side_gear():
    """axis +x after placement; blank frame z = axial, big plane at A_S is flat (bed)"""
    b = build_side_blank()
    b = b.fuse(Part.makeCylinder(SIDE_NOSE_R, A_S_TOE - SIDE_NOSE_X + NOSE_OVER, V(0, 0, SIDE_NOSE_X)))
    b = b.cut(rot(hexz(HEX_SOCK, SOCK_FLOOR, A_S + 1), Z, 30))
    return rot(b.removeSplitter(), Y, 90)


def build_spider_gear():
    """axis +y after placement"""
    b = build_side_blank()
    b = b.fuse(Part.makeCylinder(SPI_NOSE_R, A_S_TOE - SPI_NOSE_Y + NOSE_OVER, V(0, 0, SPI_NOSE_Y)))
    b = b.cut(Part.makeCylinder(SPI_BORE / 2, 40, V(0, 0, -5)))
    return rot(rot(b.removeSplitter(), X, -90), Y, SPIDER_PH)


PH_RING, PH_PIN = 0.0, 16.4


def xcyl(r, x0, x1, y=0.0, z=0.0):
    return Part.makeCylinder(r, x1 - x0, V(x0, y, z), X)


def ycyl(r, y0, y1, x=0.0, z=0.0):
    return Part.makeCylinder(r, y1 - y0, V(x, y0, z), Y)


def zcyl(r, z0, z1, x=0.0, y=0.0):
    return Part.makeCylinder(r, z1 - z0, V(x, y, z0), Z)


def xrev(pts):
    p = [V(x, r, 0) for x, r in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).revolve(O, X, 360)


def yrev(pts):
    p = [V(r, y, 0) for y, r in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).revolve(O, Y, 360)


def xann(r0, r1, x0, x1):
    return xcyl(r1, x0, x1).cut(xcyl(r0, x0 - 1, x1 + 1))


def yann(r0, r1, y0, y1):
    return ycyl(r1, y0, y1).cut(ycyl(r0, y0 - 1, y1 + 1))


def pillar(sg, zz):
    pts = [V(-0.5, 12.15, 0), V(1.5, 12.15, 0), V(1.5, 18.1, 0), V(-6.45, 18.1, 0)]
    w = Part.Face(Part.makePolygon(pts + pts[:1])).extrude(V(0, 0, 3.0))
    w.translate(V(0, 0, 7.2))
    if sg < 0:
        w = w.mirror(O, Y)
    if zz < 0:
        w = w.mirror(O, Z)
    return w


def build_carrier(ring):
    c = ring.fuse(xrev([(-13.6, 0), (-13.6, 15.9), (-8.37, R_CO), (XW, R_CO), (XW, 0)])).removeSplitter()
    cav = xrev([(-XE, 0), (-XE, R_POCK), (-XW, R_POCK), (-XW, 15.17), (-8.37, R_CAV), (XW + 0.5, R_CAV), (XW + 0.5, 0)])
    for sg in (1, -1):
        cone = Part.makeCone(4.0, 4.0 + (R_CAV + 1 - PADY), R_CAV + 1 - PADY, V(0, PADY, 0), Y)
        cav = cav.cut(cone if sg > 0 else cone.mirror(O, Y))
        for zz in (1, -1):
            cav = cav.cut(xcyl(CPB_R, -XW, XW + 1, sg * CPB_Y, zz * CPB_Z))
    c = c.cut(cav)
    c = c.fuse(xrev([(-XE - 0.01, 0), (-XE - 0.01, BOSS_OD / 2), (-XE + BOSS_PROT - 0.6, BOSS_OD / 2), (-XE + BOSS_PROT, BOSS_OD / 2 - 0.6), (-XE + BOSS_PROT, 0)])).fuse(xann(RING_R0, RING_R1, -XE - 0.01, -XE + RING_H))
    for sg in (1, -1):
        for zz in (1, -1):
            c = c.fuse(pillar(sg, zz))
    c = c.cut(xcyl(BOSS_ID / 2, -XF - 1, 0.0))
    for sg in (1, -1):
        s0, s1 = sorted((sg * (PADY - 0.2), sg * SEAT_Y1))
        slot = box(0, XW + 1, s0, s1, -SEAT_D / 2, SEAT_D / 2).fuse(ycyl(SEAT_D / 2, s0, s1))
        c = c.cut(slot)
        for zz in (1, -1):
            c = c.cut(xcyl(CAP_PAD_R, XW - CAP_PAD_D, XW + 1, sg * CPB_Y, zz * CPB_Z))
            c = c.cut(xcyl(1.4, XW - CPB_DEEP, XW + 1, sg * CPB_Y, zz * CPB_Z))
    return c.removeSplitter()


def build_cap():
    c = xcyl(R_CO, XW, XF).cut(xcyl(R_POCK, XW - 1, XE))
    c = c.fuse(xrev([(XE - BOSS_PROT, 0), (XE - BOSS_PROT, BOSS_OD / 2 - 0.6), (XE - BOSS_PROT + 0.6, BOSS_OD / 2), (XE + 0.01, BOSS_OD / 2), (XE + 0.01, 0)])).fuse(xann(RING_R0, RING_R1, XE - RING_H, XE + 0.01))
    fz = SEAT_D / 2 - 0.15
    for sg in (1, -1):
        y0, y1 = sorted((sg * (PADY + 0.2), sg * (SEAT_Y1 - 0.15)))
        c = c.fuse(box(PIN_D / 2 + 0.3, XW + 0.01, y0, y1, -fz, fz))
        for zz in (1, -1):
            c = c.fuse(xcyl(CAP_BUT_R, XW, XE + 0.01, sg * CPB_Y, zz * CPB_Z).common(xcyl(R_CO, XW - 1, XE + 1)).cut(xcyl(11.0, XW - 2, XE + 2)))
            c = c.fuse(xcyl(CAP_PAD_R - 0.15, XW - CAP_PAD_D, XW + 0.01, sg * CPB_Y, zz * CPB_Z))
            c = c.cut(xcyl(1.6, XW - CAP_PAD_D - 1, CAP_SEAT_X - SKIN, sg * CPB_Y, zz * CPB_Z))
            c = c.cut(xcyl(CAP_CB_R, CAP_SEAT_X, XF + 1, sg * CPB_Y, zz * CPB_Z))
    return c.cut(xcyl(BOSS_ID / 2, XW - 4, XF + 1)).removeSplitter()


R_J, R_NECK, R_FLANK = 4.7, 3.7, 5.2
BED_Z = -3.7
X_TIP = 4.15
X_HEXEND = 12.3
PORT_END, YOKE_HEX_DEPTH = 16.2, 10.2
X_KEEP0 = XB_END
X_G0, X_G1 = X_KEEP0 - KEEP_GAP, X_KEEP0 + KEEP_T + KEEP_GAP
X_WEB0 = XJ - D["PF_AX"] - D["PF_SH"] - D["PLG_WEB"]
KEEP_SLOT_R, KEEP_SCREW_Z, KEEP_SCREW_ZP = 4.3, 14.5, 9.3
for _k, _v in dict(SHAFT_X0=X_TIP, PLG_XS=X_WEB0, PLG_X0=X_WEB0 + D["PLG_WEB"], PLG_PIN=XJ - D["PF_AX"] - 0.0 - 0.0 + 0.0 - 0.0).items():
    D[_k] = _v
D["PLG_PIN"] = D["PLG_X0"] + D["PF_SH"]
D["PLG_C"] = D["PLG_PIN"] + D["PF_AX"]
assert abs(D["PLG_C"] - XJ) < 1e-9


def round_flat(r, x0, x1, flat=BED_Z):
    s = xcyl(r, x0, x1)
    yf = r * math.sqrt(2) - abs(flat)
    t = r / math.sqrt(2)
    pts = [V(x0, -yf, flat), V(x0, yf, flat), V(x0, t, -t), V(x0, 0, 0), V(x0, -t, -t)]
    wedge = Part.Face(Part.makePolygon(pts + pts[:1])).extrude(V(x1 - x0, 0, 0))
    return s.fuse(wedge)


def neck_oct(x0, x1):
    rho = R_NECK / math.cos(math.pi / 8)
    pts = [V(x0, rho * math.cos(math.radians(22.5 + 45 * k)), rho * math.sin(math.radians(22.5 + 45 * k))) for k in range(9)]
    return Part.Face(Part.makePolygon(pts)).extrude(V(x1 - x0, 0, 0))


def below(x0, x1, z=BED_Z):
    return box(x0 - 1, x1 + 1, -40, 40, z - 40, z)


def build_plug_shaft():
    s = D["build_plug_shaft"]()
    s = s.cut(xann(R_NECK, 10.0, X_G0 + 0.0, X_G1 + 0.4))
    s = s.fuse(round_flat(R_J, X_HEXEND, X_G0 + 0.0)).fuse(neck_oct(X_G0 - 0.5, X_G1 + 0.4)).fuse(round_flat(R_FLANK, X_G1, X_WEB0 + 0.5))
    return s.cut(below(0, 60)).removeSplitter()


def build_pinion_shaft():
    y0 = Z_PIN_TOE
    head = D["hexprism"](11.0, y0, y0 + 2.4)
    tip = Y_RING_END + PORT_END
    s = head.fuse(round_flat(R_J, y0 + 2.0, X_G0y())).fuse(neck_oct(X_G0y() - 0.5, X_G1y() + 0.4)).fuse(round_flat(R_FLANK, X_G1y(), X_G1y() + 1.6))
    s = s.fuse(D["hexprism"](8.0, X_G1y() - 0.01, tip))
    s = s.cut(zcyl(1.4, -10, 10, tip - 5.9, 0)) if False else s
    s = s.cut(below(y0, tip))
    s = s.cut(Part.makeCylinder(1.4, 20, V(tip - 5.9, 0, -10), Z))
    return rot(s.removeSplitter(), Z, 90)


def X_G0y():
    return Y_RING_END - KEEP_GAP


def X_G1y():
    return Y_RING_END + KEEP_T + KEEP_GAP


def build_keeper(zs=14.5):
    t = KEEP_T
    plate = box(0, t, -6.5, 6.5, -6.0, zs - 3.3).fuse(Part.makeCylinder(6.5, t, V(0, 0, zs - 3.3), X))
    slot = box(-1, t + 1, -KEEP_SLOT_R, KEEP_SLOT_R, -7, 0).fuse(Part.makeCylinder(KEEP_SLOT_R, t + 2, V(-1, 0, 0), X))
    plate = plate.cut(slot).cut(Part.makeCylinder(1.7, t + 2, V(-1, 0, zs), X))
    return plate.removeSplitter()


def build_sleeve(ax, c0):
    s = Part.makeCylinder(6.0, LINER_L2, V(0, 0, 0), Z).cut(Part.makeCylinder(5.0, LINER_L2 + 2, V(0, 0, -1), Z))
    s = rot(s, Y, 90) if ax == "x" else rot(s, X, -90)
    c0 = c0 - LINER_L2 / 2
    s.translate(V(c0, 0, 0) if ax == "x" else V(0, c0, 0))
    return s


def build_pin():
    s = round_flat(PIN_D / 2, -PIN_HALF, PIN_HALF, flat=-2.0).cut(below(-PIN_HALF, PIN_HALF, -2.0))
    return rot(s.removeSplitter(), Z, 90)


def build_pinion(blank):
    p = rot(rot(blank, X, -90), Y, PH_PIN)
    p = p.cut(ycyl(5.0, 0, 40)).cut(rot(D["hexprism"](11.5, Z_PIN_TOE - 1, Z_PIN_TOE + 2.4), Z, 90))
    return p.removeSplitter()


def build_core():
    blanks = dict(ring=build_ring_blank(), pin=build_pinion_blank(), side=build_side_blank())
    P = {}
    ring = rotx(ring_place(blanks["ring"]), PH_RING)
    P["Carrier"] = build_carrier(ring)
    P["Cap"] = build_cap()
    P["Pinion"] = build_pinion(blanks["pin"])
    sg = build_side_gear()
    P["SideGear_R"] = sg
    P["SideGear_L"] = rot(sg, Z, 180)
    sp = build_spider_gear()
    P["SpiderGear_1"] = sp
    P["SpiderGear_2"] = rot(sp, X, 180)
    P["SpiderPin"] = build_pin()
    P["PinionShaft"] = build_pinion_shaft()
    pl = build_plug_shaft()
    P["PlugShaft_R"] = pl
    P["PlugShaft_L"] = rot(pl, Z, 180)
    P["Keeper_R"] = mv(build_keeper(), X_KEEP0, 0, 0)
    P["Keeper_L"] = rot(P["Keeper_R"], Z, 180)
    return P, blanks


# ---------------------------------------------------------------- housing: two open trays (1.6 walls) with beams for the shaft stacks, bulkhead plates for the carrier thrust, columns for the screws
AP_OUT, AP_IN, END_T, WALL_T, YT = 30.25, 28.65, 2.0, 1.6, 30.3
XWALL, BKH_R, BKH_T = 17.3, 13.0, 3.21
Y_RING_END, RING_ROOT = 70.9, 5.0
Y_BLK = YE_END + RING_ROOT
Y_PIN_BACK = Z_PIN
SLOT_HW, SLOT_FLOOR, BLK_HW = 11.15, -12.2, 13.55
JR, JC, CONE_H = 12.0, 15.0, 3.0
SPIG_D = 2.0
ARM_PIL = ((-24.3, 11.0), (-24.3, -11.0), (-12.0, 24.5), (-12.0, -24.5), (13.5, 11.5), (13.5, -11.5))
ARM_PIL_DEPTH = 8.0
CLOSE_POS = ((-23.5, -26.0), (23.5, -26.0), (-25.5, 26.0), (25.5, 26.0), (-21.0, 33.0), (21.0, 33.0), (-21.0, -33.0), (21.0, -33.0))
CLOSE_SEAT_Z = -9.95
MOUNT_PIL = ((8.0, 16.0), (-8.0, 16.0), (8.0, -16.0), (-8.0, -16.0))
SPRING_PIL = ((22.0, 8.0), (22.0, -8.0), (-22.0, 8.0), (-22.0, -8.0))
KEEL = [(-8.5, 0), (8.5, 0), (1, -7.5), (1, -AP_OUT), (-1, -AP_OUT), (-1, -7.5)]
BKH = [(-BKH_R, 0), (BKH_R, 0), (BKH_R, -1.2), (0, -BKH_R - 1.2), (-BKH_R, -1.2)]
HEAD_FREE_R = 13.2


def px(pts, x0, x1):
    p = [V(x0, y, z) for y, z in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).extrude(V(x1 - x0, 0, 0))


def py(pts, y0, y1):
    p = [V(x, y0, z) for x, z in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).extrude(V(0, y1 - y0, 0))


def pz(pts, z0, z1):
    p = [V(x, y, z0) for x, y in pts]
    return Part.Face(Part.makePolygon(p + p[:1])).extrude(V(0, 0, z1 - z0))


def octagon(x0, x1, ap=APO):
    r = ap / math.cos(math.radians(22.5))
    pts = [V(x0, r * math.cos(math.radians(22.5 + 45 * k)), r * math.sin(math.radians(22.5 + 45 * k))) for k in range(9)]
    return Part.Face(Part.makePolygon(pts)).extrude(V(x1 - x0, 0, 0))


def stack_profile(u0):
    """(u, r) profile cutter along an axis: lip bore through, two liner pockets, u0 = first lip face"""
    p0 = u0 + LIP_T2
    p1 = p0 + PK_L2
    m1 = p1 + LIP_T2
    p2 = m1 + PK_L2
    end = p2 + LIP_T2
    rl, rp = LIP_BORE_D / 2, POCK_D / 2
    return [(u0 - 3, 0), (u0 - 3, rl), (p0, rl), (p0, rp), (p1, rp), (p1, rl), (m1, rl), (m1, rp), (p2, rp), (p2, rl), (end + 3, rl), (end + 3, 0)], (p0, p1, m1, p2)


def xstack(sg):
    pr, st = stack_profile(XWALL)
    s = xrev(pr)
    return (s if sg > 0 else s.mirror(O, X)), st


def ystack():
    pr, st = stack_profile(YB_ZERO)
    p = [V(r, u, 0) for u, r in pr]
    return Part.Face(Part.makePolygon(p + p[:1])).revolve(O, Y, 360), st


def spigot_ring(sg):
    x1 = XB_END
    g = xrev([(x1 - 0.02, 21.26), (x1 + SPIG_D, 19.2), (x1 + SPIG_D, 21.76), (x1 - 0.02, 23.82)])
    return g if sg > 0 else g.mirror(O, X)


def tray_lower(rings=True):
    xi, yi = XB_END - END_T, YT - WALL_T
    L = box(-XB_END, XB_END, -YT, YT, -AP_OUT, 0).cut(box(-xi, xi, -yi, yi, -AP_IN, 1.0))
    for sg in (1, -1):
        a, b = sorted((sg * XWALL, sg * XB_END))
        L = L.fuse(px(KEEL[:3] + [(-1, -7.5)], a, b))
        a, b = sorted((sg * 20.5, sg * XB_END))
        L = L.fuse(px(KEEL, a, b))
        a, b = sorted((sg * XWALL, sg * (XWALL + BKH_T)))
        plate = px(BKH, a, b)
        wedge = py([(XWALL - 0.1, -9.0), (XWALL + BKH_T + 0.01, -HEAD_FREE_R - 0.01), (XWALL + BKH_T + 0.01, -40), (XWALL - 0.1, -40)], -40, 40)
        plate = plate.cut(wedge if sg > 0 else wedge.mirror(O, X))
        L = L.fuse(plate)
    L = L.fuse(py(KEEL, YB_ZERO, Y_BLK)).fuse(box(-BLK_HW, BLK_HW, YE_END, Y_BLK, -AP_OUT, 0))
    L = L.removeSplitter()
    for sg in (1, -1):
        L = L.cut(xstack(sg)[0])
    L = L.cut(ystack()[0]).cut(ycyl(5.45, YE_END - 1, Y_BLK + 1))
    L = L.cut(box(-SLOT_HW, SLOT_HW, YE_END, Y_BLK + 0.1, SLOT_FLOOR, 1.0)).cut(box(-SLOT_HW, SLOT_HW, -YT - 0.1, -yi, SLOT_FLOOR, 1.0))
    for sx in (1, -1):
        t = pz([(sx * (SLOT_HW + 0.01), Y_BLK - 3.5), (sx * (SLOT_HW + 0.01), Y_BLK - 1.5), (sx * (SLOT_HW - 0.96), Y_BLK - 2.5)], SLOT_FLOOR, 0.0)
        L = L.fuse(t)
    if rings:
        yr = yrev([(YB_ZERO + 0.01, 6.6), (YB_ZERO + 0.01, 9.0), (Y_PIN_BACK + 0.15, 8.2), (Y_PIN_BACK + 0.15, 7.4)])
        for sx in (1, -1):
            yr = yr.cut(py([(sx * 1.0, -7.5), (sx * 8.5, 0.0), (sx * 30.0, 0.0), (sx * 30.0, -30.0), (sx * 1.0, -30.0)], Y_PIN_BACK - 1, YB_ZERO + 1))
        L = L.fuse(yr)
        rb = xrev([(XWALL + 0.01, 8.3), (XWALL + 0.01, 10.25), (XWALL - 0.65, 9.55), (XWALL - 0.65, 8.3)])
        ext = py([(16.0, -7.48), (XWALL - 0.1, -9.0), (XWALL + BKH_T + 0.01, -HEAD_FREE_R - 0.01), (XWALL + BKH_T + 0.01, -40), (16.0, -40)], -40, 40)
        rb = rb.cut(ext)
        L = L.fuse(rb).fuse(rb.mirror(O, X))
    for sg in (1, -1):
        L = L.fuse(spigot_ring(sg))
    return L.common(box(-60, 60, -60, 60, -60, 0)).removeSplitter()


def column(x, y, half):
    """screw column OD 9 on the bed side: bottom half well from the bed to the seat then a 0.2 skin and a clear hole, top half hollow below a pilot cap"""
    if half < 0:
        c = zcyl(4.5, -AP_OUT, 0.0, x, y)
        return c, [zcyl(3.3, -AP_OUT - 1, CLOSE_SEAT_Z, x, y), zcyl(1.7, CLOSE_SEAT_Z + SKIN, 0.0, x, y)]
    c = zcyl(4.5, 0.0, AP_OUT, x, y)
    return c, [zcyl(3.3, 9.0, AP_OUT + 1, x, y), zcyl(1.4, 0.0, 7.6, x, y)]


def half_features(h, half):
    for x, y in CLOSE_POS:
        c, cuts = column(x, y, half)
        h = h.fuse(c)
        for k in cuts:
            h = h.cut(k)
    for sg in (1, -1):
        for y, z in ARM_PIL:
            if z * half > 0:
                xa, xb = sorted((sg * (XB_END - END_T - 8.0), sg * (XB_END - END_T + 0.01)))
                za, zb = (-AP_OUT, z + 3.3) if half < 0 else (z - 3.3, AP_OUT)
                h = h.fuse(box(xa, xb, y - 3.3, y + 3.3, za, zb))
                h = h.cut(xcyl(1.4, XB_END - ARM_PIL_DEPTH, XB_END + 1, y, z) if sg > 0 else xcyl(1.4, -XB_END - 1, -XB_END + ARM_PIL_DEPTH, y, z))
    if half > 0:
        for sg in (1, -1):
            xa, xb = sorted((sg * (XB_END - END_T - 8.0), sg * (XB_END - END_T + 0.01)))
            h = h.fuse(box(xa, xb, -3.3, 3.3, KEEP_SCREW_Z - 3.3, AP_OUT))
            h = h.cut(xcyl(1.4, XB_END - 9.0, XB_END + 1, 0, KEEP_SCREW_Z) if sg > 0 else xcyl(1.4, -XB_END - 1, -XB_END + 9.0, 0, KEEP_SCREW_Z))
        for x, y in MOUNT_PIL + SPRING_PIL:
            h = h.fuse(zcyl(3.5, AP_IN - 6.0, AP_IN + 0.01, x, y)).cut(zcyl(1.4, AP_OUT - 6.0, AP_OUT + 1, x, y))
    return h.removeSplitter()


def build_housing_halves(rings=True):
    L = tray_lower(rings)
    U = L.mirror(O, Z)
    gap = lambda sg: box(*sorted((sg * XB_END, sg * (XB_END + 3.0))), -7.2, 7.2, 12.0, 30.0)
    U = U.cut(gap(1)).cut(gap(-1))
    return half_features(L, -1), half_features(U, 1)


def build_journal_ring():
    y0, yb, ye = YE_END, Y_BLK, Y_RING_END
    pts = [(y0, 0), (y0, JR), (yb, JR), (yb, JC), (yb + 1.2, JC), (yb + 1.2 + CONE_H, JR), (ye - 1.2, JR), (ye - 1.2, JC), (ye, JC), (ye, 0)]
    r = yrev(pts)
    r = r.cut(box(11.0, 20, y0 - 1, yb, -20, 20)).cut(box(-20, -11.0, y0 - 1, yb, -20, 20))
    g = [V(rr, yy, 0) for yy, rr in ((y0 + 0.3, 12.1), (y0 + 2.5, 10.0), (y0 + 4.7, 12.1))]
    r = r.cut(Part.Face(Part.makePolygon(g + g[:1])).revolve(O, Y, 360))
    r = r.cut(ycyl(5.45, y0 - 1, ye + 1)).cut(ycyl(1.4, ye - 9.0, ye + 1, 0, KEEP_SCREW_ZP))
    return r.removeSplitter()


STUB_FACE, PILOT_D, PILOT_DEEP, PILOT_XZ = -56.0, 2.8, 8.0, ((10.0, 6.0), (10.0, -6.0), (-10.0, 6.0), (-10.0, -6.0))


def build_journal_stub():
    pts = [(STUB_FACE, 0), (STUB_FACE, JC), (-46.9, JC), (-46.9, JR), (-34.5, JR), (-31.5, JC), (-30.3, JC), (-30.3, JR), (-28.5, JR), (-27.7, 12.8), (-26.5, 12.8), (-26.5, 0)]
    r = yrev(pts)
    r = r.cut(box(11.0, 20, -30.3, -26.5, -20, 20)).cut(box(-20, -11.0, -30.3, -26.5, -20, 20))
    r = r.cut(ycyl(8.0, -45.1, -23.0))
    for x, z in PILOT_XZ:
        r = r.cut(ycyl(PILOT_D / 2, STUB_FACE - 1, STUB_FACE + PILOT_DEEP, x, z))
    return r.removeSplitter()


def stub_pilot_report(s):
    out = dict(face=STUB_FACE, depth=PILOT_DEEP, xz=PILOT_XZ)
    wall, beyond = 9.0, 9.0
    for x, z in PILOT_XZ:
        assert not s.isInside(V(x, STUB_FACE + PILOT_DEEP - 0.05, z), 1e-6, True) and not s.isInside(V(x, STUB_FACE + 0.05, z), 1e-6, True)
        assert s.isInside(V(x, STUB_FACE + PILOT_DEEP + 0.05, z), 1e-6, True)
        for k in range(36):
            a = math.radians(10 * k)
            for y in (STUB_FACE + 0.5, STUB_FACE + PILOT_DEEP - 0.5):
                d = PILOT_D / 2 + 0.05
                while d < 6.0 and s.isInside(V(x + d * math.cos(a), y, z + d * math.sin(a)), 1e-6, True):
                    d += 0.05
                wall = min(wall, d - PILOT_D / 2)
        y = STUB_FACE + PILOT_DEEP
        while s.isInside(V(x, y + 0.05, z), 1e-6, True):
            y += 0.05
        beyond = min(beyond, y - (STUB_FACE + PILOT_DEEP))
    out.update(wall=round(wall, 2), solid_beyond=round(beyond, 2), volume=round(s.Volume / 1000.0, 2))
    return out


# ---------------------------------------------------------------- arms (hub frame: kingpin = Z axis through origin, outboard -X, +Y ahead)
L_N, L_W = XJ + 18.4, XJ + 44.88
PLATE_T, PLATE_AP, OPEN_R, RECESS_D = 5.0, 29.0, 11.5, 2.3
BAR_Y0, BAR_Y1, WEB_Y0 = -8.0, 16.5, 13.8
LUG_X1 = 5.2
TIE_PIL_DEPTH = 5.8


def build_arm(Lk):
    xf = Lk - XB_END
    c = H["build_carrier"](stops=True)
    c = c.common(box(-14.0, LUG_X1, -40, 40, -40, 40))
    c = c.cut(box(-12.0, -LUG_X1, -40, 40, 26.3, 29.5))
    c = c.cut(box(-12.0, LUG_X1 + 0.1, -17.0, H["LUG_Y0"] - 0.001, 26.3, 29.5))
    x0 = LUG_X1 - 0.1
    xp = xf - PLATE_T
    body = box(x0, xp + 0.01, BAR_Y0, BAR_Y1, H["LUG_Z0"], 29.0).fuse(box(x0, xp + 0.01, BAR_Y0, BAR_Y1, -29.0, -H["LUG_Z0"])).fuse(box(x0, xp + 0.01, WEB_Y0, BAR_Y1, -29.0, 29.0))
    plate = octagon(xp, xf, PLATE_AP).common(box(xp - 1, xf + 1, -40, BAR_Y1, -40, 40))
    t = OPEN_R / math.sqrt(2)
    sl = (OPEN_R * 1.45 - t) / t
    ap = 20.8
    jp = [(-ap, 0.0), (sl * 19.0 - ap, 19.0), (3.7, 19.0), (3.7, -t), (sl * t - ap, -t)]
    gable = Part.Face(Part.makePolygon([V(xp - 1, y, z) for y, z in jp] + [V(xp - 1, jp[0][0], jp[0][1])])).extrude(V(xf - xp + 2, 0, 0))
    plate = plate.cut(xcyl(OPEN_R, xp - 1, xf + 1)).cut(gable)
    recess = xrev([(xf + 0.01, 0), (xf + 0.01, 24.1), (xf - RECESS_D, 24.1 - 1.03 * RECESS_D), (xf - RECESS_D, 0)])
    head = xcyl(3.7, xp - 1, xf + 1, 0, KEEP_SCREW_Z)
    a = c.fuse(body).fuse(plate).removeSplitter().cut(recess).cut(head)
    for zz in (11.5, -11.5):
        a = a.cut(box(-4.5, xp + 0.01, 10.0, 17.0, zz - 3.1, zz + 3.1))
    for y, z in ARM_PIL:
        a = a.cut(xcyl(1.7, xp - 1, xf + 1, y, z))
    for yy in (-3.0, 7.0):
        a = a.cut(Part.makeCylinder(1.4, TIE_PIL_DEPTH + 1, V(xp - 10.0, yy, 29.0 - TIE_PIL_DEPTH), Z))
    return a.removeSplitter()


def build_arm_L(Lk):
    return build_arm(Lk).mirror(O, X)


# ---------------------------------------------------------------- assembly in the car frame
S = H["S"]
SCR = H["screw"]
KIT_ARM_X = dict(N=L_N, W=L_W)


def split_housing(h):
    return h.common(box(-60, 60, -60, 60, 0, 60)), h.common(box(-60, 60, -60, 60, -60, 0))


def to_car(shape, Lk, left):
    """hub frame (outboard -X) to car frame: left=True stays on the -x side, False mirrors to +x"""
    s = shape.copy() if left else shape.mirror(O, X)
    s.translate(V(-Lk if left else Lk, 0, 0))
    return s


def hub_refs(arm_len):
    kit = H["jkit"]()
    P0, R0 = H["build_parts"](), H["build_refs"]()
    out = {n: P0[n] for n in ("Knuckle", "StubYoke", "Wheel", "Tyre", "PivotBush_1", "PivotBush_2", "Sleeve_1", "Sleeve_2")}
    for n in ("Ref_PivotScrew_U", "Ref_PivotScrew_L", "Ref_LockScrew", "Ref_HubScrew", "Ref_HubWasher", "Ref_JointCross", "Ref_PinA", "Ref_PinB"):
        out[n] = R0[n]
    ear, hc = S["EAR_OUT"], S["HEAD_CB"]
    ax = S["AX"]
    if arm_len == L_N:
        out["Ref_DoubleFork"] = R0["Ref_DoubleFork"]
        lc = S["LC_D"]
        out["Ref_PinC"] = S["screw"](V(lc - ax, 0, ear - hc), -Z, 20.0)
    else:
        ch = S["chain"](S["LC_S"], 0, short=True)
        lc = S["LC_S"]
        out["Ref_JointYoke_A"], out["Ref_JointYoke_B"], out["Ref_ShortLink"] = ch["JointYoke_2"], ch["JointYoke_3"], ch["ShortLink"]
        cp = S["screw"](V(S["XC"], 0, S["CB_Z"]), -Z, S["C_LEN"])
        out["Ref_ClampA"], out["Ref_ClampB"] = mv(S["qxf"](cp), S["AX"]), mv(rot(cp, X, 90), S["LC_S"] - S["AX"])
        out["Ref_PinC"] = S["screw"](V(lc - ax, 0, ear - hc), -Z, 20.0)
    out["Ref_JointCross_2"] = mv(rot(kit["Cr"], Z, 180), lc)
    out["Ref_PinD"] = S["screw"](V(lc + ax, -(ear - hc), 0), Y, 20.0)
    return out


def assemble(fast=False):
    P, blanks = build_core()
    P.pop("Keeper_R"), P.pop("Keeper_L")
    xs = {}
    for sg, nm in ((1, "R"), (-1, "L")):
        k = mv(build_keeper(), X_KEEP0, 0, 0)
        xs[nm] = k if sg > 0 else rot(k, Z, 180)
    P["Keeper_R"], P["Keeper_L"] = xs["R"], xs["L"]
    kp = rot(build_keeper(KEEP_SCREW_ZP), Z, 90)
    P["Keeper_P"] = mv(kp, 0, Y_RING_END, 0)
    P["HousingBottom"], P["HousingTop"] = build_housing_halves()
    P["JournalRing"], P["JournalStub"] = build_journal_ring(), build_journal_stub()
    i = 1
    for sg in (1, -1):
        st = xstack(sg)[1]
        for a, b in ((st[0], st[1]), (st[2], st[3])):
            P["Sleeve_%d" % i] = build_sleeve("x", sg * (a + b) / 2)
            i += 1
    st = ystack()[1]
    for a, b in ((st[0], st[1]), (st[2], st[3])):
        P["Sleeve_%d" % i] = build_sleeve("y", (a + b) / 2)
        i += 1
    for tag, Lk in (("N", L_N), ("W", L_W)):
        a = build_arm(Lk)
        P["Arm_" + tag] = to_car(a, Lk, True)
        P["Arm_%s_L" % tag] = to_car(a, Lk, False)
    return P, blanks


def screw_refs(core=False):
    R = {}
    SCR = H['core'] if core else H['screw']
    i = 1
    for x, y in CLOSE_POS:
        R["Ref_CloseScrew_%d" % i] = SCR(V(x, y, CLOSE_SEAT_Z), Z, 16.0)
        i += 1
    i = 1
    for sy in (1, -1):
        for sz in (1, -1):
            R["Ref_CapScrew_%d" % i] = SCR(V(CAP_SEAT_X, sy * CPB_Y, sz * CPB_Z), -X, 12.0)
            i += 1
    R["Ref_KeepScrew_R"] = SCR(V(XB_END + KEEP_T, 0, KEEP_SCREW_Z), -X, 8.0)
    R["Ref_KeepScrew_L"] = SCR(V(-XB_END - KEEP_T, 0, KEEP_SCREW_Z), X, 8.0)
    R["Ref_KeepScrew_P"] = SCR(V(0, Y_RING_END + KEEP_T, KEEP_SCREW_ZP), -Y, 8.0)
    i = 1
    for sg in (1, -1):
        for y, z in ARM_PIL:
            R["Ref_ArmScrew_%s_%d" % ("R" if sg > 0 else "L", i)] = SCR(V(sg * (XB_END + PLATE_T), y, z), -sg * X, 12.0)
            i += 1
    return R


# ---------------------------------------------------------------- verification
SAG, LOST_MAX, MIN_GAP, FLOAT, SKIN = 0.3, 1.0, 0.6, 0.15, 0.2
OPEN = []
SIGMA_MAX, T_RING = 15.0, 607.0


def lewis(N, m, delta, xs, gap_n, ha, hf, face, torque, share=1.0):
    """root bending of one tooth loaded at its tip at mid face, MPa; dimensions scaled to mid face"""
    cd = math.cos(delta)
    rho_p = m * N / cd / 2
    rb = rho_p * math.cos(PA)
    rc = m / 2 * N / math.sin(delta)
    k = (rc - face / 2) / rc
    rm = m * N / 2 * k
    ft = torque / rm * share
    inv = lambda a: math.tan(a) - a
    s = m * (math.pi / 2 + 2 * xs * math.tan(PA)) - gap_n / math.cos(PA)
    th = s / (2 * rho_p)
    rf = rho_p - hf
    r0 = max(rb, rf)
    half = th + inv(PA) - inv(math.acos(min(1.0, rb / r0)))
    sr = 2 * r0 * math.sin(half) * k
    h = (ha + (rho_p - r0)) * k
    return 6 * ft * h / (face * sr ** 2), ft, sr, h


def tooth_stress():
    return dict(
        ring=lewis(RN, FM, DELTA_R, X_R, GAP_F, HA_R, HF_R, FACE_F, T_RING),
        pinion=lewis(PN, FM, DELTA_P, X_P, GAP_F, HA_P, HF_P, FACE_F, T_RING * PN / RN),
        side=lewis(SN, SM, DELTA_S, 0.0, GAP_S2, HA_S, HF_S, FACE_S, T_RING / 2, 0.5),
        spider=lewis(SN, SM, DELTA_S, 0.0, GAP_S2, HA_S, HF_S, FACE_S, T_RING / 2, 0.5))


def gear_metrics(blanks, fast=False):
    """flank gap, tip to root both ways, whole-solid gap, overlap: final drive and side/spider, over mesh phases and float extremes"""
    out = {}
    pr = Pair(blanks["ring"], blanks["pin"], dict(delta=DELTA_R), dict(delta=DELTA_P), zone_lo=HA_R - 0.5)
    pr.zb = blanks["pin"].common(prof_zone(DELTA_P, HA_P - 0.5, 99.0))
    pr.za = blanks["ring"].common(prof_zone(DELTA_R, HA_R - 0.5, 99.0))
    pa = lambda s, a: rotx(ring_place(s), a)
    pb = lambda s, a: roty(pin_place(s), PH_PIN + a * RN / PN)
    phases = (0.0, 10.0) if fast else (0.0, 5.0, 10.0, 15.0)
    floats = [(0, 0), (FLOAT, FLOAT), (-FLOAT, -FLOAT), (FLOAT, -FLOAT), (-FLOAT, FLOAT)]
    if fast:
        floats = floats[:3]
    res = []
    for a in phases:
        for fx, fy in floats:
            m = pair_metrics(pr, pa, pb, 0, 0, a, da=(fx, 0, 0), db=(0, fy, 0))
            res.append(dict(m, ph=a, fx=fx, fy=fy))
    out["final"] = res
    sd = blanks["side"]
    ps = Pair(sd, sd, dict(delta=DELTA_S), dict(delta=DELTA_S))
    ps.za = sd.common(prof_zone(DELTA_S, HA_S - 0.5, 99.0))
    ps.zb = ps.za
    ps.fa = sd.common(prof_zone(DELTA_S, -1.0, 1.0))
    ps.fb = ps.fa
    sa = lambda s, a: rotx(rot(s, Y, 90), a)
    sb = lambda s, a: roty(rot(s, X, -90), -a)
    res = []
    for a in ((0.0, 18.0) if fast else (0.0, 9.0, 18.0, 27.0)):
        for fx, fy in floats:
            m = pair_metrics(ps, sa, sb, 0, 0, a, da=(fx, 0, 0), db=(0, fy, 0))
            res.append(dict(m, ph=a, fx=fx, fy=fy))
    out["side"] = res
    return out


def near(a, b, lim=8.0):
    p, q = a.BoundBox, b.BoundBox
    d = [max(p.XMin - q.XMax, q.XMin - p.XMax, 0), max(p.YMin - q.YMax, q.YMin - p.YMax, 0), max(p.ZMin - q.ZMax, q.ZMin - p.ZMax, 0)]
    return math.sqrt(sum(v * v for v in d)) < lim


def mvs(s, dx=0.0, dy=0.0, dz=0.0):
    return mv(s, dx, dy, dz)


def housing_plain():
    """housing without the deliberate thrust rings (spinning to fixed clearance; thrust gaps are measured separately)"""
    b, t = build_housing_halves(False)
    return b.fuse(t)


def clearance_table(P, fast=False):
    """spinning parts to fixed parts at nominal and both float extremes, thrust faces excluded by using the housing without its rings"""
    hp = housing_plain()
    fixed = dict(Housing=hp, JournalRing=P["JournalRing"], JournalStub=P["JournalStub"], Arm_N=P["Arm_N"], Arm_W_L=P["Arm_W_L"], Keeper_R=P["Keeper_R"], Keeper_L=P["Keeper_L"], Keeper_P=P["Keeper_P"])
    for i in range(1, 7):
        fixed["Sleeve_%d" % i] = P["Sleeve_%d" % i]
    groups = dict(
        carrier=(["Carrier", "Cap", "SideGear_L", "SideGear_R", "SpiderGear_1", "SpiderGear_2", "SpiderPin"], X),
        pinion=(["Pinion", "PinionShaft"], Y),
        plug_R=(["PlugShaft_R"], X), plug_L=(["PlugShaft_L"], X))
    out = {}
    for g, (names, ax) in groups.items():
        for n in names:
            for fn, fs in fixed.items():
                if fn.startswith("Sleeve") and not (n.startswith("Plug") or n == "PinionShaft"):
                    continue
                worst = 99.0
                for f in ((0.0,) if (fast or fn.startswith("Keeper")) else (0.0, FLOAT, -FLOAT)):
                    sh = P[n].copy()
                    sh.translate(ax * f)
                    if near(sh, fs, 3.0):
                        worst = min(worst, dist(sh, fs))
                out[(n, fn)] = round(worst, 3)
    return out


def thrust_gaps(P):
    t = {}
    ring = dict(P)
    hh = P["HousingTop"].fuse(P["HousingBottom"])
    t["carrier_housing"] = round(dist(P["Carrier"], hh), 3)
    t["cap_housing"] = round(dist(P["Cap"], hh), 3)
    t["sideR_cap"] = round(dist(P["SideGear_R"], P["Cap"]), 3)
    t["sideL_carrier"] = round(dist(P["SideGear_L"], P["Carrier"]), 3)
    t["spider1_carrier"] = round(dist(P["SpiderGear_1"], P["Carrier"]), 3)
    t["spider2_carrier"] = round(dist(P["SpiderGear_2"], P["Carrier"]), 3)
    t["sideR_pin"] = round(dist(P["SideGear_R"], P["SpiderPin"]), 3)
    t["sideL_pin"] = round(dist(P["SideGear_L"], P["SpiderPin"]), 3)
    t["plugR_keeper"] = round(dist(P["PlugShaft_R"], P["Keeper_R"]), 3)
    t["plugL_keeper"] = round(dist(P["PlugShaft_L"], P["Keeper_L"]), 3)
    t["pinion_keeper"] = round(dist(P["PinionShaft"], P["Keeper_P"]), 3)
    t["pinion_housing_back"] = round(dist(P["Pinion"], hh), 3)
    return t


def nose_gaps(P):
    """real side gear and spider solids (noses included) with every axial float combination: the two stops are independent, so the smallest gap must stay open"""
    m = 9.0
    for sd, sp, s in (("SideGear_R", "SpiderGear_1", 1), ("SideGear_L", "SpiderGear_2", -1), ("SideGear_R", "SpiderGear_2", 1), ("SideGear_L", "SpiderGear_1", -1)):
        for dx in (-FLOAT, FLOAT):
            for dy in (-FLOAT, FLOAT):
                m = min(m, dist(mv(P[sd], dx, 0, 0), mv(P[sp], 0, dy, 0)))
    return round(m, 3)


def driver(p, d, length=60.0, r=3.0):
    return Part.makeCylinder(r, length, p, d)


def sweep(mov, fixed, v, length=60.0, step=2.0):
    worst = 0.0
    for i in range(int(round(length / step)) + 1):
        o = length - i * step
        for a in mov.values():
            m = a.copy()
            m.translate(v * o)
            worst = max(worst, max(vol(m, b) for b in fixed.values()))
    return round(worst, 4)


def drivers():
    d, hh = {}, 3.2
    for i, (x, y) in enumerate(CLOSE_POS, 1):
        d["Ref_CloseScrew_%d" % i] = (driver(V(x, y, CLOSE_SEAT_Z - hh), -Z), -Z)
    i = 1
    for sy in (1, -1):
        for sz in (1, -1):
            d["Ref_CapScrew_%d" % i] = (driver(V(XF, sy * CPB_Y, sz * CPB_Z), X), X)
            i += 1
    d["Ref_KeepScrew_R"] = (driver(V(XB_END + KEEP_T + hh, 0, KEEP_SCREW_Z), X), X)
    d["Ref_KeepScrew_L"] = (driver(V(-XB_END - KEEP_T - hh, 0, KEEP_SCREW_Z), -X), -X)
    d["Ref_KeepScrew_P"] = (driver(V(0, Y_RING_END + KEEP_T + hh, KEEP_SCREW_ZP), Y), Y)
    i = 1
    for sg in (1, -1):
        for y, z in ARM_PIL:
            d["Ref_ArmScrew_%s_%d" % ("R" if sg > 0 else "L", i)] = (driver(V(sg * (XB_END + PLATE_T + hh), y, z), sg * X), sg * X)
            i += 1
    return d


def assembly_steps(P, R, step=2.0):
    r = {}
    R = screw_refs(core=True)
    drv = drivers()
    car = P["Carrier"]
    gears = dict(SpiderPin=P["SpiderPin"], S1=P["SpiderGear_1"], S2=P["SpiderGear_2"])
    r["01_sideL_into_carrier"] = sweep(dict(g=P["SideGear_L"]), dict(c=car), X, 60, step)
    r["02_pin_and_spiders_into_carrier"] = sweep(gears, dict(c=car, g=P["SideGear_L"]), X, 60, step)
    r["03_sideR_into_carrier"] = sweep(dict(g=P["SideGear_R"]), dict(c=car, g1=P["SideGear_L"], **gears), X, 60, step)
    inner = dict(c=car, gl=P["SideGear_L"], gr=P["SideGear_R"], **gears)
    r["04_cap_on"] = sweep(dict(cap=P["Cap"]), inner, X, 60, step)
    inner["cap"] = P["Cap"]
    r["05_cap_screws_with_drivers"] = max(sweep({n: R[n], n + "_d": drv[n][0]}, inner, X, 60, step) for n in R if n.startswith("Ref_CapScrew"))
    liners = {n: P[n] for n in ("Sleeve_1", "Sleeve_2", "Sleeve_3", "Sleeve_4")}
    r["06_liners_into_bottom_half"] = sweep(liners, dict(b=P["HousingBottom"]), Z, 60, step)
    rotating = dict(inner, **{n: R[n] for n in R if n.startswith("Ref_CapScrew")})
    still = dict(pinion=P["Pinion"], pshaft=P["PinionShaft"], s5=P["Sleeve_5"], s6=P["Sleeve_6"], jr=P["JournalRing"], js=P["JournalStub"])
    angs = (0.0,) if FAST else (0.0, 20.0, 40.0)
    ba = {}
    for ang in angs:
        bundle = dict({n: rotx(s, ang) for n, s in rotating.items()}, **still)
        fx0 = dict(b=P["HousingBottom"], **liners)
        o7 = sweep(bundle, fx0, Z, 60, step)
        fx0.update(bundle)
        o8 = sweep(dict(t=P["HousingTop"]), fx0, Z, 60, step)
        ba[ang] = (o7, o8)
    r["bundle_angles"] = ba
    good = next((a for a in angs if max(ba[a]) < 1e-3), angs[0])
    r["07_bundle_into_bottom_half"], r["08_top_half_on"] = ba[good]
    bundle = dict({n: rotx(s, good) for n, s in rotating.items()}, **still)
    fx = dict(b=P["HousingBottom"], **liners)
    fx.update(bundle)
    fx["t"] = P["HousingTop"]
    r["09_closing_screws_with_drivers"] = max(sweep({n: R[n], n + "_d": drv[n][0]}, fx, -Z, 60, step) for n in R if n.startswith("Ref_CloseScrew"))
    r["10_plugR_in"] = sweep(dict(p=P["PlugShaft_R"]), fx, X, 60, step)
    r["10_plugL_in"] = sweep(dict(p=P["PlugShaft_L"]), fx, -X, 60, step)
    fx.update(pr=P["PlugShaft_R"], pl=P["PlugShaft_L"])
    r["11_keepers_slide_in"] = max(sweep(dict(k=P["Keeper_R"]), fx, Z, 40, step), sweep(dict(k=P["Keeper_L"]), fx, Z, 40, step), sweep(dict(k=P["Keeper_P"]), fx, Z, 40, step))
    for n, k in (("Ref_KeepScrew_R", "Keeper_R"), ("Ref_KeepScrew_L", "Keeper_L"), ("Ref_KeepScrew_P", "Keeper_P")):
        fx[k] = P[k]
    r["12_keeper_screws_with_drivers"] = max(sweep({n: R[n], n + "_d": drv[n][0]}, fx, drv[n][1], 60, step) for n in R if n.startswith("Ref_KeepScrew"))
    r["13_arm_N_on"] = sweep(dict(a=P["Arm_N"]), fx, -X, 60, step)
    r["13_arm_W_L_on"] = sweep(dict(a=P["Arm_W_L"]), fx, X, 60, step)
    fx.update(an=P["Arm_N"], aw=P["Arm_W_L"])
    r["14_arm_screws_with_drivers"] = max(sweep({n: R[n], n + "_d": drv[n][0]}, fx, drv[n][1], 60, step) for n in R if n.startswith("Ref_ArmScrew"))
    return r


PRINT_UP = dict(HousingBottom="+Z", HousingTop="-Z", Carrier="+X", Cap="-X", SideGear_R="-X", SideGear_L="+X", SpiderGear_1="-Y", SpiderGear_2="+Y",
                SpiderPin="+Z", Pinion="-Y", PinionShaft="+Z", PlugShaft_R="+Z", PlugShaft_L="+Z", Keeper_R="+X", Keeper_L="-X", Keeper_P="+Y",
                Sleeve_1="+X", Sleeve_2="+X", Sleeve_3="+X", Sleeve_4="+X", Sleeve_5="+Y", Sleeve_6="+Y", JournalRing="-Y", JournalStub="+Y", Arm_N="-Y", Arm_W="-Y", Arm_N_L="-Y", Arm_W_L="-Y")
COPIES = dict(HousingBottom=1, HousingTop=1, Carrier=1, Cap=1, SideGear_R=2, SpiderGear_1=2, SpiderPin=1, Pinion=1, PinionShaft=1, PlugShaft_R=2, Keeper_R=3, Sleeve_1=6, Arm_N=1, Arm_N_L=1)


GB = {"NO_RUN": True, "__name__": "gearbox"}


def island_check(name, s, step=0.1):
    """no area threshold: slice the part in print orientation every 0.1 and list every region of a layer that does not touch the layer below (a point of the part that starts in mid air)"""
    from shapely.ops import unary_union
    p = GB["to_print"](name, s)
    tri = GB["mesh"](p)
    h = tri[:, :, 2].max()
    prev, sig0, found = None, None, []
    for k in range(int(h / step)):
        z = step * k + step / 2 + 1e-3
        g = GB["region"](tri, z)
        for dz in (0.0137, 0.0271, 0.0413):
            if g is None:
                g = GB["region"](tri, z + dz)
        if g is None or g.is_empty:
            continue
        sig = (round(g.area, 3), round(g.length, 3))
        if sig == sig0:
            continue
        if prev is not None:
            low = prev.buffer(0.02)
            for c in getattr(g, "geoms", [g]):
                if c.area > 1e-6 and not c.intersects(low):
                    found.append((round(z, 1), round(c.area, 3), [round(c.centroid.x, 1), round(c.centroid.y, 1)]))
        prev, sig0 = g, sig
    return found


def print_checks(P):
    """one checker for every part: gearbox_module.printable (45 degree faces, bridges, 0.3 layer sag, 0.03 area, bed 60, height 4 x, first layer wall 0.8), run once per unique shape"""
    if "printable" not in GB:
        exec(compile(open("/home/mikhail/Documents/cad/RC Car/gearbox_module.py").read(), "gearbox_module.py", "exec"), GB)
    GB["PRINT_UP"] = PRINT_UP
    groups = []
    for n, sh in P.items():
        sign, axis = PRINT_UP[n]
        v = V(*[(1 if sign == "+" else -1) if a == axis else 0 for a in "XYZ"])
        t = sh.copy()
        t.transformShape(App.Placement(V(), App.Rotation(v, Z)).toMatrix())
        bb = t.optimalBoundingBox(False, False)
        key = (round(sh.Volume, 1), tuple(sorted(round(d, 1) for d in (bb.XLength, bb.YLength, bb.ZLength))))
        for g in groups:
            if g[0] == key:
                g[1].append(n)
                break
        else:
            groups.append((key, [n], (bb.XLength, bb.YLength, bb.ZLength)))
    out = {}
    for key, ms, size in groups:
        r = GB["printable"](ms[0], P[ms[0]])
        r["islands"] = island_check(ms[0], P[ms[0]])
        out[ms[0]] = dict(r, twins=ms[1:], volume=round(key[0] / 1000.0, 2), size=[round(x, 1) for x in size])
    return out


def hub_frame_parts(Lk, arm):
    P0, R0 = H["build_parts"](), H["build_refs"]()
    P0["HubCarrier"] = arm
    return P0, R0


def steer_clear(Lk, arm, statics, angles=None):
    """Knuckle, Wheel, Tyre, stub, bushes, screws swept through the steering range, distance to arm and centre section (hub frame)"""
    P0, R0 = hub_frame_parts(Lk, arm)
    mov = {n: P0[n] for n in ("Knuckle", "Wheel", "Tyre", "StubYoke", "PivotBush_1", "PivotBush_2")}
    for n in ("Ref_PivotScrew_U", "Ref_PivotScrew_L", "Ref_LockScrew", "Ref_HubScrew", "Ref_HubWasher"):
        mov[n] = R0[n]
    fixed = dict(statics, Arm=arm)
    angs = angles or [-28.0, -24.0, -16.0, -8.0, 0.0, 8.0, 16.0, 24.0, 28.0]
    out = {}
    stops = (H["stop_angle"](P0, R0, 1), H["stop_angle"](P0, R0, -1))
    for a in angs:
        if a > stops[0] - 0.01 or -a > stops[1] - 0.01:
            a = max(-stops[1] + 0.01, min(stops[0] - 0.01, a))
        row = {}
        for n, sh in mov.items():
            r = sh.copy()
            r.rotate(O, Z, a)
            row[n] = min(dist(r, f) for f in fixed.values() if near(r, f, 6.0)) if any(near(r, f, 6.0) for f in fixed.values()) else 99.0
        out[round(a, 1)] = {k: round(v, 2) for k, v in row.items()}
    return out, stops


def joint_envelope(Lk):
    sph = lambda x: Part.makeSphere(12.5, V(x, 0, 0))
    return sph(0.0).fuse(sph(Lk - XJ)).fuse(xcyl(12.5, 0.0, Lk - XJ))


def hub_statics(P, Lk):
    """centre section parts that stay put, moved into the hub frame of the -x side arm"""
    return {n: mv(P[n], Lk, 0, 0) for n in ("HousingTop", "HousingBottom", "Keeper_L", "PlugShaft_L", "Cap", "Carrier")}


def joint_clear(Lk, arm, statics):
    env = joint_envelope(Lk)
    fixed = dict(statics, Arm=arm)
    return {n: round(dist(env, f), 3) for n, f in fixed.items()}


def section_props(rects):
    A = sum((y1 - y0) * (z1 - z0) for y0, y1, z0, z1 in rects)
    yc = sum((y1 - y0) * (z1 - z0) * (y0 + y1) / 2 for y0, y1, z0, z1 in rects) / A
    zc = sum((y1 - y0) * (z1 - z0) * (z0 + z1) / 2 for y0, y1, z0, z1 in rects) / A
    Iy = sum((y1 - y0) * (z1 - z0) ** 3 / 12 + (y1 - y0) * (z1 - z0) * ((z0 + z1) / 2 - zc) ** 2 for y0, y1, z0, z1 in rects)
    Iz = sum((z1 - z0) * (y1 - y0) ** 3 / 12 + (y1 - y0) * (z1 - z0) * ((y0 + y1) / 2 - yc) ** 2 for y0, y1, z0, z1 in rects)
    zmax = max(max(abs(z0 - zc), abs(z1 - zc)) for y0, y1, z0, z1 in rects)
    ymax = max(max(abs(y0 - yc), abs(y1 - yc)) for y0, y1, z0, z1 in rects)
    return A, Iy, Iz, zmax, ymax


def arm_strength(Lk):
    """30 N vertical, 15 N lateral, 15 N fore-aft at the tyre patch (55 below the axle, 11.69 outboard of the kingpin), resultants at the arm root (housing face) and bolted joint"""
    FZ, FX, FY, HP, SC = 30.0, 15.0, 15.0, 55.0, 11.69
    xf = Lk - XB_END
    lever = xf + SC
    My, Mz, T = FZ * lever + FX * HP, FY * lever, FY * HP
    rects = [(BAR_Y0, BAR_Y1, 21.9, 29.0), (BAR_Y0, BAR_Y1, -29.0, -21.9), (WEB_Y0, BAR_Y1, -21.9, 21.9)]
    A, Iy, Iz, zm, ym = section_props(rects)
    sig = FX / A + My * zm / Iy + Mz * ym / Iz
    J = 2 * 0.286 * 24.5 * 7.1 ** 3 + (1 / 3) * 43.8 * 2.7 ** 3
    tau = T * 7.1 / J
    shear = math.hypot(FZ, FY) / (2 * 24.5 * 7.1)
    zlug = (H["LUG_Z0"] + H["LUG_CB"]) / 2
    Fres = math.hypot(FX, FY)
    rl = Fres * (55.0 + zlug) / (2 * zlug)
    lug = rl * H["STRUT_Y0"] / ((29.0 - H["LUG_Z0"]) * ((2 * H["BLK_HW"]) ** 3 - H["BORE_D"] ** 3) / (6 * 2 * H["BLK_HW"]))
    bush_bear = rl / (H["BUSH_OD"] * (H["LUG_CB"] - H["LUG_Z0"]))
    ys, zs = [y for y, z in ARM_PIL], [z for y, z in ARM_PIL]
    tens = lambda M, d: max(M * x / sum(v * v for v in d) for x in d)
    t_mz = max(tens(Mz, [y + 29.0 for y in ys]), tens(Mz, [16.5 - y for y in ys]))
    t_my = max(tens(My, [z + 29.0 for z in zs]), tens(My, [29.0 - z for z in zs]))
    t_screw = t_my + t_mz + FX / len(ARM_PIL)
    t_front = tens(Mz, [16.5 - y for y in ys])
    pre = 0.0
    eng = 12.0 - PLATE_T
    return dict(L=Lk, xf=round(xf, 2), lever=round(lever, 2), My=round(My), Mz=round(Mz), T=round(T), A=round(A, 1), sigma_root=round(sig, 2), tau_torsion=round(tau, 2), shear=round(shear, 3),
                lug_bend=round(lug, 2), lug_reaction_N=round(rl, 1), bush_bearing=round(bush_bear, 2), screw_tension_N=round(t_screw, 1), front_hold_N=round(t_front, 1), spigot_torsion_MPa=round(T / 22.5 / (2 * 22.5 * SPIG_D), 2), screw_MPa=round(t_screw / 5.03, 2),
                engagement=eng, pullout_MPa=round(t_screw / (math.pi * 3.0 * eng), 2), spigot_bearing_MPa=round(math.hypot(FZ, FY) / (2 * 21.8 * SPIG_D) + My / (2 * 21.8) / (2 * 21.8 * SPIG_D), 2))


def hex_report(P):
    sg = P["SideGear_R"]
    top = max(x / 20.0 for x in range(-400, 400) if sg.isInside(V(x / 20.0, 4.97, 0.0), 1e-6, True))
    eng = top - X_TIP - FLOAT
    rc = HEX_SOCK / math.sqrt(3) * 8.0 / HEX_SOCK
    out = dict(engagement=round(eng, 2))
    for T in (T_RING / 2, T_RING):
        out["MPa_at_%d" % round(T)] = round(T / (6 * rc) / (1.0 * eng), 2)
    return out


def clamp_report():
    pts = []
    for k in range(0, 101):
        a = k / 100.0
        pts += [(-XB_END + 2 * XB_END * a, YT), (-XB_END + 2 * XB_END * a, -YT), (XB_END, -YT + 2 * YT * a), (-XB_END, -YT + 2 * YT * a)]
    pts += [(-BLK_HW + 2 * BLK_HW * a / 10, Y_BLK) for a in range(11)] + [(0.0, Y_BLK), (BLK_HW, Y_BLK), (-BLK_HW, Y_BLK)]
    d = max(min(math.hypot(x - cx, y - cy) for cx, cy in CLOSE_POS) for x, y in pts)
    return round(d, 1)


def neck_stress():
    T = T_RING / 2
    d = 2 * R_NECK
    return dict(T=T, tau=round(16 * T / (math.pi * d ** 3), 2), tau_full_ring=round(16 * T_RING / (math.pi * d ** 3), 2))


def lowest_point(objs):
    return min(s.optimalBoundingBox(False, False).ZMin for n, s in objs.items() if not any(k in n for k in ("Tyre", "Wheel")))


def overlaps(objs, pairs_skip=()):
    out = []
    names = list(objs)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            if (a, b) in pairs_skip or (b, a) in pairs_skip:
                continue
            v = vol(objs[a], objs[b])
            if v > 1e-3:
                out.append((a, b, round(v, 3)))
    return out


def car_hub_refs(P, fast=False):
    """kit parts in assembled position: narrow arm on the -x side with the DoubleFork, wide arm on the +x side with the ShortLink"""
    refs = {}
    for tag, Lk, left in (("N", L_N, True), ("W", L_W, False)):
        for n, s in hub_refs(Lk).items():
            refs["Ref_%s_%s" % (tag, n.replace("Ref_", ""))] = to_car(s, Lk, left)
    return refs


def verify(P, R, blanks, fast=False):
    t0 = time.time()
    rep = {}
    step = 5.0 if fast else 1.0
    rep["valid"] = {n: (s.isValid(), len(s.Solids), round(s.Volume, 1)) for n, s in P.items()}
    active = {n: s for n, s in P.items() if n not in ("Arm_W", "Arm_N_L")}
    cores = screw_refs(core=True)
    rep["overlap"] = overlaps(dict(active, **cores))
    full = screw_refs()
    rep["hex"], rep["clamp_mm"] = hex_report(P), clamp_report()
    rep["engaged_mm"] = {}
    for n, sc in full.items():
        tot = sum(vol(sc, s_) for s_ in active.values())
        rep["engaged_mm"][n] = round(tot / (math.pi * (1.5 ** 2 - 1.4 ** 2)), 1)
    refs = car_hub_refs(P)
    ref_cores = {n: s for n, s in refs.items()}
    ov = []
    for n, s in refs.items():
        host = "Arm_N" if "_N_" in n else "Arm_W_L"
        for hn in (host, "HousingTop", "HousingBottom", "Keeper_L", "Keeper_R", "PlugShaft_L", "PlugShaft_R"):
            if near(s, P[hn], 1.0):
                v = vol(s, P[hn])
                if v > 1e-3 and not ("Ref_N_PivotScrew" in n or "PivotScrew" in n):
                    ov.append((n, hn, round(v, 3)))
    rep["hub_overlap"] = ov
    print("overlaps done", round(time.time() - t0), flush=True)
    rep["plays"] = measured_plays(P)
    rep["rim"] = carrier_rim(P["Carrier"])
    rep["stack"] = worst_stack(blanks, rep["plays"], fast)
    rep["body_clear"] = body_clear(P, rep["plays"])
    print("stack done", round(time.time() - t0), flush=True)
    rep["contact"] = contact_report(blanks, fast)
    print("contact done", round(time.time() - t0), flush=True)
    rep["teeth"] = teeth_from_solids(P)
    rep["rotation"] = rotation_sweep(P, R, fast)
    rep["keepers"] = keeper_sweeps(P, fast)
    rep["shoulder"] = shoulder_area()
    rep["pfloat"] = pinion_float(P)
    rep["psupport"] = pinion_support(rep["plays"])
    rep["lug"] = lug_match(build_arm(L_N))
    yk = ycyl(9.7, Y_RING_END + PORT_END - YOKE_HEX_DEPTH, Y_RING_END + 40.0)
    rep["yoke_clear"] = round(dist(R["Ref_KeepScrew_P"], yk), 3)
    print("gears done", round(time.time() - t0), flush=True)
    rep["thrust"] = thrust_gaps(P)
    rep["nose_gap"] = nose_gaps(P)
    rep["stub"] = stub_pilot_report(P["JournalStub"])
    rep["clear"] = clearance_table(P, fast)
    print("clear done", round(time.time() - t0), flush=True)
    rep["steps"] = assembly_steps(P, R, step)
    print("steps done", round(time.time() - t0), flush=True)
    rep["joint_steps"] = joint_steps(P, refs, step)
    print("joint steps done", round(time.time() - t0), flush=True)
    rep["strength"] = {"N": arm_strength(L_N), "W": arm_strength(L_W), "neck": neck_stress()}
    rep["arms"] = {}
    for tag, Lk in (("N", L_N), ("W", L_W)):
        arm = build_arm(Lk)
        st = hub_statics(P, Lk)
        ent = dict(joint=joint_clear(Lk, arm, {k: v for k, v in st.items() if k not in ("PlugShaft_L", "Cap", "Carrier")}))
        angs = [-28.0, 0.0, 28.0] if fast else [-28.0, -20.0, -10.0, 0.0, 10.0, 20.0, 28.0]
        ent["steer"], ent["stops"] = steer_clear(Lk, arm, st, angs)
        if not fast:
            P2, R2 = hub_frame_parts(Lk, arm)
            ent["hub_assembly"] = H["assembly"](P2, R2)
        rep["arms"][tag] = ent
        print("arm", tag, "done", round(time.time() - t0), flush=True)
    low = lowest_point(dict(active, **refs))
    rep["ground"] = dict(lowest=round(-low, 2), clearance=round(55.0 + low, 2))
    rep["mount_plane_z"] = AP_OUT
    rep["tracks"] = {t: dict(track=round(2 * (Lk + 11.69), 1), over_tyres=round(2 * (Lk + 24.69), 1), over_hubs=round(2 * (Lk + 37.8), 1)) for t, Lk in (("N", L_N), ("W", L_W))}
    if not fast:
        rep["print"] = print_checks(P)
        print("print done", round(time.time() - t0), flush=True)
    return rep


FROZEN = dict(HousingTop=41294.4, HousingBottom=38644.7, Pinion=2583.4, SideGear_R=966.4, SideGear_L=966.4, SpiderGear_1=913.4, SpiderGear_2=913.4, PlugShaft_R=3285.3, PlugShaft_L=3285.3, PinionShaft=4114.2, Keeper_R=400.5, Keeper_P=265.3, JournalRing=8790.3, JournalStub=12417.8)


def carrier_rim(c):
    out = 9.0
    for x in (-1.0, 5.0, 10.0):
        for sg in (1, -1):
            y = 18.0
            while y < 22.0 and not c.isInside(V(x, sg * y, 0.0), 1e-6, True):
                y += 0.02
            y0 = y
            while y < 24.0 and c.isInside(V(x, sg * y, 0.0), 1e-6, True):
                y += 0.02
            out = min(out, y - y0)
    return round(out, 2)


def check(rep, fast=False):
    for n, v in FROZEN.items():
        assert abs(rep["valid"][n][2] - v) < 0.25, (n, rep["valid"][n][2], v)
    assert (BOSS_OD - BOSS_ID) / 2 - 0.1 >= 1.1
    assert rep["rim"] >= 1.19, rep["rim"]
    assert all(v[0] and v[1] == 1 for v in rep["valid"].values()), rep["valid"]
    ok_thread = [o for o in rep["overlap"] if not (o[0].startswith("Ref_") or o[1].startswith("Ref_"))]
    assert not ok_thread, ok_thread
    assert all(o[2] < 0.1 or (("CloseScrew" in o[1] and o[2] < 1.3) or ("CapScrew" in o[1] and o[2] < 1.6)) for o in rep["overlap"]), rep["overlap"]
    assert all(v >= 5.9 for v in rep["engaged_mm"].values()), rep["engaged_mm"]
    assert not rep["hub_overlap"], rep["hub_overlap"]
    assert rep["hex"]["engagement"] >= 6.0 and rep["hex"]["MPa_at_607"] <= 8.0, rep["hex"]
    assert rep["clamp_mm"] <= 35.0, rep["clamp_mm"]
    assert all(v < 1e-3 for v in rep["joint_steps"].values()), rep["joint_steps"]
    for k, d in rep["contact"].items():
        assert d["missing"] == 0 and d["variation"] <= 0.15, (k, d)
    pl_ = rep["plays"]
    assert 0.25 <= pl_["hex_socket"] / 1.1547 <= 0.3, pl_
    assert pl_["plug_journal"] >= 0.25 and pl_["pinion_journal"] >= 0.25 and pl_["boss"] >= 0.25 and pl_["spider_bore"] >= 0.3 and 0.1 <= pl_["pin_seat"] <= 0.15, pl_
    for k, d in rep["stack"].items():
        assert min(d["axial"].values()) >= 0.6, (k, "axial only", d["axial"])
        if k == "side" and min(d["worst"].values()) < 0.3:
            OPEN.append("side gear/spider full play box corner %s < 0.3 (side gear is located by hex and boss in series, %.2f mm radial; a carrier-located counterbore or groove fails the print bridge rule)" % (d["worst"], rep["plays"]["side_radial"]))
        else:
            assert min(d["worst"].values()) >= 0.3, (k, "full play box corner", d["worst"])
    assert all(v["sigma"] <= SIGMA_MAX for v in rep["teeth"].values()), rep["teeth"]
    assert rep["rotation"]["overlap"] < 1e-3 and min(v for k, v in rep["rotation"]["dist"].items() if k.startswith("Ref_")) >= 0.8 and min(rep["rotation"]["dist"].values()) >= 0.6, rep["rotation"]
    assert min(rep["keepers"].values()) >= 0.29, rep["keepers"]
    sh = rep["shoulder"]
    assert sh["outer_mm2"] >= 10.0 and sh["neck_tau_607"] <= 8.0, sh
    assert 80.0 / sh["outer_mm2"] <= 8.0 and 40.0 / sh["inner_mm2"] <= 8.0, sh
    pf = rep["pfloat"]
    assert pf["toward_back"] <= 0.16 and pf["toward_toe"] <= 0.02 and pf["pinion_axial_range"] <= 0.31, pf
    ps_ = rep["psupport"]
    assert ps_["mesh_motion_bearing"] <= 0.5 and ps_["beam_deflection_at_mesh"] <= 0.3, ps_
    assert all(abs(v) < 1e-3 for v in rep["lug"].values()), rep["lug"]
    assert rep["yoke_clear"] >= 0.79, rep["yoke_clear"]
    assert rep["body_clear"] >= 0.3, rep["body_clear"]
    assert rep["nose_gap"] >= 0.0, rep["nose_gap"]
    assert rep["stub"]["depth"] >= 8.0 and rep["stub"]["wall"] >= 1.6 and rep["stub"]["solid_beyond"] >= 1.0, rep["stub"]
    th = rep["thrust"]
    for k, v in th.items():
        assert 0.13 <= v <= 0.2, (k, v)
    for (a, b), v in rep["clear"].items():
        lim = 0.19 if b.startswith("Sleeve") else (0.14 if b.startswith("Keeper") else MIN_GAP)
        assert v >= lim, (a, b, v)
    assert all(v < 1e-3 or ((k.startswith("09") and v < 1.3) or (k.startswith("05") and v < 1.6)) for k, v in rep["steps"].items() if k != "bundle_angles"), rep["steps"]
    assert any(max(v) < 1e-3 for v in rep["steps"]["bundle_angles"].values()), rep["steps"]["bundle_angles"]
    for tag, e in rep["arms"].items():
        assert e["stops"] == (27.97, 27.97), e["stops"]
        assert min(min(r["Wheel"], r["Tyre"]) for r in e["steer"].values()) >= 2.0, e["steer"]
        assert e["joint"]["Arm"] >= 0.8 and e["joint"]["Keeper_L"] >= 0.8 and e["joint"]["HousingTop"] >= 0.8, e["joint"]
        if "hub_assembly" in e:
            h = e["hub_assembly"]
            assert all(v < 1e-3 for k, v in h.items() if k[0].isdigit()) and not any(h["final_core_overlaps"].values()), h
    for t in ("N", "W"):
        s = rep["strength"][t]
        assert s["sigma_root"] <= 15 and s["tau_torsion"] <= 8 and s["lug_bend"] <= 8 and s["bush_bearing"] <= 8 and s["screw_MPa"] <= 200 and s["pullout_MPa"] <= 8 and s["engagement"] >= 6, s
    assert rep["strength"]["neck"]["tau"] <= 8
    assert rep["ground"]["lowest"] <= 30.5, rep["ground"]
    if "print" in rep:
        for n, r in rep["print"].items():
            assert not r["slopes"], (n, r["slopes"][:5])
            assert r["nlayers"] == 0, (n, r["layers"])
            assert not r["islands"], (n, r["islands"][:6])
            assert r["bed"] >= 60.0 or n.startswith("Sleeve"), (n, r["bed"])
            assert r["tall"] <= 4.0 and r["thin"] <= 1.0, (n, r["tall"], r["thin"])


def put(doc, name, shape):
    assert shape.isValid() and len(shape.Solids) == 1, name
    o = doc.addObject("Part::Feature", name)
    o.Shape = shape
    return o


def main():
    t0 = time.time()
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    P, blanks = assemble()
    R = screw_refs()
    rep = verify(P, R, blanks, FAST)
    print("REPORT", rep, flush=True)
    check(rep, FAST)
    print("OPEN", OPEN, flush=True)
    if "print" in rep:
        tot = 0.0
        for n, r in rep["print"].items():
            members = [m for m in [n] + r["twins"] if m not in ("Arm_W", "Arm_W_L")]
            tot += r["volume"] * len(members)
            print("TABLE %-14s up %s size %s cm3 %.2f copies %d (%s) bed %.0f" % (n, PRINT_UP[n], r["size"], r["volume"], len(members), ",".join(members), r["bed"]), flush=True)
        print("TOTAL plastic per axle (default plate, narrow arms, incl. placeholder liners) cm3 %.1f" % tot, flush=True)
    for n, s in P.items():
        if n == "Arm_W":
            s = mv(s, 0, 0, 100)
        if n == "Arm_N_L":
            s = mv(s, 0, 0, 160)
        put(doc, n, s)
    for n, s in R.items():
        put(doc, n, s)
    for n, s in car_hub_refs(P).items():
        put(doc, n, s)
    doc.recompute()
    doc.saveAs(OUT)
    print("saved", OUT, round(time.time() - t0), flush=True)
    return doc



def joint_steps(P, refs, step=2.0):
    """plug side joint: the arm with the hub unit and the far cross on the DoubleFork or link slides onto the housing end face and the plug fork, then pin D from the rear and the arm screws with the hub unit in place (no wheel)"""
    out = {}
    drv = drivers()
    cores = screw_refs(core=True)
    for tag, arm, plug, keep, sg, pre in (("N", "Arm_N", "PlugShaft_L", "Keeper_L", -1, "Ref_N_"), ("W", "Arm_W_L", "PlugShaft_R", "Keeper_R", 1, "Ref_W_")):
        mine = {n: s for n, s in refs.items() if n.startswith(pre) and not any(k in n for k in ("Wheel", "Tyre", "HubScrew", "HubWasher", "PinD"))}
        mov = dict(mine, arm=P[arm])
        fixed = dict(h1=P["HousingTop"], h2=P["HousingBottom"], plug=P[plug], keep=P[keep], jr=P["JournalRing"], js=P["JournalStub"])
        out["%s_unit_onto_plug" % tag] = sweep(mov, fixed, sg * X, 60.0, step)
        pf = refs[pre + "PinD"]
        pind = H["core"](V(pf.BoundBox.Center.x, pf.BoundBox.YMin + 3.0, pf.BoundBox.Center.z), Y, 20.0, 5.5, 3.0)
        d = driver(V(pf.BoundBox.Center.x, pf.BoundBox.YMin, pf.BoundBox.Center.z), -Y)
        fixed2 = dict(fixed, **mov)
        out["%s_pinD_from_rear" % tag] = sweep({"p": pind, "d": d}, fixed2, -Y, 60.0, step)
        fixed2["pinD"] = pind
        side = "R" if sg > 0 else "L"
        out["%s_arm_screws_hub_in_place" % tag] = max(sweep({n: cores[n], n + "_d": drv[n][0]}, fixed2, drv[n][1], 60.0, step) for n in cores if n.startswith("Ref_ArmScrew_" + side))
    return out


def section_stress(blank, N, m, delta, face, torque, share=1.0):
    """Lewis root bending cut from a solid: slice the toothed solid at mid face, take the tooth thickness at the root fillet tangent (one fillet radius above the root circle) over the material arc fraction, height from there to the tip along the cone normal, real face width, load at the tip"""
    from shapely.geometry import Polygon, Point
    rc = m / 2 * N / math.sin(delta)
    zt, z0 = (rc - face) * math.cos(delta), rc * math.cos(delta)
    zm = (zt + z0) / 2
    ws = blank.slice(Z, zm)
    w = max(ws, key=lambda e: e.BoundBox.XLength)
    pts = [(v.x, v.y) for v in w.discretize(Deflection=0.005)]
    poly = Polygon(pts).buffer(0)
    rr = [math.hypot(x, y) for x, y in pts]
    rf, rt = min(rr), max(rr)
    r0 = rf + FILLET_R * zm / z0
    n = 7200
    inside = sum(poly.contains(Point(r0 * math.cos(2 * math.pi * k / n), r0 * math.sin(2 * math.pi * k / n))) for k in range(n))
    s = inside / n * 2 * math.pi * r0 / N
    h = (rt - r0) * math.cos(delta)
    rp = zm * math.tan(delta)
    ft = torque / rp * share
    return dict(sigma=6 * ft * h / (face * s * s), s=s, h=h, ft=ft, face=face, rf=rf, rt=rt)


def max_r(shape, axis, c0, c1):
    """largest distance from the axis of any vertex of the shape between c0 and c1 along the axis"""
    lo, hi = (0, 1)
    box_ = box(-40, 40, c0, c1, -40, 40) if axis == "y" else box(c0, c1, -40, 40, -40, 40)
    cut = shape.common(box_)
    return max(math.hypot(v.X, v.Z) if axis == "y" else math.hypot(v.Y, v.Z) for v in cut.Vertexes)


def travel(shape, axis, c, R, dirs):
    """contact bisection in closed form: how far the section of the shape at c can slide in each unit direction before a point leaves the bore of radius R about the axis"""
    pts = []
    for w in shape.slice(X if axis == "x" else Y, c):
        pts += [((v.y, v.z) if axis == "x" else (v.x, v.z)) for v in w.discretize(Deflection=0.01)]
    out = {}
    for name, u in dirs.items():
        out[name] = min(-(p[0] * u[0] + p[1] * u[1]) + math.sqrt(max(0.0, (p[0] * u[0] + p[1] * u[1]) ** 2 + R * R - p[0] ** 2 - p[1] ** 2)) for p in pts)
    return out


def measured_plays(P):
    """real radial play from the solids: liner bore radius 5.0 minus the largest radius of the journal in the liner, boss bore minus hex corner, socket circumradius minus hex corner"""
    pj = max_r(P["PinionShaft"], "y", 33.2, 33.3)
    gj = max_r(P["PlugShaft_R"], "x", 22.3, 22.4)
    hx = max_r(P["PlugShaft_R"], "x", 9.0, 9.1)
    jb = max_r(P["PlugShaft_R"], "x", 13.3, 13.4)
    pin = max_r(P["SpiderPin"], "y", -0.1, 0.1)
    span, over = (YE_END - LIP_T2) - (YB_ZERO + LIP_T2), (YB_ZERO + LIP_T2) - (Z_PIN_TOE + Z_PIN) / 2
    pl = dict(pinion_journal=5.0 - pj, plug_journal=5.0 - gj, boss=BOSS_ID / 2 - jb, hex_socket=HEX_SOCK / math.sqrt(3) - hx, spider_bore=SPI_BORE / 2 - pin, pin_seat=SEAT_D / 2 - pin, span=span, overhang=over)
    dirs = {"+a": (1, 0), "-a": (-1, 0), "+b": (0, 1), "-b": (0, -1)}
    tp = travel(P["PinionShaft"], "y", 33.25, 5.0, dirs)
    tg = travel(P["PlugShaft_R"], "x", 22.35, 5.0, dirs)
    tb1, tb2 = travel(P["PlugShaft_R"], "x", 11.5, BOSS_ID / 2, dirs), travel(P["PlugShaft_R"], "x", 13.4, BOSS_ID / 2, dirs)
    tb = {k: min(tb1[k], tb2[k]) for k in dirs}
    k = 1 + 2 * over / span
    pl["pinion_mesh"] = pl["pinion_journal"] * k
    pl["pm_x"], pl["pm_z"] = max(tp["+a"], tp["-a"]) * k, max(tp["+b"], tp["-b"]) * k
    pl["car_y"] = max(tg["+a"], tg["-a"]) + max(tb["+a"], tb["-a"])
    pl["car_z"] = max(tg["+b"], tg["-b"]) + max(tb["+b"], tb["-b"])
    pl["carrier_radial"] = pl["plug_journal"] + pl["boss"]
    pl["side_radial"] = pl["hex_socket"] + pl["boss"]
    pl["spider_radial"] = pl["spider_bore"] + pl["pin_seat"]
    return {k: round(v, 3) for k, v in pl.items()}


def contact_sweep(ga, gb, pa, pb, steps):
    """drive gear a through its angles; for each, rotate follower b from the centred mesh until the solids touch on either flank: backlash angle (follower degrees) = gap between the two touching angles"""
    out = []
    for a in steps:
        A = pa(ga, a)
        ends = []
        for sg in (1, -1):
            lo, hi, s = 0.0, None, 0.0
            while s < 40.0:
                s += 1.5
                if vol(A, pb(gb, a, sg * s)) > 1e-3:
                    hi = s
                    break
                lo = s
            if hi is None:
                ends.append(None)
                continue
            for _ in range(8):
                mid = (lo + hi) / 2
                if vol(A, pb(gb, a, sg * mid)) > 1e-3:
                    hi = mid
                else:
                    lo = mid
            ends.append(sg * lo)
        out.append(None if None in ends else ends[0] - ends[1])
    return out


def contact_report(blanks, fast=False):
    st = 3.0 if fast else 1.0
    res = {}
    for name, ga, gb, pa, pb, pitch in (
            ("final", blanks["ring"], blanks["pin"], lambda sh, a: rotx(ring_place(sh), a), lambda sh, a, s: roty(pin_place(sh), PH_PIN + a * RN / PN + s), 360.0 / RN),
            ("side", blanks["side"], blanks["side"], lambda sh, a: rotx(rot(sh, Y, 90), a), lambda sh, a, s: roty(rot(sh, X, -90), SPIDER_PH - a - s), 360.0 / SN)):
        steps = [i * st for i in range(int(pitch / st) + 1)]
        bl = contact_sweep(ga, gb, pa, pb, steps)
        v = [b for b in bl if b is not None]
        res[name] = dict(n=len(bl), missing=len(bl) - len(v), backlash_min=round(min(v), 2), backlash_max=round(max(v), 2), variation=round(max(v) - min(v), 3))
    return res


def body_clear(P, pl):
    """real Carrier and Pinion solids over the corners of the directional play box (larger directional travel of each fit, summed in series, plus the 0.15 floats): smallest whole-solid gap"""
    import itertools
    box_ = (pl["pm_x"] + FLOAT, FLOAT + pl["car_y"], pl["pm_z"] + pl["car_z"])
    m = 99.0
    body = P["Carrier"].common(box(-9.5, 13.0, -40, 40, -40, 40))
    for d in itertools.product((-1, 0, 1), repeat=3):
        if d[1] == 0 and d != (0, 0, 0):
            continue
        m = min(m, dist(body, mv(P["Pinion"], *[d[i] * box_[i] for i in range(3)])))
    return round(m, 3)


def worst_stack(blanks, pl, fast=False):
    """ring/pinion and side/spider flank gap, tip to root both ways and whole-solid gap with every part at the corners of its real float and radial play (relative offset box, 27 corners, several mesh phases)"""
    import itertools
    out = {}
    cases = []
    pr = Pair(blanks["ring"], blanks["pin"], dict(delta=DELTA_R), dict(delta=DELTA_P), zone_lo=HA_R - 0.5)
    pr.zb = blanks["pin"].common(prof_zone(DELTA_P, HA_P - 0.5, 99.0))
    pr.za = blanks["ring"].common(prof_zone(DELTA_R, HA_R - 0.5, 99.0))
    pa = lambda sh, a: rotx(ring_place(sh), a)
    pb = lambda sh, a: roty(pin_place(sh), PH_PIN + a * RN / PN)
    rg = (pl["pinion_mesh"] + FLOAT, FLOAT + pl["carrier_radial"], pl["pinion_mesh"] + pl["carrier_radial"])
    cases.append(("final", pr, pa, pb, rg, (0.0, 5.0, 10.0, 15.0)))
    sd = blanks["side"]
    ps = Pair(sd, sd, dict(delta=DELTA_S), dict(delta=DELTA_S))
    ps.za = sd.common(prof_zone(DELTA_S, HA_S - 0.5, 99.0))
    ps.zb = ps.za
    ps.fa = sd.common(prof_zone(DELTA_S, -1.0, 1.0))
    ps.fb = ps.fa
    sa = lambda sh, a: rotx(rot(sh, Y, 90), a)
    sb = lambda sh, a: roty(rot(sh, X, -90), SPIDER_PH - a)
    rs = (pl["spider_radial"] + FLOAT, FLOAT + pl["side_radial"], pl["spider_radial"] + pl["side_radial"])
    pitch = 360.0 / SN
    cases.append(("side", ps, sa, sb, rs, (0.0, pitch / 4, pitch / 2, 3 * pitch / 4)))
    for name, prr, fa_, fb_, r3, phases in cases:
        nom = pair_metrics(prr, fa_, fb_, 0, 0, phases[0])
        w = dict(whole=9.0, flank=9.0, tip_a=9.0, tip_b=9.0)
        n = 0
        for a in (phases[:2] if fast else phases):
            for d in itertools.product((-1, 0, 1), repeat=3):
                if fast and sum(abs(v) for v in d) < 2:
                    continue
                m = pair_metrics(prr, fa_, fb_, 0, 0, a, db=tuple(d[i] * r3[i] for i in range(3)))
                n += 1
                if m["ov"] > 1e-3:
                    w = {k: min(w[k], -m["ov"]) for k in w}
                else:
                    w = {k: min(w[k], m[k]) for k in w}
        ax = dict(whole=9.0, flank=9.0, tip_a=9.0, tip_b=9.0)
        for a in (phases[:2] if fast else phases):
            for d in itertools.product((-1, 0, 1), (-1, 0, 1), (0,)):
                m = pair_metrics(prr, fa_, fb_, 0, 0, a, db=(d[0] * FLOAT, d[1] * FLOAT, 0.0))
                ax = {k: min(ax[k], -m["ov"] if m["ov"] > 1e-3 else m[k]) for k in ax}
        out[name] = dict(nominal={k: nom[k] for k in w}, worst=w, axial=ax, offsets=tuple(round(v, 2) for v in r3), n=n)
    return out


def teeth_from_solids(P):
    out = {}
    out["ring"] = section_stress(rot(P["Carrier"], Y, 90), RN, FM, DELTA_R, FACE_F, T_RING)
    out["pinion"] = section_stress(rot(rot(P["Pinion"], Y, -PH_PIN), X, 90), PN, FM, DELTA_P, FACE_F, T_RING * PN / RN)
    out["side"] = section_stress(rot(P["SideGear_R"], Y, -90), SN, SM, DELTA_S, FACE_S, T_RING / 2, 0.5)
    out["spider"] = section_stress(rot(rot(P["SpiderGear_1"], Y, -SPIDER_PH), X, 90), SN, SM, DELTA_S, FACE_S, T_RING / 2, 0.5)
    return {k: {kk: round(v, 2) for kk, v in d.items() if kk in ("sigma", "s", "h", "ft", "face")} for k, d in out.items()}


def housing_region(P):
    b, t = build_housing_halves(False)
    h = b.fuse(t)
    return h.common(box(-26, 26, -33, 33, -33, 33))


def rotation_sweep(P, R, fast=False):
    """every part and Ref that turns with the carrier, full turn: overlap every 3 degrees, distance to the fixed housing every 15"""
    reg = housing_region(P)
    grp = {n: P[n] for n in ("Carrier", "Cap", "SideGear_L", "SideGear_R", "SpiderGear_1", "SpiderGear_2", "SpiderPin")}
    grp.update({n: R[n] for n in R if n.startswith("Ref_CapScrew")})
    ov, dmin = 0.0, {n: 99.0 for n in grp}
    for a in range(0, 360, 15 if fast else 3):
        for n, sh in grp.items():
            t = rotx(sh, float(a))
            ov = max(ov, vol(t, reg))
            if a % 15 == 0 and near(t, reg, 3.0):
                dmin[n] = min(dmin[n], dist(t, reg))
    return dict(overlap=round(ov, 4), dist={k: round(v, 3) for k, v in dmin.items()})


def keeper_sweeps(P, fast=False):
    """each shaft neck turned through 360 degrees at the three float positions against its keeper: radial clearance of the neck, face gaps at the float ends"""
    res = {}
    for sh, kp, ax, c0, c1 in (("PlugShaft_R", "Keeper_R", X, X_G0 + 0.3, X_G1 - 0.3), ("PlugShaft_L", "Keeper_L", X, -(X_G1 - 0.3), -(X_G0 + 0.3)), ("PinionShaft", "Keeper_P", Y, X_G0y() + 0.3, X_G1y() - 0.3)):
        s0 = P[sh]
        axn = "y" if ax == Y else "x"
        bx = box(-40, 40, c0, c1, -40, 40) if axn == "y" else box(c0, c1, -40, 40, -40, 40)
        neck = s0.common(bx)
        w = 99.0
        for f in ((0.0,) if fast else (-FLOAT, 0.0, FLOAT)):
            for a in range(0, 360, 30 if fast else 15):
                t = neck.copy()
                t.rotate(O, ax, float(a))
                t.translate(ax * f)
                w = min(w, dist(t, P[kp]))
        res[sh] = round(w, 3)
    return res


def shoulder_area():
    from shapely.geometry import Point, Polygon
    from shapely.ops import unary_union
    r, flat = R_J, BED_Z
    yf, t = r * math.sqrt(2) - abs(flat), r / math.sqrt(2)
    wedge = Polygon([(-yf, flat), (yf, flat), (t, -t), (0, 0), (-t, -t)])
    sec = unary_union([Point(0, 0).buffer(r, 64), wedge]).intersection(Polygon([(-9, flat), (9, flat), (9, 9), (-9, 9)]))
    slot = unary_union([Point(0, 0).buffer(KEEP_SLOT_R, 64), Polygon([(-KEEP_SLOT_R, -9), (KEEP_SLOT_R, -9), (KEEP_SLOT_R, 0), (-KEEP_SLOT_R, 0)])])
    inner = sec.difference(slot).area
    sec2 = unary_union([Point(0, 0).buffer(R_FLANK, 64), Polygon([(-(R_FLANK * 1.414 - 4), flat), (R_FLANK * 1.414 - 4, flat), (R_FLANK / 1.414, -R_FLANK / 1.414), (0, 0), (-R_FLANK / 1.414, -R_FLANK / 1.414)])]).intersection(Polygon([(-9, flat), (9, flat), (9, 9), (-9, 9)]))
    outer = sec2.difference(slot).area
    return dict(inner_mm2=round(inner, 1), outer_mm2=round(outer, 1), neck_tau_607=round(16 * T_RING / (math.pi * (2 * R_NECK) ** 3), 2))


def pinion_float(P):
    hh = P["HousingTop"].fuse(P["HousingBottom"])
    pos, neg = D["travel"](P["Pinion"], Y, [hh, P["PinionShaft"]], 1.0)
    sp_, sn_ = D["travel"](P["PinionShaft"], Y, [hh, P["Keeper_P"]], 1.0)
    return dict(toward_back=pos, toward_toe=neg, shaft_float=2 * FLOAT, total_vs_housing=round(pos + neg + 0.0, 3), pinion_axial_range=round(pos + sn_, 3))


def pinion_support(pl):
    """mesh point motion from bearing play and beam deflection under 40 N separating force (cantilever beam from the front wall, section cut from the keel polygon)"""
    from shapely.geometry import Polygon
    keel = Polygon([(-8.5, 0), (8.5, 0), (1, -7.5), (1, -AP_OUT), (-1, -AP_OUT), (-1, -7.5)])
    # bending about x (vertical load): I = integral z^2 dA about the centroid, polygon moments
    cx, cz = keel.centroid.x, keel.centroid.y
    c = list(keel.exterior.coords)
    Ix = 0.0
    for (x0, z0), (x1, z1) in zip(c[:-1], c[1:]):
        a = x0 * z1 - x1 * z0
        Ix += a * ((z0 - cz) ** 2 + (z0 - cz) * (z1 - cz) + (z1 - cz) ** 2)
    Ix = abs(Ix) / 12.0
    E, F = 2500.0, 40.0
    ym, y1, y2, yw = (Z_PIN_TOE + Z_PIN) / 2, (YB_ZERO + LIP_T2 + PK_L2 / 2), (YB_ZERO + 2 * LIP_T2 + 1.5 * PK_L2), YT
    L = y2 - y1
    a = y1 - ym
    r2, r1 = F * a / L, F * (1 + a / L)
    d1, d2 = y1 - yw, y2 - yw
    dl1 = (r1 * d1 ** 3 / 3 - r2 * d1 ** 2 * (3 * d2 - d1) / 6) / (E * Ix)
    dl2 = (r1 * d1 ** 2 * (3 * d2 - d1) / 6 - r2 * d2 ** 3 / 3) / (E * Ix)
    slope = (dl2 - dl1) / L
    dm = abs(dl1 - slope * (y1 - ym))
    di = math.pi / 64 * (2 * R_J) ** 4
    dsh = F * a * a * (L + a) / (3 * E * di)
    return dict(I_keel_mm4=round(Ix), span_mm=round(pl["span"], 2), overhang_mm=round(pl["overhang"], 2), mesh_motion_bearing=pl["pinion_mesh"], beam_deflection_at_mesh=round(dm, 4), shaft_deflection=round(dsh, 4))


def lug_match(arm_hub):
    """the arm lug region against the HubCarrier it copies, same bores, counterbores, stops, lock hole: volume difference in the lug regions"""
    hc = H["build_carrier"]()
    out = {}
    for tag, bx in (("upper_lug", box(-5.2, 5.0, -8.0, 16.5, 15.0, 40)), ("lower_lug", box(-5.2, 5.0, -8.0, 16.5, -40, -15.0)), ("lock_lug", box(-14.0, -5.2, -8.0, 16.5, -40, 0.0))):
        out[tag] = round(hc.common(bx).Volume - arm_hub.common(bx).Volume, 3)
    return out


if "NO_RUN" not in globals():
    main()
