#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 19:30
# @Author : XXX
# @Site : 
# @File : 多线程爬取.py
# @Software: PyCharm
from requests_html import HTMLSession
import asyncio
from multiprocessing.pool import Pool
import time


def parse_html(num):
    print("开始爬取：")
    time.sleep(2)
    print("爬取结束")


if __name__ == '__main__':
    iter_obj = [1, 2, 3, 4, 5, 6, 7, 8]
    pool = Pool(5)
    result = pool.map(parse_html, iter_obj)
    print(result)
