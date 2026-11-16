# Gearbox module: GA37RG gearmotor ON TOP of the cardboard floor drives a servo shifted THREE SPEED sliding gear transmission (separate flat gears on carriers). 8 mm hex through shaft (Y axis, 16 mm plain hex ports front and rear, dia 2.8 cross pilot 5.9 from each tip) 29 mm below the floor underside; everything under the floor sits in a printed CasePan.
# Shafts in one plane (x = 0): motor axis z 57.9, layshaft z 25.7, through shaft z 0. Module 1, shift pairs sum to 64 (centre distance 32.2): C 44:20, B 38:26, A 31:33 (motor gear first); fixed transfer 28:23 (centre distance 25.7). Largest gear tip dia 46.0 (MotorGear_C).
# Ratios and shaft rpm at 100 rpm motor: A 1.144 (114 rpm), B 1.779 (178 rpm), C 2.678 (268 rpm). Servo positions in stroke order: B (rear), A (mid), C (front), 0.8 mm gear to gear gap at each neutral midpoint (shift step 2 x (face 5.1 + 0.8) = 11.8, stroke 23.6). The order B, A, C is forced (A, B, C or C, B, A put a motor tip circle across a non partner slide gear). Shift only while the gears turn slowly.
# Servo force (B6, accepted): stroke 23.6 within +-40 deg needs an 18.4 mm pin radius, so a 0.08 N.m servo gives 4.36 N at the fork (asserted at 4.35 unrounded); the guide friction (mu about 0.4 times the push) takes roughly 40 percent of that, leaving about 2.6 N to move the fork. estimates() asserts every stress under 15 MPa at that force, ring wall 1.6 included.
# Sizes: footprint on the floor (parts above the floor top) 93.8 x 153.4 (x -42.8 to +51.0: ears and ServoMount wall; y +65 to -88.4: Bracket pad to ServoMount crossbar). Floor cut-out 64.0 x 102.6 (x -32..32, y +13.2 behind to -89.4 ahead, y = 0 is the Bracket front face): the length is over the 92 allowance (accepted, asserted at most the measured extent of the parts through the slab plus 2.0, i.e. 1.0 clear all round) mostly because the 23.6 stroke and the 49.6 long fork guide set UF = 82.2 (plus the plate and the two rod screw heads for the front edge), and the layshaft rear boss and thrust head (z up to 32, inside the 4 mm floor) set the rear edge at +13.2. Lower plates are 59.6 wide (2.2 clear each side; the fork tower and block are inside 1.4 or more). Plastic 168.1 cm3 (CasePan 38.0 cm3).
# CasePan (A1): printed pan under the floor, 2.0 walls, outer x +-32.2, y +15.1 to -87.3 (long with the 16 mm hex ports passing through slots 11.4 wide in both end walls), floor outer z -15.4, rim z 28.2 (0.8 under the floor underside). Depth below the floor underside 44.4; with 100 mm wheels on the through shaft axis the pan bottom is 34.6 above the ground. 4 x M3x8 from below, heads fully sunk in 3.2 deep dia 6.6 counterbores (M3 pan head is dia 6 x 3.2, so the bottom is flush, 0.3 radial; a 0.2 sacrificial skin closes the dia 3.6 hole at the counterbore ceiling, see the print paragraph), through posts into pilots in 4 rails (two on the Bracket rear face, two on the FrontPlate rear face, x +-19), asserted 2.0 wall. Gaps: 0.9 to the shafts and T2, 1.0 to the fork block, 0.4 to the lower plates, 0.8 to the floor. Prints open side up, no supports; vertical corners r4, 2.0 chamfer at the base (45 deg), rim 0.8 chamfer, 0.8 fillets blend the end slot edges. The case is not fully closed: the end wall slots (about 330 mm2 per end) run up to the rim because the pan has to lift on from below past the shaft, a lid for them is not modelled. The front wall has a notch 8 wide (1.0 clear round each dia 6 rod screw head) from z 23.6 up to the rim so the two FrontPlate rod screw heads, which stand 3.2 proud of the plate, clear it while it lifts on. Removal order: take the CasePan off first, then pull the ThroughShaft (its dia 12.6 head would hit the 11.4 end slot with the pan on).
# Liners (A2): PTFE tube 10 ID x 12 OD to be used as plain bearings, 4 liners of LINER_L 8.0: Sleeve_1 (through shaft rear) y 1.6..9.6 z 0, Sleeve_2 (through shaft front) u 75.3..83.3 z 0, Sleeve_3 (layshaft rear) y 1.6..9.6 z 25.7, Sleeve_4 (layshaft front) u 75.3..83.3 z 25.7. Printed placeholders named Sleeve_1..4 (one print group, 4 copies, standing on end). Pocket bore LINER_BORE 12.2 (tune after measuring the tube), 2.0 wall boss with cone blend, 1.6 lip with a 10.6 bore (layshaft front pocket is blind, 1.6 floor). Rear liners go in from the rear to the front lip; front liners go in from the plate rear face to the front lip. Retention the other way: the thrust heads (dia 12.6 round collars on the REAR end of both shafts, 0.2 off the liner end) hold the rear liners, the T2 and T1 hub ends (0.2 off the liner end) hold the front liners. Nothing larger than the hex ever passes through a liner (heads and hubs stay behind or in front of them). 8.0 AF hex (9.24 across corners) in the dia 10.0 bore: 0.38 radial. Each shaft floats 0.4 total (0.2 head face, 0.2 hub face). MotorCap stub bore: no liner (stub dia 10 runs in a 10.6 bore beside a 9.0 boss; a 16.2 boss would hit the gear C hub), so it stays a printed bore.
# ServoMount (A3, A5): a bridge fastened at BOTH ends: front end (crossbar) to the FrontPlate with 2 x M3x12, rear end (a 4.0 thick tie plate over the rear +x Bracket ear, x 33.2 to 50.8, y -3.1 to +16.8, corners r2, 0.8 bed chamfer) to the Bracket with the ear bolt at x 38, y 12 (dia 3.6 pass hole, 3.0 ring wall asserted), which becomes an M3x16 through tie, ear and cardboard with a nut below the floor. Own part, prints on its outer wall face (-X up), no supports, everything is a prism along x and every strip stays inside the wall outline (the old 5 mm rear chamfer of the wall left the strip corner floating, removed). Crossbar (3.2 thick, in front of the FrontPlate) is held by 2 x M3x12 from the front (holes x 33.6 and 40.2, 6.6 apart: heads dia 6.0 never overlap, asserted spacing at least head + 0.5, and the heads are modelled in the dia 6 driver sweeps) into pilots in a bar on the FrontPlate rear face (FrontPlate is a plain plate plus the screw bar, a flat wing and a short -x glue lip, prints front face down); base slab, 3.2 wall rail, post and strip under each servo tab, 0.8 chamfer round the bed face. Solid sections measured on the shape: crossbar 3.2 x 7.8, slab 4.0 x 7.6, wall 3.2 x 21.7, tab strips 6.7 x 21.7 and 4.8 x 6.7, FrontPlate 3.0 x 10.7, bar 11.0 x 7.0, rod 6.8 x 6.8, tie plate 4.0 x 17.8, Bracket ear 4.0 x 18.0 (all at least 3 x 6). Servo tab screws are the servo kit M2 thread forming screws into dia 1.6 pilots, slotted 1 mm outward, driven with a tilted driver; the hole is 2.25 from the body end so the body side wall cannot reach 2.0: measured 0.86 (MISSED). The pilots are slotted 1 mm outward (covers hole spacing +1) but not inward: a spacing of 26.5 (-1) puts the holes 0.5 inside, and the strip cannot grow inward because the body is there, so that case is not covered (a through bolt with a clamp strap is the real fix if it strips). TOL_CASES include a shrink case (grow -1) for the arm and mount clearances.
# Servo tolerance (B4): every body dimension +-1 mm, tab height +-1, horn height +-1 (arm +-2 total, TOL_CASES in step_tol), plus a rigid shaft shift of +-1 in x and in y (SHIFTS: pin to fork overlap 0). The arm bottom sits ARM_CLR 1.5 + 2 above a pin tower on the fork block (tower z 40.2, slot 11.4 wide in x and 6.4 in y for the dia 4.0 pin, 1.3 side walls, roof a flat 8.4 wide bridge at the full 6.4 slot length with 50 deg corner walls, so the pin stays free over its sweep incl. the +-1 shifts; fit after the print change: pin to slot slack measured 1.2 each way, 2.4 total, same as before, asserted 1.1 to 1.3 in step_tol). Pin 8.2 long: engaged at least 2.7 at the high end, arm 1.5 above the tower at the low end, pin 2.2 above the rod, arm 1.0 from the mount, body clear of the mount: all asserted. The pin sits at the REAR of the block (6.5 behind the tower start), so the arm stays clear of MotorGear_C. Arm to horn recess is 2.0 deep for the 1.8 horn (0.2) and 0.3 per side: it is the torque carrying exception to the gap table.
# Mounting (A4): four corner ears on the Bracket pad flush with its underside, bolt holes dia 3.6 at x +-38, y +12 and +56 (76 x 44 pattern), 3.0 wall (ear radius 4.8, underside 50 deg or steeper so it prints without support), 3 x M3x12 and 1 x M3x16 (the tie ear at x 38, y 12 also clamps the ServoMount) bolt + nut through the cardboard (Ref_Bolts); driver dia 6 x 60 from above proved. Glue land kept: rear pad 61 mm and 6 dia 5 holes, -x lip 2.4 mm, pad wing now 68 wide (2 mm on the cardboard each side of the cut-out), pad top area 34 cm2; no 10 mm target.
# Hardware: GA37RG; 6 x M3x8 motor (from the front); 4 x M3x6 grub (motor carrier flat from above, SlideCap from below onto a dimple, T1 45 deg from below left, T2 from below; the T1 and T2 pilots sit 3.5 in front of the gear face so a dia 6 driver clears the gear, proved without excluding the host part); 1 x M3x16 MotorCap (axial, head at the bottom of a dia 6.6 bore 14.2 deep, 10.5 mm above the carrier arbor end, 1.7 stub wall round it, 5.5 mm of thread into the 10 deep carrier pilot; the dia 6 driver runs the bore with 0.3 radial, measured on the shape, and is swept against every step 7 part, before the FrontPlate goes on); 2 x M3x8 FrontPlate into Rod ends (from the front, 6.5 mm of thread into the 9 deep pilot) and 2 x M3x8 Bracket to Rod ends (axial from the rear face of the Bracket, through a dia 3.6 hole in the 1.4 thick pocket floor, 0.2 skin cleared first into a dia 2.8 pilot 9 deep in each rod rear end, 6.6 mm of thread, 2.0 walls; the rear rod positions are free behind the plate, 2.4 under the pad and 17 from the motor body, so no cross screw is needed; the heads stand 3.2 proud on the rear face; the rods sit on the pocket floors so the screws only clamp, and the rear rod screws are serviced only with the module off the cardboard (the floor slab and the CasePan stand in the way of the driver, it is swept before step 11); each rod is now a tie bar screwed at both ends: with CasePan and ServoMount off, Bracket, rods and FrontPlate cannot be pulled apart, asserted from the measured pilots and holes); the six motor face counterbores are dia 6.6; 2 x M3x12 ServoMount to FrontPlate (from the front); 4 x M3x8 CasePan (from below); screw totals asserted against the kit list in check(): M3x8 x 14, M3x12 x 5, M3x16 x 2, M3x6 grub x 4; 2 x M2 servo kit screws in the tabs; servo horn centre screw from the servo kit; 4 ear bolts with 4 nuts through the ears: 3 x M3x12 plus 1 x M3x16 at the tie ear (x 38, y 12), which also clamps the ServoMount tie plate (from above); hot glue through the pad holes; 4 PTFE liners 12 x 10 x 8 (later). The ear bolts and the four rod screw heads (Ref_Heads) are modelled, plus the ServoMount heads and the driver in the sweeps.
# Servo ES08MA II class, dimensions UNVERIFIED catalogue values (SV_*): body 23.0 x 11.5 x 24.0, tab span 32.5, tab 2.0 thick 16.0 below the top, hole spacing 27.5, spline 4.8 dia 2.7 long, horn 14 long.
# Parts (25, 0 supports): Bracket, FrontPlate, MotorCarrier, MotorCap, MotorGear_B/A/C, SlideCarrier (gear C integral), SlideGear_A/B, SlideCap (spool, 6.8 flange: 2.0 walls round the grub), Layshaft, ThroughShaft, T1, T2, ShiftFork (ring wall 1.6, pin tower), Rod_1/2 (6.8 square, 2.0 pilot walls), ServoArm, CasePan, ServoMount, Sleeve_1..4. PLA, 0.4 nozzle, 0.2 layers. Ref_Motor, Ref_Servo, Ref_Floor, Ref_Bolts, Ref_Heads are not printed.
# Print rules (supports OFF, every part in PRINT_UP), measured on the shapes in printable() and asserted in check() with no exemption except BED_EXEMPT: P1 no down face shallower than 45 deg (50 deg built where possible: ear undersides, case base chamfer, rod pocket mouths); P2 no flat ledge, ring or step that starts in mid air, only true bridges (convex, straight span 10 or less, solid under both ends); P3 a ceiling pierced by a smaller hole is not a bridge, so the six motor counterbores (ceiling z 2.4), the two Bracket rod pockets (z 2.6), the four CasePan counterbores (3.2), the MotorCap arbor recess (3.0) and the ServoArm horn recess (2.0) each keep a sacrificial 0.2 skin across the hole above the ceiling, a modelled part of the solid that a dia 3.6 drill (dia 3.2 for the arm) clears before assembly, and the ceiling stays a clean bridge on a layer boundary; P4 horizontal round holes over dia 6 get a teardrop or flat roof (none exist, the largest is the dia 5 glue holes, the ShiftFork pin slot roof is an 8.4 wide flat bridge with 50 deg corner walls), holes of dia 6 or less stay round and the layer test accepts exactly their roof footprint; P5 every 0.2 layer (cut from the tessellated shape at mid layer, shapely) is compared with the layer below grown by 0.3: no region may lie outside it except a bridge; P6 bed contact at least 60 mm2, height at most 4 x the smaller side of the first layer footprint, first layer walls at least 0.8 (area lost by opening the first layer by 0.4 at most 1 mm2). BED_EXEMPT lists Sleeve_1..4 for P6 bed contact only (34.5 mm2): they are placeholders for 12 x 10 PTFE tube cut to 8 mm, 12 dia x 8 squat with no overhang. Fits after the print changes: MotorCap arbor recess 8.7 (0.35 radial on the dia 8.0 arbor, was 0.2); MotorCarrier D bore 6.3 on the dia 6.0 motor shaft (0.15 radial, was 0.075, which printed too tight), flat 5.8 over the 5.5 motor flat, held by the grub; rod pockets 2.6 deep, so each rod is 0.1 shorter (end gap still 0.0, the pocket floor is 1.4); motor counterbores 2.4 deep (heads 0.8 proud, M3x8 engagement 6.4); horn recess 2.0 over the 1.8 horn (0.2, was 0.1); the ShiftFork rod guide mouth at the bed end is a 0.45 deep 50 deg lead in so the first layer wall stays 0.8 (the far end keeps the 0.8 deep one); the ear undersides, CasePan base chamfer (2.0 x 1.68) and the pocket mouths are 50 deg (ServoMount bed chamfers stay 45 deg, the limit, a 50 deg chamfer failed on the end edges).
# Print orientation (PRINT_UP): Bracket +Y, FrontPlate +Y (front face down), MotorCarrier -Y, MotorCap -Y, motor and slide gears +Y, SlideCarrier +Y, SlideCap -Y, T1 -Y, T2 -Y, ShiftFork -Y (ring and block rear faces on the bed, 45 deg front slope on the tower), shafts and rods +Z (flat on a hex flat), ServoArm -Z, CasePan +Z, ServoMount -X, Sleeves +Y.
# Assembly order (each step is a 1 mm translation sweep in step_assembly with zero common volume; fork at mid stroke when the servo goes in; floor slab present from step 11): 1 Sleeve_1 and Sleeve_3 into the Bracket from the rear, Sleeve_2 and Sleeve_4 into the FrontPlate from its rear face; 2 motor into the Bracket from the rear, 6 screws from the front; 3 MotorCarrier on the D shaft, grub from above; 4 MotorGear_B; 5 Layshaft pushed in from the REAR through Sleeve_3 (head stops 0.2 from the liner); 6 slide unit built loose on the SlideCarrier (SlideGear_A, SlideGear_B, ShiftFork ring, SlideCap, grub from below), then onto the Layshaft from the front; 7 MotorGear_A, MotorGear_C, MotorCap and its M3x16 screw; 8 T1 on the Layshaft (grub 45 deg from below left, left slack until step 10 because the plate carries the Sleeve_4 gauge face); T2 is NOT fitted yet, so nothing loose falls off the mesh when the module is lowered; 9 Rod_1, Rod_2 from the front through the fork block; 10 FrontPlate (with Sleeve_2, Sleeve_4) from the front, 2 M3x8 into the rod ends, then 2 M3x8 axially from the rear face of the Bracket into the rod rear ends (driver dia 6 x 60 swept from the head top with every part of steps 1 to 10 and the front heads present: motor, gears, slide unit, cap, T1, rods, FrontPlate; nothing else exists yet, and the floor slab must not be there since it would cut the driver, so these are driven before step 11); 11 module lowered through the cut-out onto the cardboard, 3 ear bolts (M3x12, not the rear +x ear); 12 T2 raised from below into mesh with T1 (up-sweep proved, hold it by hand), then ThroughShaft pushed in from the rear under the floor through Sleeve_1, T2 and Sleeve_2, T2 grub from below. Axial setting: with a 0.2 mm feeler gauge between each rear head and its Sleeve_1/Sleeve_3 and another between each hub end (T1, T2) and its Sleeve_4/Sleeve_2, push the shaft against the gauges and tighten the T1 grub (after step 10, proved reachable with the plate on) and the T2 grub; the hub grub pilots are only 2.7 to 2.9 deep (the hub wall, 2.85, is the limit) so use M3x6 grubs with thread locker; 13 CasePan up from below, 4 M3x8; 14 ServoMount lowered onto the cardboard against the FrontPlate, 2 M3x12 from the front, then the M3x16 down through the tie plate, rear +x ear and cardboard with a nut below (driver dia 6 x 60 from above proved); 15 servo with horn and ServoArm lowered (pin into the tower slot), 2 M2 servo kit tab screws.
# Glue and fit calibration: printed bores a part turns in 0.3 radial or more, spinning or sliding to fixed gaps 0.8 or more (1.0 for SlideCap to Bracket and ServoArm to anything fixed), thrust faces 0.2 each (sum 0.3 to 0.5), the ShiftFork block rides Rod_1 in an 8.4 pocket (0.8 per side, BLK_PK) while the Bracket and FrontPlate pockets keep 0.5 per side for the pushed in rods (the rod ends sit on the pocket floors, 0.0 end gap, so the screws clamp without pulling the plates), M3 pass holes dia 3.6, pilots dia 2.8 with 2.0 walls, walls 1.2 or more.
import FreeCAD as App, Part, math
import numpy as np
from shapely.geometry import MultiLineString, Point, Polygon
from shapely.ops import linemerge, unary_union

