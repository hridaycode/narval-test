#!/bin/bash

#SBATCH --job-name=graph_summary
#SBATCH --time=00:05:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --output=graph_summary_%j.out

module load python/3.11.5

source ~/venvs/ml/bin/activate

python graph_summary.py