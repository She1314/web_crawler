#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/23 12:55
# @Author : XXX
# @Site : 
# @File : selenium_COVID-19.py
# @Software: PyCharm
import time

from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia'


def browser_url():
    browser = webdriver.Chrome()
    browser.get(url=url)
    browser.execute_script("window.scrollTo(0, 6500)")

    browser.find_element(By.XPATH, '//*[@id="foreignTable"]/div').click()
    time.sleep(3)
    tree = etree.HTML(browser.page_source)
    for tr in tree.xpath('//table[@class="VirusTable_1-1-319_3U6wJT VirusTable_1-1-319_s83y8p"]/tbody/tr'):
        country = tr.xpath('./td/a/div[1]/text()|./td/div[@class="VirusTable_1-1-319_AcDK7v"]/text()')[0]
        add_num = tr.xpath('./td[2]/text()')[0]
        grand_total = tr.xpath('./td[3]/text()')[0]
        cure_num = tr.xpath('./td[4]/text()')[0]
        die_num = tr.xpath('./td[5]/text()')[0]
        print(country, add_num, grand_total, cure_num, die_num)


if __name__ == '__main__':
    browser_url()
