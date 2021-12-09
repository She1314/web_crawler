#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/9 20:29
# @Author : XXX
# @Site : 
# @File : qq音乐.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get(url='https://qzone.qq.com/')

browser.switch_to.frame('login_frame')

browser.find_element(By.ID, 'switcher_plogin').click()

browser.find_element(By.ID, 'u').send_keys('2185902575')
browser.find_element(By.ID, 'p').send_keys('密码')
browser.find_element(By.ID, 'login_button').click()
time.sleep(5)
print(browser.find_element(By.XPATH, '//div[@class="head-nav"]/ul/li[4]/a'))
# browser.find_element()