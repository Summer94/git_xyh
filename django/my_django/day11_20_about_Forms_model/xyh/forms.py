# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 20:59
# @Author  : summer
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import Pub

from django.core.exceptions import ValidationError

class Form(forms.ModelForm):
    class Meta:
        model = Pub
        fields = "__all__"
        labels = {
            "name": "出版社名称",
            "addr": "出版社地址",
        }
        error_messages = {
            "name": {
                "min_length": "用户名最短4位",
                "max_length": "最大长度不能超过12"
            },
            "addr": {
                "max_length": "最大长度不能超过255"
            },
            "required": "不能为空"

        }
    def clean_name(self):
        value = self.cleaned_data.get("name")
        if 4 <= len(value) <=12:
            return value
        else:
            raise ValidationError("出版社名称数量要小于12大于4")


