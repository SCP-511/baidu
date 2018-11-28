# -*- coding:utf-8 -*-

"""redis操作文件"""
# Third-Party imports
import redis
import json

# Project imports
from django.conf import settings


class RedisBackend(object):
    """
    Redis task result store.
    """

    def __init__(self, conf):
        self.redis = redis.Redis(**conf)

    def send(self, key, value):
        # logging
        self.redis.rpush(key, value)

    def lsend(self, key, value):
        # logging
        self.redis.lpush(key, value)

    def accept(self, key):
        return self.redis.lpop(key)

    def set_key_value(self, key, value):
        self.redis.set(key, value)

    def get_value(self, key):
        return self.redis.get(key)

    def get_allkeys(self, key):
        """
        模糊匹配
        """
        return self.redis.keys(key)

    def delete(self, key):
        self.redis.delete(key)

    def exists(self, key):
        return self.redis.exists(key)
