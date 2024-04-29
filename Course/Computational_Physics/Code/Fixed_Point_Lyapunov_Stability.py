import numpy as np
import matplotlib.pyplot as plt

# 设置绘图字体
plt.rcParams['font.size'] = 21
plt.rcParams['font.family'] = 'Times New Roman'

# 计算函数值
def sin(r, x):
    return r * np.sin(np.pi * x)

# 计算导数值
def sin_derivative(r, x):
    return np.pi * r * np.cos(np.pi * x)

n = 100000  # 待计算的r值的数量
xmin = 0.0
xmax = 1.0
r = np.linspace(xmin, xmax, n)  # 生成r的值，范围从xmin到xmax
iterations = 1000  # 迭代次数
last = 100  # 要记录的最后一些迭代的数量
x = 1e-5 * np.ones(n)  # 初始x的值，为一个很小的正数
lyapunov = np.zeros(n)  # 用于存储李雅普诺夫指数的数组

x_last = np.empty((last, len(r)))  # 存储最后100次迭代结果的数组
x_last.fill(np.nan)  # 初始时用NaN填充

# 开始迭代
for i in range(iterations):
    x = sin(r, x)  # 更新x值
    x_derivative = sin_derivative(r, x)  # 计算每一步的导数
    # 避免除以零错误，忽略该情况
    with np.errstate(divide='ignore', invalid='ignore'):
        # 仅计算非零导数的log值
        valid_indices = x_derivative != 0
        lyapunov[valid_indices] += np.log(abs(x_derivative[valid_indices]))

    # 存储最后`last`次迭代的x值
    if i >= (iterations - last):
        x_last[i - (iterations - last)] = x

# 完成所有迭代后计算平均的李雅普诺夫指数
lyapunov /= iterations

# 清理lyapunov数组中的无效值
lyapunov[np.isinf(lyapunov)] = np.nan  # 将无穷值替换为NaN
finite_lyapunov = lyapunov[np.isfinite(lyapunov)]
if finite_lyapunov.size > 0:
    lyapunov_min = np.min(finite_lyapunov)
    lyapunov[np.isnan(lyapunov)] = lyapunov_min  # 将NaN替换为最小的有限值
else:
    lyapunov_min = -2  # 如果所有值都是非有限的，使用一个默认值
    lyapunov.fill(lyapunov_min)

# 绘制双分支图
plt.figure(figsize=(12, 6))
plt.plot(r, x_last.T, ',k', alpha=0.25)
plt.xlim(xmin, xmax)
plt.title("Bifurcation diagram")
plt.xlabel('r')
plt.ylabel('x')
plt.grid(True)
plt.show()

# 绘制李雅普诺夫指数图
plt.figure(figsize=(12, 6))
colors = np.where(lyapunov >= 0, 'r', 'g')
plt.scatter(r, lyapunov, color=colors, s=0.1, alpha=0.5)
plt.xlim(xmin, xmax)
plt.ylim(lyapunov_min / 2, -1 * lyapunov_min / 2)  # 根据计算得到的最小值设置y轴的范围
plt.title("Lyapunov Exponent")
plt.xlabel('r')
plt.ylabel('Lyapunov exponent')
plt.grid(True)
plt.show()