# -*- coding:utf-8 -*-

import pymongo
import json
import time
from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from spiders.categoryspiders import CategorySpider
from config import get_settings
from utils import get_mongod, get_front_date


if __name__ == '__main__':
    settings = get_settings()
    db = get_mongod()
    # 加载设置
    process = CrawlerProcess(settings)

    data = db.config.find({'status': 0}).limit(1)
    for i in data:
        print(i)
        process.crawl(CategorySpider, i['rule'])
        i['status'] = 1  # 标记已经爬取
        # print {"_id": i['_id']}, {"$set": {"status": 1}}
        db.config.update({"_id": i['_id']}, {"$set": {"status": 1}})
    process.start()
