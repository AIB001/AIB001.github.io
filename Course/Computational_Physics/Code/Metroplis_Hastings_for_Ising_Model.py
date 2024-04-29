import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation
from numba import jit
from matplotlib.animation import PillowWriter
import argparse
import os

# 定义命令行输入
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ising Model Simulation using Metroplis-Hasting algorithm (CUDA Acceleration version)")
    parser.add_argument("-step", type=int, default=100000, help='simulation steps, each step randomly generate one point in lattice and judge whether update or not')
    parser.add_argument("-beta", nargs='+', type=float, default=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0], help="set different beta for simulation, beta = 1/(kb*T)")
    parser.add_argument("-J", type=float, default=1.0, help=r"E = - J * \sum_{(i,j)}\sigma_i*\sigma_j")
    parser.add_argument("-size", type=int, default=20, help="define the lattice size as size*size")
    parser.add_argument("-sw", "-sampling_window", dest="sampling_window", type=int, default=100, help="sampling energy for each sampling window")

    args = parser.parse_args()
    steps = args.step
    beta_set = sorted(set(args.beta))
    J = args.J
    lattice_size = args.size
    sampling_window = args.sampling_window

# 定义绘图字体
plt.rcParams['font.size'] = 21
plt.rcParams['font.family'] = 'Times New Roman'

# 物理常数定义
# kb = 1.0
# T = 1.0
# beta = 1/(kb * T)
J = 1.0

def moving_average(data, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(data, window, 'same')

# 计算总自旋转函数
def total_spin(lattice):
    return np.sum(lattice)

# jit加速能量计算和Metropolis-Hastings算法
@jit(nopython=True)
def energy(lattice):
    total_energy = 0
    for i in range(lattice.shape[0]):
        for j in range(lattice.shape[1]):
            spin = lattice[i, j]
            neighbors = lattice[(i+1)%lattice.shape[0], j] + lattice[i, (j+1)%lattice.shape[1]] + lattice[(i-1)%lattice.shape[0], j] + lattice[i, (j-1)%lattice.shape[1]]
            total_energy += -J * spin * neighbors
    return total_energy / 2

@jit(nopython=True)
def Metropolis_Hastings(lattice_point, beta):
    length, width = lattice_point.shape
    i = np.random.randint(length)
    j = np.random.randint(width)
    spin = lattice_point[i, j]
    neighbors = lattice_point[(i+1)%length, j] + lattice_point[i, (j+1)%width] + lattice_point[(i-1)%length, j] + lattice_point[i, (j-1)%width]
    delta_energy = 2 * J * spin * neighbors
    if delta_energy < 0 or np.random.rand() < np.exp(-beta * delta_energy):
        lattice_point[i, j] *= -1
    return lattice_point

# 生成初始晶格·
def lattice_gen(len=20, wid=20):
    spin = np.array([-1, 1])
    random_matrix = np.random.choice(spin, size=(len, wid))
    return random_matrix

# 初始化晶格和存储能量列表
# window_size = 10  # 选择窗口大小

energy_set = []
total_spin_set = []

# 对所有的beta进行模拟
for beta in beta_set:
    energies = []
    spins = [] 
    lattice = lattice_gen(lattice_size, lattice_size)
    for step in range(steps):
        lattice = Metropolis_Hastings(lattice, beta)
        if step % sampling_window == 0:
            energies.append(energy(lattice))
            spins.append(total_spin(lattice))
    energy_set.append(energies)
    total_spin_set.append(spins)

# 对所有的beta进行绘图，绘制总能量随模拟步长的变化
index = 0
for beta in beta_set:
    plt.plot(range(0, steps, sampling_window), energy_set[index], lw=3, label='beta = {:.1f}'.format(beta))
    plt.xlabel('Simulation Step')
    plt.ylabel('Energy')
    plt.title('Energy Variation with Simulation Step')
    index += 1
plt.legend(loc='upper left', bbox_to_anchor=(0.8, 1))
# plt.ylim((-800,-600))
plt.show()

# 绘制自选随模拟步长的变化
index = 0
for beta in beta_set:
    plt.plot(range(0, steps, sampling_window), total_spin_set[index], lw=3, label='beta = {:.1f}'.format(beta))
    plt.xlabel('Simulation Step')
    plt.ylabel('Total Spin')
    plt.title('Total Spin Variation with Simulation Step')
    index += 1
plt.legend(loc='upper left', bbox_to_anchor=(0.8, 1))
# plt.ylim((-800,-600))
plt.show()

# 绘制最终模拟结果图，模拟晶格的图片
plt.figure(figsize=(10, 10))
plt.imshow(lattice, cmap='gray', extent=[0, lattice_size, 0, lattice_size])
plt.title('Final Lattice Configuration')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# 随机种子对最终总自旋的影响
spin_for_seed = []
def random_seed():
    seeds = [14, 21, 1101, 2024, 5000]
    for seed in seeds:
        np.random.seed(seed)
        lattice = lattice_gen(lattice_size, lattice_size)
        for step in range(steps):
            lattice = Metropolis_Hastings(lattice, beta)
            if step % sampling_window == 0:
                spin_for_seed.append(total_spin(lattice))
        print('total spin for random seed {}, is {}'.format(seed, spin_for_seed[-1]))

random_seed()

# 开始绘制动画
#定义动画的采样间隔
sampling_interval = int(steps / 600)

# 动画帧更新函数，同时更新晶格和能量
def update(frame):
    global ax1, ax2
    ax1.clear()
    ax2.clear()
    lattice, energy = frame_list[frame]
    
    # 使用viridis colormap
    ax1.imshow(lattice, cmap='viridis', extent=[0, lattice_size, 0, lattice_size])
    
    # 含颜色注释的标题
    ax1.set_title('Step: {} (Yellow: Spin up, Purple: Spin down)'.format(frame * sampling_interval))
    ax1.set_xticks([])
    ax1.set_yticks([])

    # 更新能量图，加粗线条
    ax2.plot(range(0, (frame + 1) * sampling_interval, sampling_interval), energy_list[:frame + 1], color='blue', linewidth=2.5)
    ax2.set_xlim(0, steps)
    ax2.set_ylim(min(energy_list), max(energy_list))
    ax2.set_xlabel('Simulation Step')
    ax2.set_ylabel('Energy')

frame_list = []
energy_list = []
lattice = lattice_gen(lattice_size, lattice_size)
for step in range(steps):
    lattice = Metropolis_Hastings(lattice, 1.0)  # beta=1.0 的模拟
    current_energy = energy(lattice)
    if step % sampling_interval == 0:
        frame_list.append((np.copy(lattice), current_energy))
        energy_list.append(current_energy)

# 创建图形和轴对象，通过调整子图参数来给能量演化图预留足够空间
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 15),
                               gridspec_kw={'height_ratios': [2.5, 1]})
fig.subplots_adjust(hspace=0.2)  # 调整子图间距

# 创建FuncAnimation对象
ani = FuncAnimation(fig, update, frames=len(frame_list), interval=1000/30)

output_file = "simulation_animation_200_300000.gif"
writer = PillowWriter(fps=30)

#需要的时候取消注释，保存动画
ani.save(output_file, writer=writer)

plt.show()