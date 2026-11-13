# Motor module: GA37RG gearmotor sits ON TOP of the cardboard floor (bracket glued flat by its pad); only the bracket tongue (20 wide) and bearing tube, ShaftGear, the lower rim of MotorGear and the 8 mm hex through shaft (Y, ports front and rear) hang below.
# Floor slot to cut: 74 wide (x, centred on the bracket) by 47.5 long (y, from 16 ahead of the plate front face to 31.5 behind it); shaft axis is 29 mm below the floor underside.
# FLOOR_T = 4 mm cardboard is assumed (unconfirmed); the tooth counts re-pick from it (motor to pad gap must land in 1 to 3.5 mm) and the slot follows.
# Hardware: GA37RG, 6 x M3x8 motor (from the front), 1 x M3x6 MotorGear lock screw (from above), 2 x DriveCoupler + M3x16 (wheel_mount.py), hot glue through the pad holes.
# Assembly: 1 glue Bracket over the slot; 2 motor onto the plate rear face (shaft through the plate), six M3x8 from the front; 3 MotorGear on the D shaft, lock screw;
# 4 ShaftGear held in mesh below the floor, ThroughShaft in from the rear through tube, plate and ShaftGear; 5 couplers pinned on both ends (they hold the shaft in).
# Ratio 69:23, the shaft turns 3 x motor speed in the opposite direction (about 300 RPM, 1.5 kg.cm before losses at 12 V).
import FreeCAD as App, Part, math

D = {"NO_RUN": True, "__name__": "differential"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/differential.py").read(), "differential.py", "exec"), D)
V, O, box, prism, rot, lib_shape = (D[k] for k in ("V", "O", "box", "prism", "rot", "lib_shape"))
SHAFT_AF = D["SHAFT_AF"]
import freecad.gears.commands as gc

DOC_NAME = "MotorModule"
OUT = "/home/mikhail/Documents/cad/RC Car/MotorModule.FCStd"
X, Y, Z = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)

AXIS_DEPTH, FLOOR_T, PAD_T = 29.0, 4.0, 4.0
FLOOR_TOP = AXIS_DEPTH + FLOOR_T
PAD_Z0, PAD_Z1 = FLOOR_TOP, FLOOR_TOP + PAD_T
M, PA, CLEARANCE, BACKLASH = 1.25, 20.0, 0.25, 0.25
FACE, PLAY = 8.0, 0.2
MOT_GB_D, MOT_GB_L, MOT_CAN_D, MOT_BODY = 37.0, 24.5, 36.2, 57.8
GAP_MIN, GAP_MAX = 1.0, 3.5


def pick_teeth(floor_t):
    for ns in range(10, 60):
        if 2 * M * ns + PLAY - MOT_GB_D / 2 - AXIS_DEPTH - floor_t - PAD_T >= GAP_MIN:
            return 3 * ns, ns


NM, NS = pick_teeth(FLOOR_T)
CD = M * (NM + NS) / 2 + PLAY
MX, MZ = 0.0, CD
PHASE_M, PHASE_S = 1.304, 11.739

MOT_SH_D, MOT_FLAT_AF, MOT_FLAT_L, MOT_SH_L, MOT_BOSS_D, MOT_BOSS_L = 6.0, 5.5, 14.0, 20.0, 12.0, 5.0
MOT_PCD, MOT_HOLE_D, MOT_CB_D, MOT_CB_DEEP, MOT_BOSS_HOLE = 31.0, 3.4, 6.2, 2.5, 12.6
SCREW_HEAD_H, LOCK_LEN, LOCK_PILOT = 2.4, 6.0, 2.8
SOCKET, BORE, JOURNAL, PILOT, PS_OUT, PS_PILOT = 8.3, 9.6, 9.3, 2.8, 16.0, 5.9
CPL_D, CPL_L, CPL_PIN = 14.0, 17.5, 4.0
STAND = PS_OUT - PS_PILOT - CPL_PIN
END_GAP = 0.2

