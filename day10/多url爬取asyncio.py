#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 20:44
# @Author : XXX
# @Site : 
# @File : 多url爬取asyncio.py
# @Software: PyCharm
import asyncio
from time import sleep


async def parse(url):
    print("开始爬取：", url)
    await asyncio.sleep(1)
    print("爬取结束：", url)
    return url


urls = [
    "https://tieba.baidu.com/",
    "https://tieba.baidu.com/1",
    "https://tieba.baidu.com/2",
    "https://tieba.baidu.com/3",
    "https://tieba.baidu.com/4",
    "https://tieba.baidu.com/5"
]
tasks = []
for i in urls:
    result = parse(url=i)
    task = asyncio.ensure_future(coro_or_future=result)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(fs=tasks))
