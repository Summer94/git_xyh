# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 15:09
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"login/", views.login),
]

