#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/7 10:07
# @Author : XXX
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm
from multiprocessing.pool import Pool


def func(data):
    print("开始启动:", data)
    print("结束进程：", data)


if __name__ == '__main__':
    func(range(100))
    pool = Pool(9)
    pool.map(func, [i for i in range(100)])
