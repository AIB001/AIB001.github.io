import numpy as np
import matplotlib.pyplot as plt
import scipy
import time
import argparse
import sys

# 定义字体与字号
plt.rcParams['font.family']='Times New Roman'
plt.rcParams['font.size']=18

# 定义物理常数
hbar = 1.0546 * (10 ** -34)
Me = 9.109 * (10 ** -31)

# 初始化偏微分方程的解。设置初始条件和边界条件
def phi_init(ht, L, sigma, k, N):
    hx = L/N
    phi = np.zeros([N+1, 10001], dtype=complex)
    for i in range(0, N+1):
        phi[i, 0] = (np.e ** (-((i * hx - L/2) ** 2 )/(2 * (sigma ** 2)))) * (np.e ** (1j * k * i * hx))
    phi[0,0] = 0
    phi[N,0] = 0
    return phi

# 利用迭代法求解薛定谔方程
def Differential_onestep_iter(phi, step, ht, L, N, target=10**-6): # target是迭代精度
    hx = L / N
    delta = 1.0 
    complex_factor = 1 / (1 + (1j * hbar * ht) / (2 * Me* (hx**2)))
   
    while delta > target:
        phi_prim = np.copy(phi[:, step])
        for index in range(1, N):  # Corrected range to exclude N
            phi_step = (1j * hbar * ht / (4 * Me)) * (phi[index+1, step] + phi[index-1, step]) / (hx ** 2) \
                       + phi[index, step-1] \
                       + ((1j * hbar * ht / (4 * Me)) * (phi[index+1, step-1] + phi[index-1, step-1] - 2 * phi[index, step-1]) / (hx ** 2))
            phi_step *= complex_factor
            phi[index, step] = phi_step
# 判断迭代收敛
        delta = np.max(np.abs(phi_prim - phi[:, step]))
    
    return phi

# 利用求解线性方程组进行时间演化求解
def Differential_onestep_matrix(phi, step, ht, L, N):
    hx = L / N
    # 定义矩阵元
    a1 = 1 + 1j * hbar * ht / (2 * Me * hx**2)
    a2 = -1j * hbar * ht / (4 * Me * hx**2)
    b1 = 1 - 1j * hbar * ht / (2 * Me * hx**2)
    b2 = 1j * hbar * ht / (4 * Me * hx**2)

    # 初始化A，B矩阵
    A = np.zeros((N-1, N-1), dtype=complex)
    B = np.zeros((N-1, N-1), dtype=complex)

    # 设置A,B举证的对角元和对角元附近的元素
    np.fill_diagonal(A, a1)
    np.fill_diagonal(B, b1)
    np.fill_diagonal(A[1:], a2)
    np.fill_diagonal(A[:, 1:], a2)
    np.fill_diagonal(B[1:], b2)
    np.fill_diagonal(B[:, 1:], b2)

    # 通过逆矩阵运算更新下一步
    phi_next = np.dot(np.linalg.inv(A), np.dot(B, phi[1:N, step-1]))

    # 更新时间维度的矩阵，并保持边界条件
    phi[1:N, step] = phi_next

    return phi

# 绘图模块将三张图竖直排列
def plot(phi, steps, L, N):
    x = np.linspace(0, L, N+1)
    plt.figure(figsize=(15, 10))

    for t in steps:
        real_part = phi[:, t].real
        imag_part = phi[:, t].imag
        prob_density = np.abs(phi[:, t])**2

        plt.subplot(3, 1, 1)
        plt.plot(x, real_part, label=f'Step {t}')
        plt.title('Real Part of $\phi$')
        plt.xlabel('$x$')
        plt.ylabel('Real Part')

        plt.subplot(3, 1, 2)
        plt.plot(x, imag_part, label=f'Step {t}')
        plt.title('Imaginary Part of $\phi$')
        plt.xlabel('$x$')
        plt.ylabel('Imaginary Part')

        plt.subplot(3, 1, 3)
        plt.plot(x, prob_density, label=f'Step {t}')
        plt.title('Probability Density $|\phi|^2$')
        plt.xlabel('$x$')
        plt.ylabel('$|\phi|^2$')

    for i in [1, 2, 3]:
        plt.subplot(3, 1, i)
        plt.legend()
    
    plt.tight_layout()
    plt.show()

# 定义输入模块，利用argparse进行命令行传参
parser = argparse.ArgumentParser(description="Quantum Mechanics Simulation.")
parser.add_argument("-mode", choices=["iter", "matrix"], default="iter", help="Calculation mode (iter or matrix). Default is iter.")
parser.add_argument("-step", nargs='+', type=int, default=[0,300,800,500,2000], help="Calculation steps. Can specify multiple, such as '500 1000'. Default is [0,300,800,500,2000].")

args = parser.parse_args()

calc_mode = args.mode
steps = sorted(set(args.step))

# 定义初始参数，也可以写进argparse中
L = 10 ** -8
sigma = 10 ** -10
k = 5 * (10 ** 10)
ht = 10 ** -18
N = 1000

phi = phi_init(ht, L, sigma, k, N)

# 记录运算所需的时间，比较迭代法和求解线性方程所需的时间
start_time = time.time()
last_step = 0
for step in steps:
    for i in range(last_step + 1, step + 1):
        if calc_mode == "iter":
            phi = Differential_onestep_iter(phi, i, ht, L, N)
        elif calc_mode == "matrix":
            phi = Differential_onestep_matrix(phi, i, ht, L, N)
    last_step = step

end_time = time.time()

plot(phi, steps, L, N)  
#输出运行时间
print(f"Total running time equals {end_time - start_time}s")