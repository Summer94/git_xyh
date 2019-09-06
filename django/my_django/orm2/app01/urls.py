# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 11:24
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views



urlpatterns = [
    url('login/', views.login, name='login'),
]