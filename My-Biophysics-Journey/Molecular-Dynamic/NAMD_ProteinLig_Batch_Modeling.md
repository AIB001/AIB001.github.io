# Protein-Ligands 批量建模

## 1.预处理文件夹构成

### 1.1 文件夹构成

> + 主文件夹：` addatomname`
>
>   + 第一部分：`pre-mol2 file `
>
>   >`pre-mol2file_1.mol2`
>   >
>   >`pre-mol2file_1.mol2`
>   >
>   >......
>   >
>   >`pre-mol2filen_n.mol2`
>
> + 第二部分：处理脚本
>
>   >`addatomname.py`：利用`rdkit`给转化得到的`.pdb`文件加氢、编号（`Atom name`）
>   >
>   >`addatomname.sh`：调用`openbabel`，先将`pre-mol2file`转化为`.pdb`文件，然后调用`addatomname.py`处理`pdb`文件，最后将编号、加氢后的`pdb`文件转化会`mol2`文件，并输出到`mol2_re`文件夹底下
>
> + `mol2_re`文件夹：用于存放添加原子编号修正后的`mol2`文件，可以直接变成建模的主文件夹，也可以单独移出

### 1.2 `addatomname.sh`

```shell
#!/bin/bash
# conda activate numpy

mkdir mol2_re # if mol2_re doesn't exist

files=$(ls *.mol2)
for file in $files; do
    filename="${file%.*}"
    echo $filename '2333333333'
    obabel -imol2 "${filename}.mol2" -opdb -O "${filename}.pdb" -h
    mv "${filename}.pdb" mol2_re
    cd mol2_re
    python ../addatomnameindex.py "${filename}" "/mnt/c/Users/Apple/Desktop/addatomname" # change to real path
    obabel -ipdb "${filename}_re.pdb" -omol2 -O "${filename}.mol2" -h
    echo ${filename} add atom name successfully!
    rm "${filename}.pdb"
    rm "${filename}_re.pdb"
    cd ..
done
```



## 2. 批量建模文件夹构成

### 2.1 文件夹构成

> + 主文件夹：` Batch_Modeling`
>
>   + 第一部分：`mol2 file `
>
>     >`mol2file_1.mol2`
>     >
>     >`mol2file_1.mol2`
>     >
>     >......
>     >
>     >`mol2filen_n.mol2`
>
>   + 第二部分：处理脚本
>
>     >`my_paracharm.py`：动态网页爬虫，用于从$cgenff$官网获取小分子拓扑-力场参数的`.str`文件
>     >
>     >`strdivid.py`：将获取的`.str`文件分割成`.rtf`拓扑文件和`.prm`力场参数文件（可以不用）
>     >
>     >`check.py`：检查是否正常生成了力场文件
>     >
>     >`residuetype_LP.py`：用于修正生成力场文件中的`Long-Pairs`孤对电子以及修正`RESI UNK`
>     >
>     >`ffgen.sh`：批量获取力场，在同一目录下建立文件夹，在文件夹中保存拓扑-力场参数文件；分割拓扑-力场参数文件
>     >
>     >`vmdmodel.sh`：检查完毕后建模
>
>   + 第三部分：建模文件子文件夹`system_build`
>
>     > + 建模所需蛋白质文件`.pdb file`
>     > + `psfgen.tcl`：vmd建模`tcl`脚本
>     > + 建模需要调用的拓扑文件（`.str`,`.rtf`文件）

### 2.2 `ffgen.sh`&`vmdmodel.sh`

#### 2.2.1 `ffgen.sh`

```shell
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
    # python ../my_paramchem.py -u ****** -p ****** -c $file # change your personal account
    # python ../my_paramchem.py -u ****** -p ****** -c $file
    echo "ff file of" $filename has generated successfully 
    python ../strdivid.py "$(pwd)"
    pdbname="${filename}.pdb"
    obabel -imol2 $filename.str.mol2 -opdb -O $pdbname
    vmd -dispdev text -e ../system_build/psfgen.tcl -args $filename
    cd ..
done

```

