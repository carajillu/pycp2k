from pycp2k import CP2K
from pycp2k.workflows.optimizer import get_scf_df, change_optimizer
from ase.io import read, write
import pandas as pd
import os
import subprocess
import globß

if __name__=="__main__":
    calc=CP2K()
    calc.cp2k_command="/Users/jclarknicholas/local/cp2k/bin/cp2k.psmp"
    calc.parse("Ni.in")
    calc.project_name="Ni.OT_0"
    calc.working_directory=os.getcwd()
    try:
        calc.run()
    except:
        pass
    finally:
        cmd=["cp",f"{calc.project_name}-RESTART.wfn","RESTART.wfn"]
        subprocess.run(cmd)
        os.mkdir(calc.project_name)
        cmd=["mv"]+glob.glob(f"{calc.project_name}.*")+glob.glob(f"{calc.project_name}-*")+[f"{calc.project_name}/"]
        subprocess.run(cmd)
        scf=get_scf_df(f"{calc.project_name}/{calc.project_name}.out")
        scf.to_csv("sc.csv",header=True,sep=" ",index=False)
        change_optimizer(scf_df=scf,calculator=calc,tolerance=100)
        del(calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.OT)
        del(calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF._subsections['OT'])
        calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.SMEAR.Method="FERMI_DIRAC"
        calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.Added_mos="500 500"
        calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.MIXING.Method="BROYDEN_MIXING"
        calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.MIXING.Alpha=0.6
        calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.MIXING.Beta=1.0
        calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.MIXING.Nbroyden=15
        calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.Wfn_restart_file_name="RESTART.wfn"

        for i in reversed(range(0,501)):
            calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.SMEAR.Electronic_temperature=500
            calc.project_name=f"Ni.{i}"
            try:
               calc.run()
            except:
                print(f"run with electronic temperature {calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.SMEAR.Electronic_temperature} not converged")
            cmd=["cp",f"{calc.project_name}-RESTART.wfn","RESTART.wfn"]
            subprocess.run(cmd)
            os.mkdir(calc.project_name)
            cmd=["mv"]+glob.glob(f"{calc.project_name}.*")+glob.glob(f"{calc.project_name}-*")+[f"{calc.project_name}/"]
            subprocess.run(cmd)
            scf=get_scf_df(f"{calc.project_name}/{calc.project_name}.out",scf_df=scf)
            scf.to_csv("sc.csv",header=True,sep=" ",index=False)
            break
                    
