#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/9 21:02
# @Author : XXX
# @Site : 
# @File : index.py
# @Software: PyCharm
from requests_html import HTMLSession
from lxml import etree
url = 'https://sh.lianjia.com/ershoufang/'

session = HTMLSession()
response = session.get(url=url)
tree = etree.HTML(response.text)
for i in tree.xpath('//ul[@class="sellListContent"]/li'):
    print(i.xpath('./div[@class="info clear"]/div/span/text()'))
