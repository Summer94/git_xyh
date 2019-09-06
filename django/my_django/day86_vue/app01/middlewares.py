# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 19:37
# @Author  : summer
# @File    : middlewares.py
# @Software: PyCharm

from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class VueMiddlerware(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        if request.method == "OPTIONS":
            # 证明它是复杂请求先发预检
            response["Access-Control-Allow-Methods"] = "DELETE, POST"
            response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
