# -*- coding:utf-8 -*-

import scrapy
import datetime
from scrapy.linkextractor import LinkExtractor
from items import *
from spiders.basespiders import BaseSpider


class DetailSpider(BaseSpider):
    """
    获取详情链接
    """
    name = None

    def __init__(self, rule):
        next_step = 'download'
        item = DetailItem()
        next_name = 'download'
        super(DetailSpider, self).__init__(rule, next_step, item, next_name)
