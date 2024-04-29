import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.family']='Times New Roman'
plt.rcParams['font.size']=21

def runge_kutta_4th_order(f, y0, t, k):
    h = t[1] - t[0]
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(0, len(t) - 1):
        k1 = f(y[i], t[i], k)
        k2 = f(y[i] + h * k1 / 2, t[i] + h / 2, k)
        k3 = f(y[i] + h * k2 / 2, t[i] + h / 2, k)
        k4 = f(y[i] + h * k3, t[i] + h, k)
        y[i + 1] = y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y

omega = 1.0
k = 0.1

def damped_oscillator(y, t, k):
    dydt = np.zeros_like(y)
    dydt[0] = y[1]
    dydt[1] = -omega**2 * y[0] - k * y[1]
    return dydt
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 21

def runge_kutta_4th_order(f, y0, t, k):
    h = t[1] - t[0]
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(0, len(t) - 1):
        k1 = f(y[i], t[i], k)
        k2 = f(y[i] + h * k1 / 2, t[i] + h / 2, k)
        k3 = f(y[i] + h * k2 / 2, t[i] + h / 2, k)
        k4 = f(y[i] + h * k3, t[i] + h, k)
        y[i + 1] = y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y

def damped_oscillator(y, t, k):
    dydt = np.zeros_like(y)
    dydt[0] = y[1]
    dydt[1] = -omega**2 * y[0] - k * y[1]
    return dydt

omega = 1.0
t = np.linspace(0, 100, 10000)
y0 = [1.0, 0.0]

plt.figure(figsize=(10, 6))  # 设置画布大小

# 遍历不同的k值
for k in np.arange(0, 5.2, 0.2):
    y = runge_kutta_4th_order(damped_oscillator, y0, t, k)
    plt.plot(t, y[:, 0], label=f'k={k:.1f}')

plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Damped Oscillator Motion for Various k')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()  # 调整布局以防止标签被剪切
plt.show()
t = np.linspace(0, 100, 10000)
y0 = [1.0, 0.0]

k = 0.1
y = runge_kutta_4th_order(damped_oscillator, y0, t, k)

plt.plot(t, y[:, 0])
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Damped Oscillator Motion with k=0.1')
plt.show()