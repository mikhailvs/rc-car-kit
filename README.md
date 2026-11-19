# RC car kit

3D printed drivetrain modules for a hot-glue-and-cardboard RC car that kids can build. Work in progress: the first wheel mount, the CVT and the differential have been test printed so far.

Each module is a parametric FreeCAD script that generates its `.FCStd` model. Run a script inside FreeCAD 1.1 (the `freecad.gears` workbench is required) to rebuild its model.

| Script | Module | State |
|---|---|---|
| `differential.py` | Enclosed axle module: bevel differential, shaft input, chain-through output or plug, bolt ears, PTFE liner pockets | checked on the model |
| `wheel_mount.py` | Wheel mount, steerable or locked, takes a drive shaft for a powered wheel | checked on the model |
| `wheel_mount2.py` | Wheel mount, second design: knuckle pushes up onto a single kingpin post under a glue pad, axle runs in PTFE liner pockets | checked on the model |
| `drive_shaft.py` | Drive shaft with captured universal joints and a telescoping middle | checked on the model |
| `drive_hub.py` | Driven and steered wheel hub: drive joint centred on the steering pivot, knuckle on two screw pivots, printed wheel with TPU tyre, mirrored carrier and knuckle for the other side | checked on the model |
| `axle.py` | Solid axle: compact differential centre section (bevel final drive 18/11, two spider gears, retained plug shafts, round pivot journals) with bolt-on arms in two widths that carry the drive hub knuckles | checked on the model |
| `rod_frame.py` | Test platform frame on two 8 mm carbon rods: per axle an inner and an outer bracket with caps that hold the axle's pivot journals so it rocks about its drive shaft line, crossing coil springs on pads, pinch clamps and rod end stops, gearbox cradle | checked on the model |
| `steering.py` | Steering that rides on the front axle: bolt-on knuckle arms, tie rod in two lengths, servo mount on the axle pivot end, lever on the servo horn | checked on the model |
| `ptfe_jig.py` | Cutting jig for the PTFE liners: tube over a pin in an 8 mm deep pocket, blade runs on the top face, plus a go/no-go gauge | checked on the model |
| `motor_module.py` | GA37 gearmotor geared 3:1 to a through shaft with front and rear ports | checked on the model |
| `gearbox_module.py` | Servo-shifted 3 speed sliding-gear motor module with a bottom case and PTFE liner pockets | checked on the model |
| `cvt_module.py` | Servo-shifted pinched-disc CVT motor module | parked: test print showed tight fits, and the sliding carriage is prone to binding |
| `make_print_project.py` | Writes a Bambu Studio `.3mf` print project per module | working |

## Kit standards

- Drive shafts are 8 mm hex. Every shaft end that takes a joint is a port: 16 mm of plain hex with a 2.8 mm cross pilot 5.9 mm from the tip.
- The chassis is a flat cardboard floor. Axle modules, wheel mounts and drive shafts hang under it, with shaft axes 29 mm below its underside. Motor modules sit on top with the drive hanging through a cut-out.
- PLA on a 0.4 mm nozzle, no supports, M3 screws.

## Paths

The scripts save to absolute paths under `/home/mikhail/Documents/cad/RC Car/` and `make_print_project.py` expects the AstoCAD and Bambu Studio AppImages under `/home/mikhail/AppImages/`. Change the `OUT` constant in each script and the paths at the top of `make_print_project.py` for another machine.
