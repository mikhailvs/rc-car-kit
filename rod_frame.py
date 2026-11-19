# Rod frame module (rev 5) for the RC car kit: two 8 mm carbon rods (495 long, x +-28.6) carry two identical axle carriers (outer + inner bracket + 2 caps each) and the GearboxCradle.
# Frame axes = gearbox frame: y fore-aft (+y forward), z up, gearbox through shaft on x=0,z=0. Axle frame: x lateral, y input port side +y, origin on the pinion axis (axle.py).
# Layout: ports face the gearbox, ShortLink each side, wheelbase from measured port tips. Front axle = rear axle turned 180 degrees about z.
# Rods end 23.9 past each axle origin (rod length 495, wheelbase/2 - 247.5); the outer clamps hold them from the rod end to 2.0 short of the slit end, 22.1 mm of rod, and a cross screw (stop) sits 5.1 beyond the rod end.
# ASSEMBLY ORDER: 1 brackets and cradle slide onto the rods, rods in from the front, then the cross stop screws (rear pair before the rods go in, FRONT pair after the rods are in, heads outboard so the driver runs straight out); 2 car on its back: pads on the housing, SeatCups on the domes, axles lifted into the upper half bores, caps and M3x12 from below; 3 springs along their axes into pin and cup; 4 shafts fitted with their yoke screws; 5 ONLY THEN inner bracket and cradle clamps tightened (the rigid shafts set the spacing: tip to tip 69.142 against a 68.942 stack, axle float 0.2). Removal: shaft off its port first (with the shaft in place PinionShaft and yoke overlap for the first 12 mm of the drop), springs off by hand, four caps off, axle drops.
# Carrier: the INNER bracket (input side) holds the JournalRing in an UPPER half bore (cone rim on the housing side 0.2, flat collar face 0.2) and clamps both rods; the OUTER bracket carries the JournalStub radially (0.8 end gaps, 7.8 wide) and
# hangs from the rod ends by two cantilever arms (rods end 24 mm past the axle origin, the stub is 46 past). Caps (lower half bores, 2 x M3x12 each, fitted from below) take spring preload and rebound.
# Springs: one per side, TANGENT layout (axis tangent to the arc the pad seat travels, about 77 deg from vertical), crossing the centre line at y +-7; pad end = pin on a wedge pad (pad bolted on housing top pilots), frame end = cup in a boss hanging from the opposite arm.
# Stops: flat faces on blocks under each arm meeting the housing top flat at the stop angle (compression in the layers). Print: brackets and caps stand on y, pads and cradle on z, supports off.
# Bench steps: 1 rods through carriers and cradle; 2 clamp screws; 3 car on its back, pads on housing top (M3x8 into pilots), axle up into the upper half bores, caps and M3x12; 4 springs along their axes into pin and cup; 5 shafts and yoke screws. Axle comes out by removing the four caps (springs lifted off first).
import FreeCAD as App, Part, math, os, sys, time
import numpy as np
from shapely.geometry import MultiLineString, Point, Polygon, LineString, box as _sbox
from shapely.ops import linemerge, unary_union
from shapely import affinity

FAST = bool(os.environ.get("RF_FAST"))
V = App.Vector
O = V(0, 0, 0)
X, Y, Z = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
HERE = "/home/mikhail/Documents/cad/RC Car/"
AXLE_DIR = os.environ.get("RF_AXLE_DIR", HERE)
OUT = os.environ.get("RF_OUT", HERE + "RodFrame.FCStd")
UPV = {"+X": X, "-X": V(-1, 0, 0), "+Y": Y, "-Y": V(0, -1, 0), "+Z": Z, "-Z": V(0, 0, -1)}
P1_COS, FLAT_COS = math.cos(math.radians(45.0)) + 1e-4, 0.9999
SAG_MAX, HOLE_R_MAX, BRIDGE_MAX, LAYER, FIRST_WALL, BED_MIN, TALL_MAX = 0.3, 3.0, 10.0, 0.2, 0.8, 60.0, 4.0
HEAD_D, HEAD_H, WASHER_D, WASHER_ID, WASHER_T, SCREW_D = 6.0, 3.2, 7.0, 3.2, 0.5, 3.0
NUT_AF, NUT_POCKET_AF, NUT_T = 5.5, 6.1, 2.4
PASS_D, TAP_D = 3.6, 2.8
PRINT_UP = {}
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

def prism_g(g, y0, y1):
    out = None
    for p in getattr(g, "geoms", [g]):
        s = prism_xz(list(p.exterior.coords)[:-1], y0, y1)
        for h in p.interiors:
            s = s.cut(prism_xz(list(h.coords)[:-1], y0 - 1, y1 + 1))
        out = s if out is None else out.fuse(s)
    return out.removeSplitter()


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
    return dict(bed=round(first.area, 1), tall=round(h / min(b[2] - b[0], b[3] - b[1]), 2), thin=round(lost, 2), layers=bad[:60], nlayers=len(bad))


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
    return bad[:60], len(bad)

def gap(a, b, thr):
    ba, bb = a.BoundBox, b.BoundBox
    if (ba.XMin - thr > bb.XMax or bb.XMin - thr > ba.XMax or ba.YMin - thr > bb.YMax or bb.YMin - thr > ba.YMax or ba.ZMin - thr > bb.ZMax or bb.ZMin - thr > ba.ZMax):
        return 99.0
    return a.distToShape(b)[0]




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






# ---------------------------------------------------------------- constants
ROD_D, ROD_BORE, ROD_L = 8.0, 8.5, 495.0
R_BR = ROD_BORE / 2
XR = 28.6
ZR = float(os.environ.get("RF_ZR", "56.0"))
BLK_W, EAR_OUT, T_RING = 1.2, 6.0, 3.6
BLK_X0, BLK_X1 = XR - R_BR - BLK_W, XR + R_BR + EAR_OUT
BLK_Z0, BLK_Z1 = ZR - R_BR - T_RING, ZR + R_BR + T_RING
CAP_R, CAP_R_OUT = 19.0, 20.6
CAP_SX = 16.5
BLK_Z0T, BLK_Z1T = ZR - R_BR - 2.0, ZR + R_BR + 2.0
BLK_X1T = XR + R_BR + 2.0
Y_THICK0, Y_THICK1 = -39.0, 0.0
SLIT = 2.4
CLAMP_F, MU = 60.0, 0.2
ROOF_T, NUT_CL = 2.4, 0.3
JR, JC = 12.0, 15.0
BORE_R = JR + 0.3
TRAVEL = 20.0
WHEEL_X = 83.37
THETA = math.degrees(math.asin(TRAVEL / WHEEL_X))
SPR_OD, SPR_WIRE, SPR_FREE, SPR_SOLID = 9.13, 1.04, 34.9, 13.0
SPR_RATE = float(os.environ.get("RF_RATE", "2.2"))
SPR_BODY = 9.4
XC, ZC = 10.0, 36.2
LMID = 24.3
CUPSEP, DOME_R, DOME_B = 9.5, 7.0, 4.5
YS = 21.5
PIN_R, PIN_L, CUP_R, CUP_D = 2.35, 4.0, 5.65, 4.5
STOP_CLR = 0.05
YIN0, YIN1 = 53.9, 69.5
YOUT0, YOUT1 = -46.1, -38.3
ARM_Y1 = 31.5
BOSS_BOT = 35.0
AXLE_SLIP = 0.2
ROD_END_Y = -23.9
Y_STOP = -29.0
ARCH_R = 17.0
KP = {"N": 71.68, "W": 98.16}
STEER = 27.97
GROUND = 55.0


def mirror_x(s):
    return s.mirror(O, X)


def load_refs():
    R = {}
    for tag, path in (("Axle", AXLE_DIR + "Axle.FCStd"), ("DriveShaft", HERE + "DriveShaft.FCStd"), ("Gearbox3", HERE + "Gearbox3.FCStd")):
        d = App.openDocument(path)
        R[tag] = {o.Name: o.Shape.copy() for o in d.Objects if hasattr(o, "Shape") and o.Shape.Solids}
        App.closeDocument(d.Name)
    return R


def rad(s, y):
    w = s.slice(Y, y)
    return Part.makeCompound(w).BoundBox.XMax if w else 0.0


def measure(R):
    A, DS, GB = R["Axle"], R["DriveShaft"], R["Gearbox3"]
    m = {}
    m["port_y"] = A["PinionShaft"].BoundBox.YMax
    t = GB["ThroughShaft"].BoundBox
    m["gb_y0"], m["gb_y1"] = t.YMin, t.YMax
    m["joff"] = -DS["DummyPort_1"].BoundBox.XMax
    mid = lambda n: (DS[n].BoundBox.XMin + DS[n].BoundBox.XMax) / 2
    m["lcs"] = mid("Shown_JointCross_S2") - mid("Shown_JointCross_S1")
    m["depth"] = DS["DummyPort_1"].BoundBox.XMax - DS["Shown_JointYoke_S1"].BoundBox.XMin
    hb, ht = A["HousingBottom"].BoundBox, A["HousingTop"].BoundBox
    m["hx"], m["hy0"], m["hy1"], m["hz"] = hb.XMax, hb.YMin, hb.YMax, ht.ZMax
    jr, js = A["JournalRing"], A["JournalStub"]
    # asserted journal numbers
    assert abs(m["port_y"] - 87.1) < 0.05 and abs(m["hz"] - 30.25) < 0.01 and abs(m["hy1"] - 53.1) < 0.05 and abs(m["hy0"] + 37.5) < 0.05, m
    assert abs(rad(jr, 58.0) - JR) < 0.05 and abs(rad(jr, 69.0) - JR) < 0.05 and abs(rad(jr, 70.3) - JC) < 0.05 and abs(rad(jr, 54.0) - JC) < 0.05 and abs(rad(jr, 56.0) - 13.3) < 0.1, "ring profile"
    assert abs(rad(js, -42.0) - JR) < 0.05 and abs(rad(js, -47.5) - JC) < 0.05 and abs(rad(js, -35.5) - JR) < 0.1 and abs(rad(js, -37.4) - JR) < 0.05, "stub profile"
    assert abs(jr.BoundBox.YMin - 48.1) < 0.05 and abs(js.BoundBox.YMin + 56.0) < 0.05
    pil = sorted((round(f.Surface.Center.x, 2), round(f.Surface.Center.y, 2)) for f in A["HousingTop"].Faces if f.Surface.__class__.__name__ == "Cylinder" and abs(f.Surface.Radius - 1.4) < 0.01 and abs(f.Surface.Axis.z) > 0.99 and f.BoundBox.ZMax > 29)
    assert set(pil) >= {(22.0, 8.0), (22.0, -8.0), (-22.0, 8.0), (-22.0, -8.0), (8.0, 16.0), (-8.0, 16.0), (8.0, -16.0), (-8.0, -16.0)}, pil
    m["pilots"] = pil
    nar, wid = A["Ref_N_Tyre"].BoundBox, A["Ref_W_Tyre"].BoundBox
    assert abs((nar.XMin + nar.XMax) / 2 + WHEEL_X) < 0.02 and abs(nar.ZMax - GROUND) < 0.01
    m["track_N"] = 2 * WHEEL_X
    m["track_W"] = wid.XMin + wid.XMax
    assert abs(m["joff"] - 12.03) < 0.01 and abs(m["lcs"] - 44.88) < 0.01
    m["pitch"] = m["lcs"] + 2 * m["joff"]
    m["YR"] = m["gb_y0"] - m["pitch"] - m["port_y"] - AXLE_SLIP
    m["YF"] = m["gb_y1"] + m["pitch"] + m["port_y"] + AXLE_SLIP
    m["wheelbase"] = m["YF"] - m["YR"]
    return m


