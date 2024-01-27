import os
import sys
from sys import argv

filename = str(sys.argv[1])
workpath = str(sys.argv[2])

workpath = os.path.join(workpath, 'mol2_re')
if not os.path.exists(workpath):
    os.makedirs(workpath)
os.chdir(workpath)

pdb_input_filename = f"{filename}.pdb"
pdb_output_filename = f"{filename}_re.pdb"


def add_atom_names_to_pdb(pdb_input_path, pdb_output_path):
    with open(pdb_input_path, 'r') as input_file:
        lines = input_file.readlines()

    with open(pdb_output_path, 'w') as output_file:
        atom_count = {}
        for line in lines:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                # PDB 格式中，元素符号通常在 76-77 位置，这里先提取
                element_symbol = line[76:78].strip()
                if element_symbol == '':  # 如果 PDB 没有元素符号，则从原子名称中提取
                    element_symbol = line[12:16].strip()

                # 如果列表中没有该元素，则初始化计数为1
                # 否则，对已存在的元素计数加1
                atom_count[element_symbol] = atom_count.get(element_symbol, 0) + 1
                
                # 创建原子名（元素符号 + 当前元素的唯一编号）
                atom_name = f"{element_symbol}{atom_count[element_symbol]}"
                atom_name = atom_name.ljust(4)
                
                # 排列新的行数据
                new_line = line[:12] + atom_name + line[16:76] + element_symbol.rjust(2) + '\n'
                output_file.write(new_line)
            else:
                output_file.write(line)

# 调用函数，用正确的文件路径替换 'input.pdb' 和 'output.pdb'
add_atom_names_to_pdb(pdb_input_filename, pdb_output_filename)