import argparse
from pycp2k import CP2K
from ase.io import read, write
from pycp2k.workflows.utils import atom_info

def parse():
    parser = argparse.ArgumentParser(description='Singlepoint calculation from castep cell')
    parser.add_argument("--project_name", type=str, default="cp2k", help="CP2K>GLOBAL>PROJECT_NAME")
    parser.add_argument("--cell", type=str, required=True, help='Path to cell file')
    parser.add_argument("--cp2k_input_template", type=str, required=True, help='Path to cp2k input template file')
    parser.add_argument("--output", type=str, required=True, help='Path to resulting cp2k input file')
    return parser.parse_args()

def gen_cubic_cell():
    raise(NotImplementedError,"gen_cubic_cell not yet implemented")

def add_atoms(calc, atoms):
    if atoms.cell:
       # set cell vectors if they exist
       calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.CELL.A=" ".join(map(str, atoms.cell[0]))
       calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.CELL.B=" ".join(map(str, atoms.cell[1]))
       calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.CELL.C=" ".join(map(str, atoms.cell[2]))

    # TODO: set periodicity and cell angles
    # set coordinates
    default_keyword=[]
    for i in range(len(atoms)):
        default_keyword.append(atoms[i].symbol+" "+" ".join(map(str, atoms.positions[i])))
    calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.COORD.Default_keyword=default_keyword

def add_kinds(calc, cell):
    symbols=[]
    for atom in cell:
        if atom.symbol not in symbols:
            symbols.append(atom.symbol)

    #get potential templates
    potential_lst=calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_list[0].Potential.split("-")
    potential_tp="-".join(potential_lst[0:len(potential_lst)-1])+"-q"
    
    #get basis set templates
    basis_tps=[]
    for j in range(len(calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_list[0].Basis_set)):
        basis_lst=calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_list[0].Basis_set[j].split("-")
        basis_tps.append("-".join(basis_lst[0:len(basis_lst)-1])+"-q")
 
    calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_list=[]
    for symbol in symbols:
        calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_add(symbol)
        calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_list[-1].Potential=potential_tp+str(atom_info.valence_electrons_ecp[symbol])
        calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_list[-1].Basis_set=[]
        for basis_tp in basis_tps:
            calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_list[-1].Basis_set.append(basis_tp+str(atom_info.valence_electrons_ecp[symbol]))

if __name__=="__main__":
    args = parse()
    cell = read(args.cell)
    calc=CP2K()
    calc.parse(args.cp2k_input_template)
    add_system(calc, cell)
    add_kinds(calc,cell)
    calc.write_input_file(args.output)
    