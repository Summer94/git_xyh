# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 15:39
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register/', views.register, name="register"),
    url(r'login/', views.my_login, name="my_login"),
    url(r'index/', views.index, name="index"),
    url(r'logout/', views.my_logout, name="logout"),
    url(r'set_pwd/', views.set_pwd, name="set_pwd"),


    # 测试上传文件
    url(r'put/', views.put, name="put"),
]