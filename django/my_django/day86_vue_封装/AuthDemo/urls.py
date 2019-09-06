# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 19:49
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/', views.RegisterView.as_view()),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^test/', views.TestView.as_view()),
    url(r'^permission/', views.PermissionView.as_view()),
]
