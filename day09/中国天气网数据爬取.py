#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/3 16:05
# @Author : XXX
# @Site :
# @File : 中国天气网数据爬取.py
# @Software: PyCharm
from requests_html import HTMLSession
import pymongo


class WeatherSpider:
    def __init__(self):
        self.session = HTMLSession()
        self.url = 'https://www.tianqi.com/chinacity.html'
        self.conn = pymongo.MongoClient()

    def parseData(self):
        response = self.session.get(url=self.url)
        for data in response.html.xpath('//div[@class="citybox"]/h2/a | //div[@class="citybox"]/span/a'):
            place_name = data.xpath('//a/text()')[0]
            place_href = data.xpath('//a/@href')[0]
            print(place_href)
            from_data = {'地名': place_name, '地址': 'https://www.tianqi.com' + place_href}
            self.mongodb_data(from_data=from_data)

    def mongodb_data(self, from_data):
        # 连接mongoDB数据库Spider
        conn_spider_db = self.conn['spider']
        conn_spider_collections = conn_spider_db['weather']
        conn_spider_collections.insert_one(from_data)


if __name__ == '__main__':
    spider = WeatherSpider()
    spider.parseData()
