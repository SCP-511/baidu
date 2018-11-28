# -*- coding: utf-8 -*-

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# See https://doc.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    # 'scrapy_jsonrpc.webservice.WebService': 500,
    'scrapy.telnet.TelnetConsole': None
}
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tutorial.pipelines.TutorialPipeline': 300,
}

# MONGODB 主机名
MONGODB_HOST = "127.0.0.1"
# MONGODB 端口号
MONGODB_PORT = 27017
# 数据库名称
MONGODB_DBNAME = "tutorial"

#通用爬虫配置
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10  #100
#设置Log级别:
LOG_LEVEL = 'INFO'
#爬取深度
DEPTH_LIMIT = 1
# Disable cookies (enabled by default)
COOKIES_ENABLED = False
#禁止重试:
RETRY_ENABLED = True
#减小下载超时:
DOWNLOAD_TIMEOUT = 15
#关闭重定向:
REDIRECT_ENABLED = False
# 启用 “Ajax Crawlable Pages” 爬取
AJAXCRAWL_ENABLED = True
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# REDIS_URL = 'redis://127.0.0.1:6379'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"


START_URL = 'start_url'
DOWNLOAD_URL = 'download_url'
DETAIL_URL = 'detail_url'
DOWNLOAD_PATH = '/data/apps'
DOWNLOAD_APK_PATH = 'download_apk_path'

# 本机redis
REDIS_KEY = 'process'
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
# REDIS_PASSWORD = 'afc7c7180c3c43b51b1ebfebae76b5e8'
# REDIS_PARAMS = {
#     'password': 'afc7c7180c3c43b51b1ebfebae76b5e8',
# }
REDIS_CONF = {
    'host': REDIS_HOST,
    # 'password': REDIS_PASSWORD,
    'port': REDIS_PORT,
    'db': 0,
}

