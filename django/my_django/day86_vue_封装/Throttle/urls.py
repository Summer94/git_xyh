# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 20:49
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'test/',views.TestView.as_view()),
]