import os

# workpath = arg[1]

workpath = r'C:\Users\Apple\Desktop\addatomname\mol2_re'
os.chdir(workpath)
dir_list = os.listdir()
folder_list = [folder for folder in dir_list if os.path.isdir(folder)]

for folder in folder_list:
    folder_path = os.path.join(os.getcwd(),folder)
    rtf_file = folder +'.rtf'

    if not os.path.exists(os.path.join(folder_path, rtf_file)):
        print(folder)