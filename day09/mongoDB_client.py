#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/3 16:19
# @Author : XXX
# @Site : 
# @File : mongoDB_client.py
# @Software: PyCharm
import pymongo

client = pymongo.MongoClient()

db = client['spider']

collections = db['stu']
print(tuple(collections.find()))