PLATE_T, PR, TR = 5.0, 26.0, 10.0
TUBE_L, TUBE_D, BOSS_D = 25.0, 16.0, 14.0
TUBE_END = PLATE_T + TUBE_L
THRUST = 0.3
G0, G1 = -THRUST - FACE, -THRUST
SG_HUB = STAND - END_GAP
MG_GAP, MG_FLOOR, MG_HUB_D = 1.5, 1.2, 12.0
MG_TIP = PLATE_T - MOT_SH_L
G0M, G1M = -MG_GAP - FACE, -MG_GAP
MG_HUB_L = G0M - MG_TIP + MG_FLOOR
MG_LOCK_Y = G0M - MG_HUB_L / 2
MG_BORE, MG_FLAT_AF = 6.15, 5.675
TIP_F, TIP_R = G0 - PS_OUT, TUBE_END - SG_HUB + PS_OUT
JF_Y, JR_L = (0.3, PLATE_T + 0.6), 8.0
JR_Y = (TUBE_END - JR_L, TUBE_END - 0.25)

PAD_Y1 = PLATE_T + MOT_BODY + 3.2
RAIL_X, RAIL_Y1, RAIL_CLR = (9.0, 13.0), PLATE_T + MOT_BODY, 0.3
GUS_X0, GUS_H, GUS_L = 20.0, 11.0, 25.0
GLUE_D = 5.0
GLUES = [(sx * 21.5, y) for sx in (-1, 1) for y in (38.0, 50.0, 62.0)]
SLOT_X, SLOT_Y0, SLOT_Y1 = 74.0, -16.0, 31.5
SLOT_LEN = SLOT_Y1 - SLOT_Y0
SLOT_MARGIN = 1.5
ASM_PARTS = ("Bracket", "MotorGear", "ShaftGear", "ThroughShaft")
COLORS = dict(Bracket=(0.5, 0.5, 0.55), MotorGear=(0.9, 0.5, 0.1), ShaftGear=(0.2, 0.7, 0.4), ThroughShaft=(0.7, 0.3, 0.8))


def yc(r, y0, y1, x=0.0, z=0.0):
    return Part.makeCylinder(r, y1 - y0, V(x, y0, z), Y)


def yhex(af, y0, y1):
    return rot(D["hexprism"](af, y0, y1), Z, 90)


def zhole(r, x, y, z0, z1):
    t, w = r / math.sqrt(2), r * math.sqrt(2) - r - 1
    pts = [V(x + a, y + b, z0) for a, b in ((-t, t), (t, t), (w, r + 1), (-w, r + 1))]
    return Part.makeCylinder(r, z1 - z0, V(x, y, z0), Z).fuse(prism(pts, V(0, 0, z1 - z0)))


def gear(n, y0, phase):
    s = lib_shape(App.ActiveDocument, gc.InvoluteGear, num_teeth=n, module="%g mm" % M, height="%g mm" % FACE,
                  pressure_angle="%g deg" % PA, clearance=CLEARANCE, backlash="%g mm" % BACKLASH, axle_hole=False)
    s = rot(rot(s, Z, phase), X, -90)
    s.translate(V(0, y0, 0))
    return s


def build_motor_gear():
    g = gear(NM, G0M, PHASE_M).fuse(yc(MG_HUB_D / 2, G0M - MG_HUB_L, G0M + 0.01))
    g.translate(V(MX, 0, MZ))
    bore = yc(MG_BORE / 2, MG_TIP, G1M + 1, MX, MZ).common(
        box(MX - 5, MX + 5, MG_TIP, G1M + 2, MZ - 5, MZ + MG_FLAT_AF - MG_BORE / 2)).fuse(yc(MG_BORE / 2, MG_TIP + MOT_FLAT_L, G1M + 1, MX, MZ))
    g = g.cut(bore).cut(Part.makeCylinder(LOCK_PILOT / 2, 10, V(MX, MG_LOCK_Y, MZ + 1)))
    return g.removeSplitter()


