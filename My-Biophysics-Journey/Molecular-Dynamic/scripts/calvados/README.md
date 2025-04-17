# CALVADOS Bench Model

This script tend to streamline the model process for calvados model.

## Simulation Set Up

Under calvados environment, i.e. run `conda activate calvados`, run the script:
````bash
bash bench_model.sh <chain_number> <initial_tempreature>
````

A directory entitled "<initial_temperature>" will be established, where contains all simulation scripts you need (same temperature, different chain number, ranging from <chain_number> to <chain_number> + 10). 

## Run Simulation in Cluster

````bash
bash calvados_bench_submit.sh <initial_temperature>
````

## Self Define

Under `./demo/input`, you can replace your sequence information into `fastalib.fasta` and meanwhile revise the protein name, `<name>` , in the first line correspondingly. Also, force field parameters can be revised in `residues_CALVADOS2.csv`.

The python scripts can be executed as following:

````bash
 python prepare.py --name <name> --replica <replica number> --box <x> <y> <z> --temp <temperature> --time <time>
 # The unit of time is nanoseconds
````

