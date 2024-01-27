#!/bin/bash
# conda activate numpy

files=$(ls *.mol2)
for file in $files; do
    filename="${file%.*}"
    python residuetype_LP.py "$(pwd)" $filename
    cd $filename
    vmd -dispdev text -e ../system_build/psfgen.tcl -args $filename 
    echo "${filename} has been modeled succeddfully!"
    cd ..
done


# this is for test


# filename="CDI5"
# python residuetype_LP.py "$(pwd)" $filename
# cd $filename
# vmd -dispdev text -e ../system_build/psfgen.tcl -args $filename
# echo "${filename} has been modeled succeddfully!"
# cd ..



# for file in ./*.mol2; do
#     if [[ $file == *".str"* ]]; then
#         new_file="${file/.str/}"
#         mv "$file" "$new_file"
#         echo "已删除 '$file' 中的 '.str'。新文件名为 '$new_file'。"
#     fi
# done

# python strdivid.py "$(pwd)" 
