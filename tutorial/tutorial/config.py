# -*- coding:utf-8 -*-

import pymongo
import json
import time
from multiprocessing import Process
# from spiders.links_category import CategorySpider
# from spiders.links_listpage import ListPageSpider
# from spiders.links_detailpage import DetailPageSpider
# from spiders.links_download import DownloadSpider
from spiders.basespiders import BaseSpider
from spiders.categoryspiders import CategorySpider
from spiders.pagespiders import PageSpider
from spiders.detailspiders import DetailSpider
from spiders.downloadspiders import DownloadSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from utils import get_mongod
#spider相关设置
settings = get_project_settings()


'''
Scrapy框架的高度灵活性得益于其数据管道的架构设计，开发者可以通过简单的配置就能轻松地添加新特性。
我们可以通过如下的方式添加pipline。
'''
# settings.set("ITEM_PIPELINES" , {
#     'pipelines.DuplicatesPipeline': 200,
#     'pipelines.IpProxyPoolPipeline': 300,
# })

#设置默认请求头
settings.set("DEFAULT_REQUEST_HEADERS",{
  'Accept': 'text/html, application/xhtml+xml, application/xml',
  'Accept-Language': 'zh-CN,zh;q=0.8'}
)

#注册自定义中间件，激活切换UA的组件和切换代理IP的组件
settings.set("DOWNLOADER_MIDDLEWARES",{
   'useragent_middlewares.UserAgent': 1,
   # 'proxy_middlewares.ProxyMiddleware':100,
   # 'scrapy.downloadermiddleware.useragent.UserAgentMiddleware' : None,
})
#设置爬取间隔
settings.set("DOWNLOAD_DELAY", 2)

#禁用cookies
settings.get("COOKIES_ENABLED",False)

#设定是否遵循目标站点robot.txt中的规则
settings.get("ROBOTSTXT_OBEY",True)


def get_settings():
    return settings


if __name__ == '__main__':
    db = get_mongod()
    # 加载设置
    process = CrawlerProcess(settings)
    flag = False

    data = db.detail.find({'status': 0})
    for i in data[:10]:
        process.crawl(DownloadSpider, i['rule'])
        i['status'] = 1  # 标记已经爬取
        db.detail.update({"_id": i['_id']}, {"$set": {"status": 1}})
    process.start()