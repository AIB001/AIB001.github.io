#usage: python prepare.py --name <name> --replica <replica number> --box <x> <y> <z>
#e.g. python prepare.py --name FUS_1_163 --replica 1 --box 25.0 25.0 25.0
# python FUS_1_163_1/run.py --path FUS_1_163_1
import os
from calvados.cfg import Config, Job, Components
import subprocess
import numpy as np
from argparse import ArgumentParser
from Bio import SeqIO

parser = ArgumentParser()
parser.add_argument('--name',nargs='?',required=True,type=str)
parser.add_argument('--replica',nargs='?',required=True,type=int)
parser.add_argument('--box', nargs=3, type=float, default=[15, 15, 150], help='Box size in x, y, z dimensions')
parser.add_argument('--temp', nargs='?', type=int, default=300, help='Set Simulation temperature')
parser.add_argument('--time', nargs='?', type=int, default=2000, help='Set Simulation time (ns)')
args = parser.parse_args()

cwd = os.getcwd()
N_save = int(5e4)

sysname = f'{args.name:s}_{args.replica:d}'
replica_number = args.replica
x, y, z = args.box
t = args.temp
time = 2 * args.time



config = Config(
  # GENERAL
  sysname = sysname, # name of simulation system
  box = [x, y, z], # nm
  temp = t,
  ionic = 0.1, # molar
  pH = 7.5,
  topol = 'slab',

  # RUNTIME SETTINGS
  wfreq = N_save, # dcd writing frequency, 1 = 10fs
  steps = time*N_save, # number of simulation steps
  runtime = 0, # overwrites 'steps' keyword if > 0
  platform = 'CUDA', # 'CUDA'
  restart = 'checkpoint',
  frestart = 'restart.chk',
  verbose = True,
  slab_eq = True,
  steps_eq = 100*N_save,
)

# PATH
path = f'{cwd}/{sysname}'
print(path)
subprocess.run(f'mkdir -p {path}',shell=True)
subprocess.run(f'mkdir -p data',shell=True)

analyses = f"""

from calvados.analysis import calc_slab_profiles

calc_slab_profiles(path="{path:s}",name="{sysname:s}",output_folder="data",ref_atoms="all",start=0)
"""

config.write(path,name='config.yaml',analyses=analyses)

components = Components(
  # Defaults
  molecule_type = 'protein',
  nmol = 1, # number of molecules
  restraint = False, # apply restraints
  charge_termini = 'both', # charge N or C or both or none
  
  # INPUT
  ffasta = f'{cwd}/input/fastalib.fasta', # input fasta file
  fresidues = f'{cwd}/input/residues_CALVADOS2.csv', # residue definitions
)

components.add(name=args.name, nmol=replica_number)

components.write(path,name='components.yaml')

