import numpy as np
from scipy.linalg import solve

def linear_equation():
    order = 4
    equation = np.array([[1.3, 6.3, -3.5,  2.8,  1.8],
                         [5.6, 0.9,  8.1, -1.3, 16.6],
                         [7.2, 2.3, -4.4,  0.5, 15.1],
                         [1.5, 0.4,  3.7,  5.9, 36.9]])

    return equation, order

equation, order = linear_equation()

def Gaussian_elimination(input_equation):
    #定义交换矩阵，记录每一步迭代的时候是否有因为头元素为0而出现的交换
    exchange_record = np.full((4, 4), -1)
    equation = input_equation
    for index in range(0, order):
        if equation[index, index] != 0:
            pass
        else:
            i = index
            while equation[index, i] != 0:
                i += 1
            exchange_record[index, index] = exchange_record[index, i] = 1
            equation[:, [index, i]] = equation[:, i, index]

        for line in range(index+1, order):
            equation[line, :] = equation[line, :] - (equation[line, index] / equation[index, index]) * equation[index, :]
            # print(equation)
    return equation, exchange_record

# 求解经过高斯消元处理后的矩阵，和记录交换的矩阵，返回求解的向量
def gauss_solve(equation, order, exchange):
    solution = np.zeros(order) # 将所有解的初始值设置为0
    # 依次迭代获得解
    for index in reversed(range(order)):
        for i in range(0, order):
            solution[index] = solution[index] - solution[i] * equation[index, i]
        solution[index] = solution[index] + equation[index, order] # 加上常数项的一项
        solution[index] = solution[index] / equation[index, index]

    # 输出解答的同时返回解的向量
    for index in range(0, order):
        print("x{} = {:.2f}".format(index+1, solution[index]))
    return solution

input_eq, order = linear_equation()
equation, exchange_record = Gaussian_elimination(input_eq)

print(equation)
print(exchange_record)

print("Solution from Gaussian elimination is:")
gauss_solve(equation, order, exchange_record)

# 获取系数矩阵和常数向量
equation, order = linear_equation()  # 修改这一行
coefficients = equation[:, :-1]  # 所有行，除最后一列之外的所有列
constants = equation[:, -1]  # 所有行，只有最后一列

# 使用 NumPy 的 solve 函数求解
solutions = np.linalg.solve(coefficients, constants)
print("Solution from numpy", solutions)