D = {"NO_RUN": True, "__name__": "differential"}
exec(compile(open("/home/mikhail/Documents/cad/RC Car/differential.py").read(), "differential.py", "exec"), D)
V, O, box, prism, rot, lib_shape, hexprism = (D[k] for k in ("V", "O", "box", "prism", "rot", "lib_shape", "hexprism"))
SHAFT_AF = D["SHAFT_AF"]
import freecad.gears.commands as gc

DOC_NAME = "Gearbox3"
OUT = "/home/mikhail/Documents/cad/RC Car/Gearbox3.FCStd"
X, Y, Z = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
R3 = math.sqrt(3.0)

AXIS_DEPTH, FLOOR_T, PAD_T = 29.0, 4.0, 4.0
FLOOR_TOP = AXIS_DEPTH + FLOOR_T
PAD_Z0, PAD_Z1 = FLOOR_TOP, FLOOR_TOP + PAD_T
M, PA, CLEARANCE, BACKLASH, PLAY = 1.0, 20.0, 0.25, 0.25, 0.2
NM = dict(B=38, A=31, C=44)
NS = dict(B=26, A=33, C=20)
NT1, NT2 = 28, 23
CD1 = M * (NM["A"] + NS["A"]) / 2 + PLAY
CD2 = M * (NT1 + NT2) / 2 + PLAY
MZ, ZL = CD1 + CD2, CD2
FACE_W, CHAMF = 5.1, 1.0
PLATE_T, FPLATE_T = 4.0, 3.0

MOT_GB_D, MOT_GB_L, MOT_CAN_D, MOT_BODY = 37.0, 24.5, 36.2, 57.8
MOT_SH_D, MOT_FLAT_AF, MOT_FLAT_L, MOT_SH_L, MOT_BOSS_D, MOT_BOSS_L = 6.0, 5.5, 14.0, 20.0, 12.0, 5.0
M3_HEAD_D, M3_HEAD_H, HEAD_BORE = 6.0, 3.2, 6.6
MOT_PCD, MOT_HOLE_D, MOT_CB_D, MOT_CB_DEEP, MOT_BOSS_HOLE = 31.0, 3.6, HEAD_BORE, 2.4, 12.6
SKIN = 0.2
MG_BORE, MG_FLAT_AF = 6.3, 5.8
SOCKET, PILOT, PS_OUT, PS_PILOT = 8.3, 2.8, 16.0, 5.9
SLIDE_AF = 9.0

# servo, catalogue values, UNVERIFIED, to be measured
SV_L, SV_W, SV_H, SV_TAB_SPAN, SV_TAB_T, SV_TAB_Z = 23.0, 11.5, 24.0, 32.5, 2.0, 16.0
SV_HOLE_SP, SV_SPLINE_D, HORN_LEN = 27.5, 4.8, 14.0
SV_OVER = 1.0

# axial map, u = -y measured forward from the Bracket front face
S_STEP, W_SLIDE_PITCH = 2 * (FACE_W + 0.8), 7.2
W_MOTOR_PITCH = W_SLIDE_PITCH + S_STEP
STROKE = 2 * S_STEP
CARR_AF, GEAR_AF = 12.0, 12.3
SL_AF, SL_GAF = 13.0, 13.3
HUB_R, SPA_R, SPC_R = 9.0, 9.7, 8.3

FLANGE_T, GROOVE_W, GROOVE_R, FLANGE_R = 6.8, 4.2, 8.9, 11.3
SPOOL_U0 = 1.0
SPOOL_U1 = SPOOL_U0 + FLANGE_T + GROOVE_W
M0 = SPOOL_U1 + 0.1
RING_RI, RING_T = GROOVE_R + 0.8, 3.5
RING_RO = RING_RI + 1.6
RING_U0 = SPOOL_U0 + FLANGE_T + 0.4

# guide: one 5.4 square rod in a 6.4 pocket (0.5 per side); the servo pin drops through a slot in the block roof, so the push line sits close to the rod axis
ROD_S, ROD_PK, ROD_X = 6.8, 7.8, 23.8
BLK_PK = ROD_S + 2 * 0.8
AT, PIN_D, GRV_W = 3.2, 4.0, 6.4
BLK_Z1 = FLOOR_TOP
ARM_TOL, ARM_CLR, ENGAGE_MIN, PIN_L = 2.0, 1.5, 2.5, 8.2
TW_RAMP, TW_Z1, TW_HALF, TW_SLOT = 7.0, 40.2, 7.0, 5.7
ROOF_HALF = 4.2
ARM_Z0 = TW_Z1 + ARM_CLR + ARM_TOL
ARM_Z1 = ARM_Z0 + AT
RECESS = 2.0
ROD_Z = BLK_Z1 - 1.2 - BLK_PK / 2
GRV_Z = ROD_Z + BLK_PK / 2
PIN_H = PIN_L
PIN_Z0 = ARM_Z0 - PIN_H
BLK_Z0 = ROD_Z - BLK_PK / 2 - 1.2
BLK_X0, BLK_X1 = ROD_X - BLK_PK / 2 - 1.2, ROD_X + BLK_PK / 2 + 1.2
LEVER = math.hypot(ROD_X, ROD_Z - ZL)
BLK_U0 = RING_U0
MOUTH = 0.8
BLK_L = math.ceil(round((2 * LEVER + 2 * MOUTH + 0.2) * 10, 6)) / 10
STOP_GAP = 0.8
UF = math.ceil(round(BLK_U0 + BLK_L + STROKE + STOP_GAP, 6) * 10) / 10
PHI_MAX = 40.0
R_P = S_STEP / math.sin(math.radians(PHI_MAX))
XS = ROD_X + R_P * (1 + math.cos(math.radians(PHI_MAX))) / 2
PIN_U = BLK_U0 + 6.5
YP_MID = PIN_U + S_STEP

def yc(r, y0, y1, x=0.0, z=0.0):
    return Part.makeCylinder(r, y1 - y0, V(x, y0, z), Y)


def ycu(r, u0, u1, x=0.0, z=0.0):
    return yc(r, -u1, -u0, x, z)


def yhex(af, y0, y1, cx=0.0, cz=0.0):
    s = rot(hexprism(af, y0, y1), Z, 90)
    s.translate(V(cx, 0, cz))
    return s


def yhexu(af, u0, u1, cx=0.0, cz=0.0):
    return yhex(af, -u1, -u0, cx, cz)


def move(s, dx=0.0, dy=0.0, dz=0.0):
    s = s.copy()
    s.translate(V(dx, dy, dz))
    return s


def vol(a, b):
    return a.common(b).Volume


def dist(a, b):
    return a.distToShape(b)[0]


def tip(n):
    return n * M / 2 + M


def root(n):
    return n * M / 2 - M * (1 + CLEARANCE)


def ph_up(n):
    return 90.0 % (360.0 / n)


def ph_dn(n):
    return (270.0 - 180.0 / n) % (360.0 / n)


def gear(n, u0, phase, cz=0.0, w=FACE_W):
    s = lib_shape(App.ActiveDocument, gc.InvoluteGear, num_teeth=n, module="%g mm" % M, height="%g mm" % w,
                  pressure_angle="%g deg" % PA, clearance=CLEARANCE, backlash="%g mm" % BACKLASH, axle_hole=False)
    s = rot(rot(s, Z, phase), X, -90)
    s.translate(V(0, -(u0 + w), cz))
    for ye, sg in ((-(u0 + w), 1), (-u0, -1)):
        pts = [(tip(n) - CHAMF, 0.0), (tip(n) + 1.0, CHAMF + 1.0), (tip(n) + 1.0, -1.0), (tip(n) - CHAMF, -1.0)]
        poly = [V(r, ye + sg * t, cz) for r, t in pts]
        s = s.cut(Part.Face(Part.makePolygon(poly + [poly[0]])).revolve(V(0, 0, cz), Y, 360))
    return s.removeSplitter()


def dbore(u0, u1):
    return ycu(MG_BORE / 2, u0, u1, 0, MZ).common(box(-5, 5, -u1 - 1, -u0 + 1, MZ - 5, MZ + MG_FLAT_AF - MG_BORE / 2))


def radial(r, cx, cz, ux, uz, u, rin, rout):
    d = V(ux, 0, uz)
    return Part.makeCylinder(r, rout - rin, V(cx, -u, cz) + d * rin, d)


def mouth(xc, zc, y, sgn, size, ch=0.8, k=0.84):
    def sq(h, yy):
        return Part.makePolygon([V(xc - h, yy, zc - h), V(xc + h, yy, zc - h), V(xc + h, yy, zc + h), V(xc - h, yy, zc + h), V(xc - h, yy, zc - h)])
    return Part.makeLoft([sq(size / 2 + k * (ch + 0.1), y - sgn * 0.1), sq(size / 2, y + sgn * ch)], True)


# liners (PTFE tube later), bosses, thrust heads, case
LINER_BORE, LINER_OD, LINER_ID, LINER_L = 12.2, 12.0, 10.0, 8.0
LIP_T, LIP_BORE, BOSS_WALL, THRUST = 1.6, 10.6, 2.0, 0.2
BOSS_R = LINER_BORE / 2 + BOSS_WALL
HEAD_D, HEAD_T = 12.6, 2.4
RB, FB = LIP_T + LINER_L - PLATE_T, LIP_T + LINER_L - FPLATE_T
POCK_Y1 = LIP_T + LINER_L
HEAD_Y0 = POCK_Y1 + THRUST
HEAD_Y1 = HEAD_Y0 + HEAD_T
CASE_T, PAN_GAP = 2.0, 0.9
PAN_Y_R = HEAD_Y1 + PAN_GAP
PAN_U_F = UF + FPLATE_T + 0.4
PAN_ZIN, PAN_ZOUT, PAN_RIM = -13.4, -15.4, AXIS_DEPTH - 0.8
PAN_XI = 30.2
HEAD_CB = M3_HEAD_H
PAN_NOTCH = 1.0
PAN_XO = PAN_XI + CASE_T

# ---- motor side: carrier (hex arbor, shoulder, D bore), cap with stub, three gears with hubs
GU = dict(B=M0, A=M0 + W_MOTOR_PITCH, C=M0 + 2 * W_MOTOR_PITCH)
HUBLEN = W_MOTOR_PITCH - FACE_W
CAP_U0 = GU["C"] + FACE_W + 0.1
ARB_END = CAP_U0 + 3.0
STUB_D = 10.0
STUB_END = UF + 0.8
CAP_PLATE_FLOOR = UF + FPLATE_T - 1.2
KIT_LENGTHS = (8.0, 12.0, 16.0)
CAP_SCREW_L, CAP_ENGAGE, CARR_PILOT = 16.0, 5.5, 10.0
CAP_SEAT = ARB_END + CAP_SCREW_L - CAP_ENGAGE
CAP_CB = STUB_END - CAP_SEAT
ROD_SCREW_L, ROD_REAR_L, ROD_PILOT, MOUNT_SCREW_L, PAN_SCREW_L, MOTOR_SCREW_L, GRUB_L = 8.0, 8.0, 9.0, 12.0, 8.0, 8.0, 6.0
PILOT_TIP, ROD_POCKET = 0.2, 2.6
FLANGE_U0 = 2.5


def build_motor_carrier():
    c = ycu(HUB_R, FLANGE_U0, M0, 0, MZ).fuse(yhexu(CARR_AF, M0 - 0.01, CAP_U0, 0, MZ)).fuse(ycu(4.0, CAP_U0 - 0.01, ARB_END, 0, MZ))
    c = c.cut(dbore(FLANGE_U0 - 1, FLANGE_U0 + 14.0))
    c = c.cut(radial(PILOT / 2, 0, MZ, 0, 1, (FLANGE_U0 + M0) / 2, 0, HUB_R + 1))
    c = c.cut(ycu(PILOT / 2, ARB_END - CARR_PILOT, ARB_END + 1, 0, MZ))
    return c.removeSplitter()


