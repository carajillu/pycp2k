from copy import deepcopy

from ase.lattice.cubic import Diamond
atoms = Diamond(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                  symbol='Si',
                  latticeconstant=5.430697500,
                  size=(1, 1, 1))
print(atoms)

from pycp2k.templates.GLOBAL.GLOBAL import pyCP2K
calc=pyCP2K(cp2k_command="wsl mpirun -np 1 /usr/bin/cp2k.psmp", #replace this with your actual cp2k commmand (e.g. "mpirun -np 4 cp2k.psmp")
          #working_directory=os.getcwd(),
          project_name="energy_force_Si", #Project files will have this base name
          run_type="ENERGY_FORCE",
          print_level="MEDIUM")

from pycp2k.templates.FORCE_EVAL.xTB_templates import add_xTB_OT
from pycp2k.templates.MOTION.GEO_OPT.minimization import add_minimization

calc_xtb_ot=deepcopy(calc)
calc_xtb_ot.CP2K_INPUT.GLOBAL.Project_name="xtb_ot"
calc_xtb_ot.project_name="xtb_ot"

add_xTB_OT(atoms=atoms, calc=calc_xtb_ot,
           feval_idx=0,
           preconditioner="FULL_ALL",minimizer="DIIS", # Options for pycp2k.templates.FORCE_EVAL.DFT.SCF.OT.add_OT
           scf_guess="RESTART",max_scf=20,eps_scf=1e-6, # Options for pycp2k.templates.FORCE_EVAL.DFT.SCF.loop.add_inner_SCF
           outer_max_scf=2,outer_eps_scf=1e-6, # Options for pycp2k.templates.FORCE_EVAL.DFT.SCF.loop.add_outer_SCF
           #FIXME: Add option to run with non-cubic cells and no PBC # Options for pycp2k.templates.FORCE_EVAL.SUBSYS.add_atoms.add_cell
           )

add_minimization(calc=calc_xtb_ot, atoms=atoms,
                 feval_idx=0, # Index of the force eval to use
                 max_iter=100, # Maximum number of minimization steps
                 energy_tol=1e-6, force_tol=1e-3) # Tolerances for convergence

calc_xtb_ot.run()