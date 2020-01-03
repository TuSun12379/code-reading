"""Based on code of Stef Smeets: https://github.com/stefsmeets/lines , 用于计算X-射线和电子的原子散射因子及绘图"""

import numpy as np
import matplotlib.pyplot as plt
from it_table_4322 import it_table_4322
from it_table_4323 import it_table_4323
from wk1995 import wk1995
from dt1969 import dt1969


def gaussian(a, b, s): # 返回高斯函数
    """General Gaussian"""
    return a * np.exp(-b * s**2)


def plot_sf_atoms(atoms, s,tables, kind="xray"):   # 绘制原子散射因子图
    for atom in atoms:  # 针对存在多种原子的情况
        data = tables[atom] # 从字典中提取计算原子散射因子的系数
        y = calc_sf(atom, data, s, kind) # 知道原子的种类，原子散射因子系数，计算范围，以及原子散射因子的类型，计算原子散射因子
        plt.plot(s, y, label=atom) # 绘制图表，以s为横坐标，y为纵坐标，标签为原子散射因子类型

    plt.ylabel("f") # 设置y轴标签
    plt.xlabel(r"$\sin(\theta)/\lambda (1/\mathrm{\AA})$") # 设置x轴标签，以latex格式
    plt.legend() # 添加图例
    plt.show() # 显示完整图像

def calc_sf(atom, data, s, kind="xray"): # 此函数的主要目的是确定计算那个原子散射因子，针对X射线和电子存在两种不同的情况
    if kind == 'xray':
        return calc_sf_xray(atom, data, s)
    elif kind == "electron":
        return calc_sf_electron(atom, data, s)
    else:
        raise NameError


def calc_sf_electron(atom,  data,   s):
    """scattering factor function for electron/it432x table"""  # 计算电子的原子散射因子
    total = None
    for i in range(5):
        a, b, dZ = data[2+i], data[7+i], data[1]
        y = gaussian(a, b, s)

        if total is None:
            total = y
        else:
            total += y
    return total

def calc_sf_xray(atom,  data,   s):
    """Scattering factor function for xray/wk1995 table"""  # 计算X射线的原子散射因子
    total = None
    for i in range(5):
        a, b, c = data[0+i], data[5+i], data[10]   # wk95
        y = gaussian(a, b, s)

        if total is None:
            total = y + c
        else:
            total += y
    return total

def main():
    atoms = ['Si', 'O']
    # s = [0, 2, 0.01]
    s = np.arange(0, 2, 0.01)
    # tables = wk1995 # for X-ray
    tables = it_table_4323 # for electrons
    # print(s)
    # print_table_topas(atoms, s)
    plot_sf_atoms(atoms, s, tables, kind = "electron")

if __name__ == '__main__':
    main()