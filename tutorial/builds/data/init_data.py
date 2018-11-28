# -*- coding:utf-8 -*-

import os
import pymongo
from scrapy.utils.project import get_project_settings
settings = get_project_settings()
# os.environ['SCRAPY_SETTINGS_MODULE'] = 'tutorial.settings'
# settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
# settings.setmodule(settings_module_path, priority='project')
host = settings["MONGODB_HOST"]
port = settings["MONGODB_PORT"]
dbname = settings["MONGODB_DBNAME"]
# 创建MONGODB数据库链接
client = pymongo.MongoClient(host=host, port=port)
# 指定数据库
mydb = client[dbname]
# # 存放数据的数据库表名

data = [
    {
        'name': 'category',
        'step': 'category',
        'domain_name': u'百度',
        'allowed_domains': 'shouji.baidu.com',
        'start_urls': ['https://shouji.baidu.com/software/', 'https://shouji.baidu.com/game/'],
        'category_xpaths': '//ul[@class="cate-body"]/li',  # 获取分类links
        'page_xpaths': '//div[@class="pager"]/ul/li',  # 获取分页links
        'detail_xpaths': '//div[@class="app-bd"]/ul/li/a[@class="app-box"]',  # 获取详情links
        'download_xpaths': '//div[@class="area-download"]/a[@class="apk"]',  # 获取下载地址
        'app_name': '//div[@class="content-right"]/h1[@class="app-name"]/span/text()',  # app名
        'downloadnumber': '//div[@class="detail"]/span[@class="download-num"]/text()'  # 下载次数
    },
    {
        'name': 'category',
        'step': 'category',
        'domain_name': u'小米',
        'allowed_domains': 'app.mi.com',
        'start_urls': ['http://app.mi.com/'],
        'category_xpaths': '//h1[@class="sidebar-h"]/ul[@class="category-list"]/li',  # 获取分类links
        'page_xpaths': '//div[@class="main-h"]/a[@class="more"]',  # 获取分页links
        'detail_xpaths': '//ul[@class="applist"]/li/a',  # 获取详情links
        'download_xpaths': '//div[@class="app-info-down"]/a[@class="download"]',  # 获取下载地址
        'app_name': '//div[@class="app-info"]/div[@class="intro-titles"]/h3/text()',  # app名
        'downloadnumber': '//div[@class="app-info"]/div[@class="intro-titles"]/span[@class="app-intro-comment"]/text()'  # 下载次数
    }

]


def insert(data):
    print(host)
    db = mydb['config']
    for i in data:
        db.insert({'rule': i, 'status': 0})


if __name__ == '__main__':
    # 初始化聚焦爬虫 xpath
    insert(data)
