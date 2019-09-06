# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 20:59
# @Author  : summer
# @File    : forms.py
# @Software: PyCharm

from django import forms

class PublisherForm(forms.Form):
    title = forms.CharField(
        max_length=32,
        label="出版社名",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
        },
    )
    addr = forms.CharField(
        max_length=32,
        label="地址",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
        },
    )