import numpy as np
import random 
import matplotlib.pyplot as plt

# 定义绘图字体
plt.rcParams['font.size']=21
plt.rcParams['font.family']='Times New Roman'

# 利用Numpy的向量化操作提高运算速度
# 随机游走函数，输入初始粒子数和模拟步数，返回用于绘图的分布函数
def random_walk(num_particles, steps):
    # 生成所有随机步骤
    steps_taken = np.random.choice([-1, 1, 0], size=(num_particles, steps), p=[1/6, 1/2, 1/3])
    # 累加步骤以获得每个粒子的最终位置
    final_positions = np.sum(steps_taken, axis=1)
    # 计算每个位置的粒子数
    position_range = np.arange(-steps, steps+1)
    distribution = np.histogram(final_positions, bins=np.arange(-steps-0.5, steps+1.5, 1))[0]

    return position_range, distribution

# 定义初始粒子数和模拟步数
num_particles = 10**6
steps = 100

x, distribution = random_walk(num_particles, steps)

# 使用 bar 来绘制柱状图
plt.bar(x, distribution)
plt.plot(x, distribution, color = 'red', lw = 3)
plt.title('Random Walk with $10^6$ particles')
plt.xlabel('Distance')
plt.ylabel('Numbers')
plt.show()