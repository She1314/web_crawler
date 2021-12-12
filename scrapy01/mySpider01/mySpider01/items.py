# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy01.Field()
    pass


class QiushiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy01.Field()
    author = scrapy.Field()
    content = scrapy.Field()


class LianJiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy01.Field()
    data = scrapy.Field()
