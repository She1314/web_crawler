import time

import scrapy
import logging
from myscrapy02.items import TaoCheItem, DetailItem


class TaocheSpider(scrapy.Spider):
    name = 'taoche'
    # allowed_domains = ['www.taoche.com']
    start_urls = ['https://beijing.taoche.com/audi/?page=%s']

    def parse(self, response):
        # 获取最大页数。获取最大页数的标签名
        max_page = response.xpath('//div[@class="paging-box the-pages"]/div/a[last()-1]/text()').extract_first()
        for i in range(1, 2):
            url = self.start_urls[0] % i
            yield scrapy.Request(url=url, callback=self.parse_html, meta={'page': i})
        logging.warning(msg=max_page)

    def parse_html(self, response):
        # time.sleep(5)
        for li in response.xpath('//*[@id="container_base"]/ul/li'):
            title = li.xpath('./div[2]/a/span/text()').extract_first()
            image_name = li.xpath('./div[1]/div/a/img/@src').extract_first()
            price = li.xpath('./div[2]/div[1]/i/text()').extract_first()
            buy_date = li.xpath('./div[2]/p/i[1]/text()').extract_first()
            mileage = li.xpath('./div[2]/p/i[2]/text()').extract_first()
            city = li.xpath('./div[2]/p/i[3]/text()').extract_first().strip()
            detail_url = li.xpath('./div[1]/div/a/@href').extract_first()
            # print(title, buy_date, image_name, price, mileage, city)
            item = TaoCheItem()
            item['title'] = title
            item['image_name'] = image_name
            item['price'] = price
            item['buy_date'] = buy_date
            item['mileage'] = mileage
            item['city'] = city
            yield scrapy.Request(
                url=detail_url,
                callback=self.detail_parse,
                meta={'item': item}
            )

    def detail_parse(self, response):
        time.sleep(2)
        attrs = response.xpath('//div[@class="summary-attrs"]/dl[3]/dd/text()').extract_first()
        displacement, gearbox = tuple(attrs.split('/'))
        detail = DetailItem()
        detail['gearbox'] = gearbox
        detail['displacement'] = displacement
        # logging.warning(attrs)
        item = response.meta['item']
        item['detail'] = detail
        logging.warning(item)
        # return item
