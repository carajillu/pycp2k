#!/bin/bash

#SBATCH --job-name=mpi_test
#SBATCH --nodes=10
#SBATCH --output=mpi_test.o
#SBATCH --error=mpi_test.e
##SBATCH --ntasks-per-node=128
#SBATCH --cpus-per-task=1
#SBATCH --time=00:20:00

#SBATCH --account=e05-surfin-mat
#SBATCH --partition=standard
#SBATCH --qos=short  

module load PrgEnv-gnu
module load cray-fftw
module load mkl

CP2K_DIR=/mnt/lustre/a2fs-work4/work/y07/shared/apps/core/cp2k/cp2k-2025.2
source $CP2K_DIR/tools/toolchain/install/setup
export PATH=${CP2K_DIR}/exe/local:$PATH

source /work/e05/shared/pycp2k/anaconda3/bin/activate
conda activate pycp2k
echo $CONDA_PREFIX

python mace_dask.py --input_structure HfO2_supercell.pdb \
	--cp2k_command cp2k.psmp --cp2k_nodes 2 --cp2k_mpi_processes 128 --cp2k_omp_threads 2 \
	--dask_scale 4 \
	--mace_num_threads 256