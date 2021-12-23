# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging

from itemadapter import ItemAdapter
import pymysql
from pymongo import MongoClient

user = 'root'
password = '824921'
port = 3306
database = 'spider'
host = '127.0.0.1'


# conn = pymysql.connect(user=user, host=host, port=port, database=database, password=password)

# cursor = conn.cursor()


class Myscrapy02Pipeline:
    def process_item(self, item, spider):
        return item


class QiuBaiPipeline:
    def process_item(self, item, spider):
        if spider.name == 'qiubai':
            # cursor.execute(f'''insert into qiubai(neckname, joke) values ("{item['author']}", "{item['content']}")''')
            # conn.commit()
            return item


host_mongo = '127.0.0.1'
client = MongoClient(host=host_mongo, port=27017)
db = client.spider
collection = db.taoche


class TaoChePipeline:
    def process_item(self, item, spider):
        if spider.name == 'taoche':
            collection.insert_one(dict(item))
            return item
