# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 20:40
# @Author  : summer
# @File    : versions.py
# @Software: PyCharm

# 版本控制类
class Myversion(object):
    def determine_version(self, request, *args, **kwargs):
        version = request.query_params.get("version", "v1")
        return version