#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/6 20:21
# @Author : XXX
# @Site : 
# @File : session.py
# @Software: PyCharm
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://tieba.baidu.com/f?kw=%E8%B5%9B%E5%8D%9A%E6%9C%8B%E5%85%8B2077'
response= session.get(url=url)
print(response.request.headers)