def wheel_directions():
    Rz = lambda a: np.array([[math.cos(a), -math.sin(a), 0], [math.sin(a), math.cos(a), 0], [0, 0, 1]])
    out = []
    for Rm in (Rz(0), Rz(math.pi)):
        w_in = Rm.T @ np.array([0, 1.0, 0])[:]
        xw = Rm @ np.array([1.0, 0, 0])
        out.append(float(xw[0] * w_in[1]))
    assert abs(out[0] - out[1]) < 1e-9 and abs(out[0]) > 0.5, out
    return out[0]


def at_axle(s, axle, M):
    """axle frame to document frame; axle 'R' rear (identity) or 'F' front (turned 180 about z)"""
    s = s.copy()
    if axle == "F":
        s.rotate(O, Z, 180.0)
    s.translate(V(0, M["YR"] if axle == "R" else M["YF"], 0))
    return s


def tilt(s, phi):
    s = s.copy()
    s.rotate(O, Y, -phi)
    return s


def rotkp(s, kx, deg):
    s = s.copy()
    s.rotate(V(kx, 0, 0), Z, deg)
    return s


STEERED = ("Knuckle", "StubYoke", "Wheel", "Tyre", "PivotBush_1", "PivotBush_2", "Sleeve_1", "Sleeve_2", "PivotScrew_U", "PivotScrew_L", "LockScrew", "HubScrew", "HubWasher")


def axle_parts(R, arms, st=0.0):
    """moving group in the axle frame: centre parts + both arm sets ('N' or 'W'), steering st on the right side, -st on the left"""
    A = R["Axle"]
    out = {}
    for n, s in A.items():
        if n.startswith(("Arm_", "Ref_N_", "Ref_W_")):
            continue
        out[n] = s
    pre = "Ref_%s_" % arms
    srcs = {}
    for n, s in A.items():
        if n.startswith(pre):
            srcs[n[len(pre):]] = s
    armname = {"N": ("Arm_N", "N_L"), "W": ("Arm_W_L", "W")}[arms]
    arm_assembled = A["Arm_N"] if arms == "N" else A["Arm_W_L"]
    left_src = arms == "N"   # narrow hub refs sit at -x, wide at +x
    for n, s in srcs.items():
        base = n.replace("_2", "") if n.endswith("_2") else n
        for side in (1, -1):
            sh = s if ((s.BoundBox.XMax > 0) == (side > 0)) else mirror_x(s)
            kx = side * KP[arms]
            ang = st * (1 if side > 0 else -1) if any(n.startswith(k) for k in STEERED) else 0.0
            out["%s_%s%s" % ("Hub" + arms, n, "R" if side > 0 else "L")] = rotkp(sh, kx, ang) if ang else sh
    for side in (1, -1):
        sh = arm_assembled if ((arm_assembled.BoundBox.XMax > 0) == (side > 0)) else mirror_x(arm_assembled)
        out["Arm%s_%s" % (arms, "R" if side > 0 else "L")] = sh
    return out


# ---------------------------------------------------------------- spring kinematics (axle frame, x z plane; right spring at y +YS, left at y -YS)
# the SeatCup sits on a dome of the pad centred C (turns with the axle); the spring line runs from the frame cup seat B to C, seat A is CUPSEP short of C
RA = math.hypot(XC, ZC)
TX, TZ = -ZC / RA, XC / RA
A0 = (XC + CUPSEP * TX, ZC + CUPSEP * TZ)
BXZ = (A0[0] + LMID * TX, A0[1] + LMID * TZ)
TH = math.radians(THETA)


def dome_c(sx, phi):
    x, z = sx * XC, ZC
    c, s = math.cos(math.radians(phi)), math.sin(math.radians(phi))
    return (x * c - z * s, x * s + z * c)


def spring_state(sx, phi):
    c, b = dome_c(sx, phi), (sx * BXZ[0], BXZ[1])
    d = (c[0] - b[0], c[1] - b[1])
    D = math.hypot(*d)
    L = D - CUPSEP
    a = (b[0] + d[0] / D * L, b[1] + d[1] / D * L)
    return a, b, L, c, (d[0] / D, d[1] / D)


def spring_tab():
    k = SPR_RATE
    rows = [(phi, sx, spring_state(sx, phi)) for phi in np.linspace(-THETA, THETA, 9) for sx in (1, -1)]
    Ls = [r[2][2] for r in rows]
    angs, rel = [], []
    for phi, sx, st in rows:
        s0 = spring_state(sx, 0.0)
        angs.append(math.degrees(math.acos(max(-1, min(1, st[4][0] * s0[4][0] + st[4][1] * s0[4][1])))))
    def moment(phi):
        m = 0.0
        for sx in (1, -1):
            a, b, L, c, u = spring_state(sx, phi)
            f = k * (SPR_FREE - L)
            m += c[1] * f * u[0] - c[0] * f * u[1]
        return m
    h = 1e-3
    ks = (moment(h) - moment(-h)) / (2 * h) * 180 / math.pi
    ang_pad = []
    for phi, sx, st in rows:
        c, s_ = math.cos(math.radians(phi)), math.sin(math.radians(phi))
        n = (sx * TX, TZ)
        pa = (c * n[0] - s_ * n[1], s_ * n[0] + c * n[1])
        ax = (-st[4][0], -st[4][1])
        ang_pad.append(abs(math.degrees(math.atan2(ax[0] * pa[1] - ax[1] * pa[0], ax[0] * pa[0] + ax[1] * pa[1]))))
    return dict(Lmin=min(Ls), Lmax=max(Ls), ang=max(angs), ks=ks, f0=k * (SPR_FREE - LMID), tilt3=math.degrees(3.0 * WHEEL_X / ks),
                comp_min=SPR_FREE - max(Ls), solid_gap=min(Ls) - SPR_SOLID, M0=moment(0.0), cup_rot=max(ang_pad))


def stop_plane_z(x):
    c = math.cos(TH)
    return 30.25 / c + abs(x) * math.tan(TH) + STOP_CLR


# ---------------------------------------------------------------- 2D sections
def rblock(sx):
    x0, x1 = sorted((sx * BLK_X0, sx * BLK_X1))
    return sbox(x0, x1, BLK_Z0, BLK_Z1)


def section_plate(outer):
    arch = Point(0, 0).buffer(ARCH_R, quad_segs=24).intersection(sbox(-ARCH_R - 1, ARCH_R + 1, 0, ARCH_R + 1))
    ears = unary_union([sbox(12, 22.0, 0, 9), sbox(-22.0, -12, 0, 9)])
    g = [arch, ears]
    for sx in (1, -1):
        g.append(LineString([(sx * 14.5, 4), (sx * XR, ZR - 6)]).buffer(3.0, cap_style=2))
        g.append(rblock(sx))
    return unary_union(g).buffer(0.01).intersection(sbox(-60, 60, 0.0, 100))


def tdrop_poly(R, sign=1.0):
    """circle plus a 45 degree apex toward +first coordinate (sign -1: toward minus)"""
    pts = [(sign * R * math.cos(math.radians(a)), R * math.sin(math.radians(a))) for a in range(45, 316, 15)]
    return Polygon([(sign * R * math.sqrt(2), 0.0)] + pts)


def teardrop_cut(R, length, base, axis, apex_y=True, extra=0.0):
    """round pocket along axis (unit V in xz plane) from base, roof apex toward +y (print up)"""
    poly = tdrop_poly(R)
    pl = [V(0, p[0], p[1]) for p in list(poly.exterior.coords)[:-1]]
    f = Part.Face(Part.makePolygon(pl + pl[:1]))
    s = f.extrude(V(length, 0, 0))
    a = math.degrees(math.atan2(axis.z, axis.x))
    s.rotate(O, Y, -a)
    s.translate(base)
    return s


def tdrop_z(R, x, y, z0, z1, sign):
    poly = tdrop_poly(R, sign)
    pl = [V(x + p[1], y + p[0], z0) for p in list(poly.exterior.coords)[:-1]]
    return Part.Face(Part.makePolygon(pl + pl[:1])).extrude(V(0, 0, z1 - z0))


def tdrop_x(R, y, z, x0, x1):
    poly = tdrop_poly(R, 1.0)
    pl = [V(x0, y + p[1], z + p[0]) for p in list(poly.exterior.coords)[:-1]]
    return Part.Face(Part.makePolygon(pl + pl[:1])).extrude(V(x1 - x0, 0, 0))


def nut_pocket_z(x, y, z0, z1):
    return hexz(NUT_POCKET_AF, x, y, z0, z1, 0.0)