def build_motor_cap():
    c = ycu(8.5, CAP_U0, CAP_U0 + 4.0, 0, MZ).fuse(ycu(STUB_D / 2, CAP_U0 + 3.99, STUB_END, 0, MZ))
    c = c.cut(ycu(4.35, CAP_U0 - 1, CAP_U0 + 3.0, 0, MZ))
    c = c.cut(ycu(1.8, CAP_U0 + 3.0 + SKIN, STUB_END + 1, 0, MZ)).cut(ycu(HEAD_BORE / 2, CAP_SEAT, STUB_END + 1, 0, MZ))
    return c.removeSplitter()


def motor_gear(k):
    u = GU[k]
    g = gear(NM[k], u, ph_up(NM[k]), MZ)
    if k != "B":
        g = g.fuse(ycu(HUB_R, u - HUBLEN, u + 0.01, 0, MZ))
    lo = u - (HUBLEN if k != "B" else 0.0)
    return g.cut(yhexu(GEAR_AF, lo - 1, u + FACE_W + 1, 0, MZ)).removeSplitter()


# ---- slide side at tau = 0 (stroke moves it forward by tau): C integral at the front, spool with the fork groove at the rear
SU = dict(B=M0, A=M0 + W_SLIDE_PITCH, C=M0 + 2 * W_SLIDE_PITCH)
SHUB = W_SLIDE_PITCH - FACE_W
SLEEVE_U0 = SPOOL_U0 + 0.5
SLEEVE_U1 = SU["C"] + FACE_W
SCREW_U = SPOOL_U0 + FLANGE_T / 2


def build_slide_carrier():
    c = yhexu(SL_AF, SLEEVE_U0, SLEEVE_U1)
    c = c.fuse(ycu(SPC_R, SU["C"] - SHUB, SU["C"] + 0.01))
    c = c.fuse(gear(NS["C"], SU["C"], ph_dn(NS["C"])))
    c = c.cut(yhexu(SLIDE_AF, SLEEVE_U0 - 1, SLEEVE_U1 + 1))
    return c.cut(Part.makeCylinder(1.2, 0.6, V(0, -SCREW_U, -SL_AF / 2 - 0.1), Z)).removeSplitter()


def slide_gear(k):
    u = SU[k]
    g = gear(NS[k], u, ph_dn(NS[k]))
    lo = u
    if k == "A":
        g = g.fuse(ycu(SPA_R, u - SHUB, u + 0.01))
        lo = u - SHUB
    return g.cut(yhexu(SL_GAF, lo - 1, u + FACE_W + 1)).removeSplitter()


def build_spool():
    s = ycu(GROOVE_R, SPOOL_U0 + FLANGE_T - 0.01, SPOOL_U1).fuse(ycu(FLANGE_R, SPOOL_U0, SPOOL_U0 + FLANGE_T))
    s = s.cut(yhexu(SL_GAF, SPOOL_U0 - 1, SPOOL_U1 + 1))
    return s.cut(Part.makeCylinder(PILOT / 2, 12, V(0, -SCREW_U, -4.0), V(0, 0, -1))).removeSplitter()


# ---- shafts, transfer gears, rods
BOSS_T = 3.5
LAY_U0, LAY_U1 = -HEAD_Y1, UF + FPLATE_T - LIP_T - 1.0
TG_U0 = SU["C"] + FACE_W + STROKE + 1.5
GRUB_U = TG_U0 + FACE_W + 3.5
T_HUB_U1 = UF - FB - THRUST
TS_U0 = -(PAN_Y_R + CASE_T + PS_OUT)
TS_U1 = PAN_U_F + CASE_T + PS_OUT


def flat_head(s, cz, u0, u1):
    return s.cut(box(-10, 10, -u1 - 1, -u0 + 1, cz - 10, cz - SHAFT_AF / 2))


def build_layshaft():
    s = yhexu(SHAFT_AF, LAY_U0, LAY_U1, 0, ZL).fuse(ycu(HEAD_D / 2, -HEAD_Y1, -HEAD_Y0, 0, ZL))
    return flat_head(s, ZL, LAY_U0, LAY_U1).removeSplitter()


def build_throughshaft():
    s = yhexu(SHAFT_AF, TS_U0, TS_U1).fuse(ycu(HEAD_D / 2, -HEAD_Y1, -HEAD_Y0))
    s = flat_head(s, 0.0, TS_U0, TS_U1)
    for u in (TS_U0 + PS_PILOT, TS_U1 - PS_PILOT):
        s = s.cut(Part.makeCylinder(PILOT / 2, 20, V(0, -u, -10), Z))
    return s.removeSplitter()


def build_t1():
    g = gear(NT1, TG_U0, ph_up(NT1), ZL).fuse(ycu(7.0, TG_U0 + FACE_W - 0.01, T_HUB_U1, 0, ZL))
    g = g.cut(yhexu(SOCKET, TG_U0 - 1, T_HUB_U1 + 1, 0, ZL))
    d = V(-1, 0, -1)
    d.normalize()
    return g.cut(Part.makeCylinder(PILOT / 2, 12, V(0, -GRUB_U, ZL) + d * 3.5, d)).removeSplitter()


def build_t2():
    g = gear(NT2, TG_U0, ph_dn(NT2), 0.0).fuse(ycu(7.0, TG_U0 + FACE_W - 0.01, T_HUB_U1))
    g = g.cut(yhexu(SOCKET, TG_U0 - 1, T_HUB_U1 + 1))
    return g.cut(Part.makeCylinder(PILOT / 2, 12, V(0, -GRUB_U, -3.5), V(0, 0, -1))).removeSplitter()


ROD_U0, ROD_U1 = -ROD_POCKET, UF + FPLATE_T - 1.5


def build_rod(sx):
    r = box(sx * ROD_X - ROD_S / 2, sx * ROD_X + ROD_S / 2, -ROD_U1, -ROD_U0, ROD_Z - ROD_S / 2, ROD_Z + ROD_S / 2)
    r = r.makeChamfer(0.6, [e for e in r.Edges if abs(e.BoundBox.YLength - (ROD_U1 - ROD_U0)) < 1e-6])
    r = r.cut(ycu(PILOT / 2, ROD_U1 - ROD_PILOT, ROD_U1 + 1, sx * ROD_X, ROD_Z))
    return r.cut(ycu(PILOT / 2, ROD_U0 - 1, ROD_U0 + ROD_PILOT, sx * ROD_X, ROD_Z)).removeSplitter()


# ---- shift fork (ring in the spool groove, strap to a guide block on the rod), servo arm, servo and motor references
STRAP_X0, STRAP_Z0, STRAP_Z1 = RING_RO - 1.0, ZL - 2.3, ZL + 4


def build_fork():
    ring = ycu(RING_RO, RING_U0, RING_U0 + RING_T, 0, ZL).cut(ycu(RING_RI, RING_U0 - 1, RING_U0 + RING_T + 1, 0, ZL))
    strap = box(STRAP_X0, BLK_X0 + 0.5, -(RING_U0 + RING_T), -RING_U0, STRAP_Z0, STRAP_Z1)
    blk = box(BLK_X0, BLK_X1, -(BLK_U0 + BLK_L), -BLK_U0, BLK_Z0, BLK_Z1)
    blk = blk.cut(box(ROD_X - BLK_PK / 2, ROD_X + BLK_PK / 2, -(BLK_U0 + BLK_L) - 1, -BLK_U0 + 1, ROD_Z - BLK_PK / 2, ROD_Z + BLK_PK / 2))
    blk = blk.cut(mouth(ROD_X, ROD_Z, -BLK_U0, -1, BLK_PK, 0.45)).cut(mouth(ROD_X, ROD_Z, -(BLK_U0 + BLK_L), 1, BLK_PK))
    u_b1 = PIN_U + GRV_W / 2 + 2.0
    x0 = ROD_X - TW_HALF
    tw = [V(x0, -BLK_U0, BLK_Z1 - 0.01), V(x0, -BLK_U0, TW_Z1), V(x0, -u_b1, TW_Z1), V(x0, -u_b1 - TW_RAMP, BLK_Z1 - 0.01)]
    blk = blk.fuse(Part.Face(Part.makePolygon(tw + [tw[0]])).extrude(V(2 * TW_HALF, 0, 0)))
    y0s, yf = -(PIN_U - GRV_W / 2), -(PIN_U + GRV_W / 2)
    yw = yf + (TW_SLOT - ROOF_HALF) * math.tan(math.radians(50.0))
    sl = [V(ROD_X - TW_SLOT, y0s, BLK_Z1), V(ROD_X + TW_SLOT, y0s, BLK_Z1), V(ROD_X + TW_SLOT, yw, BLK_Z1), V(ROD_X + ROOF_HALF, yf, BLK_Z1), V(ROD_X - ROOF_HALF, yf, BLK_Z1), V(ROD_X - TW_SLOT, yw, BLK_Z1)]
    blk = blk.cut(Part.Face(Part.makePolygon(sl + [sl[0]])).extrude(V(0, 0, TW_Z1 + 1 - BLK_Z1)))
    return ring.fuse(strap).fuse(blk).removeSplitter()


def arm_phi(tau):
    return math.degrees(math.asin((tau - S_STEP) / R_P))


def build_arm_local():
    """arm at phi = 0, pivot at origin, points toward -x, pin at x = -R_P pointing down"""
    pts = [V(0, -4.5, ARM_Z0), V(-14.5, -4.5, ARM_Z0), V(-R_P, -3.0, ARM_Z0), V(-R_P, 3.0, ARM_Z0), V(-14.5, 4.5, ARM_Z0), V(0, 4.5, ARM_Z0)]
    bar = Part.Face(Part.makePolygon(pts + [pts[0]])).extrude(V(0, 0, AT))
    a = bar.fuse(Part.makeCylinder(6.0, AT, V(0, 0, ARM_Z0), Z)).fuse(Part.makeCylinder(3.0, AT, V(-R_P, 0, ARM_Z0), Z))
    a = a.cut(Part.makeCylinder(3.7, RECESS, V(0, 0, ARM_Z1 - RECESS), Z)).cut(box(-HORN_LEN - 0.3, 0.3, -3.3, 3.3, ARM_Z1 - RECESS, ARM_Z1 + 1))
    a = a.cut(Part.makeCylinder(1.6, ARM_Z1 - RECESS - SKIN - ARM_Z0 + 1, V(0, 0, ARM_Z0 - 1), Z))
    return a.fuse(Part.makeCylinder(PIN_D / 2, PIN_H + 0.01, V(-R_P, 0, PIN_Z0), Z)).removeSplitter()


def place_arm(tau, dz=0.0, dx=0.0, dy=0.0):
    a = build_arm_local()
    a.rotate(V(0, 0, 0), Z, arm_phi(tau))
    a.translate(V(XS + dx, -YP_MID + dy, dz))
    return a


def build_motor():
    s = yc(MOT_GB_D / 2, PLATE_T, PLATE_T + MOT_GB_L, 0, MZ).fuse(yc(MOT_CAN_D / 2, PLATE_T + MOT_GB_L - 0.01, PLATE_T + MOT_BODY, 0, MZ))
    s = s.fuse(yc(MOT_BOSS_D / 2, PLATE_T - MOT_BOSS_L, PLATE_T + 0.01, 0, MZ))
    s = s.fuse(yc(MOT_SH_D / 2, PLATE_T - MOT_SH_L, PLATE_T, 0, MZ).cut(
        box(-5, 5, PLATE_T - MOT_SH_L - 1, PLATE_T - MOT_SH_L + MOT_FLAT_L, MZ + MOT_FLAT_AF - MOT_SH_D / 2, MZ + 5)))
    return s


# ---- plates
PR_UP = 22.0
LOW_X, LOW_Z0, LOW_Z1 = 29.8, -11.0, 40.0
PAD_Y1 = PLATE_T + MOT_BODY + 3.2
SERVO_ZSF = ARM_Z1 + 1.8
SEAT_Z = SERVO_ZSF + SV_H - SV_TAB_Z - SV_TAB_T
SV_UC = YP_MID - 5.6
WALL_X0 = XS + SV_W / 2 + SV_OVER / 2 + 1.5
WALL_X1 = WALL_X0 + 3.2
GLUES_R = [(sx * 21.0, y) for sx in (-1, 1) for y in (12.0, 30.0, 48.0)]
CUT_X0, CUT_X1 = -32.0, 32.0
CUT_Y0, CUT_Y1 = -(UF + FPLATE_T + M3_HEAD_H + 1.0), HEAD_Y1 + 1.0
EAR_X, EAR_YS, EAR_R, EAR_HOLE, BOLT_L = 38.0, (12.0, 56.0), 4.8, 3.6, 12.0
PX, PZ, WING_Z0, WING_Z1, BAR_L = (33.6, 40.2), 36.5, FLOOR_TOP, FLOOR_TOP + 7.0, 8.0
RAIL_X, RAIL_W, RAIL_Z1 = 19.0, 6.8, LOW_Z0 + 8.2
XBAR_T = 3.2
SM_U1 = UF + FPLATE_T + XBAR_T
MOUNT_PILOT = MOUNT_SCREW_L - XBAR_T + PILOT_TIP
PAN_PILOT_Z1 = PAN_ZOUT + HEAD_CB + PAN_SCREW_L + PILOT_TIP
ROD_HEAD_U1 = UF + FPLATE_T + M3_HEAD_H
STRIP2_Z0 = ARM_Z1 + ARM_TOL + 1.0
U_BODY0, U_BODY1 = SV_UC - SV_L / 2 - SV_OVER / 2, SV_UC + SV_L / 2 + SV_OVER / 2
SM_U0, SM_U2 = SV_UC - 18.8, SV_UC + 18.8
TAB_PILOT, TAB_GAP = 1.6, 0.1
TIE_T, TIE_R = 4.0, 2.0
SLAB_X0 = PX[1] + 3.5
TIE_EAR = (EAR_X, EAR_YS[0])
TIE_X0, TIE_Y0, TIE_Y1 = EAR_X - EAR_R, -(SM_U0 + 1.0), EAR_YS[0] + EAR_R
TIE_TOP, TIE_BOLT_L = PAD_Z1 + TIE_T, BOLT_L + TIE_T


def rbox(x0, x1, y0, y1, z0, z1, r, ch=0.0):
    b = box(x0, x1, y0, y1, z0, z1)
    es = [e for e in b.Edges if abs(e.BoundBox.YLength - abs(y1 - y0)) < 1e-6]
    return b.makeFillet(r, es)


def zhole(r, x, y, z0, z1):
    return Part.makeCylinder(r, z1 - z0, V(x, y, z0), Z)


def window(x0, x1, z0, z1, y0, y1, r=3.0):
    return rbox(x0, x1, y0 - 1, y1 + 1, z0, z1, r)


def boss(b, z, y0, sgn, length):
    """round boss on a plate face at y0 growing toward +y, blended with a cone"""
    b = b.fuse(yc(BOSS_R, y0, y0 + length, 0, z))
    return b.fuse(Part.makeCone(BOSS_R + 2.5, BOSS_R, 2.5, V(0, y0 - sgn * 0.01, z), V(0, sgn, 0)))


def mouth_cut(b, z, y_end, sgn):
    return b.cut(Part.makeCone(LINER_BORE / 2 + 0.7, LINER_BORE / 2, 0.7, V(0, y_end + sgn * 0.1, z), V(0, -sgn, 0)))


