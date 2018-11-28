# -*- coding:utf-8 -*-

import pymongo
import json
import time
from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from spiders.downloadspiders import DownloadSpider
from spiders.categoryspiders import CategorySpider
from config import get_settings
from utils import get_mongod, get_front_date
from settings import REDIS_CONF, REDIS_KEY
from backend import RedisBackend


if __name__ == '__main__':
    settings = get_settings()
    backend = RedisBackend(REDIS_CONF)

    process = CrawlerProcess(settings)
    for i in range(0, 20):
        data = backend.accept('%s_%s' % (REDIS_KEY, 'download'))
        if not data:
            break
        _d = eval(data)
        process.crawl(DownloadSpider, _d['rule'])
    process.start()

# if __name__ == '__main__':
#     settings = get_settings()
#     db = get_mongod()
#     # 加载设置
#     process = CrawlerProcess(settings)
#     date = get_front_date()
#     data = db.detail.find({'status': 0, 'date': {'$gt': date}}).sort('date', -1).limit(20)
#     for i in data:
#         process.crawl(DownloadSpider, i['rule'])
#         i['status'] = 1  # 标记已经爬取
#         db.detail.update({"_id": i['_id']}, {"$set": {"status": 1}})
#     process.start()