def hex_x_v(af, y, z, x0, x1):
    r = af / math.sqrt(3)
    pts = [V(x0, y + r * math.cos(math.radians(30 + 60 * k)), z + r * math.sin(math.radians(30 + 60 * k))) for k in range(7)]
    return Part.Face(Part.makePolygon(pts)).extrude(V(x1 - x0, 0, 0))


def clamp_cuts(sx, y0, y1, ys, ztop_ear=True):
    """slit from the bore outward, screw hole, nut slot entered from outboard (roof ROOF_T, floor >= 1.2, 0.3 clearance all round the nut)"""
    xs = sx * (XR + R_BR + 3.0)
    x0, x1 = sorted((sx * XR, sx * (BLK_X1 + 1.0)))
    nw = NUT_AF + 2 * NUT_CL
    nl = (NUT_AF * 2 / math.sqrt(3)) / 2 + NUT_CL
    n0, n1 = sorted((xs - sx * nl, sx * (BLK_X1 + 1.0)))
    zt = ZR - SLIT / 2 - ROOF_T
    return [box(x0, x1, y0, y1, ZR - SLIT / 2, ZR + SLIT / 2), cylz(PASS_D / 2, xs, ys, BLK_Z0 - 4, BLK_Z1 + 1),
            box(n0, n1, ys - nw / 2, ys + nw / 2, zt - (NUT_T + 2 * NUT_CL), zt)]


def tdrop_x_y(R, y, z, x0, x1):
    poly = tdrop_poly(R, 1.0)
    pl = [V(x0, y + p[0], z + p[1]) for p in list(poly.exterior.coords)[:-1]]
    return Part.Face(Part.makePolygon(pl + pl[:1])).extrude(V(x1 - x0, 0, 0))


STOP_BUMP = 3.0


def stop_cuts(sx):
    """cross screw across the bore beyond the rod end: head OUTBOARD in a teardrop counterbore (straight driver path outward), nut in a rectangular pocket on the inboard bump"""
    nw = NUT_AF + 2 * NUT_CL
    pk0, pk1 = sorted((sx * (BLK_X0 - STOP_BUMP - 1.0), sx * BLK_X0))
    c0, c1 = sorted((sx * (BLK_X1 - 2.5), sx * (BLK_X1 + 1.0)))
    xa, xb = sorted((sx * (BLK_X0 - STOP_BUMP - 1.0), sx * (BLK_X1 + 1.0)))
    return [Part.makeCylinder(PASS_D / 2, xb - xa, V(xa, Y_STOP, ZR), X), tdrop_x_y(3.4, Y_STOP, ZR, c0, c1),
            box(pk0, pk1, Y_STOP - nw / 2, Y_STOP + nw / 2, ZR - 3.5, ZR + 3.5)]


def stop_bump(sx):
    x0, x1 = sorted((sx * (BLK_X0 - STOP_BUMP), sx * BLK_X0 + sx * 0.2))
    return box(x0, x1, YOUT0, Y_STOP + 4.25, ZR - 4.7, ZR + 4.7)


def cap_solid(y0, y1, inner):
    RC = CAP_R if inner else CAP_R_OUT
    NX = 12.8 if inner else 12.0
    d = Point(0, 0).buffer(RC, quad_segs=24).intersection(sbox(-RC - 1, RC + 1, -RC - 1, 0)).intersection(unary_union([sbox(-NX, NX, -RC - 1, 0), sbox(-RC - 1, RC + 1, -6, 0)]))
    ears = unary_union([sbox(12, 22.0, -6, 0), sbox(-22.0, -12, -6, 0)])
    s = prism_g(unary_union([d, ears]), y0, y1)
    s = s.cut(cyly(BORE_R, y0 - 1, y1 + 1, 0, 0))
    ym = (y0 + y1) / 2
    for sx in (1, -1):
        s = s.cut(cylz(PASS_D / 2, sx * CAP_SX, ym, -7, 1))
    if inner:
        s = s.cut(cone_cut(1.0))
    return s.removeSplitter()


def cone_cut(extra=0.0):
    pts = [V(0, YIN0 - 1, 0), V(15.6 + extra, YIN0 - 1, 0), V(15.6 + extra, YIN0, 0), V(JR + extra, YIN0 + 3.6, 0), V(0, YIN0 + 3.6, 0)]
    f = Part.Face(Part.makePolygon(pts + pts[:1]))
    return f.revolve(O, Y, 360)


def stop_block(sx):
    x0, x1 = sorted((sx * 24.0, sx * 29.2))
    H = BLK_Z0T - stop_plane_z(24.0) + 1.0
    y0, y1 = -4.0, 8.0
    b = box(x0, x1, y0 - H, y1, 0.0, BLK_Z0T + 0.5)
    b = b.cut(face_cutter(x0 - 1, x1 + 1, y0 - H - 1, y1 + 1))
    tap = [V(-50, y0 - H, BLK_Z0T + 0.5), V(-50, y0 - H, BLK_Z0T), V(-50, y0, BLK_Z0T - H), V(-50, y1, BLK_Z0T - H), V(-50, y1, BLK_Z0T + 0.5)]
    prism = Part.Face(Part.makePolygon(tap + tap[:1])).extrude(V(100, 0, 0))
    return b.common(prism)


def face_cutter(x0, x1, y0, y1, off=0.0):
    """removes everything below the stop plane (the plane seen from x z, symmetric in |x|)"""
    pts = [(x0, -50.0), (x1, -50.0), (x1, stop_plane_z(x1) + off), (x0, stop_plane_z(x0) + off)]
    if x0 < 0 < x1:
        raise ValueError
    f = Part.Face(Part.makePolygon([V(x, y0, z) for x, z in pts] + [V(pts[0][0], y0, pts[0][1])]))
    return f.extrude(V(0, y1 - y0, 0))


def spring_boss(sx_arm):
    """boss under the arm on side sx_arm holding the cup of the spring on the opposite side"""
    sxs = -sx_arm
    bx = sx_arm * abs(BXZ[0])
    ysp = YS * sxs
    t = V(sxs * TX, 0, TZ)
    Bv = V(bx, ysp, BXZ[1])
    mouth = Bv - t * CUP_D
    xa = sx_arm * BLK_X0
    x0, x1 = sorted((sx_arm * 30.0, mouth.x - sx_arm * 1.9))
    yb0, yb1 = ysp - CUP_R - 1.2, ysp + CUP_R * 1.4142 + 1.2
    H = BLK_Z0T - BOSS_BOT
    ys0 = yb0 - H
    b = box(x0, x1, ys0, yb1, BOSS_BOT, BLK_Z0T + 2.2)
    b = b.cut(face_cutter(x0, x1, ys0 - 1, yb1 + 1, 1.15))
    tap = [V(-60, ys0, BLK_Z0T + 2.2), V(-60, ys0, BLK_Z0T), V(-60, yb0, BLK_Z0T - H), V(-60, yb1, BLK_Z0T - H), V(-60, yb1, BLK_Z0T + 2.2)]
    b = b.common(Part.Face(Part.makePolygon(tap + tap[:1])).extrude(V(120, 0, 0)))
    xin = mouth.x - sx_arm * 1.9
    w = abs(xin - xa)
    if w > 0.01:
        pts = [V(xa + sx_arm * 5.0, ys0, -50), V(xa, ys0, -50), V(xin, ys0 + w, -50), V(xin - sx_arm * 5.0, ys0 + w, -50), V(xin - sx_arm * 5.0, yb1 + 1, -50), V(xa + sx_arm * 5.0, yb1 + 1, -50)]
        xt = Part.Face(Part.makePolygon(pts + pts[:1])).extrude(V(0, 0, 200))
        b = b.common(xt)
    return b, teardrop_cut(CUP_R, CUP_D + 14.0, Bv, -t)


# ---------------------------------------------------------------- parts
def build_bracket(outer):
    y0, y1 = (YOUT0, YOUT1) if outer else (YIN0, YIN1)
    plate = section_plate(outer)
    parts = [prism_g(plate, y0, y1)]
    ya1 = ARM_Y1 if outer else y1
    ya1s = {-1: ARM_Y1, 1: 8.0}
    cuts = []
    for sx in (1, -1):
        if outer:
            xlo, xhi = sorted((sx * BLK_X0, sx * BLK_X1T))
            parts.append(box(xlo, xhi, y0, ya1s[sx], BLK_Z0T, BLK_Z1T))
            xa, xb = sorted((sx * BLK_X0, sx * BLK_X1))
            thick = box(xa, xb, Y_THICK0, Y_THICK1, BLK_Z0, BLK_Z1)
            yz = [V(-80, Y_THICK0, BLK_Z0T + 0.0), V(-80, Y_THICK0 + (BLK_Z0T - BLK_Z0), BLK_Z0), V(-80, Y_THICK1, BLK_Z0), V(-80, Y_THICK1, BLK_Z1), V(-80, Y_THICK0 + (BLK_Z0T - BLK_Z0), BLK_Z1), V(-80, Y_THICK0, BLK_Z1T)]
            thick = thick.common(Part.Face(Part.makePolygon(yz + yz[:1])).extrude(V(160, 0, 0)))
            e = abs(BLK_X1 - BLK_X1T)
            xy = [V(sx * (BLK_X0 - 1), Y_THICK0, -30), V(sx * BLK_X1T, Y_THICK0, -30), V(sx * BLK_X1, Y_THICK0 + e, -30), V(sx * BLK_X1, Y_THICK1, -30), V(sx * (BLK_X0 - 1), Y_THICK1, -30)]
            thick = thick.common(Part.Face(Part.makePolygon(xy + xy[:1])).extrude(V(0, 0, 150)))
            parts.append(thick)
            parts.append(stop_block(sx))
            parts.append(stop_bump(sx))
            b, cup = spring_boss(sx)
            parts.append(b)
            cuts.append(cup)
    s = fuse(*parts)
    cuts.append(cyly(BORE_R, y0 - 1, y1 + 1, 0, 0))
    ym = (y0 + y1) / 2
    for sx in (1, -1):
        if outer:
            cuts.append(cyly(R_BR, y0 - 1, ya1s[sx] + 1, sx * XR, ZR))
            cuts += clamp_cuts(sx, ROD_END_Y - 0.2, -2.0, -13.0)
            cuts += stop_cuts(sx)
        else:
            cuts.append(cyly(R_BR, y0 - 1, y1 + 1, sx * XR, ZR))
            cuts += clamp_cuts(sx, y0 - 1, y1 + 1, ym)
        cuts.append(cylz(1.4, sx * CAP_SX, ym, -1, 8))
    if not outer:
        cuts.append(cone_cut())
    for c in cuts:
        s = s.cut(c)
    return s.removeSplitter()


