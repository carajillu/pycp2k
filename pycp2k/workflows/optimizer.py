from pycp2k import CP2K

import pandas as pd
def get_scf_df(outfile=None,scf_df=None):
    step=[]
    update_method=[]
    time=[]
    convergence=[]
    total_energy=[]
    change=[]
    midlines=["\n", 
              "  ------------------------------------------------------------------------------\n",
              "  Step     Update method      Time    Convergence         Total energy    Change\n"]
    
    parsing=False
    with open(outfile, "r") as f:
        for line in f:
            if "SCF WAVEFUNCTION OPTIMIZATION" in line or "outer SCF iter" in line:
                parsing=True
                continue
            if ("SCF run converged" in line) or ("Leaving inner SCF loop" in line) or ("outer SCF loop converged" in line):
                parsing=False
                continue
            if parsing:
                print(line)
                if line in midlines:
                    continue
                line=line.split()
                step.append(int(line[0]))
                update_method.append(line[1])
                time.append(float(line[-4]))
                convergence.append(float(line[-3]))
                total_energy.append(float(line[-2]))
                change.append(float(line[-1]))
    
    df=pd.DataFrame()
    df['step']=step
    df['update_method']=update_method
    df['time']=time
    df['convergence']=convergence
    df['total_energy']=total_energy
    df['change']=change

    if scf_df is not None:
        return pd.concat([scf_df,df])
    else:
        return df
    
def change_optimizer(scf_df: pd.DataFrame, calculator: CP2K):
    if scf_df.convergence.iloc[-1] <= float(calculator.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.Eps_scf):
        print(f"This run seems already converged to {scf_df.convergence.iloc[-1]}. Returning same calculator.")
        return calculator
    calculator.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.Scf_guess = "RESTART"
    
    #Get the average of the difference in convergence values between consecutive steps over the first 5 steps, then same over last 5 steps
    avg_change_first = scf_df.convergence.iloc[:5].diff().mean()
    avg_change_last = scf_df.convergence.iloc[-5:].diff().mean()
    print(f"Average fluctuation in convergence between consecutive steps\n \
            over first 5 steps: {avg_change_first}\n \
            over last 5 steps: {avg_change_last}")
    return calculator

    