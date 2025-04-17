#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <链条数> <初始温度>"
    exit 1
fi

chains=$1
initial_temp=$2

mkdir -p "${initial_temp}k"
cd "${initial_temp}k" || exit

for i in {1..10}; do
    current_chains=$((chains + i - 1))
    
    cp -r ../demo "demo_${i}"
    
    cd "demo_${i}" || exit
    sed -i "s/XXX/${current_chains}/g" calvados.md.slurm.sh
    
    if [ "$i" -eq 1 ]; then
        sed -i "s/YYY/${initial_temp}/g" calvados.md.slurm.sh
    else
        sed -i "s/YYY/${initial_temp}/g" calvados.md.slurm.sh
    fi
    
    mv ../demo_${i} "../FUS_1_163_phase_diagram_${current_chains}_${initial_temp}k"
    
    cd ..
done

echo "${initial_temp}k at low density region model has completed"
