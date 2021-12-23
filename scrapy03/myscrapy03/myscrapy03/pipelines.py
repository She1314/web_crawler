# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017)
db = client.spider
collection = db.wuyou


class Myscrapy03Pipeline:
    def process_item(self, item, spider):
        return item


class WuYouPipeline:
    def process_item(self, item, spider):
        if spider.name == 'wuyou':
            print(dict(item))
            collection.insert_one(dict(item))
            return item
