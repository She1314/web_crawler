#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/8 21:31
# @Author : XXX
# @Site : 
# @File : selenuim.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url='https://qzone.qq.com/')
# browser.find_element_by_id()
browser.switch_to.frame('login_frame')
browser.find_element(By.ID, 'switcher_plogin').click()


browser.find_element(By.XPATH())