def build_shaft_gear():
    g = gear(NS, G0, PHASE_S).fuse(yc(BOSS_D / 2, G0 - SG_HUB, G0 + 0.01))
    return g.cut(yhex(SOCKET, TIP_F, G1 + 1)).removeSplitter()


def build_shaft():
    s = yhex(SHAFT_AF, TIP_F, TIP_R).fuse(yc(JOURNAL / 2, *JF_Y)).fuse(yc(JOURNAL / 2, *JR_Y))
    s = s.cut(box(-10, 10, TIP_F - 1, TIP_R + 1, -10, -SHAFT_AF / 2))
    for y in (TIP_F + PS_PILOT, TIP_R - PS_PILOT):
        s = s.cut(Part.makeCylinder(PILOT / 2, 20, V(0, y, -10), Z))
    return s.removeSplitter()


def rails():
    clr = yc(MOT_GB_D / 2 + RAIL_CLR, PLATE_T - 1, RAIL_Y1 + 1, MX, MZ)
    return [box(sx * RAIL_X[0], sx * RAIL_X[1], PLATE_T - 0.01, RAIL_Y1, PAD_Z1 - 0.01, MZ).cut(clr) for sx in (-1, 1)]


def gussets():
    z0, y0 = PAD_Z1 - 0.01, PLATE_T - 0.01
    out = []
    for sx in (-1, 1):
        x0 = sx * GUS_X0
        pts = [V(x0, y0, z0), V(x0, y0, z0 + GUS_H), V(x0, y0 + GUS_L, z0)]
        out.append(prism(pts, V(sx * (PR - GUS_X0), 0, 0)))
    return out


def build_bracket():
    pad = box(-PR, PR, PLATE_T, PAD_Y1, PAD_Z0, PAD_Z1)
    pad = pad.makeFillet(4.0, [e for e in pad.Edges if abs(e.BoundBox.ZLength - PAD_T) < 1e-6 and e.BoundBox.YMin > PAD_Y1 - 1])
    b = pad.fuse(box(-PR, PR, 0, PLATE_T, PAD_Z0, MZ)).fuse(yc(PR, 0, PLATE_T, MX, MZ))
    b = b.fuse(box(-TR, TR, 0, PLATE_T, 0, PAD_Z0 + 1)).fuse(yc(TR, 0, PLATE_T)).fuse(yc(TUBE_D / 2, PLATE_T - 0.01, TUBE_END))
    for s in rails() + gussets():
        b = b.fuse(s)
    b = b.cut(yc(BORE / 2, -1, TUBE_END + 1)).cut(yc(MOT_BOSS_HOLE / 2, -1, PLATE_T + 1, MX, MZ))
    for k in range(6):
        a = math.radians(60 * k)
        x, z = MX + MOT_PCD / 2 * math.cos(a), MZ + MOT_PCD / 2 * math.sin(a)
        b = b.cut(yc(MOT_HOLE_D / 2, -1, PLATE_T + 1, x, z)).cut(yc(MOT_CB_D / 2, -1, MOT_CB_DEEP, x, z))
    for x, y in GLUES:
        b = b.cut(zhole(GLUE_D / 2, x, y, PAD_Z0 - 1, PAD_Z1 + 1))
    return b.removeSplitter()


def build_motor():
    s = yc(MOT_GB_D / 2, PLATE_T, PLATE_T + MOT_GB_L, MX, MZ).fuse(yc(MOT_CAN_D / 2, PLATE_T + MOT_GB_L - 0.01, PLATE_T + MOT_BODY, MX, MZ))
    s = s.fuse(yc(MOT_BOSS_D / 2, PLATE_T - MOT_BOSS_L, PLATE_T + 0.01, MX, MZ))
    sh = yc(MOT_SH_D / 2, PLATE_T - MOT_SH_L, PLATE_T, MX, MZ).cut(
        box(MX - 5, MX + 5, PLATE_T - MOT_SH_L - 1, PLATE_T - MOT_SH_L + MOT_FLAT_L, MZ + MOT_FLAT_AF - MOT_SH_D / 2, MZ + 5))
    return s.fuse(sh)


