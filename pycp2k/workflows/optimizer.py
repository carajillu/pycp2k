from pycp2k import CP2K

import pandas as pd

def get_scf_df(outfile=None,scf_df=None):
    step=[]
    update_method=[]
    time=[]
    convergence=[]
    total_energy=[]
    change=[]
    with open(outfile, "r") as f:
         parse=False
         for line in f:
            if "Step     Update method      Time    Convergence         Total energy    Change" in line:
               parse=True
            elif ("SCF run converged" in line) or ("SCF run NOT converged" in line):
               break
            if parse:
               try:
                  line=line.split()
                  step.append(int(line[0]))
                  update_method.append("_".join(line[1:-4]))
                  time.append(float(line[-4]))
                  convergence.append(float(line[-3]))
                  total_energy.append(float(line[-2]))
                  change.append(float(line[-1]))
               except:
                  pass
    df=pd.DataFrame()
    df['step']=step
    df["total_steps"]=range(1,df.shape[0]+1) # cause scf steps start at 1
    df['update_method']=update_method
    df['time']=time
    df['convergence']=convergence
    df['total_energy']=total_energy
    df['change']=change

    if scf_df is not None:
        return pd.concat([scf_df,df])
    else:
        return df
    
def change_optimizer(scf_df: pd.DataFrame, calculator: CP2K, tolerance: float=100):
    if scf_df.convergence.iloc[-1] <= float(calculator.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.Eps_scf):
        print(f"This run seems already converged to {scf_df.convergence.iloc[-1]}. Returning same calculator.")
        return calculator
    calculator.CP2K_INPUT.FORCE_EVAL_list[0].DFT.SCF.Scf_guess = "RESTART"
    
    #Get the average of the difference in convergence values between consecutive steps over the first 5 steps, then same over last 5 steps
    avg_change_secondlast = abs(scf_df.convergence.iloc[-10:-5].diff().mean())
    avg_change_last = abs(scf_df.convergence.iloc[-5:].diff().mean())
    print(f"Average fluctuation in convergence between consecutive steps\n \
            over second-last 5 steps: {avg_change_secondlast}\n \
            over last 5 steps: {avg_change_last}")
    return calculator

    