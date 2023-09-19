<font face='Times'>

# WSL Installation and Application
## WSL installation
Reference Zhihu Tutorial:[Tutorial](https://zhuanlan.zhihu.com/p/466001838)

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



