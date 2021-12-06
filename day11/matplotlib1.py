#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/6 17:36
# @Author : XXX
# @Site : 
# @File : matplotlib1.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np


# 绘制三角形函数
def draw_tri(points, color='red', alpha=0.5):
    plt.scatter(points[:, 1], points[:, 0], color=color, alpha=0.001)
    tri = plt.Polygon(points, color=color, alpha=alpha)
    plt.gca().add_patch(tri)


def draw_tri2(points2, color='white', alpha=1):
    plt.scatter(points2[:, 1], points2[:, 0], color=color, alpha=0.001)
    tri = plt.Polygon(points2, color=color, alpha=alpha)
    plt.gca().add_patch(tri)


# 三角形 点（x,y）
points1 = np.array([
    [0, 0],
    [0.5, 1],
    [1, 0]
])
points2 = np.array([
    [0.4, 0.4],
    [0.5, 0.2],
    [0.6, 0.4]
])
plt.figure()

# 显示三角形
draw_tri(points1)
draw_tri2(points2)
plt.show()
