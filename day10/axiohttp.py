#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 21:35
# @Author : XXX
# @Site : 
# @File : axiohttp.py
# @Software: PyCharm
import aiohttp
from requests_html import HTMLSession
import asyncio


async def get_html(url):
    print("开始爬取：", url)
    text = await parse_html(url=url)
    print("爬取结束", text)


async def parse_html(url):
    session = aiohttp.ClientSession()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    response = await session.get(url=url, headers=header)
    result = await response.text()

    headers = response.headers
    await session.close()
    return headers


urls = [
    "https://pic.netbian.com/e/search/result/index.php?page=1&searchid=45",
    "https://pic.netbian.com/e/search/result/index.php?page=2&searchid=45",
    "https://pic.netbian.com/e/search/result/index.php?page=3&searchid=45",
]
tasks = []
for i in urls:
    data = get_html(url=i)
    task = asyncio.ensure_future( data)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(future=asyncio.wait(fs=tasks))
