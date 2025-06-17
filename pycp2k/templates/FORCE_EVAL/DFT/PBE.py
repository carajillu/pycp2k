from pycp2k.templates.GLOBAL.GLOBAL import CP2K

def add_PBE(calc:CP2K,feval_idx:int=0,charge:int=0,LSD:bool=False,**kwargs):
    if  len(calc.CP2K_INPUT.FORCE_EVAL_list) <= feval_idx:
        raise ValueError(f"FORCE_EVAL section {feval_idx} not found in calculator")

    print(f"===Adding PBE to FORCE_EVAL section {feval_idx}===")
    calc.CP2K_INPUT.FORCE_EVAL_list[feval_idx].Method="QS" # This is not optional
    DFT=calc.CP2K_INPUT.FORCE_EVAL_list[feval_idx].DFT
    DFT.Charge=charge
    DFT.LSD=LSD
    # Get potential file
    DFT.Potential_file_name=kwargs.get("potential_file_name","POTENTIAL")
    print(f"Potential file: {DFT.Potential_file_name}")
    # Get basis set file
    basis_set_files=kwargs.get("basis_set_files",["BASIS_MOLOPT"])
    if not isinstance(basis_set_files,list):
        basis_set_files=[basis_set_files]
    DFT.Basis_set_file_name=basis_set_files
    print(f"Basis_set_file_name: {DFT.Basis_set_file_name}")
    calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.XC.XC_FUNCTIONAL.PBE.Section_parameters="" # just to create section?
    return

def del_PBE(calc:CP2K):
    raise NotImplementedError("Not implemented")