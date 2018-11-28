# -*- coding:utf-8 -*-

import datetime
import pymongo
from pymongo import MongoClient, database
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
#spider相关设置
settings = get_project_settings()
# MONGODB 主机名
MONGODB_HOST = "127.0.0.1"
# MONGODB 端口号
MONGODB_PORT = 27017
# 数据库名称
MONGODB_DBNAME = "tutorial"
host = MONGODB_HOST  # settings["MONGODB_HOST"]
port = MONGODB_PORT  # settings["MONGODB_PORT"]
dbname = MONGODB_DBNAME  # settings["MONGODB_DBNAME"]
# host = settings["MONGODB_HOST"]
# port = settings["MONGODB_PORT"]
# dbname = settings["MONGODB_DBNAME"]
# nodes = settings['NODES']


def get_domain(url):
    """
    通过url获取域名及协议
    :param url:
    :return: 域名 http[|s]://www.baidu.com，http or https
    """
    s = url.split('/')
    domain = None
    _http = 'http'
    for i in range(0, 3):
        if domain:
            domain = '%s/%s' % (domain, s[i])
        else:
            domain = s[i]
    if domain and len(domain) > 5:
        if 'https' == domain[:5]:
            _http = 'https'
    return domain, _http


def check_url_domain(url, _http, domain, is_domain=True, is_CH=False):
    """
    验证url的有效性
    :param url: 要验证的url
    :param _http: 本站点的http协议类型  http or  https
    :param domain: 本站点域名
    :param is_domain: 是否要求url为本站点域名下的 默认同域名
    :param is_CH: 是否容忍url中包含中文  默认不容忍
    :return:
    """
    # 必须为同一协议的url，且域名一致，且不包含中文，且url层级要高于domains层级，且url中不包含跳转  才会被收录
    rtn = False
    if len(url) > 5 and _http in url[:5]:  # 同一协议
        if not is_CH and '%' in url:  # 不包含中文
            pass
        elif len(url.split('/')) > 3 and len(url) > len(domain) + 1:  # url层级要高于domains层级
            if url.rfind('http') > 1:  # url中不包含跳转
                pass
            elif is_domain:
                # rtn =True
                if domain == url[:len(domain)]:
                    rtn = True
                else:
                    pass
            elif not is_domain:
                rtn = True
            else:
                pass
        else:
            pass
    return rtn


def get_mongod():
    """
    返回mongodb链接
    :return:
    """
    DB = database.Database(
        MongoClient(
            host=host,
            port=port,
            tz_aware=False,
            connect=True
            ),
        dbname
    )
    return DB


def get_front_date(num_days=30, date=datetime.datetime.now()):
    """
    给定 日期及 天数，推算出此日期在给定天数之前的日期
    :param date: 给定的日期
    :param num_days: 给定的天数
    :return: 返回日期-天数 后的 日期
    """
    delta = datetime.timedelta(days=num_days)
    n_days = date - delta
    return n_days.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    client = get_mongod()
    tb = client['apps']
    tb.insert({'k':'hah'})

