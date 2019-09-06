# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 16:01
# @Author  : summer
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from Course.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
