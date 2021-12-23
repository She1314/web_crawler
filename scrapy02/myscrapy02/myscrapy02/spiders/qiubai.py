import scrapy
from ..items import QiuBaiItem
import logging


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['qiubai.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        for div in response.xpath('//div[@id="content"]/div/div[2]/div'):
            author = div.xpath('.//div[1]/a[2]/h2/text()').extract_first().strip()
            content = ''.join(div.xpath('./a[1]/div/span/text()').extract()).replace('\n', '')
            # print(author, content)
            # logging.warning(author)
            qiushi = QiuBaiItem()
            qiushi['author'] = author
            qiushi['content'] = content
            yield qiushi
        next_url = response.xpath('//div[@id="content"]/div/div[2]/ul/li[last()]/a/@href').extract_first()
        print(next_url)
        i = 0
        a = i
        if next_url:
            next_url = 'https://www.qiushibaike.com' + next_url
            a += 1
            i = a
            print(f"第{i}页爬取完成")
            return scrapy.Request(url=next_url, callback=self.parse)
        # yield qiushi
