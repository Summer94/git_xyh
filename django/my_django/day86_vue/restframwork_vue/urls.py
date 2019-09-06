# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 16:52
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'book_list/', views.BookView.as_view(),),
    url(r'publisher_list/', views.PublisherView.as_view(),),
    url(r'author_list/$', views.AuthorView.as_view(),),
    url(r'author_list_edit/(?P<id>\d+)/', views.EditAuthorView.as_view(),),
]