RECESS_T = float(os.environ.get("RF_RT", "1.732"))
FACE_U = math.sqrt(DOME_R ** 2 - DOME_B ** 2)
T3 = V(TX, 0, TZ)


def to_axis(s, origin):
    s = s.copy()
    s.transformShape(App.Placement(origin, App.Rotation(X, T3)).toMatrix())
    return s


def build_pad(dome=True):
    """right pad (pilots (22,8),(22,-8)), dome centre C at y +YS; the left pad is this part turned 180 about z"""
    z0 = 30.25
    plate = prism_xy(sbox(18.0, 25.0, -11.5, 26.0).difference(Polygon([(25.2, -9.3), (25.2, -11.7), (22.8, -11.7)])), z0, z0 + 2.0)
    n = (TZ, -TX)
    C = (XC, ZC)
    band = Polygon([(C[0] + n[0] * 80 + TX * FACE_U, C[1] + n[1] * 80 + TZ * FACE_U), (C[0] - n[0] * 80 + TX * FACE_U, C[1] - n[1] * 80 + TZ * FACE_U),
                    (C[0] - n[0] * 80 + TX * -9.0, C[1] - n[1] * 80 + TZ * -9.0), (C[0] + n[0] * 80 + TX * -9.0, C[1] + n[1] * 80 + TZ * -9.0)])
    slab = band.intersection(sbox(-5, 40, z0, ZC + 6.5))
    parts = [plate, prism_g(slab, YS - 4.5, YS + 4.5)]
    s = fuse(*parts)
    cp = V(XC, YS, ZC)
    pts = [V(FACE_U + 0.1, DOME_B, 0), V(FACE_U, DOME_B, 0), V(FACE_U - (11.0 - DOME_B) * RECESS_T, 11.0, 0), V(FACE_U + 0.1, 11.0, 0)]
    s = s.cut(to_axis(Part.Face(Part.makePolygon(pts + pts[:1])).revolve(O, X, 360), cp))
    if dome:
        sph = Part.makeSphere(DOME_R, cp)
        cyl = Part.makeCylinder(DOME_B, DOME_R + 0.2 - (FACE_U - 0.02), cp + T3 * (FACE_U - 0.02), T3)
        s = s.fuse(sph.common(cyl))
    for x, y in ((22.0, 8.0), (22.0, -8.0)):
        s = s.cut(cylz(PASS_D / 2, x, y, z0 - 1, z0 + 3))
    return s.removeSplitter()


def build_cup():
    """SeatCup, local axis +Z: flat back disc r 4.6 (bed face), spring pin on the front"""
    return fuse(Part.makeCylinder(4.6, 2.5, O, Z), Part.makeCylinder(PIN_R, 2.5 + PIN_L, O, Z))


def cup_pose(cup, sx, phi):
    a, b, L, c, u = spring_state(sx, phi)
    ax = V(-u[0], 0, -u[1])
    base = V(c[0] - DOME_R * u[0] * -1 * -1 * -1 * -1 * 0 + 0, YS * sx, c[1]) - ax * 0 + V(-u[0] * -0, 0, 0)
    base = V(c[0], YS * sx, c[1]) + ax * DOME_R
    s = cup.copy()
    s.transformShape(App.Placement(base, App.Rotation(Z, ax)).toMatrix())
    return s


CR_Y = (-97.5, 72.0)
RAIL_X0, RAIL_X1, RAIL_Z0, RAIL_Z1 = 33.0, 42.0, 27.0, 33.0
GB_EARS = [(-38.0, 12.0), (38.0, 12.0), (-38.0, 56.0), (38.0, 56.0)]
CB_Z0, CB_Z1 = ZR - 6.8, ZR + 12.05
CB_HW = R_BR + 5.6


def hex_x(af, y, z, x0, x1):
    r = af / math.sqrt(3)
    pts = [V(x0, y + r * math.cos(math.radians(60 * k)), z + r * math.sin(math.radians(60 * k))) for k in range(7)]
    return Part.Face(Part.makePolygon(pts)).extrude(V(x1 - x0, 0, 0))


def build_cradle():
    parts = []
    for sx in (1, -1):
        x0, x1 = sorted((sx * RAIL_X0, sx * RAIL_X1))
        parts.append(box(x0, x1, CR_Y[0] - 7, CR_Y[1] + 7, RAIL_Z0, RAIL_Z1))
        for yc in CR_Y:
            hw = CB_HW if yc == CR_Y[0] else R_BR + 2.5
            xb0, xb1 = XR - hw, XR + hw
            xc = max(38.0, xb1)
            prof = [(30.0, RAIL_Z0), (xc, RAIL_Z0), (xc, ZR - 7.5), (xb1, ZR - 7.5), (xb1, CB_Z1 if yc == CR_Y[0] else ZR + R_BR + 2.5), (xb0, CB_Z1 if yc == CR_Y[0] else ZR + R_BR + 2.5), (xb0, ZR - 8.0), (30.0, ZR - 8.0 - (30.0 - xb0))]
            prof = [(sx * p[0], p[1]) for p in prof]
            parts.append(prism_g(Polygon(prof), yc - 7, yc + 7))
    s = fuse(*parts)
    nw = NUT_AF + 2 * NUT_CL
    nl = (NUT_AF * 2 / math.sqrt(3)) / 2 + NUT_CL
    for sx in (1, -1):
        for yc in CR_Y:
            s = s.cut(tear_roof_y_bore(sx * XR, yc))
            if yc != CR_Y[0]:
                continue
            s = s.cut(box(sx * XR - SLIT / 2, sx * XR + SLIT / 2, yc - 8, yc + 8, ZR + 5.0, CB_Z1 + 1))
            zs = ZR + 9.0
            s = s.cut(Part.makeCylinder(PASS_D / 2, 40, V(sx * XR - 20, yc, zs), X))
            xa, xb = sorted((sx * (XR - SLIT / 2 - 2.2), sx * (XR - SLIT / 2 - 2.2 - NUT_T - 2 * NUT_CL)))
            cx0, cx1 = sorted((sx * (XR + CB_HW - 1.5), sx * (XR + CB_HW + 1.0)))
            s = s.cut(tdrop_x(3.4, yc, zs, cx0, cx1))
            s = s.cut(box(xa, xb, yc - nw / 2, yc + nw / 2, zs - nl, CB_Z1 + 1))
    for x, y in GB_EARS:
        sx = 1 if x > 0 else -1
        a, b = sorted((x - sx * nl, sx * (RAIL_X1 + 1.5)))
        s = s.cut(box(a, b, y - nw / 2, y + nw / 2, RAIL_Z0 + 1.2, RAIL_Z0 + 1.2 + NUT_T + 2 * NUT_CL)).cut(cylz(PASS_D / 2, x, y, RAIL_Z0 - 1, RAIL_Z0 + 1.2 + 0.1)).cut(cylz(PASS_D / 2, x, y, RAIL_Z0 + 1.2 + NUT_T + 2 * NUT_CL + 0.2, RAIL_Z1 + 1))
    return s.removeSplitter()


def tear_roof_y_bore(x, y):
    poly = tdrop_poly(R_BR)
    pl = [(x + p[1] * 1.0, ZR + p[0]) for p in list(poly.exterior.coords)[:-1]]
    return prism_g(Polygon(pl), y - 10, y + 10)


# ---------------------------------------------------------------- fasteners (Ref objects)
def bolt(p, d, L, nut_at=None):
    parts = [m3_bolt(p, d, L)]
    if nut_at is not None:
        parts.append(m3_nut(nut_at, d, 0.0))
    return parts


def frame_fasteners(M):
    """list of (kind, bolt solids) per axle frame (rear orientation) plus cradle ones in the document frame"""
    ax = []
    ymi, ymo = (YIN0 + YIN1) / 2, (YOUT0 + YOUT1) / 2
    for sx in (1, -1):
        for ym in (ymi, ymo):
            ax.append(("cap", bolt(V(sx * CAP_SX, ym, -6.0), Z, 12.0), V(sx * CAP_SX, ym, -6.0)))
        xs = sx * (XR + R_BR + 3.0)
        for y in (ymi, -13.0):
            ax.append(("clamp", bolt(V(xs, y, BLK_Z1), -Z, 16.0, V(xs, y, ZR - SLIT / 2 - ROOF_T)), V(xs, y, BLK_Z1)))
    for sx in (1, -1):
        xi = sx * BLK_X0
        ax.append(("stop", bolt(V(sx * (BLK_X1 - 2.5), Y_STOP, ZR), V(-sx, 0, 0), 16.0, V(sx * BLK_X0, Y_STOP, ZR)), V(sx * (BLK_X1 - 2.5), Y_STOP, ZR)))
    for x, y in ((22.0, 8.0), (22.0, -8.0)):
        ax.append(("pad", bolt(V(x, y, 32.25), -Z, 8.0), V(x, y, 32.25)))
        ax.append(("pad", [rotz_s(b, 180) for b in bolt(V(x, y, 32.25), -Z, 8.0)], V(-x, -y, 32.25)))
    return ax


def rotz_s(s, deg):
    s = s.copy()
    s.rotate(O, Z, deg)
    return s


def cradle_fasteners():
    out = []
    zs = ZR + 9.0
    for sx in (1, -1):
        xh = sx * (XR + CB_HW)
        d = V(-sx, 0, 0)
        xn = sx * (XR - SLIT / 2 - 2.2)
        out.append(("cclamp", bolt(V(xh, CR_Y[0], zs), d, 16.0, V(xn, CR_Y[0], zs)), V(xh, CR_Y[0], zs)))
    for x, y in GB_EARS:
        top = 41.0 if (x, y) == (38.0, 12.0) else 37.0
        L = 16.0 if (x, y) == (38.0, 12.0) else 12.0
        out.append(("gear", bolt(V(x, y, top), -Z, L, V(x, y, RAIL_Z0 + 1.2 + NUT_T + 2 * NUT_CL)), V(x, y, top)))
    return out


