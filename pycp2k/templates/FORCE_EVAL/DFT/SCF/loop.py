from pycp2k.templates.GLOBAL.GLOBAL import CP2K

def add_inner_scf(calc:CP2K,**kwargs):
    allowed_kwargs=["scf_guess","max_scf","eps_scf","ignore_convergence_failure"]
    #inner scf loop
    SCF=calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF
    SCF.Scf_guess=kwargs.get("scf_guess","RESTART")
    SCF.Max_scf=kwargs.get("max_scf",20)
    SCF.Eps_scf=kwargs.get("eps_scf",1e-6)
    Ignore_convergence_failure=kwargs.get("Ignore_convergence_failure",False)
    if Ignore_convergence_failure:
        SCF.Ignore_convergence_failure=True
    print(f"scf_guess = {SCF.Scf_guess}")
    print(f"max_scf = {SCF.Max_scf}")
    print(f"eps_scf = {SCF.Eps_scf}")

def add_outer_scf(calc:CP2K,**kwargs):
    #outer scf loop
    SCF=calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF
    SCF.OUTER_SCF.Max_scf=kwargs.get("outer_max_scf",2)
    SCF.OUTER_SCF.Eps_scf=kwargs.get("outer_eps_scf",1e-6)
    print(f"outer_max_scf = {SCF.OUTER_SCF.Max_scf}")
    print(f"outer_eps_scf = {SCF.OUTER_SCF.Eps_scf}")