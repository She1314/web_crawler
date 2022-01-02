#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/25 17:30
# @Author : XXX
# @Site : 
# @File : index.py
# @Software: PyCharm
from requests_html import HTMLSession
from lxml import etree
from selenium import webdriver
session = HTMLSession()
bro = webdriver.Chrome()
# response = session.get(url='https://news.163.com/domestic/')
bro.get(url='https://news.163.com/domestic/')
tree = etree.HTML(bro.page_source)
for div in tree.xpath('//div[@class="ndi_main"]/div'):
    print(div.xpath('./div/div[1]/h3/a/text()'))