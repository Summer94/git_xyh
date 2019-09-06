# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 15:39
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'login/',views.login, name='login'),
    url(r'app02_publisher/',views.app02_publisher, name='app02_publisher'),
    url(r'app02_login_out/',views.app02_login_out, name='app02_login_out'),
    url(r'xyh/',views.xyh, name='xyh'),
    url(r'foo/',views.Foo.as_view()),
]