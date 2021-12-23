import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrtaocheSpider(CrawlSpider):
    name = 'crtaoche'
    allowed_domains = ['taoche.com']
    start_urls = ['http://taoche.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
