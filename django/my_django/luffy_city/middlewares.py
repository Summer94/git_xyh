# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 21:14
# @Author  : summer
# @File    : middlewares.py
# @Software: PyCharm

from django.utils.deprecation import MiddlewareMixin

class MyCores(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Headers"] = "Content-Type, AUTHENTICATION"
            response["Access-Control-Allow-Methods"] = "DELETE, PUT, PATCH"
        return response