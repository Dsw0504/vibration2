# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 14:46
# @Author  : SW D
# @FileName: wave_data.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def wave_plt(file_dir):
    file_list = os.listdir(file_dir)
    for file_name in file_list:
        # 通过numpy loadtxt读取数据
        data_np = np.loadtxt(file_dir + file_name)
        # 将数据类型转换成list
        list_data = data_np.tolist()
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        # 设置图像大小、分辨率
        plt.figure(figsize=(60, 20), dpi=100)
        # 设置图片名称
        plt.title(file_name, fontsize=30)
        # 设置横纵坐标轴
        plt.xlabel("时间", fontsize=30)
        plt.ylabel("幅值", fontsize=30)
        # 坐标轴刻度字体大小
        plt.tick_params(labelsize=30)
        # 传入数据并绘制图形
        plt.plot(list_data)
        # 保存图片
        fig_name = "D:\\PycharmProjects\\pythonProject\\fig\\" + file_name + ".png"
        plt.savefig(fig_name)
        # 展示图片
        # plt.show()
    print("ok")
