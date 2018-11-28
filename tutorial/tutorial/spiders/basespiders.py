# -*- coding:utf-8 -*-

import scrapy
import datetime
from scrapy.linkextractor import LinkExtractor
from items import *
from backend import RedisBackend
from settings import REDIS_CONF, REDIS_KEY


class BaseSpider(scrapy.Spider):
    """
    基础类
    """
    name = None

    def __init__(self, rule, next_step, item, next_name):
        self.rule = rule
        self.name = rule['name']
        self.next_step = next_step
        # spilt函数通过分隔符分割字符串，得到列表类型
        self.allowed_domains = rule['allowed_domains']
        self.start_urls = rule['start_urls']
        self.restrict_xpaths = rule['%s_xpaths' % rule['step']]
        self.item = item
        self.next_name = next_name
        super(BaseSpider, self).__init__()

    def parse(self, response):
        link = LinkExtractor(restrict_xpaths=self.restrict_xpaths)
        links = link.extract_links(response)
        for i in links:
            self.item['link'] = i.url
            self.item['text'] = i.text
            self.item['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.item['status'] = 0
            _rule = self.rule
            print(self.rule)
            _rule['start_urls'] = [i.url]
            _rule['name'] = self.next_name
            _rule['step'] = self.next_step
            self.item['rule'] = _rule
            print(_rule)
            backend = RedisBackend(REDIS_CONF)
            backend.send('%s_%s' % (REDIS_KEY, self.next_name), str(self.item))
            # print self.item
            yield self.item
