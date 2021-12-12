import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['sh.lianjia.com/ershoufang/']
    start_urls = ['http://sh.lianjia.com/ershoufang//']

    def parse(self, response):
        for div in response.xpath('//div[@id="content"]/div[1]/ul/li'):
            # author = div.xpath('.//div[1]/a[2]/h2/text()')
            data = div.xpath('./div[1]/div[1]/a/text()')
            print(data)
