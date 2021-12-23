import logging
import time

import scrapy
import setuptools.command.bdist_rpm
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from myscrapy03.items import WuYouItem


class WuyouSpider(scrapy.Spider):
    name = 'wuyou'
    # allowed_domains = ['www.51job.com']
    start_urls = ['http://www.51job.com/']

    def __init__(self):
        self.bro = webdriver.Chrome()
        super().__init__()

    def parse(self, response):
        key = input("请输入你要爬取的岗位：")
        self.bro.find_element(By.ID, 'kwdselectid').send_keys(key)
        self.bro.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/button').send_keys(Keys.ENTER)
        time.sleep(3)
        start_url = self.bro.current_url
        logging.warning(start_url)
        yield scrapy.Request(url=start_url, callback=self.wuyou_parse)

    def wuyou_parse(self, response):
        for div in response.xpath('//div[@class="j_joblist"]/div'):
            jop = div.xpath('./a/p[1]/span[1]/text()').extract_first()
            salary = div.xpath('./a/p[2]/span[1]/text()').extract_first()
            place = div.xpath('./a/p[2]/span[2]/text()').extract_first()
            logging.warning(msg=(jop, place, salary))
            item = WuYouItem()
            item['jop'] = jop
            item['salary'] = salary
            item['place'] = place
            yield item
        if self.bro.find_element(By.XPATH, '//li[@class="next"]'):
            self.bro.find_element(By.XPATH, '//li[@class="next"]').click()
            logging.warning(self.bro.current_url)
            yield scrapy.Request(url=self.bro.current_url, callback=self.wuyou_parse)

    def closed(self, spider):
        print('关闭浏览器对象!')
        self.bro.quit()