def ear(sx, y):
    """flat ear, round upper end, underside at 50 degrees or steeper so it prints with the plate face down"""
    r, d0 = EAR_R, (EAR_R + 0.05) * math.sqrt(2)
    y2 = y - d0 - 0.2 * r
    lo = max(y2 - 17.0, 0.0)
    x_lo = max(24.0, EAR_X - 0.8 * (y2 - lo))
    pts = [(24.0, y + r), (EAR_X, y + r), (EAR_X, y), (EAR_X + r, y), (EAR_X + r, y + r - d0), (EAR_X, y2), (x_lo, lo), (24.0, lo)]
    e = Part.Face(Part.makePolygon([V(sx * x, yy, PAD_Z0) for x, yy in pts] + [V(sx * pts[0][0], pts[0][1], PAD_Z0)])).extrude(V(0, 0, PAD_T))
    return e.fuse(zhole(r, sx * EAR_X, y, PAD_Z0, PAD_Z1).common(box(sx * EAR_X - r - 1, sx * EAR_X + r + 1, y, y + r + 1, PAD_Z0, PAD_Z1)))


def build_bracket():
    p = rbox(-LOW_X, LOW_X, 0, PLATE_T, LOW_Z0, LOW_Z1, 5.0)
    p = p.fuse(yc(PR_UP, 0, PLATE_T, 0, MZ)).fuse(box(-16, 16, 0, PLATE_T, 30, MZ))
    pad = box(-26, 26, PLATE_T, PAD_Y1, PAD_Z0, PAD_Z1)
    pad = pad.makeFillet(4.0, [e for e in pad.Edges if abs(e.BoundBox.ZLength - PAD_T) < 1e-6 and e.BoundBox.YMin > PAD_Y1 - 1.0])
    wing = box(-34, 34, PLATE_T - 0.01, 18.0, PAD_Z0, PAD_Z1)
    wing = wing.makeFillet(4.0, [e for e in wing.Edges if abs(e.BoundBox.ZLength - PAD_T) < 1e-6 and e.BoundBox.YMin > 17.0])
    b = p.fuse(pad).fuse(wing)
    clr = yc(MOT_GB_D / 2 + 0.3, PLATE_T - 1, PAD_Y1 - 3.2 + 1, 0, MZ)
    for sx in (-1, 1):
        b = b.fuse(box(sx * 9.0, sx * 13.0, PLATE_T - 0.01, PLATE_T + MOT_BODY, PAD_Z1 - 0.01, MZ).cut(clr))
        pts = [V(sx * 20, 0, PAD_Z1 - 0.01), V(sx * 20, 0, PAD_Z1 + 11), V(sx * 20, PLATE_T + 25, PAD_Z1 - 0.01)]
        b = b.fuse(prism(pts, V(sx * 6.0, 0, 0)))
        for y in EAR_YS:
            b = b.fuse(ear(sx, y))
        b = b.fuse(rbox(sx * RAIL_X - RAIL_W / 2, sx * RAIL_X + RAIL_W / 2, PLATE_T - 0.01, PLATE_T + RAIL_W, LOW_Z0, RAIL_Z1, 1.0))
    for z in (0.0, ZL):
        b = boss(b, z, PLATE_T - 0.01, 1, RB + 0.01)
    b = b.cut(yc(MOT_BOSS_HOLE / 2, -1, PLATE_T + 1, 0, MZ))
    for z in (0.0, ZL):
        b = b.cut(yc(LINER_BORE / 2, LIP_T, PLATE_T + RB + 1, 0, z)).cut(yc(LIP_BORE / 2, -1, LIP_T + 0.01, 0, z))
        b = mouth_cut(b, z, PLATE_T + RB, 1)
    for k in range(6):
        a = math.radians(60 * k)
        x, z = MOT_PCD / 2 * math.cos(a), MZ + MOT_PCD / 2 * math.sin(a)
        b = b.cut(yc(MOT_HOLE_D / 2, MOT_CB_DEEP + SKIN, PLATE_T + 1, x, z)).cut(yc(MOT_CB_D / 2, -1, MOT_CB_DEEP, x, z))
    for sx in (-1, 1):
        b = b.cut(box(sx * ROD_X - ROD_PK / 2, sx * ROD_X + ROD_PK / 2, -1, ROD_POCKET, ROD_Z - ROD_PK / 2, ROD_Z + ROD_PK / 2)).cut(mouth(sx * ROD_X, ROD_Z, 0.0, 1, ROD_PK))
        b = b.cut(yc(1.8, ROD_POCKET + SKIN, PLATE_T + 1, sx * ROD_X, ROD_Z))
        b = b.cut(window(min(sx * 12.0, sx * 22.0), max(sx * 12.0, sx * 22.0), 3.0, 17.0, 0, PLATE_T))
        b = b.cut(zhole(PILOT / 2, sx * RAIL_X, PLATE_T + RAIL_W / 2, LOW_Z0 - 1, PAN_PILOT_Z1))
        for y in EAR_YS:
            b = b.cut(zhole(EAR_HOLE / 2, sx * EAR_X, y, PAD_Z0 - 1, PAD_Z1 + 1))
    for x, y in GLUES_R:
        b = b.cut(zhole(2.5, x, y, PAD_Z0 - 1, PAD_Z1 + 1))
    return b.removeSplitter()


def build_front_plate():
    y0, y1 = -(UF + FPLATE_T), -UF
    p = rbox(-LOW_X, LOW_X, y0, y1, LOW_Z0, LOW_Z1, 5.0).fuse(yc(11.0, y0, y1, 0, MZ)).fuse(box(-9, 9, y0, y1, 30, MZ))
    p = p.fuse(yc(9.0, y1 - 0.01, y1 + BOSS_T, 0, MZ))
    for z in (0.0, ZL):
        p = boss(p, z, y1 - 0.01, 1, FB + 0.01)
    p = p.fuse(rbox(-34.4, -27.5, y0, -(UF - 26), PAD_Z0, PAD_Z1, 1.0))
    p = p.fuse(rbox(23.0, PX[1] + 3.4, y0, y1, WING_Z0, WING_Z1, 2.0))
    p = p.fuse(rbox(PX[0] - 3.4, PX[1] + 3.4, y1 - 0.01, y1 + BAR_L, WING_Z0, WING_Z1, 2.0))
    for px in PX:
        p = p.cut(yc(PILOT / 2, y0 - 1, y0 + MOUNT_PILOT, px, PZ))
    for z in (0.0, ZL):
        p = p.cut(yc(LINER_BORE / 2, y0 + LIP_T, y1 + FB + 1, 0, z))
        p = mouth_cut(p, z, y1 + FB, 1)
    p = p.cut(yc(LIP_BORE / 2, y0 - 1, y0 + LIP_T + 0.01, 0, 0))
    p = p.cut(yc(10.6 / 2, -(UF + FPLATE_T - 1.2), y1 + BOSS_T + 1, 0, MZ))
    for sx in (-1, 1):
        p = p.cut(box(sx * ROD_X - ROD_PK / 2, sx * ROD_X + ROD_PK / 2, -(UF + FPLATE_T - 1.5), y1 + BOSS_T + 1, ROD_Z - ROD_PK / 2, ROD_Z + ROD_PK / 2))
        p = p.cut(mouth(sx * ROD_X, ROD_Z, y1, -1, ROD_PK))
        p = p.cut(yc(1.8, y0 - 1, y1, sx * ROD_X, ROD_Z))
        p = p.fuse(rbox(sx * RAIL_X - RAIL_W / 2, sx * RAIL_X + RAIL_W / 2, y1 - 0.01, y1 + RAIL_W, LOW_Z0, RAIL_Z1, 1.0))
        p = p.cut(zhole(PILOT / 2, sx * RAIL_X, y1 + RAIL_W / 2, LOW_Z0 - 1, PAN_PILOT_Z1))
    p = p.cut(window(-26, -12, 1.0, 20.0, y0, y1)).cut(window(12, 26, 1.0, 20.0, y0, y1))
    return p.removeSplitter()


def xprism(pts, x0, x1):
    v = [V(x0, -u, z) for u, z in pts]
    return Part.Face(Part.makePolygon(v + [v[0]])).extrude(V(x1 - x0, 0, 0))


def build_servo_mount():
    u2e = SM_U2
    wall = xprism([(SM_U0, FLOOR_TOP), (SM_U1, FLOOR_TOP), (SM_U1, FLOOR_TOP + 8.0), (u2e + SEAT_Z - FLOOR_TOP - 8.0, FLOOR_TOP + 8.0), (u2e, SEAT_Z), (SM_U0, SEAT_Z)], WALL_X0, WALL_X1)
    wall = wall.makeFillet(2.0, [e for e in wall.Edges if abs(e.BoundBox.XLength - (WALL_X1 - WALL_X0)) < 1e-6])
    slab = box(SLAB_X0, WALL_X1, -SM_U1, -SM_U0, FLOOR_TOP, FLOOR_TOP + 4.0)
    slab = slab.makeFillet(3.0, [e for e in slab.Edges if abs(e.BoundBox.ZLength - 4.0) < 1e-6 and e.BoundBox.XMin < SLAB_X0 + 0.5])
    cross = box(PX[0] - 4.4, WALL_X1, -SM_U1, -(UF + FPLATE_T), FLOOR_TOP, FLOOR_TOP + 8.0)
    cross = cross.makeFillet(2.0, [e for e in cross.Edges if abs(e.BoundBox.YLength - 3.2) < 1e-6 and e.BoundBox.XMin < PX[0]])
    s1 = xprism([(SM_U0, FLOOR_TOP), (U_BODY0 - TAB_GAP, FLOOR_TOP), (U_BODY0 - TAB_GAP, SEAT_Z), (SM_U0, SEAT_Z)], XS - 4.0, WALL_X0 + 0.01)
    s2 = xprism([(U_BODY1 + TAB_GAP, STRIP2_Z0), (u2e, STRIP2_Z0), (u2e, SEAT_Z), (U_BODY1 + TAB_GAP, SEAT_Z)], XS - 4.0, WALL_X0 + 0.01)
    s1 = s1.makeFillet(2.0, [e for e in s1.Edges if e.BoundBox.XLength > 1 and abs(e.BoundBox.YMax + SM_U0) < 1e-6])
    s2 = s2.makeFillet(2.0, [e for e in s2.Edges if e.BoundBox.XLength > 1 and abs(e.BoundBox.YMax + u2e) < 1e-6 and abs(e.BoundBox.ZMax - SEAT_Z) < 1e-6])
    tie = box(TIE_X0, WALL_X1, TIE_Y0, TIE_Y1, PAD_Z1, TIE_TOP)
    tie = tie.makeFillet(TIE_R, [e for e in tie.Edges if abs(e.BoundBox.ZLength - TIE_T) < 1e-6 and e.BoundBox.XMax < TIE_X0 + 1e-6])
    m = wall.fuse(slab).fuse(cross).fuse(s1).fuse(s2).fuse(tie).removeSplitter()
    m = m.makeChamfer(0.8, [e for e in m.Edges if e.BoundBox.XMin > WALL_X1 - 1e-6])
    for sg, zlo in ((-1, SEAT_Z - 8.0), (1, STRIP2_Z0 - 1.0)):
        u0 = SV_UC + sg * SV_HOLE_SP / 2
        for du in (0.0, sg * SV_OVER):
            m = m.cut(Part.makeCylinder(TAB_PILOT / 2, SEAT_Z + 1 - zlo, V(XS, -(u0 + du), zlo), Z))
        m = m.cut(box(XS - TAB_PILOT / 2, XS + TAB_PILOT / 2, -(u0 + max(0, sg * SV_OVER)), -(u0 + min(0, sg * SV_OVER)), zlo, SEAT_Z + 1))
    for px in PX:
        m = m.cut(yc(1.8, -SM_U1 - 1, -(UF + FPLATE_T) + 1, px, PZ))
    m = m.cut(zhole(EAR_HOLE / 2, TIE_EAR[0], TIE_EAR[1], PAD_Z1 - 1, TIE_TOP + 1))
    return m.removeSplitter()


def build_sleeve(z, y0, y1):
    return yc(LINER_OD / 2, y0, y1, 0, z).cut(yc(LINER_ID / 2, y0 - 1, y1 + 1, 0, z))


def build_pan():
    y_hi, y_lo = PAN_Y_R + CASE_T, -(PAN_U_F + CASE_T)
    o = box(-PAN_XO, PAN_XO, y_lo, y_hi, PAN_ZOUT, PAN_RIM)
    o = o.makeFillet(4.0, [e for e in o.Edges if abs(e.BoundBox.ZLength - (PAN_RIM - PAN_ZOUT)) < 1e-6])
    o = o.makeChamfer(2.0, 1.68, [e for e in o.Edges if e.BoundBox.ZMax < PAN_ZOUT + 1e-6])
    o = o.makeChamfer(0.8, [e for e in o.Edges if e.BoundBox.ZMin > PAN_RIM - 1e-6])
    c = box(-PAN_XI, PAN_XI, -PAN_U_F, PAN_Y_R, PAN_ZIN, PAN_RIM + 1)
    c = c.makeFillet(1.0, [e for e in c.Edges if abs(e.BoundBox.ZLength - (PAN_RIM + 1 - PAN_ZIN)) < 1e-6])
    c = c.makeFillet(1.0, [e for e in c.Edges if e.BoundBox.ZMax < PAN_ZIN + 1e-6])
    pan = o.cut(c)
    for ya, yb in ((PAN_Y_R - 1, y_hi + 1), (y_lo - 1, -PAN_U_F + 1)):
        slot = box(-LIP_BORE / 2 - 0.4, LIP_BORE / 2 + 0.4, ya, yb, 0, PAN_RIM + 2).fuse(yc(LIP_BORE / 2 + 0.4, ya, yb, 0, 0))
        pan = pan.cut(slot)
    pan = pan.makeFillet(0.8, [e for e in pan.Edges if (e.BoundBox.YMax > y_hi - 1e-6 or e.BoundBox.YMin < y_lo + 1e-6) and e.BoundBox.YLength < 0.01 and e.BoundBox.ZLength > 0.5])
    for sx in (-1, 1):
        hr = M3_HEAD_D / 2 + PAN_NOTCH
        pan = pan.cut(box(sx * ROD_X - hr, sx * ROD_X + hr, -ROD_HEAD_U1 - 1.0, -(UF + FPLATE_T) + 0.2, ROD_Z - hr, PAN_RIM + 1))
        for y in (PLATE_T + RAIL_W / 2, -(UF - RAIL_W / 2)):
            x = sx * RAIL_X
            pan = pan.fuse(zhole(4.4, x, y, PAN_ZIN - 0.01, LOW_Z0)).fuse(Part.makeCone(6.6, 4.4, 2.2, V(x, y, PAN_ZIN - 0.01), Z))
            pan = pan.cut(zhole(1.8, x, y, PAN_ZOUT + HEAD_CB + SKIN, LOW_Z0 + 1)).cut(zhole(HEAD_BORE / 2, x, y, PAN_ZOUT - 1, PAN_ZOUT + HEAD_CB))
    return pan.removeSplitter()


def rod_head(sx, front):
    return Part.makeCylinder(M3_HEAD_D / 2, M3_HEAD_H, V(sx * ROD_X, -(UF + FPLATE_T) if front else PLATE_T, ROD_Z), V(0, -1, 0) if front else Y)


def build_rod_heads():
    return Part.makeCompound([rod_head(sx, f) for sx in (-1, 1) for f in (True, False)])


def ear_pos():
    return [(sx * EAR_X, y) for sx in (-1, 1) for y in EAR_YS]


def ear_top(x, y):
    return TIE_TOP if (x, y) == TIE_EAR else PAD_Z1


