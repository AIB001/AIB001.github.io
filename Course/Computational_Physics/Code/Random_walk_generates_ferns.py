import numpy as np
import matplotlib.pyplot as plt

# 定义变换函数参数
transforms = [
    {"a": 0.00, "b": 0.00, "c": 0.00, "d": 0.16, "e": 0, "f": 0.00, "p": 0.01},
    {"a": 0.85, "b": 0.04, "c": -0.04, "d": 0.85, "e": 0, "f": 1.60, "p": 0.85},
    {"a": 0.20, "b": -0.26, "c": 0.23, "d": 0.22, "e": 0, "f": 1.60, "p": 0.07},
    {"a": -0.15, "b": 0.28, "c": 0.26, "d": 0.24, "e": 0, "f": 0.44, "p": 0.07},
]

# 初始化点集
points = np.zeros((1000000, 2))
x, y = 0, 0

# 生成点
for i in range(1, len(points)):
    r = np.random.random()  # 生成[0,1)区间的随机数
    if r < transforms[0]["p"]:
        chosen_transform = transforms[0]
    elif r < transforms[0]["p"] + transforms[1]["p"]:
        chosen_transform = transforms[1]
    elif r < transforms[0]["p"] + transforms[1]["p"] + transforms[2]["p"]:
        chosen_transform = transforms[2]
    else:
        chosen_transform = transforms[3]
    
    # 根据所选的变换函数更新点位置
    x_new = chosen_transform["a"] * x + chosen_transform["b"] * y + chosen_transform["e"]
    y_new = chosen_transform["c"] * x + chosen_transform["d"] * y + chosen_transform["f"]
    points[i] = [x_new, y_new]
    x, y = x_new, y_new

# 使用plt.scatter画出点集
plt.figure(figsize=(8, 18))
plt.scatter(points[:, 0], points[:, 1], s=0.3, color="green")
plt.axis("off")  # 取消坐标轴
plt.show()