# ---------------------------------------------------------------- springs as tubes
SPR_ID = SPR_OD - 2 * SPR_WIRE


def spring_tube(sx, phi, trim=1.5):
    a, b, L, c, u = spring_state(sx, phi)
    ys = YS * sx
    p = V(a[0], ys, a[1])
    d = V(b[0] - a[0], 0, b[1] - a[1])
    d.normalize()
    L = L - trim
    return Part.makeCylinder(SPR_BODY / 2, L, p, d).cut(Part.makeCylinder(SPR_ID / 2, L + 2, p - d, d))


# ---------------------------------------------------------------- strength (analytic, stated lever arms and signs)
def clamp_model():
    """lever model of the rod clamps: returns (rows, report lines, fails)"""
    rows, rep, fails = [], [], []
    F, s = CLAMP_F, ROD_BORE - ROD_D
    xh = BLK_X0 + BLK_W / 2
    xs, xt = XR + R_BR + 3.0, BLK_X1
    k_s, k_t, k_r = (xs - xh) / (XR - xh), (xt - xh) / (XR - xh), 1.0
    N = F * k_s
    for nm, w in (("inner bracket", YIN1 - YIN0), ("outer arm", -2.0 - (ROD_END_Y - 0.2))):
        rows.append(("rod clamp jaw bending at %.0f N, %s (real ring section %.1f at the rod contact, lever %.2f, in plane)" % (F, nm, T_RING, xs - XR), 6 * F * (xs - XR) / (w * T_RING ** 2), 15.0, "w %.1f" % w))
        rows.append(("rod clamp hinge tension 1.45 x %.0f N, %s" % (F, nm), 1.45 * F / (w * BLK_W), 15.0, "wall %.1f x %.1f" % (BLK_W, w)))
        th = (s / 2) / (XR - xh)
        rows.append(("rod clamp hinge flexure strain stress (E 3500), %s: theta %.4f rad over length %.1f" % (nm, th, ROD_BORE), 3500.0 * BLK_W * th / (2 * ROD_BORE), 15.0, "wall %.1f" % BLK_W))
    nw, tr = NUT_CL * 2 + NUT_AF, ROOF_T
    rows.append(("nut slot roof (across layers, simple beam 60 N over %.1f, width 6.35)" % nw, 6 * (F * nw / 8) / (6.35 * tr ** 2), 8.0, "roof %.1f floor %.2f" % (tr, (ZR - SLIT / 2 - ROOF_T - NUT_T - 2 * NUT_CL) - BLK_Z0)))
    floor_t = (ZR - SLIT / 2 - ROOF_T - NUT_T - 2 * NUT_CL) - BLK_Z0
    if tr < 1.6 or floor_t < 1.2:
        fails.append("nut slot roof/floor %.2f %.2f" % (tr, floor_t))
    left = SLIT - s * k_t
    rep.append("CLAMP lever model: hinge x %.2f, rod contact %.2f, screw %.2f, ear tip %.2f; bore slack %.2f (bore %.2f on rod %.1f); closure to take up the slack at the screw %.2f, at the ear tip %.2f; slit %.2f leaves %.2f at the tip after the jaw touches the rod (needs 0.6)" % (xh, XR, xs, xt, s, ROD_BORE, ROD_D, s * k_s, s * k_t, SLIT, left))
    if left < 0.6:
        fails.append("slit closure left %.2f" % left)
    grip = 2 * MU * N
    rep.append("CLAMP grip at %.0f N tension, friction %.1f: rod normal force %.0f N per jaw, %.0f N along the rod per clamp; bracket (two rods) %.0f N, cradle (two clamps) see below" % (F, MU, N, grip, 2 * grip))
    if grip < 45:
        fails.append("grip %.1f" % grip)
    # cradle clamp (vertical slit, jaws bend about the ring bottom, across layers)
    zh, zs_, zc, zt = ZR - R_BR - 1.0, ZR + 9.0, ZR, CB_Z1
    kc, kt = (zs_ - zh) / (zc - zh), (zt - zh) / (zc - zh)
    Nc = F * kc
    leftc = SLIT - s * kt
    rows.append(("cradle clamp jaw bending at %.0f N (ACROSS layers), ring wall %.1f at the equator, lever %.1f, w 14" % (F, CB_HW - R_BR, zs_ - zc), 6 * F * (zs_ - zc) / (14.0 * (CB_HW - R_BR) ** 2), 8.0, "car up print"))
    rep.append("CLAMP cradle: closure at the screw %.2f, at the tip %.2f, slit %.2f leaves %.2f; normal force %.0f N, grip %.0f N per clamp, %.0f N for the cradle (two rods); flexure of the thick ring not verified" % (s * kc, s * kt, SLIT, leftc, Nc, 2 * MU * Nc, 4 * MU * Nc))
    if leftc < 0.6 or 2 * MU * Nc * 2 < 45:
        fails.append("cradle clamp closure/grip")
    return rows, rep, fails


def strength(tab):
    rows = []
    W_ROLL = 30.0 * WHEEL_X + 15.0 * 55.0
    PITCH = 15.0 * 55.0
    Xs = 24.0
    F_stop = W_ROLL / Xs
    A_stop = 5.2 * 12.0
    rows.append(("stop block (compression, in layers y-up)", F_stop / A_stop, 15.0, "force %.0f N at lever %.1f from the axis, area %.0f mm2" % (F_stop, Xs, A_stop)))
    JY = (YIN0 + YIN1) / 2 - (YOUT0 + YOUT1) / 2
    Pv = 30.0 + 15.0 + PITCH / JY
    bear_in = Pv / (2 * BORE_R * (YIN1 - YIN0))
    rows.append(("journal bore bearing (upper half, inner)", bear_in, 15.0, "vertical %.1f N over %.0f mm2 projected" % (Pv, 2 * BORE_R * (YIN1 - YIN0))))
    for nm, w, RC in (("inner", YIN1 - YIN0, CAP_R), ("outer", YOUT1 - YOUT0, CAP_R_OUT)):
        P, L = 150.0, 2 * CAP_SX
        M = P * L / 4
        Z_ = w * (RC - BORE_R) ** 2 / 6
        rows.append(("cap %s bending, simple beam between its screws at 150 N (in plane)" % nm, M / Z_, 15.0, "M %.0f N mm, section %.0f mm3, wall %.1f" % (M, Z_, RC - BORE_R)))
        rows.append(("cap screw tension %s (M3, 2 screws, 150 N)" % nm, P / 2 / 5.03, 200.0, "tension area 5.03 mm2"))
    for nm, w in (("inner", YIN1 - YIN0), ("outer", YOUT1 - YOUT0)):
        M = 0.318 * 60.0 * (BORE_R + (ARCH_R - BORE_R) / 2)
        rows.append(("arch (upper half bore) bending, 60 N up on one journal, %s, wall %.1f (in plane, layers across y)" % (nm, ARCH_R - BORE_R), M / (w * (ARCH_R - BORE_R) ** 2 / 6), 15.0, "M %.0f N mm from the solid arch ring" % M))
    rows.append(("cap screw pilot pull out 75 N per screw, thread cylinder dia 3.0 x 6.0 (pilot axis lies in the layer plane; layers across y; checked against the 8 across limit)", 75.0 / (math.pi * 3.0 * 6.0), 8.0, "shear area %.1f mm2" % (math.pi * 18.0)))
    cr, _, _ = clamp_model()
    rows += cr
    fmax = SPR_RATE * (SPR_FREE - tab["Lmin"])
    arm_M = fmax * 25.0 + 15.0 * 46.0
    Zarm = (BLK_X1 - BLK_X0) * (BLK_Z1 - BLK_Z0) ** 2 / 6 - math.pi * R_BR ** 4 / 4 / ((BLK_Z1 - BLK_Z0) / 2)
    rows.append(("outer arm cantilever bending (in plane)", arm_M / Zarm, 15.0, "M %.0f N mm (spring %.1f N at 25 + 15 N at 46), Z %.0f mm3" % (arm_M, fmax, Zarm)))
    rows.append(("spring pad slab root (in plane, z up)", fmax * 12.0 / (9.0 * 9.0 * 9.0 / 6.0), 15.0, "slab 9 thick x 9 wide, lever 12"))
    rows.append(("spring boss (cup wall, y-up, in plane)", fmax * 8.0 / (11.0 * 11.0 * 11.0 / 6.0), 15.0, "lever 8"))
    return rows


# ---------------------------------------------------------------- sweeps
def to_axle(s, axle, M):
    s = s.copy()
    s.translate(V(0, -(M["YR"] if axle == "R" else M["YF"]), 0))
    if axle == "F":
        s.rotate(O, Z, 180.0)
    return s


def pclass(n):
    for k in ("Tyre", "Wheel"):
        if k in n:
            return "tyre_wheel"
    return "other"


def allowed(m, f):
    if m.startswith("JournalRing") and f.startswith(("BracketIn", "CapIn")):
        return 0.12
    if m.startswith("JournalStub") and f.startswith(("BracketOut", "CapOut")):
        return 0.29
    if m.startswith("Housing") and f.startswith(("BracketOut", "BracketIn")):
        return 0.04
    if m.startswith("Spring"):
        own = m[-1]
        if f == "SeatCup_" + own:
            return 0.0
        return 0.5 if f.startswith("BracketOut") else 0.8
    if m.startswith("SeatCup"):
        own = m[-1]
        return 0.0 if f in ("Pad_" + own, "Spring_" + own) else 0.8
    if m.startswith("PinionShaft") and f.startswith("Shaft_"):
        return 0.0
    if pclass(m) == "tyre_wheel":
        return 2.0
    return 0.8


