#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/2 17:58
# @Author : 佘俊男
# @Site : 
# @File : index.py
# @Software: PyCharm
import time

from requests_html import HTMLSession


class YouLaiSpider:
    def __init__(self):
        self.session = HTMLSession()
        self.home_url = 'https://www.youlai.cn/'
        self.level_two_url = ''
        self.level_three_url = ''

    def parseLevelOne(self, levelUrl):
        response = self.session.get(url=levelUrl)
        levelUrl_second_url = response.html.xpath('//dl[@class="article_l_top disSearchMargin"]/dd/p/a/@href')
        levelUrl_second_title = response.html.xpath('//dl[@class="article_l_top disSearchMargin"]/dd/p/a/text()')
        for i in range(len(levelUrl_second_url)):
            # print(levelUrl_second_url[i], levelUrl_second_title[i])
            self.parseArticle(url=levelUrl_second_url[i], title=levelUrl_second_title[i])
        self.parseLevelThird(levelUrl_second_url=levelUrl_second_url)

    def parseLevelThirdArticle(self, Article_url):
        url = Article_url.replace('.html', '_%s.html' % 1)
        response_text = self.session.get(url=url)
        article = response_text.html.xpath(
            '//ul[@class="article_left article_l_list bd_none"]/li/dl[@class="con"]/p[1]/text()')
        print(article)

    def parseLevelThird(self, levelUrl_second_url):
        response_level_three_url = self.session.get(url='https://www.youlai.cn/dise/pk_1_12_1.html')
        # print(response_level_three_url.text)
        self.level_three_url = response_level_three_url.html.xpath('//dl[@class="textList"]/dt/a/@href')
        print(len(self.level_three_url))
        for url in self.level_three_url:
            self.parseLevelThirdArticle(Article_url=(self.home_url + url).replace('/dise', 'dise/articlelist'))
            time.sleep(2)

    def parseArticle(self, url, title):
        # self.level_two_url = url
        # Article_url = (self.home_url + self.level_two_url).replace('/dise', '/dise/articlelist')
        # print(Article_url)
        pass


if __name__ == '__main__':
    index_url = 'https://www.youlai.cn/dise/pk_1_12_1.html'
    youlai = YouLaiSpider()
    youlai.parseLevelOne(levelUrl=index_url)
