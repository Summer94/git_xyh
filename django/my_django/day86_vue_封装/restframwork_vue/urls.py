# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 16:52
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
from app01.models import Book


urlpatterns = [
    # url(r'book_list/(?P<id>\d+)/$', views.EditBookView.as_view(), ),
    # url(r'book_list/$', views.BookView.as_view(), ),
    url(r'publisher_list/$', views.PublisherView.as_view(), ),
    url(r'author_list/$', views.AuthorView.as_view(), ),
    url(r'author_list_edit/(?P<id>\d+)/', views.EditAuthorView.as_view(), ),
]

# 第一步实例化对象
router = DefaultRouter()
# 第二步把路由以及视图注册
router.register('book_list', views.BookModelView)
urlpatterns += router.urls