# -*- coding:utf-8 -*-

import schedule
import time
import pymongo
from utils import get_mongod


def job():
    """
    批量更新config表中的数据status=0
    :return:
    """
    db = get_mongod()
    db.config.update({"status": 1}, {"$set": {"status": 0}}, multi=True, upsert=False)
    print('ok')

# schedule.every(0.5).minutes.do(job) # 每隔n分钟执行一次任务
# schedule.every().hour.do(job) # 每隔一小时执行一次任务
# schedule.every().day.at("10:30").do(job) # 每天的10:30执行一次任务
schedule.every().monday.at("23:59").do(job)  # 每周一的这个时候执行一次任务
# schedule.every().wednesday.at("13:15").do(job)  # 每周三13:15执行一次任务

while True:
    schedule.run_pending()
    time.sleep(1)
