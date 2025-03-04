from pycp2k import CP2K

def initialise_dft(project_name):
    calc = CP2K()
    calc.working_directory = "./"
    calc.project_name = project_name
    calc.mpi_n_processes = 2
    CP2K_INPUT = calc.CP2K_INPUT  # This is the root of the input tree
    # Repeatable sections are added with X_add() function. Optionally you can
    # provide the Section_parameter as an argument to this function.
    FORCE_EVAL = CP2K_INPUT.FORCE_EVAL_add()
    return(calc, CP2K_INPUT)

def setup_dft(CP2K_INPUT):
    CP2K_INPUT.GLOBAL.Run_type = "RT_PROPAGATION"
    DFT = CP2K_INPUT.FORCE_EVAL_list[0].DFT
    SCF = DFT.SCF
    SCF.OT
    DFT.QS.Eps_default = 1.0E-12
    DFT.MGRID.Ngrids = 4
    DFT.MGRID.Cutoff = 300
    DFT.MGRID.Rel_cutoff = 60
    DFT.XC.XC_FUNCTIONAL.Section_parameters = "PBE"
    SCF.Scf_guess = "ATOMIC"
    SCF.Eps_scf = 1.0E-7
    SCF.Max_scf = 30
    SCF.OT.Section_parameters = "ON"

def setup_rtp(CP2K_INPUT):
    DFT = CP2K_INPUT.FORCE_EVAL_list[0].DFT
    RTP = DFT.REAL_TIME_PROPAGATION
    RTP.Max_iter = 10
    RTP.Mat_exp = 'TAYLOR'
    RTP.Eps_iter = 1.0E-9
    RTP.Initial_wfn = 'SCF_WFN'

def add_atom_kinds(CP2K_INPUT, atoms):
    DFT = CP2K_INPUT.FORCE_EVAL_list[0].DFT
    # standard MOLOPT DFT setup
    DFT.Basis_set_file_name = "BASIS_MOLOPT"
    DFT.Potential_file_name = "POTENTIAL"
    for symbol in set(atoms.get_chemical_symbols()):
        #print(symbol)
        KIND = CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_add(symbol)
        KIND.Basis_set = 'DZVP-MOLOPT-SR-GTH'
        KIND.Potential = 'GTH-PBE'

###############################################################################
##
## Main script
##
###############################################################################

# function to create CP2K input structure
calc, CP2K_INPUT = initialise_dft('test')

# setup electronic structure sections
setup_dft(CP2K_INPUT)
setup_rtp(CP2K_INPUT)

# build atomistic system
from ase.build import molecule
SUBSYS = CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS
atoms = molecule('H2O')
atoms.set_cell([10, 10, 10])
atoms.set_pbc([True, True, True])

# convert ASE atoms object to CP2K input
# poisson solver section needs work
calc.create_coord(SUBSYS,atoms=atoms)
calc.create_cell(SUBSYS,atoms=atoms)

# add basis sets and pseudo potentials
add_atom_kinds(CP2K_INPUT, atoms)

# finally write input file
calc.write_input_file('test.inp')