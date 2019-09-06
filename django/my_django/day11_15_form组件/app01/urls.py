# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 15:45
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'register/', views.register, name="register"),
    url(r'summer/', views.summer, name="summer"),
    url(r'check_regist/', views.check_regist, name="check_regist"),
    url(r'index/', views.index, name="index"),
]