import time

from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(url='https://www.jd.com/')
browser.find_element(By.ID, 'key').send_keys('笔记本')
browser.find_element(By.CLASS_NAME, 'button').click()
time.sleep(3)
tree = etree.HTML(browser.page_source)
# print(tree.xpath('//div[@class="J_goodsList"]/ul'))
for i in tree.xpath('//div[@id="J_goodsList"]/ul/li'):
    print(i.xpath('./div[@class="gl-i-wrap"]/div[3]/a/em/text()'))