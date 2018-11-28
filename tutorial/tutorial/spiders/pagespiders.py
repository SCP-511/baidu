# -*- coding:utf-8 -*-

import scrapy
import datetime
from scrapy.linkextractor import LinkExtractor
from items import *
from spiders.basespiders import BaseSpider


class PageSpider(BaseSpider):
    """
    获取分页链接
    """
    name = None

    def __init__(self, rule):
        next_step = 'detail'
        item = PageItem()
        next_name = 'detail'
        super(PageSpider, self).__init__(rule, next_step, item, next_name)