#### 2.2.2 `vmdmodel.sh`

检查力场文件、拓扑文件无误后调用，在此之前最好先注释主脚本，用`test`部分测试一个建模是否顺利

```shell
#!/bin/bash
# conda activate numpy

files=$(ls *.mol2)
for file in $files; do
    filename="${file%.*}"
    python residuetype_LP.py "$(pwd)" $filename
    cd $filename
    vmd -dispdev text -e ../system_build/psfgen.tcl -args $filename 
    echo "${filename} has been modeled succefffully!"
    cd ..
done

# this is for test

# filename="CDI1"
# python residuetype_LP.py "$(pwd)" $filename
# cd $filename
# vmd -dispdev text -e ../system_build/psfgen.tcl -args $filename
# echo "${filename} has been modeled succeddfully!"
# cd ..

```

## 3. 用法

+ 命令行进入目录` addatomname`，将准备好的`pre-mol2`文件直接放置在`addatomname`文件夹下，调用`addatomname.sh`生成包含所有处理后的`mol2`的文件夹`mol2_re`
+ 将`mol2_re`中的`mol2`文件拷贝到` Batch_Modeling`文件夹底下
+ 进入` Batch_Modeling`目录
+ 调用 `ffgen.sh`脚本生成力场文件，会在主文件夹下生成一些列的力场文件夹（虽然有点乱，懒得改了），每个文件夹的名字是对应的`mol2`文件的名字
+ 调用`check.py`检查是否正常生成力场，并修正错误
+ 调用`vmdmodel.sh`建模，建立的模型会保存到力场文件的同一个文件夹底下
+ 批量提交到集群进行分子动力学模拟

## 4. 一些解释与常见错误

### 4.1 关于预处理

在上传小分子文件时，由于最开始设计小分子的过程中并不会直接生成`mol2`文件，最终上传的文件应该是经过`openbabel`等工具转化的，因此氢原子（有时候其他原子也存在）的编号（`Aton Name`），只能识别出元素类型，并没有元素类型后的数字来对应的识别出每一个原子；但是上传`cgenff`后，生成的小分子`rtf`、`prm`文件中会给这些原来没有数字编号的原子名进行编号，而生成的导致建模的时候并不能与生成的`pdb`文件原子进行对应，导致建模失败。

简单来说，出现了含有坐标的文件中的原子名和含有拓扑信息和力场参数信息的文件中不行形成一一对应，一张老图说明关系：

需要注意的是，`openbabel`的参数`-p`会使得原来具有数字编号的原子名信息丢失，因此需要用检查文本文档的方式，利用`python`脚本添加原子编号，最后将含有正确电荷信息与原子编号的`pdb`文件转化为`mol2`文件

![MD_files](https://github.com/AIB001/NAMD/assets/141569168/e449f683-c77f-48b8-bc98-11c2fc3ab161)

### 4.2 残基类型（RESI TYPE）说明

`cgenff`生成的`rtf`文件与`pdb`文件中的残基类型不能对应，`pdb`中的残基名是`UNK`，而`rtf`中的残基名是输入的文件名

### 4.3 建模中加水的问题

在建模过程中加入出现了对体系加入了过多的水，原因是在执行`guesscoord`命令的时候，由于找不到对应的拓扑信息或者一些玄学的原因（比如很多时候换一台机器建模？），一些原子的坐标会被guess到 $(0.000\ ,0.000\ ,0.000)$的坐标原点，导致体系扩大，对应的加入了过多的水，具体信息可以参考建模时候输出的日志信息来判断

需要的脚本可以在这里找到：https://github.com/AIB001/AIB001.github.io/edit/main/My-Biophysics-Journey/Molecular-Dynamic/scripts/batch_modeling
