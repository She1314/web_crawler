#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/3 13:47
# @Author : XXX
# @Site : 
# @File : weather.py
# @Software: PyCharm
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://weather.cma.cn/'
response = session.get(url=url)

a_list = response.html.xpath('//div[@id="HOT"]/a')
print(a_list)
for i in a_list:
    scrapy = i.xpath('//div[@class="rank"]/text() | //div[@class="sname"]/text()')[0]
    print(scrapy)

