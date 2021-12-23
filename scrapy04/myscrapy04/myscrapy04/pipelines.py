# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class Myscrapy04Pipeline:
    def process_item(self, item, spider):
        return item


class ChinaZPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        logging.warning(msg=item['image_url'])
        yield scrapy.Request(item['image_url'])

    def file_path(self, request, response=None, info=None, *, item=None):
        img_name = request.url.split('/')[-1]
        return img_name

    def item_completed(self, results, item, info):
        return item
