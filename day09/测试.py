#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/3 17:47
# @Author : XXX
# @Site : 
# @File : 测试.py
# @Software: PyCharm
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.chazidian.com/xiaohua/'

response = session.get(url=url)

for i in response.html.xpath('//div[@class="cotlet"]/div'):
    print(i.xpath('//div[@class="arctcot"]/h3/a/text()'))




