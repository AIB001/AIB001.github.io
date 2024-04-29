import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size']=21
plt.rcParams['font.family']='Times New Roman'

def fx(arg):
    y = np.cos(arg) + np.cos(np.sqrt(2)*arg) + np.cos(np.sqrt(3)*arg)
    return y

def simulated_annealing(fx, sub, upper, T0=10):
    # 初始化起点
    init = np.random.random()
    init = init * (upper - sub) + sub
    best_y = fx(init)
    best_x = init
    y = best_y
    tau = 10000
    index = 0 
    while index < tau:
        # 生成新的解
        new_x = (upper - sub) * np.random.random() + sub
        new_y = fx(new_x)
        
        # 计算能量变化
        dy =  y - new_y
        
        # 更新温度
        T = T0 * (np.e ** (-index / tau))

        # 接受新的解的条件
        if dy > 0 or np.random.random() < (np.e ** (dy / T)):
            y = new_y
            index += 1
            if y < best_y:  # 检查是否为最好的结果
                best_y = y
                best_x = new_x
    
    return best_x, best_y  # 返回找到的最佳点和该点的函数值

def plot(fx, sub, upper):
    x = np.linspace(sub, upper, 1000)
    y = fx(x)
    best_x, best_y = simulated_annealing(fx, sub, upper)
    plt.plot(x, y, label = 'f(x)')
    plt.plot(best_x, best_y, '-o', markersize = 12, label = 'Global minimum Point')
    plt.text(best_x, best_y, ' Global minimum Point:({},{})'.format(best_x,best_y))
    plt.legend(loc = 'upper right')
    plt.show()


# 执行模拟退火算法并打印结果并绘图
best_x, best_y = simulated_annealing(fx, 0, 50)
print(f"全局最小点: x = {best_x}, 全局最小值: y = {best_y}")
plot(fx, 0, 50)