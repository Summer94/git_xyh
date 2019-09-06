# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 10:21
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/', views.ContentView.as_view()),

]