def build_bolts(sel="all"):
    s = None
    for x, y in ear_pos():
        tied = (x, y) == TIE_EAR
        if sel != "all" and tied != (sel == "tie"):
            continue
        t = ear_top(x, y)
        b = zhole(1.5, x, y, t - (TIE_BOLT_L if tied else BOLT_L), t).fuse(zhole(2.75, x, y, t, t + 2.0))
        s = b if s is None else s.fuse(b)
    return s


# ---- references, poses
def build_servo(tau, dzb=0.0, dza=0.0, grow=0.0, dx=0.0, dy=0.0):
    """dzb: body height error, dza: horn height error, grow: every body dimension bigger by this much"""
    zb = SEAT_Z - (SV_H - SV_TAB_Z - SV_TAB_T) + dzb
    L, W, H, SP = SV_L + grow, SV_W + grow, SV_H + grow, SV_TAB_SPAN + grow
    b = box(XS - W / 2, XS + W / 2, -(SV_UC + L / 2), -(SV_UC - L / 2), zb, zb + H)
    tab = box(XS - W / 2, XS + W / 2, -(SV_UC + SP / 2), -(SV_UC - SP / 2), SEAT_Z, SEAT_Z + SV_TAB_T)
    sp = Part.makeCylinder(SV_SPLINE_D / 2, 2.7, V(XS, -YP_MID, zb - 2.7), Z)
    horn = Part.makeCylinder(3.5, 1.9, V(XS, -YP_MID, ARM_Z1 - 1.8 + dza), Z).fuse(box(XS - HORN_LEN, XS, -YP_MID - 3, -YP_MID + 3, ARM_Z1 - 1.8 + dza, ARM_Z1 + 0.1 + dza))
    horn.rotate(V(XS, -YP_MID, 0), Z, arm_phi(tau))
    return move(b.fuse(tab).fuse(sp).fuse(horn), dx, dy)


def floor_slab():
    f = box(-120, 120, -150, 150, AXIS_DEPTH, FLOOR_TOP).cut(box(CUT_X0, CUT_X1, CUT_Y0, CUT_Y1, AXIS_DEPTH - 1, FLOOR_TOP + 1))
    for x, y in ear_pos():
        f = f.cut(zhole(EAR_HOLE / 2, x, y, AXIS_DEPTH - 1, FLOOR_TOP + 1))
    return f


PRINT_UP = dict(Bracket="+Y", FrontPlate="+Y", MotorCarrier="-Y", MotorCap="-Y", MotorGear_B="+Y", MotorGear_A="+Y", MotorGear_C="+Y",
                SlideCarrier="+Y", SlideGear_A="+Y", SlideGear_B="+Y", SlideCap="-Y", Layshaft="+Z", ThroughShaft="+Z", T1="-Y", T2="-Y",
                ShiftFork="-Y", Rod_1="+Z", Rod_2="+Z", ServoArm="-Z", CasePan="+Z", ServoMount="-X",
                Sleeve_1="+Y", Sleeve_2="+Y", Sleeve_3="+Y", Sleeve_4="+Y")
SLIDING = ("SlideCarrier", "SlideGear_A", "SlideGear_B", "SlideCap", "ShiftFork")
UPV = {"+X": X, "-X": V(-1, 0, 0), "+Y": Y, "-Y": V(0, -1, 0), "+Z": Z, "-Z": V(0, 0, -1)}
TAUS = (0.0, S_STEP / 2, S_STEP, 1.5 * S_STEP, STROKE)
NEUTRAL = (S_STEP / 2, 1.5 * S_STEP)
POS = (0.0, S_STEP, STROKE)
POS_TAU = dict(B=0.0, A=S_STEP, C=STROKE)
GEAR_AT = {0.0: "B", S_STEP: "A", STROKE: "C"}


def build_parts():
    return dict(Bracket=build_bracket(), FrontPlate=build_front_plate(), MotorCarrier=build_motor_carrier(), MotorCap=build_motor_cap(),
                MotorGear_B=motor_gear("B"), MotorGear_A=motor_gear("A"), MotorGear_C=motor_gear("C"),
                SlideCarrier=move(build_slide_carrier(), dz=ZL), SlideGear_A=move(slide_gear("A"), dz=ZL), SlideGear_B=move(slide_gear("B"), dz=ZL), SlideCap=move(build_spool(), dz=ZL),
                Layshaft=build_layshaft(), ThroughShaft=build_throughshaft(), T1=build_t1(), T2=build_t2(),
                ShiftFork=build_fork(), Rod_1=build_rod(1), Rod_2=build_rod(-1), ServoArm=place_arm(S_STEP), CasePan=build_pan(), ServoMount=build_servo_mount(),
                Sleeve_1=build_sleeve(0.0, LIP_T, POCK_Y1), Sleeve_2=build_sleeve(0.0, -(UF + FPLATE_T - LIP_T), -(UF - FB)),
                Sleeve_3=build_sleeve(ZL, LIP_T, POCK_Y1), Sleeve_4=build_sleeve(ZL, -(UF + FPLATE_T - LIP_T), -(UF - FB)))


def posed(P, tau, refs):
    d = dict(P)
    for n in SLIDING:
        d[n] = move(P[n], dy=-tau)
    d["ServoArm"] = place_arm(tau)
    d["Ref_Servo"] = build_servo(tau)
    d.update(refs)
    return d


def bbo(a, b, pad=0.0):
    p, q = a.BoundBox, b.BoundBox
    return not (p.XMax < q.XMin - pad or q.XMax < p.XMin - pad or p.YMax < q.YMin - pad or q.YMax < p.YMin - pad or p.ZMax < q.ZMin - pad or q.ZMax < p.ZMin - pad)


def engaged(tau):
    out = {}
    for m in "ABC":
        for s in "ABC":
            a0, b0 = GU[m], SU[s] + tau
            ov = min(a0 + FACE_W, b0 + FACE_W) - max(a0, b0)
            if ov > 1e-9 and tip(NM[m]) + tip(NS[s]) > CD1 - 1e-9:
                out[(m, s)] = round(ov, 3)
    return out


def step_mesh():
    rep = {}
    for k, tau in (("B", 0.0), ("A", S_STEP), ("C", STROKE)):
        g1 = gear(NM[k], GU[k], ph_up(NM[k]), MZ)
        g2 = gear(NS[k], SU[k] + tau, ph_dn(NS[k]), ZL)
        rows = []
        for i in range(8):
            a = i * 360.0 / NM[k] / 8
            m, s = g1.copy(), g2.copy()
            m.rotate(V(0, 0, MZ), Y, a)
            s.rotate(V(0, 0, ZL), Y, -a * NM[k] / NS[k])
            rows.append((round(vol(m, s), 5), round(dist(m, s), 4)))
        rep[k] = rows
    g1, g2 = gear(NT1, TG_U0, ph_up(NT1), ZL), gear(NT2, TG_U0, ph_dn(NT2), 0.0)
    rows = []
    for i in range(8):
        a = i * 360.0 / NT1 / 8
        m, s = g1.copy(), g2.copy()
        m.rotate(V(0, 0, ZL), Y, a)
        s.rotate(V(0, 0, 0), Y, -a * NT1 / NT2)
        rows.append((round(vol(m, s), 5), round(dist(m, s), 4)))
    rep["T"] = rows
    return rep


def sweep(mover, stills, offs):
    """largest common volume while the mover translates through every offset (1 mm steps); stills far from the whole path are skipped"""
    b0 = mover.BoundBox
    o = offs[-1]
    path = App.BoundBox(b0.XMin, b0.YMin, b0.ZMin, b0.XMax, b0.YMax, b0.ZMax)
    path.add(App.BoundBox(b0.XMin + o[0], b0.YMin + o[1], b0.ZMin + o[2], b0.XMax + o[0], b0.YMax + o[1], b0.ZMax + o[2]))
    near = [s for s in stills if path.intersect(s.BoundBox)]
    worst = 0.0
    for o in offs:
        m = move(mover, *o)
        for s in near:
            if bbo(m, s):
                worst = max(worst, vol(m, s))
    return round(worst, 4)


def cyl_dir(r, p, d, length, back=0.0):
    d = V(*d)
    d.normalize()
    return Part.makeCylinder(r, length, p - d * back, d)


MODULE = ("Bracket", "FrontPlate", "MotorCarrier", "MotorCap", "MotorGear_B", "MotorGear_A", "MotorGear_C", "SlideCarrier", "SlideGear_A", "SlideGear_B", "SlideCap",
          "Layshaft", "T1", "ShiftFork", "Rod_1", "Rod_2", "Sleeve_1", "Sleeve_2", "Sleeve_3", "Sleeve_4")


def step_assembly(P, refs):
    """order in the header; every insertion is a translation sweep, forward = -y, rear = +y, up = +z"""
    mot, flo, blt = refs["Ref_Motor"], refs["Ref_Floor"], refs["Ref_Bolts"]
    blt_ear, blt_tie = build_bolts("ear"), build_bolts("tie")
    d = posed(P, 0.0, refs)
    br, fp, S = d["Bracket"], d["FrontPlate"], [d["Sleeve_%d" % k] for k in (1, 2, 3, 4)]
    fwd = lambda mm: [(0, -float(i), 0) for i in range(int(mm) + 1)]
    rear = lambda mm: [(0, float(i), 0) for i in range(int(mm) + 1)]
    up = lambda mm: [(0, 0, float(i)) for i in range(int(mm) + 1)]
    dn = lambda mm: [(0, 0, -float(i)) for i in range(int(mm) + 1)]
    dr = lambda p, dd, back=0.0: cyl_dir(3.0, p, dd, 60, -back)
    z0 = lambda *ss: round(sum(vol(c, s) for c, s in ss), 4)
    r = {}
    for k, still in ((0, br), (2, br), (1, fp), (3, fp)):
        r["sleeve_%d_in" % (k + 1)] = sweep(S[k], [still], rear(24))
    r["motor_in"] = sweep(mot, [br, S[0], S[2]], rear(68))
    base = [br, mot, S[0], S[2]]
    for n, st, nn in (("MotorCarrier", 4.0, 18), ("MotorGear_B", 4.0, 20)):
        r["on_" + n] = sweep(d[n], base, fwd(nn * st))
        base.append(d[n])
    r["layshaft_in"] = sweep(d["Layshaft"], base, rear(102))
    base.append(d["Layshaft"])
    car, ga, gb, fk, cap = (d[n] for n in ("SlideCarrier", "SlideGear_A", "SlideGear_B", "ShiftFork", "SlideCap"))
    r["slide_gear_A"] = sweep(ga, [car], rear(60))
    r["slide_gear_B"] = sweep(gb, [car, ga], rear(60))
    r["slide_fork_ring"] = sweep(fk, [car, ga, gb], rear(60))
    r["slide_spool"] = sweep(cap, [car, ga, gb, fk], rear(60))
    unit = [car, ga, gb, fk, cap]
    u = car
    for x in unit[1:]:
        u = u.fuse(x)
    r["slide_unit_in"] = sweep(u, base, fwd(68))
    base += unit
    for n, st, nn in (("MotorGear_A", 4.0, 20), ("MotorGear_C", 4.0, 20), ("MotorCap", 4.0, 8), ("T1", 4.0, 10)):
        r["on_" + n] = sweep(d[n], base, fwd(nn * st))
        base.append(d[n])
    cap_head = cyl_dir(M3_HEAD_D / 2, V(0, -CAP_SEAT, MZ), (0, -1, 0), M3_HEAD_H)
    c = dr(V(0, -(CAP_SEAT + M3_HEAD_H), MZ), (0, -1, 0))
    r["cap_screw"] = z0(*[(c, s) for s in base if s is not d["T1"]] + [(cap_head, s) for s in base if s is not d["T1"]])
    r["rods_in"] = max(sweep(d[n], base, fwd(84)) for n in ("Rod_1", "Rod_2"))
    base += [d["Rod_1"], d["Rod_2"]]
    front = fp.fuse(S[1]).fuse(S[3])
    r["front_unit_on"] = sweep(front, base, fwd(84))
    bench = base + [front]
    c = dr(V(0, -SCREW_U, ZL - FLANGE_R - 0.2), (0, 0, -1))
    r["grub_spool"] = z0(*[(c, s) for s in bench if s is not cap])
    c = dr(V(0, -GRUB_U, ZL) + V(-1, 0, -1) * (7.2 / math.sqrt(2)), (-1, 0, -1))
    r["grub_t1"] = z0(*[(c, s) for s in bench])
    c = dr(V(0, -(FLANGE_U0 + M0) / 2, MZ + HUB_R + 0.2), (0, 0, 1))
    r["grub_motor"] = z0((c, mot), (c, br))
    r["motor_screws"] = z0(*[(dr(V(MOT_PCD / 2 * math.cos(math.radians(60 * k)), 0, MZ + MOT_PCD / 2 * math.sin(math.radians(60 * k))), (0, -1, 0)), d["MotorCarrier"]) for k in range(6)])
    r["front_screws"] = z0(*[(dr(V(sx * ROD_X, -(UF + FPLATE_T), ROD_Z), (0, -1, 0)), s) for sx in (-1, 1) for s in bench if s is not front])
    hf = [rod_head(sx, True) for sx in (-1, 1)]
    r["rear_screws"] = z0(*[(dr(V(sx * ROD_X, PLATE_T + M3_HEAD_H, ROD_Z), (0, 1, 0)), s) for sx in (-1, 1) for s in bench + hf])
    modl = [d[n] for n in MODULE] + [mot, d["Ref_Heads"]]
    r["lowering"] = max(sweep(s, [flo], up(78)) for s in modl)
    ts = d["ThroughShaft"]
    t2 = d["T2"]
    r["t2_up_into_mesh"] = sweep(t2, modl + [flo], dn(8))
    modl.append(t2)
    r["through_shaft_in"] = sweep(ts, modl + [flo], rear(108))
    allp = modl + [ts, flo]
    c = dr(V(0, -GRUB_U, -7.0 - 0.2), (0, 0, -1))
    r["grub_t2"] = z0(*[(c, s) for s in allp])
    pan = d["CasePan"]
    r["pan_on"] = sweep(pan, allp, dn(72))
    allp.append(pan)
    pans = [(sx * RAIL_X, y) for sx in (-1, 1) for y in (PLATE_T + RAIL_W / 2, -(UF - RAIL_W / 2))]
    r["pan_screws"] = z0(*[(dr(V(x, y, PAN_ZOUT), (0, 0, -1)), s) for x, y in pans for s in allp if s is not pan] + [(dr(V(x, y, PAN_ZOUT), (0, 0, -1)), pan) for x, y in pans])
    sm = d["ServoMount"]
    r["mount_on"] = sweep(sm, allp + [blt_ear], up(78))
    allp.append(sm)
    heads = [Part.makeCylinder(M3_HEAD_D / 2, M3_HEAD_H, V(px, -SM_U1, PZ), V(0, -1, 0)) for px in PX]
    r["mount_screws"] = z0(*[(dr(V(px, -SM_U1, PZ), (0, -1, 0)), s) for px in PX for s in allp + [h for h, qx in zip(heads, PX) if qx != px]] + [(h, s) for h in heads for s in allp])
    r["tie_bolt_in"] = sweep(blt_tie, allp + [blt_ear], up(24))
    r["tie_bolt_driver"] = z0(*[(dr(V(TIE_EAR[0], TIE_EAR[1], TIE_TOP + 2.0), (0, 0, 1)), s) for s in allp + [blt_ear, blt_tie]])
    d12 = posed(P, S_STEP, refs)
    slid = {id(x) for x in unit}
    st12 = [s for s in allp if id(s) not in slid] + [d12[n] for n in SLIDING]
    r["servo_in"] = sweep(d12["Ref_Servo"].fuse(d12["ServoArm"]), st12, up(42))
    r["tab_screws"] = z0(*[(dr(V(XS, -(SV_UC + du), SEAT_Z + SV_TAB_T + 2.4), (0, -1.0 if du > 0 else 1.0, 1)), s) for du in (-SV_HOLE_SP / 2, SV_HOLE_SP / 2) for s in st12 + [d12["Ref_Servo"], d12["ServoArm"]]])
    r["bolt_in"] = sweep(blt_ear, [br, flo], up(24))
    r["bolt_drivers"] = z0(*[(dr(V(x, y, ear_top(x, y) + 2.0), (0, 0, 1)), s) for x, y in ear_pos() for s in st12 + [d12["Ref_Servo"], d12["ServoArm"], blt]])
    return r


