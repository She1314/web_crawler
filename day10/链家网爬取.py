#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 22:13
# @Author : XXX
# @Site : 
# @File : 链家网爬取.py
# @Software: PyCharm
from requests_html import HTMLSession
import aiohttp
import asyncio
from lxml import etree

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36 "
}


async def async_parse(url):
    session = aiohttp.ClientSession()
    response = await session.get(url=url, headers=header)
    result = await response.text()
    result_text = await parse_html(html=result)
    await session.close()
    return result_text


async def parse_html(html):
    tree = etree.HTML(html)
    data = []
    for li in tree.xpath('//ul[@class="sellListContent"]/li'):
        title = li.xpath('.//div[1]/div[1]/a/text()')
        data += title
    return data


async def info_html(url):
    print("采集信息", url)
    result = await async_parse(url=url)
    print("解析完成：", result)
    return result


tasks = []
home_url = 'https://sh.lianjia.com/ershoufang/pg%s/'
for i in range(1, 3):
    continue_url = info_html(url=home_url % i)
    task = asyncio.ensure_future(coro_or_future=continue_url)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(fs=tasks))
