# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 21:41
# @Author  : summer
# @File    : permission.py
# @Software: PyCharm

from rest_framework import permissions


class MyPermission(permissions.BasePermission):
    message = "请充VIP，999一年"

    def has_permission(self, request, view):
        # 判断用户是否有权限
        if request.user.type in [1, 3]:
            return True
        return False
