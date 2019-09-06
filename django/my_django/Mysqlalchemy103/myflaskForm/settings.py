# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 16:19
# @Author  : summer
# @File    : settings.py
# @Software: PyCharm

import redis

class DevConfig(object):
    DEBUG = True
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.Redis(host="127.0.0.1", port=6379)

    #sqlalchemy配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/day104?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_MAX_OVERFLOW = 3
    SQLALCHEMY_TRACK_MODIFICATIONS = False
