# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 21:41
# @Author  : summer
# @File    : paginator.py
# @Software: PyCharm

from rest_framework import pagination

#
class MyPagination(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = "size"
    max_page_size = 4


# class MyPagination(pagination.LimitOffsetPagination):
#     default_limit = 3
#     limit_query_param = 'limit'
#     offset_query_param = 'offset'
#     max_limit = 10


# class MyPagination(pagination.CursorPagination):
#     cursor_query_param = 'cursor'
#     page_size = 3
#     ordering = '-id'
#     page_size_query_param = "size"
#     max_page_size = 3