# ---- verification
# print rules P1 to P6, measured on every printed part in its print orientation
P1_COS, FLAT_COS = math.cos(math.radians(45.0)) + 1e-4, 0.9999
SAG_MAX, BRIDGE_MAX, LAYER, HOLE_R_MAX = 0.3, 10.0, 0.2, 3.0
BED_MIN, TALL_MAX, FIRST_WALL, LOST_MAX = 60.0, 4.0, 0.8, 1.0
BED_EXEMPT = {"Sleeve_%d" % k: "P6 bed contact: placeholder for a 12 x 10 PTFE tube cut to 8 mm, 12 dia x 8 squat, no overhang, nothing to adhere to a smaller bed" for k in (1, 2, 3, 4)}


def span(f, a):
    b = f.BoundBox
    return abs(a.x) * b.XLength + abs(a.y) * b.YLength + abs(a.z) * b.ZLength


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
        if la > BRIDGE_MAX or la < 1e-9 or lb < 1e-9:
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


def wall_from(s, p, d, lim=12.0):
    """thickness of the first wall met walking from p (in a void or on its surface) along d"""
    d = V(*d)
    d.normalize()
    t = 0.0
    while t < lim and not s.isInside(p + d * t, 1e-7, True):
        t += 0.02
    t0 = t
    while t < lim and s.isInside(p + d * t, 1e-7, True):
        t += 0.02
    return round(t - t0, 2)


def ring_fill(s, p, d, r_in, r_out, a, b):
    d = V(*d)
    d.normalize()
    ring = Part.makeCylinder(r_out, b - a, p + d * a, d).cut(Part.makeCylinder(r_in, b - a, p + d * a, d))
    return round(vol(s, ring) / ring.Volume, 4)


def solid_run(s, p, d, lim=40.0, step=0.1):
    d = V(*d)
    d.normalize()
    tot = 0.0
    for sg in (1, -1):
        t = 0.0
        while t < lim and s.isInside(p + d * (sg * (t + step / 2)), 1e-7, True):
            t += step
        tot += t
    return round(tot, 1)


def void_run(s, p, d, lim=20.0, step=0.1):
    """length of the void met walking from p along d (a pilot or a hole) before material"""
    d = V(*d)
    d.normalize()
    t = 0.0
    while t < lim and not s.isInside(p + d * (t + step / 2), 1e-7, True):
        t += step
    return round(t, 1)


def hole_open(s, x, z, ya, yb, r):
    """true when a pass hole of radius r runs from ya to yb: void at r - 0.1 all round, material at r + 0.1"""
    for k in range(7):
        y = ya + (yb - ya) * k / 6.0
        for a in range(8):
            c, sn = math.cos(math.pi * a / 4), math.sin(math.pi * a / 4)
            if s.isInside(V(x + (r - 0.1) * c, y, z + (r - 0.1) * sn), 1e-7, True) or not s.isInside(V(x + (r + 0.1) * c, y, z + (r + 0.1) * sn), 1e-7, True):
                return False
    return True


# minimum gaps (mm) from the kit rules, measured with distToShape; anything not listed must be >= 0.8
RULE_FACE_MIN, RULE_FACE_MAX = 0.2, 0.25
RULE_SLIDE, RULE_SPIN, RULE_BORE, RULE_FLOAT_MIN, RULE_FLOAT_MAX, RULE_FORK_PLAY = 0.5, 0.8, 0.3, 0.3, 0.5, 0.4
F2 = RULE_FACE_MIN
FITS = {("Layshaft", "Bracket"): F2, ("T1", "FrontPlate"): F2, ("ThroughShaft", "Bracket"): F2, ("ThroughShaft", "FrontPlate"): RULE_BORE, ("T2", "FrontPlate"): F2,
        ("MotorCap", "FrontPlate"): RULE_BORE,
        ("Sleeve_1", "Bracket"): 0.0, ("Sleeve_3", "Bracket"): 0.0, ("Sleeve_2", "FrontPlate"): 0.0, ("Sleeve_4", "FrontPlate"): 0.0,
        ("ThroughShaft", "Sleeve_1"): F2, ("ThroughShaft", "Sleeve_2"): RULE_BORE, ("T2", "Sleeve_2"): F2, ("Layshaft", "Sleeve_3"): F2, ("Layshaft", "Sleeve_4"): RULE_BORE, ("T1", "Sleeve_4"): F2,
        ("ShiftFork", "SlideCap"): RULE_FORK_PLAY, ("ShiftFork", "SlideGear_B"): RULE_FORK_PLAY,
        ("ShiftFork", "Rod_1"): RULE_SPIN, ("ServoArm", "Rod_1"): RULE_SLIDE, ("ShiftFork", "ServoArm"): RULE_SLIDE, ("FrontPlate", "ShiftFork"): RULE_SPIN,
        ("Bracket", "ShiftFork"): RULE_SLIDE, ("ShiftFork", "Ref_Floor"): RULE_SLIDE, ("ServoArm", "Ref_Floor"): RULE_SLIDE,
        ("Bracket", "Rod_1"): 0.0, ("Bracket", "Rod_2"): 0.0, ("SlideCap", "Bracket"): 1.0,
        ("ServoArm", "Ref_Servo"): 0.0, ("Ref_Servo", "FrontPlate"): 0.0, ("Ref_Servo", "ServoMount"): 0.0, ("ServoMount", "FrontPlate"): 0.0, ("ServoMount", "Ref_Floor"): 0.0, ("FrontPlate", "Ref_Heads"): 0.0, ("Bracket", "Ref_Heads"): 0.0,
        ("FrontPlate", "Rod_1"): 0.0, ("FrontPlate", "Rod_2"): 0.0, ("CasePan", "Bracket"): 0.0, ("CasePan", "FrontPlate"): 0.0, ("CasePan", "ShiftFork"): RULE_SPIN,
        ("Bracket", "Ref_Floor"): 0.0, ("FrontPlate", "Ref_Floor"): 0.0, ("Bracket", "Ref_MotorBody"): 0.0, ("Bracket", "Ref_Bolts"): 0.0, ("ServoMount", "Ref_Bolts"): 0.0, ("ServoMount", "Bracket"): 0.0, ("Ref_Bolts", "Ref_Floor"): 0.0}
FLOATS = {"Layshaft": (("Layshaft", "Sleeve_3"), ("T1", "Sleeve_4")), "ThroughShaft": (("ThroughShaft", "Sleeve_1"), ("T2", "Sleeve_2"))}
GROUP = {}
for n in ("MotorCarrier", "MotorCap", "MotorGear_B", "MotorGear_A", "MotorGear_C"):
    GROUP[n] = "M"
for n in ("SlideCarrier", "SlideGear_A", "SlideGear_B", "SlideCap", "Layshaft", "T1"):
    GROUP[n] = "L"
for n in ("ThroughShaft", "T2"):
    GROUP[n] = "T"
MESHED = {frozenset(p) for p in [("MotorGear_B", "SlideGear_B"), ("MotorGear_A", "SlideGear_A"), ("MotorGear_C", "SlideCarrier"), ("T1", "T2")]}


def gapof(gap, a, b):
    return gap[(a, b)] if (a, b) in gap else gap[(b, a)]


def step_pairs(P, refs):
    ov, gap = {}, {}
    for tau in TAUS:
        d = posed(P, tau, refs)
        names = list(d)
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                if a == "Ref_Motor" or b == "Ref_Motor" or not bbo(d[a], d[b], 1.0):
                    continue
                if "CasePan" in (a, b) and not (tau == 0.0 or a in SLIDING or b in SLIDING or "ServoArm" in (a, b)):
                    continue
                v = vol(d[a], d[b])
                if v > 1e-3:
                    ov[(tau, a, b)] = round(v, 4)
                same = GROUP.get(a) is not None and GROUP.get(a) == GROUP.get(b)
                if same or frozenset((a, b)) in MESHED or (a.startswith("Ref_F") and b.startswith("Ref_F")):
                    continue
                k = (a, b)
                gap[k] = min(gap.get(k, 1e9), round(dist(d[a], d[b]), 3))
        mb = refs["Ref_MotorBody"]
        for a in names:
            if a.startswith("Ref_"):
                continue
            if bbo(d[a], mb, 1.0):
                if vol(d[a], refs["Ref_Motor"]) > 1e-3:
                    ov[(tau, a, "Ref_Motor")] = round(vol(d[a], refs["Ref_Motor"]), 4)
                gap[(a, "Ref_MotorBody")] = min(gap.get((a, "Ref_MotorBody"), 1e9), round(dist(d[a], mb), 3))
    for tau in TAUS:
        d = posed(P, tau, refs)
        mg = dict(B=d["MotorGear_B"], A=d["MotorGear_A"], C=d["MotorGear_C"])
        sg = dict(B=d["SlideGear_B"], A=d["SlideGear_A"], C=d["SlideCarrier"])
        for m in "ABC":
            for s in "ABC":
                if (m, s) in engaged(tau):
                    continue
                k = ("gear_" + m, "slide_" + s)
                gap[k] = min(gap.get(k, 1e9), round(dist(mg[m], sg[s]), 3))
    return ov, gap


TOL_CASES = ((0, 0, 0), (1, 1, 1), (-1, -1, 1), (1, -1, 1), (-1, 1, 1), (0, 0, -1))
SHIFTS = ((1.0, 0.0), (-1.0, 0.0), (0.0, 1.0), (0.0, -1.0))


def step_tol(P, refs):
    """servo +-1 mm on every body dimension, tab height and horn height: arm to block, pin engagement, pin to rod, arm to mount, body to mount"""
    sm, fp, r1 = P["ServoMount"], P["FrontPlate"], P["Rod_1"]
    t = dict(bar_clear=1e9, engage=1e9, pin_rod=1e9, arm_mount=1e9, body_vol=0.0, body_fork=1e9, pin_fork=0.0)
    for dzb, dzs, grow in TOL_CASES:
        dza = dzb + dzs
        sv = build_servo(S_STEP, dzb, dza, grow)
        t["body_vol"] = max(t["body_vol"], vol(sv, sm))
        for tau in TAUS:
            fork = move(P["ShiftFork"], dy=-tau)
            arm = place_arm(tau, dza)
            bar = arm.common(box(-100, 100, -300, 300, ARM_Z0 + dza - 0.01, ARM_Z1 + dza + 1))
            pin = arm.common(box(-100, 100, -300, 300, ARM_Z0 + dza - PIN_H - 1, ARM_Z0 + dza - 0.01))
            t["bar_clear"] = min(t["bar_clear"], dist(bar, fork))
            t["engage"] = min(t["engage"], TW_Z1 - arm.BoundBox.ZMin)
            t["pin_rod"] = min(t["pin_rod"], dist(pin, r1))
            t["arm_mount"] = min(t["arm_mount"], dist(arm, sm), dist(arm, fp))
            t["body_fork"] = min(t["body_fork"], dist(sv, fork))
    for dx, dy in SHIFTS:
        for tau in TAUS:
            arm = place_arm(tau, 0.0, dx, dy)
            fork = move(P["ShiftFork"], dy=-tau)
            pin = arm.common(box(-100, 100, -300, 300, ARM_Z0 - PIN_H - 1, ARM_Z0 - 0.01))
            t["pin_fork"] = max(t["pin_fork"], vol(pin, fork))
            t["bar_clear"] = min(t["bar_clear"], dist(arm.common(box(-100, 100, -300, 300, ARM_Z0 - 0.01, ARM_Z1 + 1)), fork))
    tw = P["ShiftFork"].common(box(BLK_X0, BLK_X1, -300, 300, BLK_Z1, TW_Z1 + 1))
    sl = []
    for tau in TAUS:
        for dx in (-1.0, 0.0, 1.0):
            ph = math.radians(arm_phi(tau))
            c = V(XS + dx - R_P * math.cos(ph), -YP_MID - R_P * math.sin(ph) + tau, 0)
            for sg in (-1, 1):
                d = 0.0
                while d < 4.0 and vol(Part.makeCylinder(PIN_D / 2, PIN_H, V(c.x, c.y + sg * (d + 0.05), PIN_Z0)), tw) < 1e-6:
                    d += 0.05
                sl.append(d)
    t["slack"] = (min(sl), max(sl))
    return {k: (round(v, 3) if not isinstance(v, tuple) else tuple(round(w, 3) for w in v)) for k, v in t.items()}


