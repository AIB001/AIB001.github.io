# import os
# import sys
# from sys import argv

# workpath = argv[1]
# obj = str(argv[2])

# folder_path = os.path.join(workpath,obj)
# os.chdir(folder_path)

# rtf_file_name = "{}.rtf".format(obj)
# prm_file_name = "{}.prm".format(obj)

# # 修改rtf文件
# rtf_file_path = os.path.join(folder_path, rtf_file_name)
# with open(rtf_file_path, "r") as file:
#     lines = file.readlines()

# charge_compen =0 

# with open(rtf_file_path, "w") as file:
#     for line in lines:
#         if 'LP1' not in line and 'LP2' not in line:
#             # 替换RESI CDI2_re. 为RESI UNK
#             file.write(line.replace("RESI {}_re.".format(obj), "RESI UNK"))
#         else:
#             charge_compen = charge_compen + 1

# # 修改prm文件，并删除包含'LP'的行
# prm_file_path = os.path.join(folder_path, prm_file_name)
# with open(prm_file_path, "r") as file:
#     lines = file.readlines()

# with open(prm_file_path, "w") as file:
#     for line in lines:
#         if 'LP1' not in line and 'LP2' not in line:
#             # 只替换RESI CDI2_re. 为RESI UNK 并删除包含'LP'的行
#             file.write(line.replace("RESI {}_re.".format(obj), "RESI UNK"))

# print("Files have been updated.")
# print(charge_compen/2)





import os
import sys
from sys import argv

workpath = argv[1]
obj = str(argv[2])

folder_path = os.path.join(workpath, obj)
os.chdir(folder_path)

rtf_file_name = "{}.rtf".format(obj)
prm_file_name = "{}.prm".format(obj)

# 修改rtf文件
rtf_file_path = os.path.join(folder_path, rtf_file_name)
with open(rtf_file_path, "r") as file:
    lines = file.readlines()

charge_compen = 0

# 计算LP的数量
for line in lines:
    if 'LP1' in line or 'LP2' in line:
        charge_compen += 1

# 处理 .rtf 文件
with open(rtf_file_path, "w") as file:
    for line in lines:
        if 'LP1' in line or 'LP2' in line:
            continue  # LP项被删除
        else:
            # 替换RESI CDI4_re. 为RESI UNK
            new_line = line.replace("RESI {}_re.".format(obj), "RESI UNK")
            new_line = line.replace("RESI {}_re".format(obj), "RESI UNK")
            if 'ATOM Cl1' in new_line:
                parts = new_line.split()
                cl_charge = float(parts[3]) + (charge_compen * 0.025)
                parts[3] = "{:.3f}".format(cl_charge)  # 格式化电荷到三位小数
                new_line = ' '.join(parts) + "\n"
            file.write(new_line)

# 处理 .prm 文件
prm_file_path = os.path.join(folder_path, prm_file_name)
with open(prm_file_path, "r") as file:
    lines = file.readlines()

with open(prm_file_path, "w") as file:
    for line in lines:
        if 'LP1' in line or 'LP2' in line:
            continue  # 存在LP项，跳过不写入
        else:
            # 替换RESI CDI4_re. 为RESI UNK
            new_line = line.replace("RESI {}_re.".format(obj), "RESI UNK")
            new_line = line.replace("RESI {}_re".format(obj), "RESI UNK")
            if 'ATOM Cl1' in new_line:
                parts = new_line.split()
                cl_charge = float(parts[3]) + (charge_compen * 0.25 + 0.05)
                parts[3] = "{:.3f}".format(cl_charge)  # 格式化电荷到三位小数
                new_line = ' '.join(parts) + "\n"
            file.write(new_line)

print("Files have been updated.")
print(charge_compen * 0.25 + 0.05)