# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings


class TutorialPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        self.sheetname = None
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        self.mydb = client[dbname]
        # # 存放数据的数据库表名
        self.post = None

    def process_item(self, item, spider):
        if self.sheetname != item.table_name:
            self.sheetname = item.table_name
            self.post = self.mydb[self.sheetname]
        else:
            self.post = self.mydb[item.table_name]

        data = dict(item)
        self.post.insert(data)
        return item
