<font face='Times'>

# NAMD Procedure-CDK7 System as Example
## Stsetm description
Cyclin-dependent kinase 7 (CDK7), along with cyclin H and MAT1, comprises the CDK-activating kinase (CAK)[1] CAK plays role in both phosphorylate C-terminal of some member in CDK-family such as CDK-1,2,3,4 and generate transcription as a compnent of TFⅡH(transalation factor).Also CAK phosphorylate.
As reported in past aticles,there are few phosphorylation site in CAK complex:
+ Ser164  in CDK7:  to promote the combination of CDK7 and Cyclin H
+ Ther170 in CDK7:  which is phosphorylated by PKC $\iota$(downstream messeager of PI3K),this phosphorytion incerease the substract specifity
+ THR315 and Ser 304 in CyclinH,which have small impact to the system when running MD
THZ1 is a covalent represser of CAK complex,which block the pocket so that CAK unable to perform phosphorylation function. And the cell cycle may stop in G2/M check point 
## Modeling with VMD
### Download PBD file
First download pdb file form https://www.rcsb.org/  with pdbID:6XD3.6XD3 includes three piptide CDK7,CyclinH,MAT1 along with the small molecular ligand THZ1.
### Divide the chain
First we need to select the ligand THZ1 than extract the object and save to pdb file or sdf file.Then we need to divide the chain to three part manually in _Pymol_, use command to divide the portein into chains:
```pymol
split_chains
```
After that export each chain and save to three pdb files:CDK7.pdb CycH.pdb and MAT1.pdb. Put three pbd file to the first fold named 'system_build'
Now, we have the baisc files we need to bulid the system
### Generate Small Molecula Force Field
In this setp, we use [CHARMM-GUI](https://www.charmm-gui.org/) to generate small molecular's force field. Login in CHARMM-GUI with e-mail,and enter ' _Ligand Reader & Modeler_' ,upload local file THZ1.pdb or THZ1.sdf,and press 'Upload MOL/MOL2/SDF'. The 2D ligand will be exported to the frame, an dthe 3D messege will be retained meanwhile.
Then we need to check and add protonation manually, particularly note atom like Nitrogen. After finish this setp,we can press'Next Step Search ligand' to generate foece field. CHARMM-GUI will search in the existing FF data to splicing and assembly the file. Finally download the result zip file which include lig.rtf, lig.prm etc.



### Use VMD to generate PSF file
In this step, we need to use _VMD_ command and _psfgen_ to generate the psf file. _VMD_ support Tcl language to run scripts. In this case, we need to assemble three piptide and THZ1 ligand together. Following scripts can meet this requirments:
#### Revalent Topology File 
Firstly, import topology file we need and import _psfgen_.File _top_all36_prot.rtf_ contains chemical bonding information.Topology file _par_all36m_prot.prm_ contains parameters to model the protein like Amina Acids FF etc. And file _toppar_all36_prot_na_combined.str_ contains FF information which we will use in following phosphorylation operation.Follows are the script:
```Tcl
# File: bpti_example.tcl
# Requirements: topology file top_all22_prot.inp in directory toppar
# PDB file 6PTI.pdb in current directory
# Create working directory; remove old output files

package require psfgen

# Read topology file
topology top_all36_prot.rtf
topology toppar_all36_prot_na_combined.str
topology par_all36_na.prm
topology par_all36m_prot.prm
topology top_all36_na.rtf
topology toppar_all36_prot_fluoro_alkanes.str
topology top_all36_cgenff.rtf
topology thz1.rtf
```

#### Rename The Residues
To ensure the resigue name in pdb file and topology file consistent, we should change residue name.
```Tcl
#rename the residues
pdbalias residue HIS HSE
pdbalias atom ILE CD1 CD
```

#### Create Segment to assemble the system
Command `segment` is used to create a set, in _psfgen User's Guide_ discribes as follows:
+ segment [segids] [resids] [residue] [first] [last] \<segment ID> [resid] [atom name] { \<commands>}
  + Purpose: Build a segment of the molecule. A segment is typically a single chain of protein or DNA,with default patches applied to the termini. Segments may also contain pure solvent or lipid. Options[segids] [resids] [residue] [first] [last] are used to query information about the specified segment.
  
Command First and Last discribes as follows:
+ first \<patch name>
  + Purpose: Override default patch applied to first residue in segment. Default is read from topology file and may be residue-specific.
  + Arguments: <patch name>: Single-target patch residue name or none.
  + Context: Anywhere within segment, does not affect later segments.
+ last \<patch name>
  + Purpose: Override default patch applied to last residue in segment. Default is read from topology
    file and may be residue-specific.
  + Arguments: <patch name>: Single-target patch residue name or none.
  + Context: Anywhere within segment, does not affect later segments.
script as follows:
```Tcl
# Build protein segment
segment THZ1 {
    pdb ligandrm.pdb
}
segment  CDK7 {
    pdb CDK7.pdb
    first ACE 
    last CT3

}
segment MAT1 {
    pdb MAT1.pdb
    first ACE
    last CT3
}
segment CycH {
    pdb CycH.pdb    
    first ACE
    last CT3
}
```
#### Apply phosphorylation with _patch_
In _psfgen_ we can use `patch` or `mutate` command to modify residues etc. In _psfgen User's Guide_ discribes as follows:
+ patch [list] \<patch residue name> \<segid:resid> [...]
    + Purpose: Apply a patch to one or more residues. Patches make small modifications to the structure
    of residues such as converting one to a terminus, changing the protonation state, or creating disulphide bonds between a pair of residues.
    + Arguments: list: Lists all patches applied explicitey using the command ’patch’.
    + listall: Lists all currently applied patches including default patches.
    \<patch residue name>: Name of patch residue from topology definition file.
    \<segid:resid>: List of segment and residue pairs to which patch should be applied.
    + Context: After one or more segments have been built.
+ mutate \<resid> \<resname>
  + Purpose: Change the type of a single residue in the current segment.
  + Arguments: \<resid>: Unique name for residue, 1–5 characters, usually numeric. \<resname>: New

In this case, to judge whether use `mutate` or `patch`,we can open topology file  _toppar_all36_prot_na_combined.str_ , if labled`RESI`,we should use command `mutate`;if label`PRES`
,we use command`patch`,code as follows:
```Tcl
segment  CDK7 {
    pdb CDK7.pdb
    first ACE 
    last CT3
    # mutate 164 SEP
}
patch THPB CDK7:170
patch SP2 CDK7:164
```
#### Subswquent Operation
After the model be established, few operation like import coordination,add water,add ion etc. should be down, code as follows:
```Tcl
writepdb complex.pdb
writepsf complex.psf

package require solvate
package require autoionize
# ionize complex
mol delete all
mol load psf complex.psf pdb complex.pdb
solvate complex.psf complex.pdb -t 12 -o solvated_complex

mol delete all
autoionize -psf solvated_complex.psf -pdb solvated_complex.pdb -sc 0.15 -o system

file delete solvated_complex.pdb 
file delete solvated_complex.psf
file delete solvated_complex.log
file delete complex.pdb
file delete complex.psf

mv system.pdb ../common
mv system.psf ../common

cd ../common
#vmd -dispdev text -e measure.tcl -args system
#vmd -dispdev text -e fix_backbone_restrain_ca_with_ligand.tcl
```

#### Complete Script
```Tcl
# File: bpti_example.tcl
# Requirements: topology file top_all22_prot.inp in directory toppar
# PDB file 6PTI.pdb in current directory
# Create working directory; remove old output files

package require psfgen

# Read topology file
topology top_all36_prot.rtf
topology toppar_all36_prot_na_combined.str
topology par_all36_na.prm
topology par_all36m_prot.prm
topology top_all36_na.rtf
topology toppar_all36_prot_fluoro_alkanes.str
topology top_all36_cgenff.rtf
topology thz1.rtf

#rename the residues
pdbalias residue HIS HSE
pdbalias atom ILE CD1 CD

# Build protein segment
segment THZ1 {
    pdb ligandrm.pdb
}

segment  CDK7 {
    pdb CDK7.pdb
    first ACE 
    last CT3
    # mutate 164 SEP
}

#patch THPB CDK7:170
#patch SP2 CDK7:164

segment MAT1 {
    pdb MAT1.pdb
    first ACE
    last CT3
}

segment CycH {
    pdb CycH.pdb    
    first ACE
    last CT3
}

#check coordinates
coordpdb ligandrm.pdb THZ1
coordpdb CDK7.pdb CDK7
coordpdb MAT1.pdb MAT1
coordpdb CycH.pdb CycH

#Phosphorylation patch

# Guess missing coordinates
guesscoord

writepdb complex.pdb
writepsf complex.psf

package require solvate
package require autoionize
# ionize complex
mol delete all
mol load psf complex.psf pdb complex.pdb
solvate complex.psf complex.pdb -t 12 -o solvated_complex

mol delete all
autoionize -psf solvated_complex.psf -pdb solvated_complex.pdb -sc 0.15 -o system

file delete solvated_complex.pdb 
file delete solvated_complex.psf
file delete solvated_complex.log
file delete complex.pdb
file delete complex.psf

mv system.pdb ../common
mv system.psf ../common

cd ../common
#vmd -dispdev text -e measure.tcl -args system
#vmd -dispdev text -e fix_backbone_restrain_ca_with_ligand.tcl

exit
```
### Manually patch bond occurs in phosphorylation
Once we apply phosphorylation like `patch SP2 CDK7:164` to the system, there may be new bonds that occues in pdb or psf files(like -OH related 'C-O'bonds). For instance, in this example we meet this ERROR twice,one in Ser164,one in Thr170 
```shell
FATAL ERROR: UNABLE TO FIND BOND PARAMETERS FOR CT1 ON2 (ATOMS 2628 2626)
``` 
To patch this paarameter, we should add corresponding parameters to the .prm file.
Firstly, we should open .pdb file and check which kind of AA this bond belong to.
SeconDly, we open .rtf file and find corresponding AA, and further find the corresponding atom type and bond.In CDK7 case, related AA is Thr, in _par_all36m_prot.rtf_ we can see:
```
RESI THR          0.00
GROUP   
ATOM N    NH1    -0.47  !     |  
ATOM HN   H       0.31  !  HN-N  
ATOM CA   CT1     0.07  !     |     OG1--HG1
ATOM HA   HB1     0.09  !     |    /
GROUP                   !  HA-CA--CB-HB  
ATOM CB   CT1     0.14  !     |    \     
ATOM HB   HA1     0.09  !     |     CG2--HG21
ATOM OG1  OH1    -0.66  !   O=C    / \    
ATOM HG1  H       0.43  !     | HG21 HG22 
GROUP                 
ATOM CG2  CT3    -0.27
ATOM HG21 HA3     0.09
ATOM HG22 HA3     0.09
ATOM HG23 HA3     0.09
GROUP   
ATOM C    C       0.51
ATOM O    O      -0.51
..
```
Follow the ERROR we can find out CT1 ON2 (ATOMS 2628 2626) corresponding for CT1 and OH1. After comfirm the atom type, we can open a new terminal and enter the dictory _common/toppar_, use follow command to mate corresponding bond parameters:
```shell
grep -a CT1 par_all36m_prot.prm | grep OH1
``` 
We get related paramters:
```
OH1  CT1   428.000     1.4200 ! ALLOW   ALI ALC ARO
CT1  CD   OH1   55.000    110.50              ! From ASPP CT2-CD-OH1
CT1  CD   ON2   55.000    110.50              ! From ASPP CT2-CD-OH1
H    OH1  CT1    57.500   106.0000 ! ALLOW   ALC ARO ALI
OH1  CT1  CT1    75.700   110.1000 ! ALLOW   ALI ALC ARO
OH1  CT1  CT3    75.700   110.1000 ! ALLOW   ALI ALC ARO
OH1  CT1  HA1    45.900   108.8900 ! ALLOW   ALI ALC ARO
OH1  CT2  CT1    75.700   110.1000 ! ALLOW   ALI ALC ARO
...
```
Then,open _par_all36m_prot.prm_, search parameter`OH1  CT1   428.000     1.4200 ! ALLOW   ALI ALC ARO`,we can locate where the parameter belong.Finally, we copy this line and rename atom type to which ERROR hints,like`ON2  CT1   428.000     1.4200 ! ALLOW   ALI ALC ARO`. 
Revise all type off parameters and submit the task to cluster again.

## Run NAMD3 in Cluster 
### Profile(.conf)
#### Equliization 
There are three steps to run equlization:First run Energy Minization(pro-lig-min) ,then run Pressure qeulization(pro-lig-preequli),finally run Equlization(pro-lig-equli). The main concern to set three step is to equilize the sysytm gradually, in other words, we first use the NPT ensemble and then use the NVT ensemble.
#### Prod.conf
Run MD and output the .log file and the .dcd file. 
### Script for submitting tasks
In ZJU-iqb 28 cluster, we use _slurm_ to submit tasks. 
### Some Normal Error
+ ERROR:Atoms moving too fast at timestep 16: simulation has become unstable (2 atoms on pe 0)
    + Cause:    Some atom's velocity exceed the limtitation
    + Solution: Open the config file pro-lig-preequil and find the following fragment:
    ```shell
    # RESPA PROPAGATOR
    # timestep                1.0
    timestep                  0.5
    useSettle                 on
    fullElectFrequency        2
    nonbondedFreq             1
    ```
    Reduce _timestep_ to a proper amount(like change from 2 to 0.5)
+ ERROR: CUDA CURAND error curandGenerateNormal(gen，gaussrand_x，n，0，1) in file src/SequencerCUDAKernel.cu，functionlangevinVelocitiesBBK2, line 4263
    + Solution: Check whether all name in config file and fix_backbone_restrain_ca_with_ligand.tcl script mathched. One another possibility is the parameters in config file need to be corrected.
+ ERROR: UNABLE TO FIND BOND PARAMETERS FOR CT1 ON2 (ATOMS 2628 2626)
    + Solution: The revalent solution has been mentioned above.
### ZJU-iqb-28 cluster
```
username:shizq
password:***********
```

## Result Visualization and RMSD Caculation
### Pymol Visulization
To display the result more visually, we can use pymol to show the dymanic process of MD results. First, we should import .pdb file to Pymol, and then import the corresponding .dcd file. And now, we can see the dymanic process and further to generate a short animation. But the system still has ions and water, we can use the following command to remove ions and water:
```py
#select ions and create object
select ions, all and ((resn SOD) or (resn CLA))
#remove and delele object
remove ion; delete ions
#delete water
remove solvent
#one command contains all operation
select ions, all and ((resn SOD) or (resn CLA)); remove ions; delete ions; remove solvent
```
After this operation, the system only remains protein and ligands.

### RMSD caculation
We can caculation RMSD using the VMD script(_vis_traj.tcl_), attention,in the usual case, replace the 'THZ1' to 'LIG'.
```Tcl
# vmd
# source ../../vis_traj.tcl 
# under prod

# load psf and dcd file
mol new system.psf type psf
# mol addfile rdrp-remtp-equil.dcd type dcd waitfor all
mol addfile pro-lig-equil.dcd type dcd waitfor all

display projection   Orthographic
# display axes off
color Display {Background} white
label textthickness 2.5
set numframes [molinfo top get numframes]
# set sel [atomselect top "not water and not resname SOD and not resname CLA"]
# $sel writepdb rdrp-remtp-preequil.pdb

# make representation
mol delrep 0 top
mol representation NewCartoon 0.300000 10.000000 4.100000 0
# mol color Structure
# mol color Beta
# mol material AOShiny
mol color ColorID 8
mol material Transparent
mol selection {protein or nucleic and not (segname RN1 and resid 20) and not (segname RN2 and (resid 10 or resid 11))}
# mol material Transparent
mol addrep top
# add rep after setting up

mol representation Licorice 0.300000 12.000000 12.000000
mol color Type
mol selection {resname THZ1}
mol material Opaque
mol addrep top

mol representation Licorice 0.300000 12.000000 12.000000
mol color Type
mol selection {(segname RN1 and resid 20) or (segname RN2 and (resid 10 or resid 11))}
mol material Opaque
mol addrep top

mol representation VDW 1.000000 12.000000
mol color Type
mol selection {resname MG or segname ZN}
mol material Opaque
mol addrep top

mol representation CPK 0.200000
mol color Type
mol selection {protein and noh and (same residue as within 5 of residue THZ1) or (same residue as within 5 of segname MG)}
mol material Opaque
mol addrep top
# update selection every frame
mol selupdate 3 top 1
mol colupdate 3 top 0

mol representation CPK 0.200000
mol color Type
mol selection {protein and noh and (same residue as within 5 of segname ZN)}
mol material Opaque
mol addrep top
# update selection every frame
mol selupdate 4 top 1
mol colupdate 4 top 0

# mol representation Surf 1.400000 0.000000
# mol color Type
# mol selection {protein and noh and (same residue as within 6 of residue LIG)}
# mol material Opaque
# mol addrep top

# mol representation Licorice 0.300000 12.000000 12.000000
# mol color Type
# mol selection {nucleic}
# mol material Opaque
# mol addrep top

# mol representation 1.000000
# mol color Type
# mol selection {water}
# mol material Opaque
# mol addrep top

# fragment: time-consuming!
# pbc wrap -centersel "protein or nucleic or resname LIG or segname MG or segname ZN" -compound segid -center com -all
# pbc wrap -centersel "protein or nucleic or resname LIG or segname MG or segname ZN" -compound chain -center com -all
# pbc join res -ref "name CA"

# align the protein
package require rmsdtt
# open the window
set w [rmsdtt_tk_cb]
$w.top.left.sel delete 1.0 end
$w.top.left.sel insert end "protein"
# set the states of checkboxes1
set rmsdtt::trace_only 0
set rmsdtt::noh 0
set rmsdtt::bb_only 1
# rmsdtt::set_sel  # verify selection
rmsdtt::doAlign

# change selection text
$w.top.left.sel delete 1.0 end
$w.top.left.sel insert end "resname THZ1"
set rmsdtt::bb_only 0
# set rmsdtt::xmgrace 1
# set rmsdtt::multiplot 0
set rmsdtt::plot_sw 1
set rmsdtt::save_sw 1
set rmsdtt::save_file sys-rmsd.dat
rmsdtt::doRmsd

set numframes [molinfo top get numframes]
# move to center. maybe execute again after aligning the protein...
set lig [atomselect top "segname RN1 and resid 20 or segname RN2 and (resid 11 or resid 10) or resname THZ1" frame [expr $numframes-1]]
# set lig [atomselect top "segname RN1 and resid 20 or segname RN2 and (resid 11or resid 10) or resname THZ1" frame 0]
set cen [measure center $lig weight mass]
foreach {x y z} $cen { break }
molinfo top set center_matrix "{{1 0 0 [expr -$x]} {0 1 0 [expr -$y]} {0 0 1 [expr -$z]} {0 0 0 1}}"
# use negative...

# animate write dcd rdrp-remtp-prod-firstpart.dcd beg 0 end 350

# set sel [atomselect top all frame [expr $numframes - 1]]
# $sel writepdb last.pdb

# set cartoon_transparency, 0.6
# bg_color white

# output for vmd
# set sele "segname PR1 and ("
# set sel [atomselect top "protein and name CA and (same residue as within 10 of (resname THZ1))"]
# foreach resid [$sel get resid] {
#     append sele  "residue $resid or "
# }
# puts $sele

# output for gmx
set sele "r"
set sel [atomselect top "protein and name CA and (same residue as within 10 of (resname THZ1))"]
foreach resid [$sel get resid] {
    append sele  "$resid or "
}
puts $sele

# # http://github.com/anjibabuIITK/CLUSTER-ANALYSIS-USING-VMD-TCL
set number 9
set rcutoff 1
set step_size 1
set nframes [molinfo top get numframes]
set inf 0
set nf $nframes
set totframes [expr $nf - 1 ]
set selA [atomselect top "resname THZ1"]
set lists [measure cluster $selA num $number cutoff $rcutoff first $inf last $totframes step $step_size distfunc rmsd weight mass]

set file [open "clus_result.dat" w]
for {set i 1} {$i <= [llength $lists]} {incr i} {
    set lst [lindex $lists [expr $i-1]]
    puts $file [format "cluster %d: %d" $i [llength $lst]]
    puts $file $lst
    puts $file ""
}
close $file

set c01 [lindex [lindex $lists 0] 0]
set sel [atomselect top all frame $c01]
set real_frame [expr $c01+1]
$sel writepdb c01_${real_frame}.pdb
puts [format "write the centroid of 1st cluster: frame %d" $real_frame]

set c02 [lindex [lindex $lists 1] 0]
set sel [atomselect top all frame $c02]
set real_frame [expr $c02+1]
$sel writepdb c02_${real_frame}.pdb
puts [format "write the centroid of 2nd cluster: frame %d" $real_frame]

# package require rmsdtt
# set w [rmsdtt_tk_cb]
# $w.top.left.sel delete 1.0 end
# $w.top.left.sel insert end "chain A and (resid 545 or resid 547 or resid 553 or resid 555 or resid 556 or resid 557 or resid 558 or resid 618 or resid 619 or 
# resid 621 or resid 622 or resid 623 or resid 624 or resid 680 or resid 681 or resid 682 or resid 683 or resid 684 or resid 688 or resid 691 or resid 758 or resid 759 or 
# resid 760 or resid 761 or resid 798 or resid 811 or resid 812 or resid 813 or resid 814)"
# set rmsdtt::trace_only 0
# set rmsdtt::noh 0
# set rmsdtt::bb_only 1
# rmsdtt::doAlign

# package require vmdmovie
# MovieMaker::moviemaker
# # install netpbm
# # set MovieMaker::presmooth 1
# set MovieMaker::prescale 1
# set MovieMaker::movieformat imgif
# set MovieMaker::framerate 30
# set MovieMaker::workdir ./
# set MovieMaker::basename ${path}
# set MovieMaker::trjstep 20
# set MovieMaker::renderer libtachyon
# set MovieMaker::movietype trajectory
# # you should click on the trjstep. this window doesn't really recognize what we write there...
# MovieMaker::buildmovie


```
## References:
[1] psfgen User's Guide 
[2] VMD User's Guide



