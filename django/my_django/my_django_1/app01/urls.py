# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 17:15
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from . import views

urlpatterns = [
    url('login/', views.login),
    url('layout/', views.layout),
    url('index/',views.index),
    url('pic/',views.pic),

]
