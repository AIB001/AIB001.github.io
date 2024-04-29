import numpy as np
from scipy.linalg import solve

# 定义方程组
def linear_equation():
    order = 4
    equation = np.array([[1.3, 6.3, -3.5,  2.8],
                         [5.6, 0.9,  8.1, -1.3],
                         [7.2, 2.3, -4.4,  0.5],
                         [1.5, 0.4,  3.7,  5.9]])
    const = [1.8, 16.6, 15.1, 36.9]
    return equation, const, order

# 进行LU分解
def LU_decomposion(matrix, order):
    L = np.full((order, order), 0, dtype=float)
    U = np.full((order, order), 0, dtype=float)
    for index in range(0, order):
        U[index, index] = 1 
    print(matrix)
    L[0, 0] = matrix[0, 0] #单独处理L[0,0]，让后面的循环不用特殊处理
    # 先求解U矩阵的每一列
    for k in range(1, order):
        for line in range(0, k):
            U[line, k] = matrix[line, k]
            for i in range(0, line):
                U[line, k] = U[line, k] - L[line, i] * U[i, k]
            U[line, k] = U[line, k] / L[line , line]
	# 根据已有的系数，求解L矩阵的行
        for column in range(0, k+1):
            L[k, column] = matrix[k, column]
            for i in range(0, column):
                L[k, column] = L[k, column] - L[k, i] * U[i, column]
    print("L matrix equils to")
    print(L)
    print("U matrix equils to")
    print(U)
    return L, U

# 得到LU矩阵后的求解，与高斯消元法类似
def LU_solve(equation, const, order):
    solution = np.zeros(order, dtype=float)
    L, U = LU_decomposion(equation, order)
    y = const
    for index in range(0, order):
        for i in range(0, index):
            y[index] = y[index] - L[index, i] * y[i]
        y[index] = y[index] / L[index, index]

    for index in reversed(range(order)):
            for i in range(0, order):
                solution[index] = solution[index] - solution[i] * U[index, i]
            solution[index] = solution[index] + y[index] # 加上常数项的一项
            solution[index] = solution[index] / U[index, index]
    
    for i in range(0, order):
        print("x{}={:.10f}".format(i+1, solution[i]))
    return solution


equation, const, order = linear_equation()

# 利用numpy的矩阵乘法检查是否成功将系数矩阵进行LU分解
# L, U = LU_decomposion(equation, 4)
# C = np.dot(L,U)
# print(C)

solution = LU_solve(equation, const, order)