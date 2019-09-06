# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 20:45
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^book', views.BookView.as_view()),
]