def step_misc(P, refs):
    r = {}
    zone = box(-300, 300, -300, 300, AXIS_DEPTH, FLOOR_TOP - 0.01)
    above = box(-300, 300, -300, 300, FLOOR_TOP - 0.01, 300)
    ext = [1e9, -1e9, 1e9, -1e9]
    for tau in TAUS:
        d = posed(P, tau, refs)
        for n, s in d.items():
            if n in ("ThroughShaft", "CasePan", "ServoMount") or (n.startswith("Ref_") and n != "Ref_Heads") or not bbo(s, zone):
                continue
            c = s.common(zone)
            if not c.Solids:
                continue
            b = c.BoundBox
            ext = [min(ext[0], b.XMin), max(ext[1], b.XMax), min(ext[2], b.YMin), max(ext[3], b.YMax)]
    r["cutout_zone_extent"] = [round(v, 2) for v in ext]
    r["lowest"] = round(min(s.BoundBox.ZMin for s in P.values()), 2)
    fb = []
    for n, s in P.items():
        if n in ("ThroughShaft", "Layshaft", "CasePan"):
            continue
        c = s.common(above)
        if c.Solids:
            fb.append(c.BoundBox)
    fb.append(refs["Ref_Motor"].BoundBox)
    r["footprint"] = (round(max(b.XMax for b in fb) - min(b.XMin for b in fb), 1), round(max(b.YMax for b in fb) - min(b.YMin for b in fb), 1))
    r["zmax_vs_motor_top"] = round(max(s.BoundBox.ZMax for s in P.values()) - refs["Ref_Motor"].BoundBox.ZMax, 2)
    r["plastic_cm3"] = round(sum(s.Volume for s in P.values()) / 1000.0, 1)
    ts = P["ThroughShaft"]
    sh = ts.slice(Y, -(TS_U0 + 5.0))[0].BoundBox
    r["ports"] = dict(rear=round(ts.BoundBox.YMax - (PAN_Y_R + CASE_T), 3), front=round(-ts.BoundBox.YMin - (PAN_U_F + CASE_T), 3))
    r["axis_below_floor"] = round(AXIS_DEPTH - (sh.ZMin + sh.ZMax) / 2, 3)
    pil = []
    for y in (-(TS_U0 + PS_PILOT), -(TS_U1 - PS_PILOT)):
        pil.append(all(not ts.isInside(V(0, y + e, 0), 1e-6, True) for e in (-1.0, 0.0, 1.0)) and all(ts.isInside(V(0, y + e, 0), 1e-6, True) for e in (-1.8, 1.8)))
    r["pilots"] = pil
    lay = P["Layshaft"]
    r["carrier_lay_gap"] = min(round(dist(posed(P, tau, refs)[n], lay), 3) for tau in TAUS for n in ("SlideCarrier", "SlideGear_A", "SlideGear_B", "SlideCap"))
    glue = [f.Area for n in ("Bracket", "FrontPlate") for f in P[n].Faces if isinstance(f.Surface, Part.Plane) and abs(f.CenterOfMass.z - PAD_Z1) < 1e-6 and f.normalAt(0, 0).z > 0.99]
    r["glue_area_cm2"] = round(sum(glue) / 100.0, 1)
    r["motor_pad_gap"] = round(refs["Ref_Motor"].BoundBox.ZMin - PAD_Z1, 3)
    r["print"] = {n: printable(n, P[n]) for n in PRINT_UP}
    drv = cyl_dir(M3_HEAD_D / 2, V(0, -(CAP_SEAT + M3_HEAD_H), MZ), (0, -1, 0), 60)
    r["cap_bore_clear"] = round(dist(drv, P["MotorCap"]), 3)
    r["heads_motor"] = round(dist(refs["Ref_Heads"], refs["Ref_MotorBody"]), 2)
    sp = P["SlideCap"]
    pts = []
    for k in range(48):
        a = 2 * math.pi * k / 48
        for rr in (1.5, 2.0, 2.4):
            for depth in (7.5, 9.0, 10.5):
                pts.append(V(rr * math.cos(a), -SCREW_U + rr * math.sin(a), ZL - depth))
    r["screw_material_fraction"] = round(sum(1 for p in pts if sp.isInside(p, 1e-6, True)) / float(len(pts)), 3)
    hub0 = GRUB_U
    rf = {}
    rf["spool"] = ring_fill(sp, V(0, -SCREW_U, ZL), (0, 0, -1), 1.4, 3.4, 6.7, 10.4)
    rf["t1"] = ring_fill(P["T1"], V(0, -hub0, ZL), (-1, 0, -1), 1.4, 3.4, 4.9, 6.0)
    rf["t2"] = ring_fill(P["T2"], V(0, -hub0, 0), (0, 0, -1), 1.4, 3.4, 4.9, 6.0)
    rf["motor_carrier"] = ring_fill(P["MotorCarrier"], V(0, -(FLANGE_U0 + M0) / 2, MZ), (0, 0, 1), 1.4, 3.4, 2.8, 8.2)
    for n, sx in (("Rod_1", 1), ("Rod_2", -1)):
        rf[n] = ring_fill(P[n], V(sx * ROD_X, -ROD_U1, ROD_Z), (0, 1, 0), 1.4, 3.4, 0.3, 8.7)
        rf[n + "_rear"] = ring_fill(P[n], V(sx * ROD_X, -ROD_U0, ROD_Z), (0, -1, 0), 1.4, 3.4, 0.3, 8.7)
    y0 = -(UF + FPLATE_T)
    for i, px in enumerate(PX):
        rf["mount_screw_%d" % i] = ring_fill(P["FrontPlate"], V(px, y0, PZ), (0, 1, 0), 1.4, 3.4, 0.2, 8.8)
    for sx in (-1, 1):
        rf["rail_rear_%d" % sx] = ring_fill(P["Bracket"], V(sx * RAIL_X, PLATE_T + RAIL_W / 2, LOW_Z0), (0, 0, 1), 1.4, 3.4, 0.2, PAN_PILOT_Z1 - LOW_Z0 - 0.2)
        rf["rail_front_%d" % sx] = ring_fill(P["FrontPlate"], V(sx * RAIL_X, -UF + RAIL_W / 2, LOW_Z0), (0, 0, 1), 1.4, 3.4, 0.2, PAN_PILOT_Z1 - LOW_Z0 - 0.2)
        for y in (PLATE_T + RAIL_W / 2, -UF + RAIL_W / 2):
            rf["post_%d_%.0f" % (sx, y)] = ring_fill(P["CasePan"], V(sx * RAIL_X, y, PAN_ZIN), (0, 0, 1), 1.8, 3.8, PAN_ZOUT + HEAD_CB - PAN_ZIN + 0.05, LOW_Z0 - PAN_ZIN - 0.05)
    for x, y in ear_pos():
        rf["ear_%d_%d" % (x, y)] = ring_fill(P["Bracket"], V(x, y, PAD_Z0), (0, 0, 1), EAR_HOLE / 2, EAR_HOLE / 2 + 3.0, 0.05, PAD_T - 0.05)
    rf["tie_hole"] = ring_fill(P["ServoMount"], V(TIE_EAR[0], TIE_EAR[1], PAD_Z1), (0, 0, 1), EAR_HOLE / 2, EAR_HOLE / 2 + 3.0, 0.05, TIE_T - 0.05)
    for i, px in enumerate(PX):
        rf["mount_pass_%d" % i] = ring_fill(P["ServoMount"], V(px, -SM_U1, PZ), (0, 1, 0), 1.8, 3.0, 0.05, 3.1)
    r["ring"] = rf
    br, fp, sm = P["Bracket"], P["FrontPlate"], P["ServoMount"]
    r["frame"] = {n: dict(front_pilot=void_run(P[n], V(sx * ROD_X, -ROD_U1, ROD_Z), (0, 1, 0)), rear_pilot=void_run(P[n], V(sx * ROD_X, -ROD_U0, ROD_Z), (0, -1, 0)),
                          front_hole=hole_open(fp, sx * ROD_X, ROD_Z, -(UF + FPLATE_T) + 0.2, -(UF + FPLATE_T) + 1.3, 1.8),
                          rear_hole=hole_open(br, sx * ROD_X, ROD_Z, ROD_POCKET + SKIN + 0.2, PLATE_T - 0.1, 1.8)) for n, sx in (("Rod_1", 1), ("Rod_2", -1))}
    r["pilot_depth"] = dict(cap=void_run(P["MotorCarrier"], V(0, -ARB_END, MZ), (0, 1, 0)), mount=min(void_run(fp, V(px, -(UF + FPLATE_T), PZ), (0, 1, 0)) for px in PX),
                            pan=min(void_run(P["Bracket"], V(sx * RAIL_X, PLATE_T + RAIL_W / 2, LOW_Z0), (0, 0, 1)) for sx in (-1, 1)) + 0.0,
                            pan_front=min(void_run(fp, V(sx * RAIL_X, -UF + RAIL_W / 2, LOW_Z0), (0, 0, 1)) for sx in (-1, 1)))
    wl = dict(fork_ring=wall_from(P["ShiftFork"], V(-RING_RI, -(RING_U0 + RING_T / 2), ZL), (-1, 0, 0)),
              boss=wall_from(br, V(-LINER_BORE / 2, PLATE_T + RB / 2, 0), (-1, 0, 0)),
              boss_mouth=wall_from(br, V(-LINER_BORE / 2 - 0.3, PLATE_T + RB - 0.02, 0), (-1, 0, 0)),
              boss_front=wall_from(fp, V(-LINER_BORE / 2, -(UF - FB / 2), 0), (-1, 0, 0)),
              lip=wall_from(br, V(LIP_BORE / 2 + 0.4, 0.0, 0), (0, 1, 0)),
              pan_side=wall_from(P["CasePan"], V(0, -20.0, 0), (1, 0, 0), 40.0),
              pan_floor=wall_from(P["CasePan"], V(10.0, -20.0, -10.0), (0, 0, -1)),
              rod_pocket_rear=wall_from(br, V(ROD_X + ROD_PK / 2 - 0.05, 1.5, ROD_Z), (1, 0, 0)),
              rod_mouth_rear=wall_from(br, V(ROD_X + 4.5, 0.02, ROD_Z), (1, 0, 0)),
              rod_pocket_front=wall_from(fp, V(ROD_X + ROD_PK / 2 - 0.05, -(UF + 0.75), ROD_Z), (1, 0, 0)),
              rod_mouth_front=wall_from(fp, V(ROD_X + 4.5, -(UF + 0.02), ROD_Z), (1, 0, 0)),
              rod_floor_rear=wall_from(br, V(ROD_X + 2.5, ROD_POCKET - 0.3, ROD_Z), (0, 1, 0)))
    r["walls"] = wl
    r["tab_wall"] = [wall_from(sm, V(XS, -U_BODY0, SEAT_Z - 4.0), (0, 1, 0)), wall_from(sm, V(XS, -U_BODY1, SEAT_Z - 1.5), (0, -1, 0))]
    c_y = -(UF + FPLATE_T + 1.6)
    sec = dict(crossbar=(solid_run(sm, V(30.0, c_y, FLOOR_TOP + 4.0), (0, 1, 0)), solid_run(sm, V(30.0, c_y, FLOOR_TOP + 4.0), (0, 0, 1))),
               slab=(solid_run(sm, V(SLAB_X0 + 2.0, -SV_UC, FLOOR_TOP + 2.0), (0, 0, 1)), solid_run(sm, V(SLAB_X0 + 2.0, -SV_UC, FLOOR_TOP + 2.0), (1, 0, 0))),
               wall=(solid_run(sm, V((WALL_X0 + WALL_X1) / 2, -SV_UC, 45.0), (1, 0, 0)), solid_run(sm, V((WALL_X0 + WALL_X1) / 2, -SV_UC, 45.0), (0, 0, 1))),
               strip1=(solid_run(sm, V(42.0, -(SM_U0 + 3.0), SEAT_Z - 4.0), (0, 1, 0)), solid_run(sm, V(42.0, -(SM_U0 + 3.0), SEAT_Z - 4.0), (0, 0, 1))),
               strip2=(solid_run(sm, V(42.0, -(SM_U2 - 3.0), SEAT_Z - 2.0), (0, 0, 1)), solid_run(sm, V(42.0, -(SM_U2 - 3.0), SEAT_Z - 2.0), (0, 1, 0))),
               plate=(solid_run(P["FrontPlate"], V(24.5, y0 + FPLATE_T / 2, PZ), (0, 1, 0)), solid_run(P["FrontPlate"], V(24.5, y0 + FPLATE_T / 2, PZ), (0, 0, 1))),
               bar=(solid_run(P["FrontPlate"], V(sum(PX) / 2, y0 + 7.0, PZ), (0, 1, 0)), solid_run(P["FrontPlate"], V(sum(PX) / 2, y0 + 7.0, PZ), (0, 0, 1))),
               tie=(min(solid_run(sm, V(x, y, PAD_Z1 + TIE_T / 2), (0, 0, 1)) for x in (36.0, 42.0, 48.0) for y in (0.0, 6.0, 14.0)), solid_run(sm, V(42.0, 6.0, PAD_Z1 + TIE_T / 2), (1, 0, 0))),
               ear=(solid_run(br, V(30.0, 10.0, PAD_Z0 + PAD_T / 2), (0, 0, 1)), solid_run(br, V(30.0, 10.0, PAD_Z0 + PAD_T / 2), (0, 1, 0))),
               rod=(solid_run(P["Rod_1"], V(ROD_X, -40.0, ROD_Z), (1, 0, 0)), solid_run(P["Rod_1"], V(ROD_X, -40.0, ROD_Z), (0, 0, 1))))
    r["sections"] = sec
    r["tol"] = step_tol(P, refs)
    return r


def estimates():
    e = {}
    F = 10.0
    e["servo_torque_Nm_at_10N"] = round(F * R_P / 1000, 3)
    e["servo_torque_limit_Nm"] = 0.5 * 0.16
    e["force_allowed_N"] = 0.5 * 0.16 * 1000 / R_P
    Fu = e["force_allowed_N"]
    w, t, rw, rd = 9.0, AT, 6.6, RECESS
    e["arm_MPa"] = round(F * R_P * (w / 2) / ((t * w ** 3 - rd * rw ** 3) / 12), 2)
    e["fork_strap_MPa"] = round(6 * F * (BLK_X0 + 0.5 - STRAP_X0) / ((STRAP_Z1 - STRAP_Z0) * RING_T ** 2), 2)
    e["ring_MPa_at_usable_force"] = round(Fu / (2 * RING_T * (RING_RO - RING_RI)) + 6 * 0.318 * Fu * (RING_RO + RING_RI) / 2 / (RING_T * (RING_RO - RING_RI) ** 2), 2)
    e["pin_MPa"] = round(32 * F * (PIN_L / 2) / (math.pi * PIN_D ** 3), 2)
    e["pin_bearing_MPa"] = round(F / (PIN_D * (TW_Z1 - PIN_Z0 - ARM_TOL)), 2)
    e["guide_len"], e["lever"] = BLK_L, round(LEVER, 2)
    e["guide_effective"] = round(BLK_L - 2 * MOUTH, 2)
    contact_z = (TW_Z1 + PIN_Z0) / 2
    pin_x_mid = XS - R_P * (1 + math.cos(math.radians(PHI_MAX))) / 2
    e["push_offset_lateral"] = round(abs(pin_x_mid - ROD_X), 2)
    e["push_offset_vertical"] = round(abs(contact_z - ROD_Z), 2)
    e["push_lateral_worst"] = round(max(abs(XS - R_P - ROD_X), abs(XS - R_P * math.cos(math.radians(PHI_MAX)) - ROD_X)), 2)
    e["ratios"] = {k: round(NM[k] / NS[k] * NT1 / NT2, 3) for k in "ABC"}
    e["rpm"] = {k: round(100 * v, 1) for k, v in e["ratios"].items()}
    pm = dict(B=1, A=2, C=3)
    ps = dict(B=3, A=2, C=1)
    e["stack_play"] = dict(nominal=0.1, worst_pm={k: round(0.15 * (pm[k] + ps[k]), 2) for k in "ABC"})
    e["engaged_worst"] = min(min(min(GU[k] + a * 0.15 * pm[k], SU[k] + POS_TAU[k] - a * 0.15 * ps[k]) + FACE_W - max(GU[k] + a * 0.15 * pm[k], SU[k] + POS_TAU[k] - a * 0.15 * ps[k]) for a in (-1, 1)) for k in "ABC")
    return e


MISSED = {}


