# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 21:40
# @Author  : summer
# @File    : auth.py
# @Software: PyCharm

from rest_framework import authentication
from AuthDemo.models import User
from rest_framework.exceptions import AuthenticationFailed


class MyAuth(authentication.BaseAuthentication):

    def authenticate(self, request):
        # 获取前端携带的token
        # 去比对这个token是否合法
        print("myauth----------")
        token = request.query_params.get("token", "")
        print(request.query_params)
        print(token)
        if not token:
            raise AuthenticationFailed("没有携带token")
        user_obj = User.objects.filter(token=token).first()
        if user_obj:
            return (user_obj, token)
        raise AuthenticationFailed("token不合法")