def sweep(R, M, fixed_doc, axles, poses, tab, arms_list):
    best = {}
    bad = []
    for axle in axles:
        fixed = {n: to_axle(s, axle, M) for n, s in fixed_doc.items()}
        fb = {n: s.BoundBox for n, s in fixed.items()}
        for arms, phis, sts in arms_list:
            for phi in phis:
                for st in sts:
                    mov = {n: tilt(s, phi) for n, s in axle_parts(R, arms, st).items()}
                    pads = {"Pad_R": build_PAD[0], "Pad_L": rotz_s(build_PAD[0], 180)}
                    for n, s in pads.items():
                        mov[n] = tilt(s, phi)
                    for sx, nm in ((1, "Spring_R"), (-1, "Spring_L")):
                        mov[nm] = spring_tube(sx, phi)
                        mov["SeatCup_" + nm[-1]] = cup_pose(build_CUP[0], sx, phi)
                    pairs = [(m, sm, f, sf, fb[f]) for m, sm in mov.items() for f, sf in fixed.items()]
                    pairs += [(m, mov[m], f, sf, sf.BoundBox) for m in ("Spring_R", "Spring_L", "SeatCup_R", "SeatCup_L") for f, sf in mov.items() if f != m and not (f.startswith("Spring") and m.startswith("Spring"))]
                    for m, sm, f, sf, b in pairs:
                        bm = sm.BoundBox
                        if True:
                            if (bm.XMin - 6 > b.XMax or b.XMin - 6 > bm.XMax or bm.YMin - 6 > b.YMax or b.YMin - 6 > bm.YMax or bm.ZMin - 6 > b.ZMax or b.ZMin - 6 > bm.ZMax):
                                continue
                            g = sm.distToShape(sf)[0]
                            key = (m.split("_")[0] if m.startswith(("Hub", "Spring", "Pad", "SeatCup")) else m, f)
                            kk = (arms, axle, m, f)
                            if g < best.get(key, (99,))[0]:
                                best[key] = (round(g, 3), axle, arms, round(phi, 1), round(st, 1), m)
    return best


def evaluate(best):
    bad, listed = [], {}
    for (m, f), v in sorted(best.items()):
        need = allowed(v[5], f)
        if v[0] < need - 1e-3:
            bad.append((m, f, v, need))
        if v[0] < 5.0:
            listed[(m, f)] = v
    return bad, listed


# ---------------------------------------------------------------- bench step and stop checks
def extra_checks(R, M, fixed, world, fails, cupl, pad, doc):
    rep = []
    th = THETA
    # 0 free space for the steering servo bracket beyond the stub end face (y < -56, 40 x 40 around the axis) on the front axle
    fxF = {n: to_axle(s, "F", M) for n, s in fixed.items() if not n.startswith("Axle")}
    zone = box(-20, 20, -400, -56.0, -20, 20)
    hit = [n for n, s in fxF.items() if vol(zone, s) > 1e-3]
    rep.append("FRONT AXLE servo zone (x,z +-20, y below -56.0 in the axle frame, stub collar end face at -56.0): frame parts inside: %s; lowest frame y in the axle frame %.1f" % (hit if hit else "NONE", min(s.BoundBox.YMin for n, s in fxF.items() if n.startswith(("Bracket", "Cap")) and "_F" in n)))
    if hit:
        fails.append("servo zone occupied %s" % hit)
    # 1 stop is the first thing to touch (stop angle plus 0.3 degree), both arm widths, both locks
    fx = {n: to_axle(s, "R", M) for n, s in fixed.items()}
    over = {}
    for arms in ("N", "W"):
        for phi in (th + 0.3, -(th + 0.3)):
            for st in (0.0, STEER, -STEER):
                mov = {n: tilt(s, phi) for n, s in axle_parts(R, arms, st).items()}
                mov["Pad_R"] = tilt(build_PAD[0], phi)
                mov["Pad_L"] = tilt(rotz_s(build_PAD[0], 180), phi)
                for sx, nm in ((1, "R"), (-1, "L")):
                    mov["Spring_" + nm] = spring_tube(sx, phi)
                    mov["SeatCup_" + nm] = cup_pose(build_CUP[0], sx, phi)
                for m, sm in mov.items():
                    for f, sf in fx.items():
                        v = vol(sm, sf)
                        if v > 1e-3:
                            over.setdefault((m.split("_")[0] if m.startswith(("Hub", "Spring", "Pad", "SeatCup")) else m, f), []).append((arms, round(phi, 1), st, round(v, 3)))
    bad = {k: v for k, v in over.items() if not ((k[0].startswith("Housing") and k[1].startswith("BracketOut")) or (k[0] == "PinionShaft" and k[1].startswith("Shaft_")))}
    rep.append("STOP FIRST CONTACT at stop + 0.3 deg, arms N and W, steering 0 and both locks: overlaps %s ; others %s" % (sorted(k for k in over if k not in bad), "NONE" if not bad else bad))
    if bad:
        fails.append("overlap before stop %s" % list(bad))
    # 2 rods slide in through all brackets and the cradle, step 12
    ycs = (M["YR"] + M["YF"]) / 2
    worst = 0.0
    frame_only = {n: s for n, s in fixed.items() if n.startswith(("Bracket", "Cradle"))}
    for sx in (1, -1):
        for off in range(-560, 1, 12):
            r = cyly(ROD_D / 2, ycs - ROD_L / 2 + off, ycs + ROD_L / 2 + off, sx * XR, ZR)
            worst = max(worst, sum(vol(r, s) for s in frame_only.values()))
    rep.append("BENCH rods slid through carriers and cradle from 560 mm out in 12 mm steps: worst overlap %.4f mm3" % worst)
    if worst > 1e-3:
        fails.append("rod slide overlap")
    # 3 axle lifted from below with pads and cups fitted (springs go in afterwards along their axes), caps off
    brk = {n: to_axle(s, "R", M) for n, s in fixed.items() if n.startswith(("Bracket", "Cradle", "Rod", "GB_"))}
    mov0 = dict(axle_parts(R, "N", 0.0))
    mov0["Pad_R"] = build_PAD[0]
    mov0["Pad_L"] = rotz_s(build_PAD[0], 180)
    for sx, nm in ((1, "R"), (-1, "L")):
        mov0["SeatCup_" + nm] = cup_pose(build_CUP[0], sx, 0.0)
    worst, wz = 0.0, 0
    for dz in range(-60, 1, 3):
        for n, s in mov0.items():
            sm = moved(s, 0, 0, dz)
            for f, sf in brk.items():
                v = vol(sm, sf)
                if v > worst:
                    worst, wz = v, (dz, n, f)
    rep.append("BENCH axle with pads and cups lifted along +z from 60 below, 3 mm steps: worst overlap %.4f mm3 %s ; springs then slide along their axes (compressing from 34.9 to 24.4, end enters the cup 4.5 deep; the compressed tube is a subset of the final tube, which has zero overlap in the sweep)" % (worst, wz))
    if worst > 1e-3:
        fails.append("axle lift overlap %s" % (wz,))
    # 3b lift with the shafts in place (expected to overlap: shafts come off before an axle is dropped)
    ysh = {n: to_axle(s, "R", M) for n, s in fixed.items() if n.startswith("Shaft_R_")}
    ov = [dz for dz in range(-60, 1, 3) if any(vol(moved(R["Axle"][pn], 0, 0, dz), ys) > 1e-3 for pn in ("PinionShaft",) for ys in ysh.values())]
    rep.append("BENCH lift with the rear shaft still on its port: PinionShaft overlaps the yoke at drops of %s mm; shaft therefore fitted after the lift and removed before a drop" % (ov,))
    # 4 caps and screws from below
    worst = 0.0
    capb = [(n, s) for kind, parts, p in frame_fasteners(M) for n, s in (("bolt", parts[0]),) if kind == "cap"]
    for cn, ct in (("CapIn", build_CAPS[0]), ("CapOut", build_CAPS[1])):
        for dz in range(-60, 1, 3):
            sm = moved(ct, 0, 0, dz)
            for n, s in mov0.items():
                worst = max(worst, vol(sm, s))
            for f, sf in brk.items():
                worst = max(worst, vol(sm, sf))
    rep.append("BENCH caps slid up from 60 below: worst overlap %.4f mm3" % worst)
    if worst > 1e-3:
        fails.append("cap slide overlap")
    # 5 driver paths (dia 6 x 60 straight, hosts excluded) at the bench step
    drv_bad, n_drv = [], 0
    def driver_ok(p, d, hosts, bolt_shapes):
        dr = Part.makeCylinder(3.0, 60.0, p - d * HEAD_H, -d)
        hit = []
        for n, s in world_all.items():
            if any(n.startswith(h) for h in hosts):
                continue
            v = vol(dr, s)
            if v > 1e-3:
                hit.append((n, round(v, 2)))
        return hit
    world_all = dict(world)
    for ax in ("R", "F"):
        for n, s in {"Pad_a": pad, "Pad_b": rotz_s(pad, 180)}.items():
            world_all["%s_%s" % (n, ax)] = at_axle(s, ax, M)
    for ax in ("R", "F"):
        for kind, parts, p in frame_fasteners(M):
            d = V(-1 if p.x > 0 else 1, 0, 0) if kind == "stop" else {"cap": Z, "clamp": -Z, "pad": -Z}[kind]
            hosts = {"cap": ("Cap", "Bracket"), "clamp": ("Bracket",), "stop": ("Bracket", "Axle_", "Pad_", "Rod"), "pad": ("Pad", "Bracket", "Rod", "Cradle", "GB_", "Shaft_")}[kind]
            pp = at_axle_pt(p, ax, M)
            dd = at_axle_dir(d, ax)
            hit = driver_ok(pp, dd, hosts, parts)
            n_drv += 1
            if hit:
                drv_bad.append((ax, kind, [round(c, 1) for c in (pp.x, pp.y, pp.z)], hit[:3]))
    for kind, parts, p in cradle_fasteners():
        d = V(-1 if p.x > 0 else 1, 0, 0) if kind == "cclamp" else -Z
        hosts = ("Cradle",) if kind == "cclamp" else ("Cradle", "GB_Bracket", "GB_ServoMount")
        hit = driver_ok(p, d, hosts, parts)
        n_drv += 1
        if hit:
            drv_bad.append((kind, [round(c, 1) for c in (p.x, p.y, p.z)], hit[:3]))
    rep.append("BENCH driver paths (dia 6 x 60 straight): %d screws checked, blocked %s" % (n_drv, drv_bad if drv_bad else "NONE"))
    if drv_bad:
        fails.append("driver paths blocked %d" % len(drv_bad))
    # 6 yoke clamp screw access (cross pilot 5.9 from each port tip, direction free to choose among +-z, +-x)
    pil = [("gb rear", V(0, M["gb_y0"] + 5.9, 0), "R"), ("axle R", V(0, M["YR"] + M["port_y"] - 5.9, 0), "R"),
           ("gb front", V(0, M["gb_y1"] - 5.9, 0), "F"), ("axle F", V(0, M["YF"] - M["port_y"] + 5.9, 0), "F")]
    for nm, p, sh in pil:
        free = []
        for dn, d in (("+z", Z), ("-z", -Z), ("+x", X), ("-x", -X)):
            dr = Part.makeCylinder(3.0, 60.0, p + d * 9.8, d)
            hit = [n for n, s in world_all.items() if not n.startswith(("Shaft_" + sh, "GB_ThroughShaft")) and not (n.startswith("Axle_") and False) and vol(dr, s) > 1e-3]
            if not hit:
                free.append(dn)
        rep.append("BENCH yoke clamp screw %s: driver directions free %s" % (nm, free if free else "NONE"))
        if not free:
            fails.append("yoke screw access %s" % nm)
    # 7 steering reservation: candidate tie rod line (dia 5) along x behind the housing, through the tilt range, against the frame parts
    best = None
    for yt in (-40.0, -42.0, -44.0):
        for zt in (-24.0, -22.0, 24.0, 26.0):
            g = 99.0
            for phi in (-th, 0.0, th):
                line = tilt(cyly(2.5, 0, 0, 0, 0) if False else Part.makeCylinder(2.5, 2 * KP["N"], V(-KP["N"], yt, zt), X), phi)
                for f, sf in fx.items():
                    if f.startswith(("Bracket", "Cap", "Cradle", "Rod")):
                        g = min(g, dist(line, sf))
            if best is None or g > best[0]:
                best = (g, yt, zt)
    rep.append("STEERING corridor: best candidate tie rod line dia 5 along x at y %.1f z %.1f (axle frame, x +-%.1f) minimum clearance to carrier, caps and rods through the tilt range %.2f (needs 0.8); knuckle arm attachment height not verified; pilots free after pads: (-8,16) and (8,-16) only, the other plate pilots are under the pad slabs" % (best[1], best[2], KP["N"], best[0]))
    return rep


