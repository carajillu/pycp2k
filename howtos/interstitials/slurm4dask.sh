#!/bin/bash

#SBATCH --job-name=tontatta
##SBATCH --output tontatta-%j.o
##SBATCH --error tontatta-%j.e
#SBATCH --ntasks=256
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128
#SBATCH --cpus-per-task=1
#SBATCH --time=00:20:00

#SBATCH --account=e05-surfin-mat
#SBATCH --partition=standard
#SBATCH --qos=short

module load cp2k/cp2k-2024.3

#export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
export OMP_NUM_THREADS=1