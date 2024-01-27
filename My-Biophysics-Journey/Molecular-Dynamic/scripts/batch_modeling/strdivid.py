import os
import sys

def update_file(file_path):
    # 打开文件并读取所有行
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 删除最后一行
    if lines:
        lines = lines[:-1]

    # 添加新的一行（内容为'END'）
    lines.append('END\n')

    # 打开文件，以写入模式重新打开
    with open(file_path, 'w') as file:
        # 将更改后的行列表写入文件
        file.writelines(lines)

    print(f'文件 {file_path} 更新完成。')


def split_text_files(folder_path, file_extension):
    file_paths = [file for file in os.listdir(folder_path) if file.endswith(file_extension)]

    for file_path in file_paths:
        with open(os.path.join(folder_path, file_path), 'r') as file:
            file_name = os.path.splitext(file_path)[0]
            rtf_file_path = os.path.join(folder_path, file_name + '.rtf')
            prm_file_path = os.path.join(folder_path, file_name + '.prm')
            rtf_text = []
            prm_text = []
            found_end = False

            for line in file:
                if 'END' in line:
                    found_end = True
                    prm_text.append(line)
                    if len(rtf_text) > 0:
                        with open(rtf_file_path, 'w') as rtf_file:
                            rtf_file.write(''.join(rtf_text))
                        rtf_text = []
                elif found_end:
                    prm_text.append(line)
                else:
                    rtf_text.append(line)
                    prm_text.append(line)

            with open(prm_file_path, 'w') as prm_file:
                prm_file.write(''.join(prm_text))
            update_file(prm_file_path)
            update_file(rtf_file_path)
            
            print(f'已生成文件：{rtf_file_path}、{prm_file_path}')


folder_path = sys.argv[1]
file_extension = '.str'

split_text_files(folder_path, file_extension)