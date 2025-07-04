from ase import Atoms
from ase.io import read
from pycp2k.templates.GLOBAL.GLOBAL import pyCP2K
from pycp2k.templates.FORCE_EVAL.xTB_templates import add_xTB_OT
from pycp2k.templates.MOTION.GEO_OPT.minimization import add_minimization

def geo_opt_xtb_ot(project_name,file_name):
    """
    Perform geometry optimization using xTB with the OT method.
    """

    atoms = Atoms(read(file_name))  # Replace with your input file
    print(atoms)

    calc=pyCP2K(cp2k_command="wsl mpirun -np 1 /usr/bin/cp2k.psmp", #replace this with your actual cp2k commmand (e.g. "mpirun -np 4 cp2k.psmp")
            # this needs to be modified to deal with wsl 
            # working_directory=os.getcwd(),
            project_name=project_name, #Project files will have this base name
            run_type="ENERGY_FORCE",
            print_level="MEDIUM")

    add_xTB_OT(atoms=atoms, 
            calc=calc,
            feval_idx=0, # Index of the force eval to use
            preconditioner="FULL_ALL",minimizer="DIIS", # Options for pycp2k.templates.FORCE_EVAL.DFT.SCF.OT.add_OT
            scf_guess="RESTART",max_scf=20,eps_scf=1e-6, # Options for pycp2k.templates.FORCE_EVAL.DFT.SCF.loop.add_inner_SCF
            outer_max_scf=2,outer_eps_scf=1e-6, # Options for pycp2k.templates.FORCE_EVAL.DFT.SCF.loop.add_outer_SCF
            #FIXME: Add option to run with non-cubic cells and no PBC # Options for pycp2k.templates.FORCE_EVAL.SUBSYS.add_atoms.add_cell
            )

    add_minimization(atoms=atoms,
                    calc=calc, 
                    feval_idx=0, # Index of the force eval to use
                    max_iter=100, # Maximum number of minimization steps
                    energy_tol=1e-6, force_tol=1e-3) # Tolerances for convergence

    calc.run()

if __name__ == "__main__":
    file_name = "TBA.xyz"
    project_name = "TBA_monomer_xtb_ot"  # Set the project name for the xTB calculation
    geo_opt_xtb_ot(project_name, file_name)  # Run the geometry optimization