def sleeve(y_in, sign):
    c = yc(CPL_D / 2, *sorted((y_in, y_in + sign * CPL_L)))
    return c.cut(yhex(SOCKET, y_in - CPL_L - 1, y_in + CPL_L + 1))


def lock_screw():
    return Part.makeCylinder(1.5, LOCK_LEN, V(MX, MG_LOCK_Y, MZ + MOT_FLAT_AF - MOT_SH_D / 2), Z)


def floor_slab():
    return box(-60, 60, -40, 90, AXIS_DEPTH, FLOOR_TOP).cut(box(-SLOT_X / 2, SLOT_X / 2, SLOT_Y0, SLOT_Y1, AXIS_DEPTH - 1, FLOOR_TOP + 1))


def below_floor(s):
    return s.common(box(-200, 200, -200, 200, -200, FLOOR_TOP - 0.01))


def vol(a, b):
    return a.common(b).Volume


def move(s, dx=0.0, dy=0.0, dz=0.0):
    s = s.copy()
    s.translate(V(dx, dy, dz))
    return s


def swing(s, a, cx=0.0, cz=0.0):
    s = s.copy()
    s.rotate(V(cx, 0, cz), Y, a)
    return s


def sweep_clear(mover, still, ys):
    return max(vol(move(mover, dy=y), still) for y in ys)


def mesh(mg, sg):
    rows = []
    for k in range(7):
        a = k * 360.0 / NM / 6
        m, s = swing(mg, a, MX, MZ), swing(sg, -a * NM / NS)
        rows.append((round(a, 2), round(vol(m, s), 4), round(m.distToShape(s)[0], 3)))
    return rows


def engagement(mg):
    z = MZ + MOT_FLAT_AF - MOT_SH_D / 2 + 0.15
    lo = PLATE_T - MOT_SH_L + 0.5
    hi = PLATE_T - MOT_SH_L + MOT_FLAT_L
    ys = [lo + 0.25 * i for i in range(int((hi - lo) / 0.25) + 1)]
    return 0.25 * sum(mg.isInside(V(MX, y + 0.125, z), 1e-6, True) for y in ys[:-1])


