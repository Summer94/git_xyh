# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 19:38
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views


urlpatterns = [
    url('login', views.login, name='login'),
    url('publisher_list/', views.publisher_list, name='publisher_list1'),
    url('add_publisher/', views.add_publisher, name='add_publisher1'),
    url('del_publisher/', views.del_publisher, name='del_publisher1'),
    url('edit_publisher/', views.edit_publisher, name='edit_publisher1'),

    url('book_list/', views.book_list, name='book_list'),
    url('add_book/', views.add_book, name='add_book'),
    url('del_book/', views.del_book, name='del_book'),
    url('edit_book/', views.edit_book, name='edit_book'),

    url('author_list/', views.author_list, name='author_list'),
    url('add_author/', views.add_author, name='add_author'),
    url('del_author/', views.del_author, name='del_author'),
    url('edit_author/', views.edit_author, name='edit_author'),

    url('admin/', views.admin, name='admin')

]