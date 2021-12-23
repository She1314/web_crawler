# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Myscrapy02Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QiuBaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy01.Field()
    author = scrapy.Field()
    content = scrapy.Field()


class TaoCheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy01.Field()
    title = scrapy.Field()
    image_name = scrapy.Field()
    price = scrapy.Field()
    buy_date = scrapy.Field()
    mileage = scrapy.Field()
    city = scrapy.Field()
    detail = scrapy.Field()


class DetailItem(scrapy.Item):
    displacement = scrapy.Field()
    gearbox = scrapy.Field()
