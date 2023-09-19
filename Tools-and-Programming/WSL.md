<font face='Times'>

# WSL Installation and Application
## WSL installation
Reference Zhihu Tutorial:[Tutorial](https://zhuanlan.zhihu.com/p/466001838)

Core commands:
```bash
wsl --install
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --set-default-version 2
```

After which, restart the computer and install *Ubuntu*

## Vim  command
After editing,there are some common vim operation and parameters:

`:w`:save file but not exit vi

`:w!`:force save but not exit vi

`:wq`:save file and exit vo meanwhile

`:q`:don't save file and exit vi meanwhile

`:q!`:force quit and don't save the file 

`:e`:give up all edition, and stgart from last save


## Anaconda Installation

To install Anaconda to WSL, we should download the package for Linux from official website:

![image](https://github.com/AIB001/AIB001.github.io/assets/141569168/44204b85-a33f-4771-bd73-3aaadbc9d8ed)

Unpackage to `/mnt/e` or where you like. Then use the command to begin the installation:`bash Anaconda3-2023.07-2-Linux-x86_64.sh`.
After, you will see like below:
![image](https://github.com/AIB001/AIB001.github.io/assets/141569168/5ec63dd0-814c-4b66-aee2-24f622374f0c)

Then we should add anaonda to environment variables,use the command below:
```bash
sudo vim /etc/profile
```

Add path below to the end of profile:
```bash
export PATH=/home/username/anaconda3/bin:$PATH
```

Reload the environment variables:
```bash
source /etc/profile
```

Try commond `conda` or `python` to check the installation. And create python environment:
```bash
conda create -n env_name python=3.11
```
And the first time in WSL,when you try to use `conda activate evn_name` to activate the environment, you may fail in activate the conda environment like the ERROR below:
```bash
usage: conda [-h] [--no-plugins] [-V] COMMAND ...
conda: error: argument COMMAND: invalid choice: 'activate' (choose from 'clean', 'compare', 'config', 'create', 'info', 'init', 'install', 'list', 'notices', 'package', 'remove', 'uninstall', 'rename', 'run', 'search', 'update', 'upgrade', 'build', 'content-trust', 'convert', 'debug', 'develop', 'doctor', 'index', 'inspect', 'metapackage', 'render', 'skeleton', 'verify', 'token', 'repo', 'server', 'env', 'pack')
shizq@DESKTOP-12CEH19:/mnt$ source activate
(base) shizq@DESKTOP-12CEH19:/mnt$ source deactivate
DeprecationWarning: 'source deactivate' is deprecated. Use 'conda deactivate'.
```
Use the common below to activate or deactivate the *base*:
```bash
souece activate
......
source deactivate
```


