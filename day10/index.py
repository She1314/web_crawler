#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 20:51
# @Author : XXX
# @Site : 
# @File : index.py
# @Software: PyCharm
import asyncio

async def parse_html(url):
    print("开始爬取：", url)
    print("结束爬取：", url)

result = parse_html(url="https://www.chzu.edu.cn")

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(result)
print(task)
loop.run_until_complete(future=task)
print(task)