#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/25 15:48
# @Author : XXX
# @Site : 
# @File : wy.py
# @Software: PyCharm
# from selenium import webdriver
# from lxml import etree
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# bro = webdriver.Chrome()
#
# bro.get(
#     url='https://music.163.com/#/song?id=1367452194')
#
# bro.switch_to.frame('g_iframe')
#
# # tree = etree.HTML(bro.page_source)
# # content = bro.find_elements(By.CLASS_NAME, 'itm')
#
# tree = etree.HTML(bro.page_source)
# # print(tree.xpath('//div[@class="cmmts j-flag"]/div'))
# for div in tree.xpath('//div[@class="cmmts j-flag"]/div'):
#     content = div.xpath('./div[2]/div[1]/div//text()')
#     print(content)
