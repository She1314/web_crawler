#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/6 20:15
# @Author : XXX
# @Site : 
# @File : index.py
# @Software: PyCharm
import aiohttp
import asyncio

url = 'https://tieba.baidu.com/f?kw=%E8%B5%9B%E5%8D%9A%E6%9C%8B%E5%85%8B2077'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}


async def info_html(url):
    session = aiohttp.ClientSession()
    response = await session.get(url=url, headers=headers)
    return response.headers

coroutine = info_html(url=url)
loop = asyncio.get_event_loop()
task =loop.create_task(coro=coroutine)
print(task)
print(loop.run_until_complete(future=task))
print(task)