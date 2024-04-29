import numpy as np

# 利用G
def Gauss_Seidel(A, b, max_iter=100, epsilon=1e-10):
    n = len(b)
    x = np.zeros(n)  # 初始解可以设置为全0或其他数

    for iter in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            sum_ax = np.dot(A[i], x_new) - A[i][i] * x_new[i]
            x_new[i] = (b[i] - sum_ax) / A[i][i]
        if np.linalg.norm(x_new - x) < epsilon:
            return x_new
        x = x_new
    return x

def make_diagonally_dominant(A, b):
    n = A.shape[0]
    for i in range(n):
        # 找到当前列中绝对值最大的行
        max_row = np.argmax(np.abs(A[i:n, i])) + i
        # 如果需要，交换行
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
    return A, b

def solve_linear_system(A, b):
    A, b = make_diagonally_dominant(A, b)
    x = Gauss_Seidel(A, b)
    return x

# 示例数据
A = np.array([[1.3, 6.3, -3.5,  2.8], [5.6, 0.9,  8.1, -1.3], [7.2, 2.3, -4.4,  0.5], [1.5, 0.4,  3.7,  5.9]], dtype=float)
b = np.array([1.8, 16.6, 15.1, 36.9], dtype=float)

# 求解
x = solve_linear_system(A, b)
print("Solution is：", x)