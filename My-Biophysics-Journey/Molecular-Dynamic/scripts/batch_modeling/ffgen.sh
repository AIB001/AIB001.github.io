#!/bin/bash
# conda activate numpy

files=$(ls *.mol2)
for file in $files; do
    mkdir temp
    filename="${file%.*}"
    mv temp $filename
    echo $filename '2333333333'
    cp $file $filename
    cd $filename
    # python ../my_paramchem.py -u shizq -p szq20020919@zju -c $file
    python ../my_paramchem.py -u hljiang -p 1998jhl0714! -c $file
    echo "ff file of" $filename has generated successfully 
    python ../strdivid.py "$(pwd)"
    pdbname="${filename}.pdb"
    obabel -imol2 $filename.str.mol2 -opdb -O $pdbname
    vmd -dispdev text -e ../system_build/psfgen.tcl -args $filename
    cd ..
done

# for file in ./*.mol2; do
#     if [[ $file == *".str"* ]]; then
#         new_file="${file/.str/}"
#         mv "$file" "$new_file"
#         echo "已删除 '$file' 中的 '.str'。新文件名为 '$new_file'。"
#     fi
# done

# python strdivid.py "$(pwd)"