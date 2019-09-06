# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 09:15
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views



urlpatterns = [
    #角色管理
    url(r'^role_list/', views.role_list, name="role_list"),
    url(r'^role_add/', views.role, name="role_add"),
    url(r'^role_edit/(\d+)/', views.role, name="role_edit"),
    url(r'^role_del/(\d+)/', views.role_del, name="role_del"),
    #菜单管理
    url(r'^menu_list/', views.menu_list, name="menu_list"),
    url(r'^menu_add/', views.menu, name="menu_add"),
    url(r'^menu_edit/(\d+)/', views.menu, name="menu_edit"),
    url(r'^menu_del/(\d+)/', views.menu_del, name="menu_del"),
    #权限管理
    url(r'^permission_add/', views.po_permission, name="permission_add"),
    url(r'^permission_edit/(\d+)/', views.po_permission, name="permission_edit"),
    url(r'^permission_del/(\d+)/', views.permission_del, name="permission_del"),

    # 权限批量录入
    url(r'^permission_entry/', views.permission_entry, name='permission_entry'),
    # 批量权限管理
    url(r'permission_update/', views.permission_update, name='permission_update')

]