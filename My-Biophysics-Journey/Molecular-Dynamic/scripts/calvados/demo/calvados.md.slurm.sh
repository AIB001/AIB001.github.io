#!/bin/bash
#SBATCH -J XXX_chains_YYY
#SBATCH -p NV4090
#SBATCH --time=168:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=11
#SBATCH --gres=gpu:1
#SBATCH --mem=30G

# For cluster in college of physics

# Decide the software version
#export LD_LIBRARY_PATH=/public/software/lib/:$LD_LIBRARY_PATH
#source /public/software/modules/apps/gromacs/gpu/2024.3-g40
#source /public/software/profile.d/apps_gromacs-intelmpi-2021.5.sh
#source /public/software/modules/compiler/intel/2021.3.0
module add compiler/intel/2021.3.0
module add mpi/openmpi/gnu/4.1.6 compiler/cuda/12.1
module add compiler/gcc/11.5.0
#module add apps/anaconda3/2024.06
#module add apps/anaconda3/2021.05

echo "=== Environment Verification ==="
echo "Python path: $(which python)"
echo "Conda env: $CONDA_DEFAULT_ENV"
echo "Python version: $(python --version)"
echo "================================"

conda init
conda activate calvados 
export PYTHONPATH="/public/home/shizhaoqi/openmm/calvados:$PYTHONPATH"
python prepare.py --replica XXX --name FUS_1_163 --temp YYY --time 500
python FUS_1_163_XXX/run.py --path FUS_1_163_XXX



echo "Start time: $(date)"
echo "SLURM_JOB_NODELIST: $SLURM_JOB_NODELIST"
echo "hostname: $(hostname)"
echo "CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES"
echo "Job directory: $(pwd)"
