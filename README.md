# RC car kit

3D printed drivetrain modules for a hot-glue-and-cardboard RC car that kids can build. Work in progress: only the wheel mount has been test printed so far.

Each module is a parametric FreeCAD script that generates its `.FCStd` model. Run a script inside FreeCAD 1.1 (the `freecad.gears` workbench is required) to rebuild its model.

| Script | Module | State |
|---|---|---|
| `differential.py` | Enclosed axle module: bevel differential, shaft input, chain-through output | checked on the model |
| `wheel_mount.py` | Wheel mount, steerable or locked, takes a drive shaft for a powered wheel | checked on the model |
| `wheel_mount2.py` | Wheel mount, second design: knuckle pushes up onto a single kingpin post under a glue pad | checked on the model |
| `drive_shaft.py` | Drive shaft with captured universal joints and a telescoping middle | checked on the model |
| `motor_module.py` | GA37 gearmotor geared 3:1 to a through shaft with front and rear ports | checked on the model |
| `cvt_module.py` | Servo-shifted pinched-disc CVT motor module | parked: test print showed tight fits, and the sliding carriage is prone to binding |
| `make_print_project.py` | Writes a Bambu Studio `.3mf` print project per module | working |

## Kit standards

- Drive shafts are 8 mm hex. Every shaft end that takes a joint is a port: 16 mm of plain hex with a 2.8 mm cross pilot 5.9 mm from the tip.
- The chassis is a flat cardboard floor. Axle modules, wheel mounts and drive shafts hang under it, with shaft axes 29 mm below its underside. Motor modules sit on top with the drive hanging through a cut-out.
- PLA on a 0.4 mm nozzle, no supports, M3 screws.

## Paths

The scripts save to absolute paths under `/home/mikhail/Documents/cad/RC Car/` and `make_print_project.py` expects the AstoCAD and Bambu Studio AppImages under `/home/mikhail/AppImages/`. Change the `OUT` constant in each script and the paths at the top of `make_print_project.py` for another machine.
