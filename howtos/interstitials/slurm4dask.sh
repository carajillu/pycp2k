#!/bin/bash
#SBATCH --job-name=main_dask
#SBATCH --output=echo_%j.o
#SBATCH --error=echo_%j.e
#SBATCH --time=0-23:59:59
#SBATCH --mem=32G
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --hint=nomultithread
#SBATCH --nodes=1
#SBATCH --partition=cpu
#SBATCH --qos=normal
#SBATCH --chdir=./ 

module purge
module load conda/25.3-python-3.12
conda activate /home/users/jclarknicolas/nvproj005/software/conda-envs/pycp2k-env 
module load scalapack/2.2.2
module load intel/mkl/2025.1
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/shared/nvproj005/software/cp2k-master/lib/ # libcp2k.so
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/shared/nvproj005/software/conda-envs/cp2k-master/lib # libdbcsr.so