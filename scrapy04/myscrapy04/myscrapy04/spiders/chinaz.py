import logging

import scrapy
from ..items import ChinazItem


class ChinazSpider(scrapy.Spider):
    name = 'chinaz'
    # allowed_domains = ['chinz.com']
    start_urls = ['https://sc.chinaz.com/tupian/meinvxiezhen.html']

    def parse(self, response):
        for url in response.xpath('//div[@id="container"]/div'):
            image_url = 'https://' + url.xpath('./div/a/img/@src2').extract_first().replace('_s', '')
            item = ChinazItem()
            item['image_url'] = image_url
            logging.warning(image_url)
            yield item
