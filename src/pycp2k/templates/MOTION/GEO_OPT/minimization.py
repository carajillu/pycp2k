from pycp2k.templates.GLOBAL.GLOBAL import CP2K
from ase import Atoms

def add_minimization(calc: CP2K, atoms: Atoms, **kwargs):
    print("=== Setting up geometry optimization ===")
    calc.CP2K_INPUT.GLOBAL.Run_type = "GEO_OPT"
    GEO_OPT = calc.CP2K_INPUT.MOTION.GEO_OPT
    GEO_OPT.Type = "MINIMIZATION" # not optional for geometry minimization
    optimizer=kwargs.get("geo_opt_optimizer", None)
    if optimizer is None:
        if len(atoms) < 500:
            GEO_OPT.Optimizer = "BFGS"
        else:
            GEO_OPT.Optimizer = "LBFGS"
    else:
        GEO_OPT.Optimizer = optimizer
    GEO_OPT.Max_iter = kwargs.get("geo_opt_max_iter", 200)
    GEO_OPT.Max_force = kwargs.get("geo_opt_max_force", 4.5e-4) # 4.5e-4 Ha/Bohr which is the CP2K default = 0.0231 eV/A
    print(f"Using {GEO_OPT.Optimizer} optimizer")
    print(f"Max iterations: {GEO_OPT.Max_iter}")
    print(f"Convergence criterion: max force = {GEO_OPT.Max_force} Ha/Bohr")
    print("=== Geometry optimization setup complete ===")
    return 