def at_axle_pt(p, axle, M):
    q = V(p.x, p.y, p.z)
    if axle == "F":
        q = V(-q.x, -q.y, q.z)
    return V(q.x, q.y + (M["YR"] if axle == "R" else M["YF"]), q.z)


def at_axle_dir(d, axle):
    return V(-d.x, -d.y, d.z) if axle == "F" else d


# ---------------------------------------------------------------- document and report
build_PAD = [None]
build_CUP = [None]
build_CAPS = [None, None]
NAMES = ("BracketOut", "BracketIn", "CapOut", "CapIn", "SpringPad")


def shaft_parts(R, m1, sign):
    ds = R["DriveShaft"]
    x0 = ds["Shown_JointYoke_S1"].BoundBox.XMin
    names = ("Shown_JointYoke_S1", "Shown_JointYoke_S2", "Shown_JointCross_S1", "Shown_ShortLink", "Shown_JointYoke_S3", "Shown_JointYoke_S4", "Shown_JointCross_S2")
    out = {}
    for n in names:
        s = ds[n].copy()
        s.translate(V(-x0, 0, 120.0))
        s.rotate(O, Z, 90 * sign)
        s.translate(V(0, m1, 0))
        out[n.replace("Shown_", "")] = s
    return out


def axis_center(s, y):
    b = Part.makeCompound(s.slice(Y, y)).BoundBox
    return ((b.XMin + b.XMax) / 2, (b.ZMin + b.ZMax) / 2)


