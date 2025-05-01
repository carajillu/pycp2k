from ase import Atoms
from pycp2k.templates.GLOBAL.GLOBAL import CP2K

valence_electrons_ecp = {
    # s-block (Alkali & Alkaline Earth)
    "H": 1, "He": 2,
    "Li": 1, "Be": 2, "Na": 1, "Mg": 2, "K": 1, "Ca": 2, "Rb": 1, "Sr": 2, "Cs": 1, "Ba": 2,
    
    # p-block (Main Group Elements)
    "B": 3, "C": 4, "N": 5, "O": 6, "F": 7, "Ne": 8,
    "Al": 3, "Si": 4, "P": 5, "S": 6, "Cl": 7, "Ar": 8,
    "Ga": 3, "Ge": 4, "As": 5, "Se": 6, "Br": 7, "Kr": 8,
    "In": 3, "Sn": 4, "Sb": 5, "Te": 6, "I": 7, "Xe": 8,
    "Tl": 3, "Pb": 4, "Bi": 5, "Po": 6, "At": 7, "Rn": 8,

    # d-block (Transition Metals)
    "Sc": 3, "Ti": 4, "V": 5, "Cr": 6, "Mn": 7, "Fe": 8, "Co": 9, "Ni": 10, "Cu": 11, "Zn": 12,
    "Y": 3, "Zr": 4, "Nb": 5, "Mo": 6, "Tc": 7, "Ru": 8, "Rh": 9, "Pd": 10, "Ag": 11, "Cd": 12,
    "Hf": 4, "Ta": 13, "W": 14, "Re": 15, "Os": 16, "Ir": 17, "Pt": 18, "Au": 19, "Hg": 12,

    # f-block (Lanthanides & Actinides)
    "La": 3, "Ce": 4, "Pr": 5, "Nd": 6, "Pm": 7, "Sm": 8, "Eu": 9, "Gd": 10, "Tb": 11, "Dy": 12, "Ho": 13, "Er": 14, "Tm": 15, "Yb": 16, "Lu": 3,
    "Ac": 3, "Th": 4, "Pa": 5, "U": 14, "Np": 15, "Pu": 16, "Am": 17, "Cm": 18, "Bk": 19, "Cf": 20, "Es": 21, "Fm": 22, "Md": 23, "No": 24, "Lr": 3
}

def add_kinds(atoms:Atoms,calc:CP2K,**kwargs):
    """
    Add kinds to the atoms object.
    """
    potential=kwargs.get("potential","GTH-PBE")
    basis_set=kwargs.get("basis_set",["DZVP-MOLOPT-SR-GTH"])
    if not isinstance(basis_set,list):
        basis_set=[basis_set]
    for symbol in set(atoms.get_chemical_symbols()):
        if symbol not in valence_electrons_ecp:
            raise ValueError(f"Atom {symbol} not supported.")
        calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_add(symbol)
        calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_list[-1].Potential=f"{potential}-q{valence_electrons_ecp[symbol]}"
        calc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.KIND_list[-1].Basis_set=basis_set
