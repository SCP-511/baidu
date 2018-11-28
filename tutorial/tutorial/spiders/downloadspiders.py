# -*- coding:utf-8 -*-

import scrapy
import datetime
import os, sys, stat, re
import urllib.request as urllib2
import random
import json
import string
from scrapy.linkextractor import LinkExtractor
from items import *
from spiders.basespiders import BaseSpider
from settings import DOWNLOAD_APK_PATH, DOWNLOAD_PATH
from backend import RedisBackend
sys.path.append('../')
from utils import get_mongod


def downloadapp(url, rule, item):
    print(url)
    # try:
    f = urllib2.urlopen(url)
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 32))
    path = os.path.join(DOWNLOAD_PATH, ran_str)
    with open(path, "wb") as code:
        code.write(f.read())
    os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    _data = {
        'domain_name': rule['domain_name'],
        'allowed_domains': rule['allowed_domains'],
        'storage': path,
        'appname': item['appname'],
        'downloadnumber': item['downloadnumber']
    }
    print(rule['domain_name'])
    print(rule['allowed_domains'])
    print(path)
    print(item['appname'])
    print(item['downloadnumber'])
    # _data = json.dumps(_data)
    # backend.send(DOWNLOAD_APK_PATH, _data)
    client = get_mongod()
    print(client)
    tb = client['apps']
    print(tb)
    print(_data)
    tb.insert(_data)
    # except:
    #     pass


class DownloadSpider(BaseSpider):
    """
    获取下载链接，并下载app
    """
    name = None

    def __init__(self, rule):
        next_step = 'app'
        item = DownloadItem()
        next_name = 'app'
        super(DownloadSpider, self).__init__(rule, next_step, item, next_name)

    def parse(self, response):
        link = LinkExtractor(restrict_xpaths=self.restrict_xpaths)
        links = link.extract_links(response)
        for i in links:
            self.item['link'] = i.url
            self.item['text'] = i.text
            self.item['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.item['status'] = 0
            _rule = self.rule
            _rule['start_urls'] = [i.url]
            _rule['name'] = self.next_name
            _rule['step'] = self.next_step
            self.item['rule'] = _rule
            print(self.rule)

            self.item['appname'] = response.xpath(self.rule['app_name']).extract()[0]
            downloadnumber = response.xpath(self.rule['downloadnumber']).extract()[0]
            self.item['downloadnumber'] = re.findall('\d+', downloadnumber)[0]
            downloadapp(i.url, _rule, self.item)
            # print self.item
            yield self.item
