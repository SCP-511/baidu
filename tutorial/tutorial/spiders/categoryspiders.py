# -*- coding:utf-8 -*-

import scrapy
import datetime
from scrapy.linkextractor import LinkExtractor
from items import *
from spiders.basespiders import BaseSpider


class CategorySpider(BaseSpider):
    """
    获取分类链接
    """
    name = None

    def __init__(self, rule):
        next_step = 'page'
        item = CategoryItem()
        next_name = 'page'
        super(CategorySpider, self).__init__(rule, next_step, item, next_name)
