#!/bin/bash
# conda activate numpy

mkdir mol2_re

files=$(ls *.mol2)
for file in $files; do
    # mkdir temp
    filename="${file%.*}"
    # mv temp $filename
    echo $filename '2333333333'
    obabel -imol2 "${filename}.mol2" -opdb -O "${filename}.pdb" -h
    mv "${filename}.pdb" mol2_re
    cd mol2_re
    python ../addatomnameindex.py "${filename}" "/mnt/c/Users/Apple/Desktop/addatomname"
    obabel -ipdb "${filename}_re.pdb" -omol2 -O "${filename}.mol2" -h
    echo ${filename} add atom name successfully!
    rm "${filename}.pdb"
    rm "${filename}_re.pdb"
    # rm "${filename}.sdf"
    # cp $file $filename
    # cd $filename
    # python ../my_paramchem.py -u shizq -p szq20020919@zju -c $file
    # echo "ff file of" $filename has generated successfully 
    # python ../strdivid.py "$(pwd)"
    # pdbname="${filename}.pdb"
    # obabel -imol2 $filename.str.mol2 -opdb -O $pdbname
    # vmd -dispdev text -e ../system_build/psfgen.tcl -args $filename
    cd ..
done