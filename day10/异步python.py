#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 20:10
# @Author : XXX
# @Site : 
# @File : 异步python.py
# @Software: PyCharm
import asyncio


async def parse(url):
    print("开始爬取：", url)
    print("结束爬取：", url)
    return url


result = parse(url="www.baidu.com")
loop = asyncio.get_event_loop()
loop.run_until_complete(result)
