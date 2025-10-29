#!/bin/bash

#SBATCH --job-name=mpi_test
#SBATCH --nodes=1
#SBATCH --output=mpi_test.o
#SBATCH --error=mpi_test.e
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00

#SBATCH --account=e05-surfin-mat
#SBATCH --partition=standard
#SBATCH --qos=standard

module load PrgEnv-gnu
module load cray-fftw
module load mkl

CP2K_DIR=/mnt/lustre/a2fs-work4/work/y07/shared/apps/core/cp2k/cp2k-2025.2
source $CP2K_DIR/tools/toolchain/install/setup
export PATH=${CP2K_DIR}/exe/local:$PATH

source /work/e05/shared/pycp2k/anaconda3/bin/activate
conda activate pycp2k
echo $CONDA_PREFIX

python mace_dask.py --cp2k_command cp2k.psmp --input_structure HfO2_supercell.pdb --slurm_config dask_cfg.sh --cp2k_mpi_processes 256
