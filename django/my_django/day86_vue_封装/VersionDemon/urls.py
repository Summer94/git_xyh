# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 20:45
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from .views import VersionView

urlpatterns = [
    # 版本控制路由
    url(r'version_demo', VersionView.as_view()),
]
