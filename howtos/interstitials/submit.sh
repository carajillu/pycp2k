#!/bin/bash

#SBATCH --job-name=$JOB_NAME
##SBATCH --output $JOB_NAME.%j.o
##SBATCH --error $JOB_NAME.%j.e
#SBATCH --ntasks=256
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128
#SBATCH --cpus-per-task=1
#SBATCH --time=00:20:00

#SBATCH --account=e05-surfin-mat
#SBATCH --partition=standard
#SBATCH --qos=short

#module load cp2k/cp2k-2024.3
module load PrgEnv-gnu
module load cray-fftw
module load mkl

CP2K_DIR=/mnt/lustre/a2fs-work4/work/y07/shared/apps/core/cp2k/cp2k-2025.2
source $CP2K_DIR/tools/toolchain/install/setup
export PATH=${CP2K_DIR}/exe/local:$PATH

#export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
export OMP_NUM_THREADS=1
export MPLCONFIGDIR=/work/e05/shared/
(base) jclarknicolas_e05@ln03:/work/e05/shared/pycp2k/pycp2k/howtos/interstitials> cat submit.sh 
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

export MPLCONFIGDIR=/work/e05/shared/

module load cp2k/cp2k-2024.3

export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
export OMP_NUM_THREADS=1
source /work/e05/shared/pycp2k/anaconda3/bin/activate
conda activate pycp2k
echo $CONDA_PREFIX
export CP2K_MPI_PROCESSES=256

#python dask_submit.py --cp2k_command cp2k.psmp --input_structure HfO2_supercell.pdb --nreps 4 --method pbe --slurm_config slurm4dask.sh --output interstititals.xyz --cp2k_mpi_proc 256
python mace_dask.py --cp2k_command cp2k.psmp --input_structure HfO2_supercell.pdb --slurm_config dask_cfg.sh