def verify(parts):
    br, mg, sg, sh = (parts[n] for n in ASM_PARTS)
    mot = build_motor()
    cf, cr = sleeve(TIP_F + PS_PILOT + CPL_PIN, -1), sleeve(TIP_R - PS_PILOT - CPL_PIN, 1)
    lk = lock_screw()
    fl, rl, gs = floor_slab(), rails(), gussets()
    P = dict(Bracket=br, Motor=mot, MotorGear=mg, ShaftGear=sg, ThroughShaft=sh, CplF=cf, CplR=cr)
    names = list(P)
    rep = {}
    rep["overlap"] = {(a, b): round(vol(P[a], P[b]), 4) for i, a in enumerate(names) for b in names[i + 1:]
                      if (a, b) != ("MotorGear", "ShaftGear") and vol(P[a], P[b]) > 1e-3}
    fits = {("Bracket", "Motor"), ("Bracket", "MotorGear"), ("Bracket", "ShaftGear"), ("Bracket", "ThroughShaft"), ("Bracket", "CplR"),
            ("Motor", "MotorGear"), ("MotorGear", "ShaftGear"), ("ShaftGear", "ThroughShaft"), ("ShaftGear", "CplF"),
            ("ThroughShaft", "CplF"), ("ThroughShaft", "CplR")}
    rep["clear"] = {(a, b): round(P[a].distToShape(P[b])[0], 3) for i, a in enumerate(names) for b in names[i + 1:]
                    if (a, b) not in fits}
    rep["fits"] = {k: round(P[k[0]].distToShape(P[k[1]])[0], 3) for k in sorted(fits)}
    rep["rail_motor"] = round(min(mot.distToShape(r)[0] for r in rl), 3)
    rep["gus_motor"] = round(min(min(P[k].distToShape(g)[0] for g in gs) for k in ("Motor", "MotorGear")), 3)
    rep["lock_vs_shaft"] = round(vol(lk, mot), 4)
    rep["mesh"] = mesh(mg, sg)
    rep["cd"] = round(math.hypot(mg.Solids[0].CenterOfMass.x - sg.Solids[0].CenterOfMass.x, mg.Solids[0].CenterOfMass.z - sg.Solids[0].CenterOfMass.z), 3)
    rep["engage"] = engagement(mg)
    bw = min(mg.slice(Y, MG_TIP + 0.5), key=lambda w: w.BoundBox.ZLength)
    rep["flat_clr"] = round(bw.BoundBox.ZMax - (MZ + MOT_FLAT_AF - MOT_SH_D / 2), 3)
    rep["end_float"] = round(cf.distToShape(sg)[0] + cr.distToShape(br)[0] + sg.distToShape(br)[0], 3)
    rep["bbox"] = {n: tuple(round(v, 2) for v in (s.BoundBox.XLength, s.BoundBox.YLength, s.BoundBox.ZLength)) for n, s in parts.items()}
    rep["bbox_min"] = {n: tuple(round(v, 2) for v in (s.BoundBox.XMin, s.BoundBox.YMin, s.BoundBox.ZMin)) for n, s in parts.items()}
    rep["axis_below_floor"] = round(fl.BoundBox.ZMin - 0.0, 3)
    rep["motor_pad_gap"] = round(mot.BoundBox.ZMin - PAD_Z1, 3)
    rep["mg_gap"] = round(-mg.BoundBox.YMax, 3)
    rep["mg_floor"] = [mg.isInside(V(MX, MG_TIP + d, MZ), 1e-6, True) for d in (-0.1, 0.1)]
    rep["mg_hub"] = round(mg.distToShape(yc(BOSS_D / 2, G0 - SG_HUB, G0 + 0.01))[0], 3)
    low = [below_floor(br), below_floor(mg), sg]
    bb = [s.BoundBox for s in low]
    need = dict(x=round(2 * max(max(abs(b.XMin), abs(b.XMax)) for b in bb), 3), y0=round(min(b.YMin for b in bb), 3), y1=round(max(b.YMax for b in bb), 3))
    rep["slot_need"] = need
    rep["floor"] = dict(br_low_x=round(max(abs(low[0].BoundBox.XMin), abs(low[0].BoundBox.XMax)), 3),
                        **{n: round(s.distToShape(fl)[0], 3) for n, s in zip(("br_low", "mg_low", "sg"), low)})
    rep["ports"] = dict(
        hex_AF=SHAFT_AF, stick_front=round(G0 - sh.BoundBox.YMin, 3), stick_rear=round(sh.BoundBox.YMax - (TUBE_END - SG_HUB), 3),
        pilot_front=round(PS_PILOT, 3), pilot_rear=round(PS_PILOT, 3),
        pilot_hole_open=[not sh.isInside(V(0, y, 0), 1e-6, True) and sh.isInside(V(0, y + 2.0, 0), 1e-6, True)
                         for y in (TIP_F + PS_PILOT, TIP_R - PS_PILOT - 0.0)])
    steps = {}
    steps["motor_in"] = sweep_clear(mot, br, [i * 3.0 for i in range(0, 25)])
    for k in range(6):
        a = math.radians(60 * k)
        x, z = MX + MOT_PCD / 2 * math.cos(a), MZ + MOT_PCD / 2 * math.sin(a)
        path = yc(MOT_CB_D / 2, G0 - 40, MOT_CB_DEEP - SCREW_HEAD_H, x, z)
        steps["screw%d" % k] = vol(path, br) + vol(path, mot) + vol(path, sg)
    steps["gear_on"] = sweep_clear(mg, mot.fuse(br), [-i * 3.0 for i in range(0, 12)])
    path = Part.makeCylinder(3.0, 40, V(MX, MG_LOCK_Y, MZ + 4.0), Z)
    steps["lock_access"] = vol(path, br) + vol(path, sg) + vol(path, mot)
    steps["shaft_in"] = sweep_clear(sh, br.fuse(sg).fuse(mot).fuse(mg), [i * 3.0 for i in range(0, 35)])
    steps["cpl_front"] = sweep_clear(cf, br.fuse(sg).fuse(mot).fuse(mg), [-i * 3.0 for i in range(0, 12)])
    steps["cpl_rear"] = sweep_clear(cr, br.fuse(sg).fuse(mot), [i * 3.0 for i in range(0, 12)])
    rep["steps"] = {k: round(v, 4) for k, v in steps.items()}
    return rep


