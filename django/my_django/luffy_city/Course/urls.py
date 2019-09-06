# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 19:42
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^category', views.CategoryView.as_view()),
    # id是课程分类的id
    url(r'^(?P<id>\d+)$', views.CourseView.as_view()),
    #获取课程详情
    url(r'detail/(?P<id>\d+)', views.CourseDetailView.as_view()),
    #课程章节以及课时表
    url(r'chapter/(?P<id>\d+)', views.ChapterView.as_view())


]