def check(rep, asm, est, P):
    assert all(s.isValid() and len(s.Solids) == 1 for s in P.values()), {n: len(s.Solids) for n, s in P.items()}
    assert all(NM[k] + NS[k] == 64 for k in "ABC") and NM == dict(B=38, A=31, C=44) and NS == dict(B=26, A=33, C=20) and (NT1, NT2) == (28, 23)
    assert min(list(NM.values()) + list(NS.values()) + [NT1, NT2]) >= 17 and 2 * max(tip(n) for n in list(NM.values()) + list(NS.values())) <= 50.0 + 1e-6
    assert abs(CD1 - 32.2) < 1e-9 and abs(MZ - CD1 - CD2) < 1e-9 and 1.0 <= MZ - MOT_GB_D / 2 - PAD_Z1 <= 3.5
    r = est["ratios"]
    assert 2.6 <= r["C"] <= 3.2 and 0.95 <= r["A"] <= 1.2, r
    for tau in POS:
        e = engaged(tau)
        k = GEAR_AT[tau]
        assert list(e) == [(k, k)] and min(e.values()) >= 4.5, (tau, e)
    for tau in NEUTRAL:
        assert not engaged(tau), (tau, engaged(tau))
    assert S_STEP / 2 - FACE_W >= RULE_SPIN - 1e-9
    assert est["engaged_worst"] >= 4.5 - 1e-9 and S_STEP - 2 * FACE_W - 0.6 > 0, est
    for k, rows in rep["mesh"].items():
        assert all(v <= 1e-3 and d > 0.02 for v, d in rows), (k, rows)
    ov, gap = rep["pairs"]
    assert not ov, ov
    bad = {}
    for (a, b), g in gap.items():
        lim = FITS.get((a, b), FITS.get((b, a), RULE_SPIN))
        if "ServoArm" in (a, b) and not ({a, b} & {"ShiftFork", "Ref_Servo"}):
            lim = max(lim, 1.0)
        if g < lim - 1e-3:
            bad[(a, b)] = (g, lim)
    assert not bad, bad
    for n, (p, q) in FLOATS.items():
        f = gapof(gap, *p) + gapof(gap, *q)
        assert RULE_FLOAT_MIN - 1e-6 <= f <= RULE_FLOAT_MAX + 1e-6, (n, f)
        assert all(0.15 - 1e-3 <= gapof(gap, *q_) <= RULE_FACE_MAX + 1e-3 for q_ in (p, q)), (n, [gapof(gap, *q_) for q_ in (p, q)])
    assert all(v < 1e-3 for v in asm.values()), asm
    m = rep["misc"]
    assert abs(m["ports"]["rear"] - PS_OUT) < 1e-3 and abs(m["ports"]["front"] - PS_OUT) < 1e-3 and all(m["pilots"]), m
    assert abs(m["axis_below_floor"] - 29.0) < 1e-6
    assert abs(arm_phi(0.0)) <= PHI_MAX + 1e-9 and abs(arm_phi(STROKE)) <= PHI_MAX + 1e-9 and abs(arm_phi(0) + arm_phi(STROKE)) < 1e-6 and abs(arm_phi(S_STEP)) < 1e-9
    assert abs(R_P * math.sin(math.radians(PHI_MAX)) - S_STEP) < 1e-9
    eff = solid_run(P["ShiftFork"], V(ROD_X + BLK_PK / 2 + 0.05, -(BLK_U0 + BLK_L / 2), ROD_Z), (0, 1, 0), 60.0, 0.02)
    m["guide_effective_measured"] = eff
    assert eff >= 2 * est["lever"] and est["guide_effective"] >= 2 * est["lever"], (eff, est)
    assert est["push_offset_vertical"] <= 0.25 * eff and est["push_offset_lateral"] <= 5.0 and est["push_lateral_worst"] <= 5.0, est
    assert max(est["arm_MPa"], est["fork_strap_MPa"], est["ring_MPa_at_usable_force"], est["pin_MPa"], est["pin_bearing_MPa"]) < 15, est
    pb = {n: p for n, p in m["print"].items() if p["slopes"] or p["nlayers"] or (p["bed"] < BED_MIN and n not in BED_EXEMPT) or p["tall"] > TALL_MAX or p["thin"] > LOST_MAX}
    assert not pb, pb
    wall = dict(spool_corner=GROOVE_R - SL_GAF / R3, carrier_flat=(SL_AF - SLIDE_AF) / 2 - 0.5, carrier_flat_plain=(SL_AF - SLIDE_AF) / 2, hubA=SPA_R - SL_GAF / R3,
                motor_hub=HUB_R - GEAR_AF / R3, ring=m["walls"]["fork_ring"], rod_pilot=(ROD_S - PILOT) / 2, block=min(BLK_Z1 - GRV_Z, ROD_X - BLK_PK / 2 - BLK_X0, ROD_Z - BLK_PK / 2 - BLK_Z0),
                pilot_flange=(FLANGE_T - PILOT) / 2, tower=min(TW_HALF - TW_SLOT, PIN_U - GRV_W / 2 - BLK_U0, 2.0), strap_ring=STRAP_Z1 - STRAP_Z0, arm_recess=AT - RECESS, arm_recess_side=4.5 - 3.3, boss=min(m["walls"][k] for k in ("boss", "boss_front")), boss_mouth=m["walls"]["boss_mouth"], lip=m["walls"]["lip"], pan=min(m["walls"]["pan_side"], m["walls"]["pan_floor"]), rod_pocket=min(m["walls"][k] for k in ("rod_pocket_rear", "rod_mouth_rear", "rod_pocket_front", "rod_mouth_front", "rod_floor_rear")))
    assert all(v >= 1.2 - 1e-9 for v in wall.values()) and wall["carrier_flat_plain"] >= 2.0 and wall["hubA"] >= 2.0 - 1e-9, wall
    assert wall["ring"] >= 1.6 - 1e-9 and wall["rod_pilot"] >= 2.0 - 1e-9 and wall["pilot_flange"] >= 2.0 - 1e-9 and wall["boss"] >= 2.0 - 1e-9 and wall["pan"] >= 1.6 and wall["lip"] >= 1.2 and wall["boss_mouth"] >= 1.2, wall
    keyed = {"MotorGear_B": (NM["B"], GEAR_AF), "MotorGear_A": (NM["A"], GEAR_AF), "MotorGear_C": (NM["C"], GEAR_AF), "SlideGear_B": (NS["B"], SL_GAF), "SlideGear_A": (NS["A"], SL_GAF),
             "SlideCarrier": (NS["C"], SLIDE_AF), "T1": (NT1, SOCKET), "T2": (NT2, SOCKET)}
    assert all(root(n) - af / R3 >= 2.0 for n, af in keyed.values()), keyed
    assert m["carrier_lay_gap"] >= RULE_SLIDE - 1e-3, m["carrier_lay_gap"]
    assert m["screw_material_fraction"] >= 0.95 and FLANGE_T / 2 >= 2.2 + 1e-9, m["screw_material_fraction"]
    assert all(v >= 0.99 for v in m["ring"].values()), {k: v for k, v in m["ring"].items() if v < 0.99}
    assert min(m["tab_wall"]) >= 0.8, m["tab_wall"]
    for k, (thin, other) in m["sections"].items():
        assert thin >= 3.0 - 1e-6 and other >= 6.0 - 1e-6, (k, thin, other)
    t = m["tol"]
    assert t["bar_clear"] >= ARM_CLR - 1e-3 and t["engage"] >= ENGAGE_MIN - 1e-3 and t["pin_rod"] >= 1.0 - 1e-3 and t["arm_mount"] >= 1.0 - 1e-3 and t["body_vol"] < 1e-3 and t["body_fork"] >= 0.8 and t["pin_fork"] < 1e-3, t
    assert 1.1 <= t["slack"][0] and t["slack"][1] <= 1.3, ("pin to fork slot slack, 1.2 each way", t["slack"])
    assert STRIP2_Z0 - (ARM_Z1 + ARM_TOL) >= 1.0 - 1e-9
    assert LIP_BORE / 2 - SHAFT_AF / R3 >= RULE_BORE - 1e-9 and 10.6 / 2 - STUB_D / 2 >= RULE_BORE - 1e-9 and MOT_BOSS_HOLE / 2 - MOT_BOSS_D / 2 >= RULE_BORE - 1e-9
    assert LINER_ID / 2 - SHAFT_AF / R3 >= RULE_BORE + 0.05 and LIP_BORE / 2 - SHAFT_AF / R3 >= RULE_BORE and LINER_BORE - LINER_OD >= 0.2 - 1e-9 and 8.0 <= LINER_L <= 10.0
    assert EAR_R - EAR_HOLE / 2 >= 3.0 - 1e-9 and LOW_X + 0.4 <= PAN_XI and CUT_X1 - LOW_X >= 1.0 and EAR_HOLE >= 3.6 and abs(PILOT - 2.8) < 1e-9 and PX[1] - PX[0] >= M3_HEAD_D + 0.5 - 1e-9
    assert SLIDE_AF - SHAFT_AF >= 2 * RULE_SLIDE and ROD_PK - ROD_S >= 2 * RULE_SLIDE and BLK_PK - ROD_S >= 2 * RULE_SPIN and GRV_W - PIN_D >= 2 * RULE_SLIDE and SL_GAF - SL_AF == GEAR_AF - CARR_AF
    ext = m["cutout_zone_extent"]
    assert CUT_X0 <= ext[0] - 1.0 and ext[1] + 1.0 <= CUT_X1 and CUT_Y0 <= ext[2] - 1.0 + 1e-6 and ext[3] + 1.0 <= CUT_Y1 + 1e-6, (ext, (CUT_X0, CUT_X1, CUT_Y0, CUT_Y1))
    cut_x, cut_y = CUT_X1 - CUT_X0, CUT_Y1 - CUT_Y0
    m["cutout"] = (round(cut_x, 1), round(cut_y, 1))
    assert cut_x <= 64 + 1e-9 and cut_y <= (ext[3] - ext[2]) + 2.0 + 1e-6, (m["cutout"], ext)
    if cut_y > 92:
        MISSED["cutout_length"] = (m["cutout"], "limit 92: the layshaft rear boss and head (z up to 32 in the floor slab) set the rear edge at y %.1f, and the front plate and its rod screw heads at y %.1f" % (CUT_Y1, -(UF + FPLATE_T + M3_HEAD_H)))
    assert m["lowest"] >= -16.0 and m["zmax_vs_motor_top"] <= 5.0 + 1e-6 and m["plastic_cm3"] < 200 and m["footprint"][0] <= 100, m
    m["case"] = dict(depth_below_floor=round(AXIS_DEPTH - PAN_ZOUT, 1), bottom_z=PAN_ZOUT, ground_clearance_100mm_wheels=round(50.0 + PAN_ZOUT, 1), screw_head_clearance=round(50.0 + PAN_ZOUT, 1))
    m["glue_land"] = dict(rear_mm=round(PAD_Y1 - PLATE_T, 1), minus_x_mm=round(CUT_X0 - (-34.4), 1), area_cm2=m["glue_area_cm2"])
    m["bolt_pattern"] = dict(x=EAR_X, y=list(EAR_YS), hole=EAR_HOLE, bolt="M3x%d, M3x%d at the ServoMount tie ear" % (BOLT_L, TIE_BOLT_L))
    assert gapof(gap, "Bracket", "ServoMount") < 1e-3 and gapof(gap, "FrontPlate", "ServoMount") < 1e-3, "ServoMount must touch both the Bracket and the FrontPlate"
    assert est["force_allowed_N"] >= 4.35, est
    cap_eng, rod_eng, rear_eng = CAP_SCREW_L - (CAP_SEAT - ARB_END), ROD_SCREW_L - (UF + FPLATE_T - ROD_U1), ROD_REAR_L - (PLATE_T + ROD_U0)
    mount_eng, pan_eng, mot_eng = MOUNT_SCREW_L - XBAR_T, PAN_SCREW_L - (LOW_Z0 - (PAN_ZOUT + HEAD_CB)), MOTOR_SCREW_L - (PLATE_T - MOT_CB_DEEP)
    assert min(cap_eng, rod_eng, rear_eng, mount_eng, pan_eng, mot_eng) >= 5.0 - 1e-9, (cap_eng, rod_eng, rear_eng, mount_eng, pan_eng, mot_eng)
    pd = m["pilot_depth"]
    assert pd["cap"] >= cap_eng and pd["mount"] >= mount_eng and pd["pan"] >= pan_eng and pd["pan_front"] >= pan_eng, (pd, cap_eng, mount_eng, pan_eng)
    assert (STUB_D - HEAD_BORE) / 2 >= 1.5 - 1e-9 and CAP_CB >= M3_HEAD_H and CAP_SEAT - ARB_END >= 4.0 and CAP_PLATE_FLOOR - STUB_END >= RULE_SPIN - 1e-9, "MotorCap counterbore"
    assert (HEAD_BORE - M3_HEAD_D) / 2 >= RULE_BORE - 1e-9 and m["cap_bore_clear"] >= RULE_BORE - 1e-3, (m["cap_bore_clear"], "driver in the MotorCap bore")
    assert PAN_ZOUT + HEAD_CB + PAN_SCREW_L <= PAN_PILOT_Z1 and RAIL_Z1 - PAN_PILOT_Z1 >= 1.2 - 1e-9 and FPLATE_T + BAR_L - MOUNT_PILOT >= 2.0 - 1e-9, "pilot ends"
    for n, f in m["frame"].items():
        assert f["front_hole"] and f["rear_hole"] and f["front_pilot"] >= rod_eng and f["rear_pilot"] >= rear_eng, (n, f, rod_eng, rear_eng)
    assert m["heads_motor"] >= RULE_SPIN - 1e-9 and m["walls"]["rod_floor_rear"] >= 1.2 - 1e-9, (m["heads_motor"], m["walls"]["rod_floor_rear"])
    screws = [("MotorCap", 1, CAP_SCREW_L, 0), ("RodFront", 2, ROD_SCREW_L, 0), ("RodRear", 2, ROD_REAR_L, 0), ("ServoMount", 2, MOUNT_SCREW_L, 0), ("CasePan", 4, PAN_SCREW_L, 0),
              ("Motor", 6, MOTOR_SCREW_L, 0), ("EarBolt", 3, BOLT_L, 0), ("TieBolt", 1, TIE_BOLT_L, 0), ("Grub", 4, GRUB_L, 1)]
    assert all(l == GRUB_L if g else l in KIT_LENGTHS for _, _, l, g in screws) and GRUB_L == 6.0, screws
    m["screws"] = {n: (c, l) for n, c, l, _ in screws}
    tot = {}
    for _, c, l, _ in screws:
        tot[l] = tot.get(l, 0) + c
    assert tot == {16.0: 2, 8.0: 14, 12.0: 5, 6.0: 4}, tot
    if min(m["tab_wall"]) < 2.0:
        MISSED["servo_tab_pilot_wall"] = (m["tab_wall"], "the servo tab hole is %.2f from the body end, so a 2.0 wall body side of the M2 pilot (dia %.1f) is impossible; measured wall shown" % (SV_HOLE_SP / 2 - SV_L / 2, TAB_PILOT))


def build_refs():
    mot = build_motor()
    body = mot.cut(yc(MOT_SH_D / 2 + 0.3, -MOT_SH_L - 1, PLATE_T + 0.001, 0, MZ))
    return dict(Ref_Motor=mot, Ref_MotorBody=body, Ref_Floor=floor_slab(), Ref_Bolts=build_bolts(), Ref_Heads=build_rod_heads())


def main():
    import time
    t0 = time.time()
    if App.listDocuments().get(DOC_NAME):
        App.closeDocument(DOC_NAME)
    doc = App.newDocument(DOC_NAME)
    P = build_parts()
    refs = build_refs()
    print("built", round(time.time() - t0, 1), flush=True)
    rep = dict(mesh=step_mesh())
    print("mesh", round(time.time() - t0, 1), flush=True)
    rep["pairs"] = step_pairs(P, refs)
    print("pairs", round(time.time() - t0, 1), flush=True)
    rep["misc"] = step_misc(P, refs)
    print("misc", round(time.time() - t0, 1), flush=True)
    asm = step_assembly(P, refs)
    est = estimates()
    print("report", rep["misc"], asm, est, flush=True)
    print("gaps", {k: v for k, v in rep["pairs"][1].items() if v < 3.0}, flush=True)
    check(rep, asm, est, P)
    print("MISSED", MISSED)
    placed = posed(P, S_STEP, refs)
    for n in PRINT_UP:
        o = doc.addObject("Part::Feature", n)
        o.Shape = placed[n]
    for n in ("Ref_Motor", "Ref_Servo", "Ref_Floor", "Ref_Bolts", "Ref_Heads"):
        o = doc.addObject("Part::Feature", n)
        o.Shape = placed[n]
    doc.recompute()
    doc.saveAs(OUT)
    return doc


if "NO_RUN" not in globals():
    main()
