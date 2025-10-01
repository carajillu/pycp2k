from dask_jobqueue import SLURMCluster
from dask.distributed import Client, wait

def parse_slurm_config(config_file):
    """ 
    Parse a SLURM job script and extract:
    - SLURM parameters as key-value pairs (e.g. "--mem": "8G")
    - Job script prologue lines (non-comment shell commands)
    """ 
    config = {"slurm": {}, "prologue": []}
            
    with open(config_file, 'r') as f:
        for line in f:
            if line.startswith("#!"):
                # Skip shebang line
                continue
            if line.startswith("#SBATCH"):
                line=line.split()[1]
                if "=" in line:
                    key, value = line.split("=")[0].strip("--"), line.split("=")[1]
                else:
                    key = line.split("=")[0]
                    value = True
                config["slurm"][key] = value
            else:
                config["prologue"].append(line.strip())
    return config

    
def create_slurm_cluster(njobs:int, slurm_config:str):
    config = parse_slurm_config(slurm_config)
    job_extra_directives=[]
    for key,value in config["slurm"].items():
        job_extra_directives.append(f"--{key}={value}")
    cluster = SLURMCluster(cores=1,
                           memory="512GB",
                           job_directives_skip=["--mem"], #don't supply anything directly, get everything from the config file 
                           job_extra_directives=job_extra_directives,
                           job_script_prologue=config["prologue"])
    with open("cluster_script.o","w") as f:
        f.write(cluster.job_script())
            
    cluster.scale(jobs=njobs) # Launch one job per system
    return cluster