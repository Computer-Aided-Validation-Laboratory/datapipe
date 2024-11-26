'''
================================================================================
pyvale: the python computer aided validation engine

License: MIT
Copyright (C) 2024 The Digital Validation Team
================================================================================
'''
import time
from pathlib import Path
from mooseherder import (MooseConfig,
                         MooseRunner,
                         GmshRunner)

SIM_PATH = Path.cwd() / "data" / "moosetransient"
GMSH_FILE = "gmsh_plate_with_hole_2d.geo"
MOOSE_FILE = "sim_moose_transient.i"

def main() -> None:

    # Run Gmsh
    gmsh_runner = GmshRunner(Path.home() / 'gmsh/bin/gmsh')
    gmsh_start = time.perf_counter()
    gmsh_runner.run(SIM_PATH / GMSH_FILE)
    gmsh_run_time = time.perf_counter()-gmsh_start


    config = {'main_path': Path.home() / 'moose',
            'app_path': Path.home() / 'proteus',
            'app_name': 'proteus-opt'}

    # Run MOOSE
    moose_config = MooseConfig(config)
    moose_runner = MooseRunner(moose_config)

    moose_runner.set_run_opts(n_tasks = 4,
                              n_threads = 2,
                              redirect_out = False)

    moose_start_time = time.perf_counter()
    moose_runner.run(SIM_PATH / MOOSE_FILE)
    moose_run_time = time.perf_counter() - moose_start_time

    print()
    print("="*80)
    print("SIMULATION COMPLETE")
    print(f"Gmsh run time = {gmsh_run_time:.2f} seconds")
    print(f"MOOSE run time = {moose_run_time:.3f} seconds")
    print("="*80)
    print()

if __name__ == '__main__':
    main()

