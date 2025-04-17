#!/bin/bash

if [ "$#" -ne 1 ]; then 
    echo "Usage: $0 <directory>"
    echo "parameter needed"
    exit 1
fi

input_temp=$1

cd "${input_temp}k" || { echo "Failed to enter directory ${input_temp}k"; exit 1; }

for dir in */; do
    cd "$dir" || { echo "Failed to enter directory $dir"; continue; }

    if [[ -f "calvados.md.slurm.sh" && -x "calvados.md.slurm.sh" ]]; then 
        conda activate calvados
	sbatch calvados.md.slurm.sh
        echo "${dir} has been submitted"
    else
        echo "executable file has not been found in $dir"
    fi

    cd .. || { echo "Failed to go back to parent directory"; exit 1; }
done 

cd .. || { echo "Failed to go back to original directory"; exit 1; }