def check(rep):
    assert NM == 3 * NS and (NM + NS) % 4 == 0, (NM, NS)
    assert not rep["overlap"], rep["overlap"]
    assert all(v >= 1.5 for v in rep["clear"].values()), rep["clear"]
    assert all(r[1] <= 0.3 and r[2] > 0 for r in rep["mesh"]), rep["mesh"]
    assert abs(rep["cd"] - CD) < 0.05 and rep["engage"] >= 8.0, rep
    assert 0.08 <= rep["flat_clr"] <= 0.15, rep["flat_clr"]
    assert rep["rail_motor"] >= 0.25 and rep["gus_motor"] >= 1.5, rep
    assert rep["fits"][("Bracket", "MotorGear")] >= 0.25, rep["fits"]
    assert 0.3 <= rep["end_float"] <= 0.8, rep["end_float"]
    assert abs(rep["mg_gap"] - MG_GAP) < 1e-3 and rep["mg_floor"] == [True, False], (rep["mg_gap"], rep["mg_floor"])
    assert rep["axis_below_floor"] == AXIS_DEPTH == 29.0 and rep["mg_hub"] >= 1.5, rep
    assert GAP_MIN <= rep["motor_pad_gap"] <= GAP_MAX, rep["motor_pad_gap"]
    n = rep["slot_need"]
    assert SLOT_X >= n["x"] + 2 * SLOT_MARGIN and SLOT_Y0 <= n["y0"] - SLOT_MARGIN and SLOT_Y1 >= n["y1"] + SLOT_MARGIN, (n, SLOT_X, SLOT_Y0, SLOT_Y1)
    assert all(v >= SLOT_MARGIN for k, v in rep["floor"].items() if k != "br_low_x"), rep["floor"]
    assert rep["floor"]["br_low_x"] <= TR + 1e-6, rep["floor"]
    assert all(v < 1e-3 for v in rep["steps"].values()), rep["steps"]
    assert abs(rep["ports"]["stick_front"] - PS_OUT) < 1e-3 and abs(rep["ports"]["stick_rear"] - PS_OUT) < 1e-3, rep["ports"]
    assert all(rep["ports"]["pilot_hole_open"]), rep["ports"]


def build_parts():
    return dict(Bracket=build_bracket(), MotorGear=build_motor_gear(), ShaftGear=build_shaft_gear(), ThroughShaft=build_shaft())


def main():
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    parts = build_parts()
    for n, s in parts.items():
        assert s.isValid() and len(s.Solids) == 1, n
        o = doc.addObject("Part::Feature", n)
        o.Shape = s
        if App.GuiUp:
            o.ViewObject.ShapeColor = COLORS[n]
    rep = verify(parts)
    print("report", rep)
    check(rep)
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