def main():
    t0 = time.time()
    fails, rep = [], []
    R = load_refs()
    M = measure(R)
    wd = wheel_directions()
    tab = spring_tab()
    ymid = (M["YR"] + M["YF"]) / 2
    assert abs(M["wheelbase"] / 2 - 247.5 - ROD_END_Y) < 0.1, (M["wheelbase"], ROD_END_Y)
    rod_y0, rod_y1 = ymid - ROD_L / 2, ymid + ROD_L / 2
    # port alignment
    pa = axis_center(R["Axle"]["PinionShaft"], 80.0)
    pg = axis_center(R["Gearbox3"]["ThroughShaft"], M["gb_y1"] - 5)
    pg2 = axis_center(R["Gearbox3"]["ThroughShaft"], M["gb_y0"] + 5)
    for c in (pa, pg, pg2):
        assert abs(c[0]) < 0.5 and abs(c[1]) < 0.5, (pa, pg, pg2)
    # parts
    bo, bi = build_bracket(True), build_bracket(False)
    co, ci = cap_solid(YOUT0, YOUT1, False), cap_solid(YIN0, YIN1, True)
    pad = build_pad()
    build_PAD[0] = pad
    build_CAPS[0], build_CAPS[1] = ci, co
    cupl = build_cup()
    build_CUP[0] = cupl
    cr = build_cradle()
    for sxa in (1, -1):
        sxs_ = -sxa
        tt = V(sxs_ * TX, 0, TZ)
        Bv_ = V(sxa * abs(BXZ[0]), YS * sxs_, BXZ[1])
        shell = Part.makeCylinder(CUP_R + 1.2, CUP_D, Bv_, -tt).cut(teardrop_cut(CUP_R, CUP_D + 14.0, Bv_, -tt))
        solid_frac = shell.common(bo).Volume / shell.Volume
        rep.append("CUP wall (arm side %+d): fraction of the 1.2 shell around the cup that is solid %.3f" % (sxa, solid_frac))
        if solid_frac < 0.985:
            fails.append("cup wall < 1.2 (%.3f)" % solid_frac)
    solid = {"BracketOut": bo, "BracketIn": bi, "CapOut": co, "CapIn": ci, "SpringPad": pad, "SeatCup": cupl}
    copies = {"BracketOut": 2, "BracketIn": 2, "CapOut": 2, "CapIn": 2, "SpringPad": 4, "SeatCup": 4, "GearboxCradle": 1}
    vol = {n: s.Volume / 1000 for n, s in dict(solid, GearboxCradle=cr).items()}
    total = sum(vol[n] * copies[n] for n in vol)
    PRINT_UP.update({"BracketOut": "+Y", "BracketIn": "-Y", "CapOut": "+Y", "CapIn": "-Y", "SpringPad": "+Z", "SeatCup": "+Z", "GearboxCradle": "+Z"})
    rep.append("PARTS (cm3 each, copies, print up):")
    for n in vol:
        b = dict(solid, GearboxCradle=cr)[n].BoundBox
        rep.append("  %-14s %.1f x %.1f x %.1f  %.2f cm3  x%d  up %s" % (n, b.XLength, b.YLength, b.ZLength, vol[n], copies[n], PRINT_UP[n]))
    rep.append("TOTAL printed %.1f cm3 (budget 150)" % total)
    if total > 170:
        fails.append("volume %.1f > 170" % total)
    # kit shafts
    m_r, m_f = M["gb_y0"] + M["depth"], M["gb_y1"] - M["depth"]
    shR, shF = shaft_parts(R, m_r, -1), shaft_parts(R, m_f, 1)
    # document
    doc = App.newDocument("RodFrame")

    def put(name, shape):
        o = doc.addObject("Part::Feature", name)
        o.Shape = shape
        return o
    fixed = {}
    for ax, tag in (("R", "1"), ("F", "2")):
        for n, s in solid.items():
            if n in ("SpringPad", "SeatCup"):
                continue
            ps = at_axle(s, ax, M)
            put((n + "_1") if ax == "R" else "Shown_%s_2" % n, ps)
            fixed["%s_%s" % (n, ax)] = ps
    padsets = {}
    for ax in ("R", "F"):
        for k, rot in (("a", 0), ("b", 180)):
            p0 = rotz_s(pad, rot) if rot else pad
            padsets[(ax, k)] = at_axle(p0, ax, M)
            put("SpringPad_1" if (ax, k) == ("R", "a") else "Shown_SpringPad_%s%s" % (ax, k), padsets[(ax, k)])
    put("SeatCup_1", moved(cupl, 60, 0, 100))
    for ax in ("R", "F"):
        for sx in (1, -1):
            put("Shown_SeatCup_%s%s" % (ax, "a" if sx > 0 else "b"), at_axle(cup_pose(cupl, sx, 0.0), ax, M))
    put("GearboxCradle", cr)
    fixed["Cradle"] = cr
    rods = []
    for sx in (1, -1):
        r = cyly(ROD_D / 2, rod_y0, rod_y1, sx * XR, ZR)
        rods.append(r)
        put("Ref_Rod_%d" % (1 if sx > 0 else 2), r)
        fixed["Rod_%d" % (1 if sx > 0 else 2)] = r
    gbp = {n: s for n, s in R["Gearbox3"].items() if n not in ("Ref_Floor", "Ref_Grubs")}
    put("Ref_Gearbox", Part.makeCompound(list(gbp.values())))
    for n, s in gbp.items():
        fixed["GB_" + n] = s
    put("Ref_Shaft_R", Part.makeCompound(list(shR.values())))
    put("Ref_Shaft_F", Part.makeCompound(list(shF.values())))
    for n, s in shR.items():
        fixed["Shaft_R_" + n] = s
    for n, s in shF.items():
        fixed["Shaft_F_" + n] = s
    for ax in ("R", "F"):
        put("Ref_Axle_" + ax, Part.makeCompound([at_axle(s, ax, M) for s in axle_parts(R, "N", 0.0).values()]))
        sp = [at_axle(spring_tube(sx, 0.0).copy(), ax, M) for sx in (1, -1)]
        put("Ref_Springs_" + ax, Part.makeCompound(sp))
    bolts, nuts, nscr = [], [], 0
    for ax in ("R", "F"):
        for kind, parts, p in frame_fasteners(M):
            bolts.append(at_axle(parts[0], ax, M))
            if len(parts) > 1:
                nuts.append(at_axle(parts[1], ax, M))
            nscr += 1
    for kind, parts, p in cradle_fasteners():
        bolts.append(parts[0])
        if len(parts) > 1:
            nuts.append(parts[1])
        nscr += 1
    put("Ref_Screws", Part.makeCompound(bolts))
    put("Ref_Nuts", Part.makeCompound(nuts))
    rep.append("FRAME SCREWS %d (budget 34 after your decision, 30 before the 4 stop screws)" % nscr)
    if nscr > 34:
        fails.append("screws %d" % nscr)
    # overall
    allz = [o.Shape.BoundBox for o in doc.Objects]
    zmin = min(b.ZMin for b in allz)
    zmax = max(b.ZMax for b in allz)
    zmax_frame = max(o.Shape.BoundBox.ZMax for o in doc.Objects if not o.Name.startswith(("Ref_", "SeatCup_1")))
    rep.append("HEIGHT: lowest point any part %.2f (axle ref %.2f) => ground clearance %.2f at tilt 0; highest part %.2f, highest FRAME part %.2f, gearbox Bracket top %.2f, overall from ground %.1f" % (
        zmin, -30.25, GROUND + zmin, zmax, zmax_frame, R["Gearbox3"]["Bracket"].BoundBox.ZMax, GROUND + zmax))
    low_axle = min(min(s.optimalBoundingBox(False, False).ZMin for n, s in axle_parts(R, "N", 0.0).items() if "Tyre" not in n and "Wheel" not in n), pad.optimalBoundingBox(False, False).ZMin)
    fr = [(o.Name, o.Shape) for o in doc.Objects if not o.Name.startswith(("SeatCup_1", "Ref_Axle", "Ref_Springs", "Ref_Screws", "Ref_Nuts", "Shown_SpringPad", "Shown_SeatCup"))]
    gc = {}
    for phi in (-THETA, 0.0, THETA):
        for n, s in fr:
            z = tilt(s, -phi).optimalBoundingBox(False, False).ZMin
            if z < gc.get(n.split("_")[0] if n.startswith("Shown_") is False else n.split("_")[1], (99, 0))[0]:
                gc[n.split("_")[0] if n.startswith("Shown_") is False else n.split("_")[1]] = (z, round(phi, 1))
    worst = min(v[0] for v in gc.values())
    rep.append("GROUND CLEARANCE relative to the tyre contact line (axle tilted by the travel, the frame rolled by 0 and +-%.2f deg about the axle line, every non-axle part): lowest axle part (housing etc, tyres excluded) z %.2f -> %.2f; lowest frame/gearbox/rod/shaft point after rolling %.2f -> %.2f; per group %s" % (THETA, low_axle, GROUND + low_axle, worst, GROUND + worst, {k: round(GROUND + v[0], 1) for k, v in sorted(gc.items())}))
    lowest_frame = min(o.Shape.optimalBoundingBox(False, False).ZMin for o in doc.Objects if not o.Name.startswith(("Ref_", "SeatCup_1")))
    if lowest_frame < -30.25 - 1e-6:
        fails.append("frame part below housing bottom %.2f" % lowest_frame)
    if zmax_frame > R["Gearbox3"]["Bracket"].BoundBox.ZMax + 1e-6:
        fails.append("frame part higher than gearbox Bracket top")
    rep.append("LAYOUT: wheelbase %.2f, track N %.1f W %.1f, overall width over tyres N %.1f, rods x +-%.1f z %.1f y %.1f..%.1f, ShortLink each side, port tips axle %.1f gearbox %.1f/%.1f, pitch port to port %.2f, wheel direction factor %.1f both axles (same)" % (
        M["wheelbase"], M["track_N"], M["track_W"], M["track_N"] + 26.0, XR, ZR, rod_y0, rod_y1, M["port_y"], M["gb_y0"], M["gb_y1"], M["pitch"], wd))
    rep.append("TRAVEL +-%.1f mm at the wheel centre = +-%.2f deg; stops: flat blocks under each arm x 24 to 29.2, y -4 to 8 (62 mm2 on the rotated top flat) against the housing top flat" % (TRAVEL, THETA))
    rep.append("SPRINGS (2, tangent, one per side, rate %.2f N/mm): dome centre C (%.1f, %.1f) y +-%.0f, line to B %.1f deg off the cup axis max; length %.2f..%.2f (solid+%.2f, compression kept %.2f at the longest); preload %.1f N each at L %.1f; k_roll %.0f N mm/rad = %.1f N mm/deg; tilt per 3 N difference %.2f deg" % (
        SPR_RATE, XC, ZC, YS, tab["ang"], tab["Lmin"], tab["Lmax"], tab["solid_gap"], tab["comp_min"], tab["f0"], LMID, tab["ks"], tab["ks"] * math.pi / 180, tab["tilt3"]))
    if tab["tilt3"] > 5 or tab["solid_gap"] < 2.0 or tab["comp_min"] < 1.5 or tab["ang"] > 6.0:
        fails.append("spring numbers %s" % tab)
    pin_room, cup_room = SPR_ID / 2 - PIN_R, CUP_R - SPR_OD / 2
    rep.append("SEATS: SeatCup flat back on a dome R%.1f (base r%.1f, cap reaches %.1f deg), cup turns up to %.1f deg relative to the pad, contact stays inside the dome (margin %.1f deg = %.1f mm of arc); pin dia %.1f length %.1f room %.2f aligned with the spring; frame cup dia %.1f depth %.1f room %.2f" % (DOME_R, DOME_B, math.degrees(math.asin(DOME_B / DOME_R)), tab["cup_rot"], math.degrees(math.asin(DOME_B / DOME_R)) - tab["cup_rot"], DOME_R * math.radians(math.degrees(math.asin(DOME_B / DOME_R)) - tab["cup_rot"]), 2 * PIN_R, PIN_L, pin_room, 2 * CUP_R, CUP_D, cup_room))
    if DOME_R * math.radians(math.degrees(math.asin(DOME_B / DOME_R)) - tab["cup_rot"]) < 2.0:
        fails.append("dome engagement < 2 mm")
    if not (0.5 <= pin_room <= 1.2 and 0.5 <= cup_room <= 1.2):
        fails.append("seat room %.2f %.2f" % (pin_room, cup_room))
    # strength
    rep.append("STRENGTH (MPa): model: combined case vertical 30 N and lateral 15 N at one tyre patch (x %.2f, 55 below), fore aft 15 N, 15 N weight; roll moment %.0f N mm on the stop (lever 24), cap 150 N" % (WHEEL_X, 30 * WHEEL_X + 15 * 55))
    rep += clamp_model()[1]
    fails += clamp_model()[2]
    for nm, sv, lim, note in strength(tab):
        rep.append("  %-62s %.1f / %.0f  %s" % (nm, sv, lim, note))
        if sv > lim:
            fails.append("strength %s %.1f > %.0f" % (nm, sv, lim))
    # print checks
    if not FAST or os.environ.get("RF_PRINT"):
        pc = dict(solid, GearboxCradle=cr)
        for n, s in pc.items():
            r = printable(n, s)
            bad = r["slopes"] or r["layers"] or r["bed"] < BED_MIN or r["tall"] > TALL_MAX or r["thin"] > 1.0
            tw = thin_walls(n, s)
            # CapIn: harmless attached, supported feather where the 45 degree cone cut crosses the side wall plane (x 11.9..12.9, z -11.6..-5.6, y 53.9..57.6), exempt by region only
            ex = lambda e: n == "CapIn" and 11.9 <= abs(e[2][0]) <= 12.9 and -11.6 <= e[2][1] <= -5.6 and 53.9 <= 69.5 - e[0] <= 57.6
            left = [e for e in tw[0] if not ex(e)]
            nleft = tw[1] - (len(tw[0]) - len(left))
            rep.append("THINWALL %-14s %d slices thinner than 1.2 outside the exempt region (%d inside it): %s" % (n, nleft, tw[1] - nleft, left[:3]))
            if nleft:
                fails.append("thinwall %s %d" % (n, nleft))
            rep.append("PRINT %-14s bed %.0f tall %.2f thin %.2f slopes %s layers(%d) %s" % (n, r["bed"], r["tall"], r["thin"], r["slopes"][:3], r["nlayers"], r["layers"][:3]))
            if bad:
                fails.append("print %s" % n)
    world = dict(fixed)
    world.update({"Axle_R": doc.getObject("Ref_Axle_R").Shape, "Axle_F": doc.getObject("Ref_Axle_F").Shape})
    rep += extra_checks(R, M, fixed, world, fails, cupl, pad, doc)
    # sweeps
    th = THETA
    if FAST:
        arms = [("N", (-th, 0.0, th), (0.0, STEER)), ("W", (-th, th), (0.0,))]
        axs = ["R"]
    else:
        arms = [("N", (-th, -th / 2, 0.0, th / 2, th), (0.0, STEER, -STEER)), ("W", (-th, 0.0, th), (0.0, STEER, -STEER))]
        axs = ["R", "F"]
    best = sweep(R, M, fixed, axs, None, tab, arms)
    bad, listed = evaluate(best)
    rep.append("SWEEP pairs under 5 mm (class: gap, axle, arms, tilt, steer, moving part) need as set by class:")
    for k, v in listed.items():
        rep.append("  %s | %s : %s need %.2f" % (k[0], k[1], v, allowed(v[5], k[1])))
    for b in bad:
        fails.append("sweep %s" % (b,))
    rep.append("done %.0fs" % (time.time() - t0))
    doc.recompute()
    doc.saveAs(OUT)
    print("\n".join(rep))
    print("FAILS:" if fails else "ALL PASS", len(fails))
    for f in fails:
        print("  FAIL", f)
    return len(fails)


if "NO_RUN" not in globals():
    code = main()
    print("EXIT", code)
