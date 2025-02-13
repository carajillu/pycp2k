from pycp2k import CP2K
from pycp2k.workflows.optimizer import get_scf_df, change_optimizer

calc = CP2K()
calc.cp2k_command = "/Users/jclarknicholas/local/cp2k/bin/cp2k.psmp"
calc.working_directory = "./"
calc.project_name = "si_bulk"
calc.mpi_n_processes = 2
calc.parse("test.in")
try:
  calc.run()
except:
  pass

df=get_scf_df("si_bulk.out")
newcalc=change_optimizer(df,calc)
print(f"scf_guess: {newcalc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.Scf_guess}")
#newcalc.run()


