#!/bin/bash
#SBATCH --job-name=single_exp
#SBATCH --output=single_exp.txt
#SBATCH -p gpu
#SBATCH --gres gpu:v100:1
#SBATCH -n 1

module load Anaconda3
source ../envs/bin/activate
which python 
module load CUDA
python mlg.py

