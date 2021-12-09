#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/9 21:38
# @Author : XXX
# @Site : 
# @File : selenium动作.py
# @Software: PyCharm
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
browser = webdriver.Chrome()

browser.get(url='https://qzone.qq.com/')

browser.switch_to.frame('login_frame')

browser.find_element(By.ID, 'switcher_plogin').click()

browser.find_element(By.ID, 'u').send_keys('2185902575')
browser.find_element(By.ID, 'p').send_keys('20196768xd666')
browser.find_element(By.ID, 'login_button').click()

time.sleep(5)
action = ActionChains(browser)
# ActionChains(browser).move_to_element(friend).perform()

browser.find_element(By.ID, 'aMyFriends').click()
# action.click_and_hold(div)
tree = etree.HTML(browser.page_source)
print(browser.page_source)
guo = tree.xpath('//a[@class="user-name textoverflow"]/text()')
# div = browser.find_element(By.CLASS_NAME, 'app_canvas_frame')
print("ok")
print(guo)
# browser.switch_to.frame(div)
# print(browser.find_element(By.ID, '//div[@class="qz-rank-list"]/ol[2]/li'))

# tree = etree.HTML(browser.page_source)
# guo = tree.xpath('//div[@class="qz-rank-list"]/ol[2]/li')
# print(guo)
# print(browser.find_element(By.XPATH, '//div[@class="bd"]/ul/li/a/span'))