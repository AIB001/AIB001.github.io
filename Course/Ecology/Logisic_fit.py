# To fit Logistic curve with this script,you should put a Excel(better to name the excel:'data.xlsx') under the same path with this python file 
# And attention that the path better not include any Chinese characters
# Change the variable 'workpath' to your own workpath
# Install Anaconda and activate your environment
# your environment should include 'numpy', 'scipy', 'matplotlib', 'pandas' is needed; when you install python ,package 'os' in installed meanwhile
# The data in your excel contain just 6 coloum, 1-3 coloum reflects to 20 $\degree C$ and 4-6 coloum reflects 30$\degree C$

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
import os

def logistic_func(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

def fit_logistic(x, y, color, temperature, marker):
    font = {
        'family': 'serif',
        'serif': ['Times New Roman'],
        'size': 12
    }
    plt.rc('font', **font)

    idx = 0
    for data in y:
        if idx <= 2:
            popt, pcov = curve_fit(logistic_func, x, data)
            L, k, x0 = popt
            print("Parameter in Group T{}:".format(idx+1))
            print("L = {:.4f}".format(L))
            print("k = {:.4f}".format(k))
            print("x0 = {:.4f}".format(x0))

            x_fit = np.linspace(0, 8, 100)
            y_fit = logistic_func(x_fit, L, k, x0)

            plt.plot(x, data, 'bo', label="Origin Data of G{}".format(idx + 1), color=color[idx % 3], marker=marker[idx])
            plt.plot(x_fit, y_fit, 'r--', label="G{}".format(idx + 1), color=color[idx % 3], linewidth=3.0)
            
            residuals = data - logistic_func(x, L, k, x0)
            rmse = np.sqrt(np.mean(residuals**2))
            print("RMSE: {:.4f}".format(rmse))
        idx += 1

    plt.xlabel("Time/Day")
    plt.ylabel("Group Amount(AU Under 650nm)")
    plt.title("Logistic Curve of {}$\degree C$".format(temperature))
    plt.legend()
    plt.show()

    plt.clf()


def fit_logistic2(x, y, color, temperature, marker):
    font = {
        'family': 'serif',
        'serif': ['Times New Roman'],
        'size': 12
    }
    plt.rc('font', **font)

    idx = 0
    for data in y:
        if idx <= 2:
            popt, pcov = curve_fit(logistic_func, x, data)
            L, k, x0 = popt
            print("Parameter in Group T{}:".format(idx+1))
            print("L = {:.4f}".format(L))
            print("k = {:.4f}".format(k))
            print("x0 = {:.4f}".format(x0))

            x_fit = np.linspace(0, 8, 100)
            y_fit = logistic_func(x_fit, L, k, x0)

            plt.plot(x, data, 'bo', label="Origin Data of {}$\degree C$".format((idx + 2)*10), color=color[idx % 3], marker=marker[idx])
            plt.plot(x_fit, y_fit, 'r--', label="G{}".format(idx + 1), color=color[idx % 3], linewidth=3.0)
            
            residuals = data - logistic_func(x, L, k, x0)
            rmse = np.sqrt(np.mean(residuals**2))
            print("RMSE: {:.4f}".format(rmse))
        idx += 1

    plt.xlabel("Time/Day")
    plt.ylabel("Group Amount(AU Under 650nm)")
    plt.title("Logistic Curve of {}$\degree C$".format(temperature))
    plt.legend()
    plt.show()

    plt.clf()

# change to your personal workpath 
workpath = r'C:\Users\Apple\Desktop\Ecology'
# os.chdir(workpath)

df = pd.read_excel(os.path.join(workpath, 'data.xlsx'))
x = np.array([0, 1, 2, 3, 4, 5, 6])

dataframe = pd.read_excel(os.path.join(workpath, 'data.xlsx'))

selected_data = dataframe.iloc[0:7, 0:6]
y1 = []
y2 = []
index = 0
for column in selected_data.columns:
    column_data = selected_data[column]
    if index <= 2:
        y1.append(column_data.values.tolist())
    if index > 2:
        y2.append(column_data.values.tolist())
    index += 1

color = ['#D16BA5','#86A8E7','#5FFBF1']
color2 = ['#C93B8C' , '#5189EF' , '#5FFB76']
color3 = ['#6A42F4' , '#66F721' , '#FE5A79']
color4 = ['#6A42F4' , '#FFA200' , '#FE5A79']
color5 = ['#E9B824', '#D83F31', '#219C90']
marker = ['o', 'd', '*']

d20 = [(y1[0][i] + y1[2][i]) / 2 for i in range(len(y1[0]))]
d30 = [(y2[1][i] + y2[2][i] + y2[0][i]) / 3 for i in range(len(y2[0]))]
d= [d20 , d30]

# Change the color you like to fit the line, there are five color sets presented 
fit_logistic(x, y1, color4, 20, marker)
fit_logistic(x, y2, color4, 30, marker)
fit_logistic2(x, d, color5, '20 & 30', marker)
