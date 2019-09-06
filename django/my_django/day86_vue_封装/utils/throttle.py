# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 20:53
# @Author  : summer
# @File    : throttle.py
# @Software: PyCharm
import time
from rest_framework import throttling

class MyThrottle(throttling.BaseThrottle):
    VisitRecord = {}
    def __init__(self):
        self.history = ""

    def allow_request(self, request, view):
        ip = request.MEAT.get("REMOTE_ADDR")
        now = time.time()
        if ip not in self.VisitRecord:
            self.VisitRecord[ip] = [now,]
            return True
        history = self.VisitRecord.get(ip)
        history.insert(0, now)
        self.history = history
        while history and now - history[-1] > 60:
            history.pop()
        if len(history) > 3:
            return False
        else:
            return True

    def wait(self):
        return self.history[-1] - self.history[0] + 60

class MyVisit(throttling.SimpleRateThrottle):
    scope = "tr"
    def get_cache_key(self, request, view):
        # 返回值应该IP
        return self.get_ident(request)






