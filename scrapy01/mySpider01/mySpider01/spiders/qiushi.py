import scrapy
from mySpider01.items import QiushiItem


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['www.qiushibaike.com/text/']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        for div in response.xpath('//div[@id="content"]/div/div[2]/div'):
            author = div.xpath('.//div[1]/a[2]/h2/text()').extract_first()
            content = ''.join(div.xpath('./a[1]/div/span/text()').extract()).replace('\n', '')
            # print(author, content)
            qiushi = QiushiItem()
            qiushi['author'] = author
            qiushi['content'] = content
            yield qiushi
