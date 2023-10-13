# <font face='Times'>

# Molecular Dynamic with GROMACS
---
## About Files in GROMACS

## Protocol of GROMACS
### Normal Protein MD
The tutorial gives Lysozyme as an example. First download the pdb file(PDB ID: 1AKI) from https://www.rcsb.org/:
```shell
wget http://www.rcsb.org/pdb/files/1AKI.pdb
```
Delete water:
```shell
grep -v HOH 1AKI.pdb > 1AKI_clean.pdb
```
#### Use pdb2gmx generate topological files
pdb2gmx is a tool to generate topological files GROMACS needs. In version 5.x, pbd2gmx is sub-unit of `gmx` command.
pdb2gmx will generate 3 files: 

1. Topology file for the molecule.(.top)
2. Position-restrained file.(.itp)
3. Preprocessed structure file.(.gro)

```shell
gmx pdb2gmx -f 1AKI_clean.pdb -o 1AKI_processed.gro -water spce
```
Parameters:
`-f`:Input file
`-ff`: Choose type of Force-Field, if don't choose ff type in command, gmx will list the ff type and will choose ff tyoe with index gmx provide, like below:
```shell
Select the Force Field:
From current directory:
 1: CHARMM36 all-atom force field (July 2017)
From '/usr/local/gromacs/share/gromacs/top':
 2: AMBER03 protein, nucleic AMBER94 (Duan et al., J. Comp. Chem. 24, 1999-2012, 2003)
 3: AMBER94 force field (Cornell et al., JACS 117, 5179-5197, 1995)
 4: AMBER96 protein, nucleic AMBER94 (Kollman et al., Acc. Chem. Res. 29, 461-469, 1996)
 5: AMBER99 protein, nucleic AMBER94 (Wang et al., J. Comp. Chem. 21, 1049-1074, 2000)
 6: AMBER99SB protein, nucleic AMBER94 (Hornak et al., Proteins 65, 712-725, 2006)
 7: AMBER99SB-ILDN protein, nucleic AMBER94 (Lindorff-Larsen et al., Proteins 78, 1950-58, 2010)
 8: AMBERGS force field (Garcia & Sanbonmatsu, PNAS 99, 2782-2787, 2002)
 9: CHARMM27 all-atom force field (CHARM22 plus CMAP for proteins)
10: GROMOS96 43a1 force field
11: GROMOS96 43a2 force field (improved alkane dihedrals)
12: GROMOS96 45a3 force field (Schuler JCC 2001 22 1205)
13: GROMOS96 53a5 force field (JCC 2004 vol 25 pag 1656)
14: GROMOS96 53a6 force field (JCC 2004 vol 25 pag 1656)
15: GROMOS96 54a7 force field (Eur. Biophys. J. (2011), 40,, 843-856, DOI: 10.1007/s00249-011-0700-9)
16: OPLS-AA/L all-atom force field (2001 aminoacid dihedrals)
```
`-water`:Choose the type of water model
`-o`:Point the output file
`-ignh`:Ignore hydrogen atoms

#### Defining Crystal Cells & Adding Solvents
##### Use `editconf` to define the box
```shell
gmx editconf -f 1AKI_processed.gro -o 1AKI_newbox.gro -c -d 1.0 -bt cubic
```
Parameters: 
`-c`:Put the protein in the center of the box
`-bt`:Define the shape of Simulation box, `cubic` defines the cubic shape, `dodecahedron`defines the dodecahedron box
`-d`:Defines the edge of the box. Extend 1.0 nm at the maximum value in the coordinate direction
##### Add solvent with `solvate`
```shell
gmx solvate -cp 1AKI_newbox.gro -cs spc216.gro -o 1AKI_solv.gro -p topol.top
```
#### Add Ions with `genion`
To add ions into he system, we should first generate .tpr topology file with `grompp`. `grompp` uses .gro file and .top file ti generate topology file in atomic level. In this step, we need ions.mdp file. mdp file is like the profile(.conf) in NAMD. 
```shell
gmx grompp -f ions.mdp -c 1AKI_solv.gro -p topol.top -o ions.tpr
``` 
Then pass the trp file to `genion` and generate the ions.
```shell
gmx genion -s ions.tpr -o 1AKI_solv_ions.gro -p topol.top -pname NA -nname CL -neutral
```
#### Run Energe-minimization, NVT and NPT
##### Energe Minimization
Generate em.trp:
```shell
gmx grompp -f minim.mdp -c 1AKI_solv_ions.gro -p topol.top -o em.tpr
```
Run MD:
```shell
gmx mdrun -v -deffnm em
```
Parameters:
`-v`:Print out every steps to the screen
`-deffnm`；Defines the output file name
##### NVT
```shell
gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr 
gmx mdrun -deffnm nvt
```
##### NPT
```shell
gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr 
gmx mdrun -deffnm npt
```
#### Run Product
```shell
gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr
gmx mdrun -deffnm md_0_1
```

### Protein-Ligand 


## .MDP File and Adjusting Parameters 
