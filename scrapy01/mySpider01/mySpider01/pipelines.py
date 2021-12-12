# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Myspider01Pipeline:
    def process_item(self, item, spider):
        return item


class QiuShiPipeline:
    fp = None

    def open_spider(self, spider):
        if spider.name == 'qiushi':
            self.fp = open(file='qiushi.json', mode='w', encoding='utf-8')
            print("开始爬取")

    def process_item(self, item, spider):
        if spider.name == 'qiushi':
            self.fp.write(f'{item["author"]}:{item["content"]}')
            return item

    def close_spider(self, spider):
        if spider.name == 'qiushi':
            print("结束爬取")
            self.fp.close()

