#!/bin/bash

#SBATCH --job-name=mpi_test
#SBATCH --nodes=1
#SBATCH --output=mpi_test.o
#SBATCH --error=mpi_test.e
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1
#SBATCH --time=00:20:00

#SBATCH --account=e05-surfin-mat
#SBATCH --partition=standard
#SBATCH --qos=short

module load cp2k/cp2k-2024.3

export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
export OMP_NUM_THREADS=1
source /work/e05/shared/pycp2k/anaconda3/bin/activate
conda activate pycp2k
echo $CONDA_PREFIX

python dask_submit.py --cp2k_command cp2k.psmp --input_structure HfO2_supercell.pdb --nreps 4 --method pbe --slurm_config slurm4dask.sh --output interstititals.xyz --cp2k_mpi_proc 256
#python dask_import.py