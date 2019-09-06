# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 17:24
# @Author  : summer
# @File    : middleware.py
# @Software: PyCharm

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.conf import settings
import re

class RBACMiddleware(MiddlewareMixin):
    def process_request(self, request):
        #获取当前请求的url
        current_url = request.path_info
        #判断当前请求的url在不在白名单中
        for url in getattr(settings, "WHITE_URLS", []):
            #匹配得上就通过
            if re.match("^{}$".format(url), current_url):
                return
        key = getattr(settings, "PERMISSION_SESSION_KEY", "permission_list")
        permission_list = request.session.get(key, [])
        #根据url匹配权限
        for pattern in permission_list:
            if re.match('^{}$'.format(pattern), current_url):
                # 匹配成功，有权限，通过
                return None
        #匹配不到则没有权限，直接返回
        else:
            return HttpResponse('没有权限!!!!')

