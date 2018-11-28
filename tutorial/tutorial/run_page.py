# -*- coding:utf-8 -*-

import pymongo
import json
import time
from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from spiders.pagespiders import PageSpider
from config import get_settings
from utils import get_mongod, get_front_date
from settings import REDIS_CONF, REDIS_KEY
from backend import RedisBackend


if __name__ == '__main__':
    settings = get_settings()
    backend = RedisBackend(REDIS_CONF)

    process = CrawlerProcess(settings)
    for i in range(0, 20):
        data = backend.accept('%s_%s' % (REDIS_KEY, 'page'))
        if not data:
            break
        _d = eval(data)
        process.crawl(PageSpider, _d['rule'])
    process.start()

    # settings = get_settings()
    # db = get_mongod()
    # # 加载设置
    # process = CrawlerProcess(settings)
    # date = get_front_date()
    # data = db.category.find({'status': 0, 'date': {'$gt': date}}).sort('date', -1).limit(20)
    # for i in data:
    #     print i['rule']
    #     process.crawl(PageSpider, i['rule'])
    #     i['status'] = 1  # 标记已经爬取
    #     print {"_id": i['_id']}, {"$set": {"status": 1}}
    #     db.category.update({"_id": i['_id']}, {"$set": {"status": 1}})
    # process.start()
