#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/10 0:10
# @Author : XXX
# @Site : 
# @File : 网易云.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from lxml import etree

url = 'https://music.163.com/#/song?id=65533'

browser = webdriver.Chrome()
# options = ChromeOptions()
# options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36')
browser.get(url=url)
# print(browser.page_source)
browser.switch_to.frame('g_iframe')
for i in browser.find_elements(By.CLASS_NAME, 'itm'):
    print(i.text)
# tree = etree.HTML(browser.page_source)
# print(tree.xpath('//div[id="auto-id-P5L0DEdMNfzaFKh5"]'))
