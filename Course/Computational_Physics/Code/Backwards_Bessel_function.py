import numpy as np
import matplotlib.pyplot as plt
import scipy 
import math
import os
import argparse 

# 将绘图的字体设置为Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# 通过解析表达式生成0阶和1阶的Bessel函数曲线
def bessel_0_1_order():
    x = np.linspace(10 ** -4, 20, 2000).reshape(2000,) # 将第一个值设置为很小的一个值，防止除以0造成的错误
    bessel_0_order =  np.sin(x)/x
    bessel_1_order = np.sin(x)/(x ** 2) - np.cos(x)/x
    # print(bessel_0_order[0], bessel_1_order[0]) # 必要时可以取消注释，用于查看初始化是否正确，成为一个检查点
    return x, bessel_0_order, bessel_1_order # 返回Bessel 函数

#用于正向迭代的公式将贝塞尔函数升1阶
def upward(order, x, bessel_seq1, bessel_seq2):
    bessel_upper_seq = np.multiply((2*order-1)/x, bessel_seq2) - bessel_seq1
    return bessel_upper_seq

# 用向上迭代的方法，输出第n阶的Bessel函数，主题通过正向的循环实现
def bessel_n_order_upward(n):
    x, bessel_0_order, bessel_1_order = bessel_0_1_order()
    bessel_n_order = bessel_1_order
    bessel_n_minus_order = bessel_0_order
    for index in range(1, n):
        temp = bessel_n_order
        bessel_n_order = upward(index+1, x, bessel_n_minus_order, bessel_n_order)
        bessel_n_minus_order = temp
    return bessel_n_order

# 用向下迭代的公式，将Bessel函数降1阶
def downwards(order, x, bessel_seq1, bessel_seq2):
    bessel_down_seq = np.multiply((2*order+3)/x, bessel_seq1) - bessel_seq2   
    return bessel_down_seq

# 用向下迭代的方法得到Bessel函数第n阶的公式，可以自定义一个足够大的top阶数，开始向下迭代
def bessel_n_order_downward(n, top):
    x, bessel_0_order, bessel_1_order = bessel_0_1_order()
    bessel_top_plus = np.zeros(2000) # 将最高的阶数设置为0
    bessel_top = np.ones(2000) # 将top - 1 阶的Bessel函数假设为1
    for index in reversed(range(n, top)):
        temp = bessel_top
        bessel_top = downwards(index, x, bessel_top, bessel_top_plus)
        bessel_top_plus = temp

    bessel_n_order = bessel_top # 记录没有归一化时n阶Bessel函数的值

    for index in reversed(range(0, n)):
        temp = bessel_top
        bessel_top = downwards(index, x, bessel_top, bessel_top_plus)
        bessel_top_plus = temp
    scaler = bessel_top / bessel_0_order # 计算归一化因子
    # print(bessel_top, bessel_0_order)

    bessel_n_order = bessel_n_order / scaler # 计算归一化之后的n阶Bessel函数
    
    return bessel_n_order

# 用于画图， 输入是记录了若干条Bessel函数的bessel_sequence_set， 还有记录了绘制那几条Bessel函数曲线的queue
def bessel_plot(x, bessel_sequence_set, queue):
    plt.figure(figsize=(12, 6))
    queue = np.append(queue, 0)
    queue = np.append(queue, 1)
    index = -2
    for sequence in bessel_sequence_set:
        plt.plot(x, sequence, label = "Bessel Function Order {}".format(queue[index]))
        index += 1
    plt.ylim(-1, 1.05)
    plt.xlabel('$x$')
    plt.ylabel('y (Bessel Function)') 
    plt.title('Bessel Function with Differrnt Order')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=2)    
    plt.legend()
    plt.show()
    return 

# 绘制正向和反向Bessel函数
def bessel_curve_cluster(queue):
    x, bessel_0_order, bessel_1_order = bessel_0_1_order()
    bessel_set1 = np.array([bessel_0_order, bessel_1_order], dtype = object)
    bessel_set2 = np.array([bessel_0_order, bessel_1_order], dtype = object)
    for index in queue:
        bessel_n_order = bessel_n_order_upward(index)
        bessel_set1 = np.append(bessel_set1, [bessel_n_order], axis=0)
        bessel_n_order = bessel_n_order_downward(index, 50)
        bessel_set2 = np.append(bessel_set2, [bessel_n_order], axis=0)

    bessel_plot(x, bessel_set1, queue)
    bessel_plot(x, bessel_set2, queue)

    return

# 设置读入参数，-n1 表示额外绘制Bessel函数读入的个数 -u 读入一个字符串类型，用于输入不同的需要绘制的Bessel函数的阶数，默认的n1=3，u="2 5 10"
# input format: python3 Bessel function.py -n1 num -u "a b c d"
# usage: Bessel function.py [-h] [-n1 N1] [-u U]

# Process the sequences

# options:
#   -h, --help  show this help message and exit
#   -n1 N1      the number of sequences
#   -u U        the sequence list
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process the sequences")
    parser.add_argument('-n1', type=int, default=3, help='the number of sequences')
    parser.add_argument('-u', default='2 5 10', help='the sequence list')
    args = parser.parse_args()

list = args.u.split()
queue = [int(i) for i in list]
print(queue)
bessel_curve_cluster(queue)


