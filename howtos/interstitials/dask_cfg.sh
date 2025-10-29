#!/bin/bash

#SBATCH --job-name=dask-worker
#SBATCH --output=dask-%j.o
#SBATCH --error=dask-%j.e
#SBATCH --ntasks=256
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128
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
