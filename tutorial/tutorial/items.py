# -*- coding: utf-8 -*-

import scrapy


class BaseItem(scrapy.Item):
    """
    基础类
    """
    table_name = 'base'
    # url
    link = scrapy.Field()
    # 文本
    text = scrapy.Field()
    # 时间
    date = scrapy.Field()
    # 状态
    status = scrapy.Field()
    # 规则配置
    rule = scrapy.Field()


class CategoryItem(BaseItem):
    """
    类别 links
    """
    table_name = 'category'


class PageItem(BaseItem):
    """
    分页 links
    """
    table_name = 'page'


class DetailItem(BaseItem):
    """
    详情页 links
    """
    table_name = 'detail'


class DownloadItem(BaseItem):
    """
    下载链接 links
    """
    table_name = 'download'
    appname = scrapy.Field()
    downloadnumber = scrapy.Field()
    # version = scrapy.Field()
