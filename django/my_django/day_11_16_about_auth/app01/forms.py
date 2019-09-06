# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 15:46
# @Author  : summer
# @File    : forms.py
# @Software: PyCharm

from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from .models import Hobby

# Create your views here.

class Regform(forms.Form):
    username = forms.CharField(
        min_length=2,
        max_length=8,
        label="用户名",
        strip=True,  # 是否移除用户输入空白
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位",
            "max_length": "用户名最长8位",
        },
        widget=forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "用户名"})
    )

    password = forms.CharField(
        min_length=8,
        max_length=11,
        label="密码",
        error_messages={
            "required": "不能为空",
            "invalid": "必须以字母开头的数字和字母的组合",
            "min_length": "密码最短8位",
            "max_length": "密码最长11位",
        },
        validators=[RegexValidator(r"^[a-zA-Z]+[0-9].", "必须以字母开头")],
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}, )

    )

    re_password = forms.CharField(
        min_length=8,
        max_length=11,
        label="确认密码",
        error_messages={
            "required": "不能为空",
            "invalid": "必须以字母开头的数字和字母的组合",
            "min_length": "密码最短8位",
            "max_length": "密码最长11位",
        },
        validators=[RegexValidator(r"^[a-zA-Z]+[0-9].", "必须以字母开头")],
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "确认密码"}, )
    )

    phone = forms.CharField(
        label="手机号",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "max_length": "手机号最长11位",
        },
        widget=forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "手机号"}, ),
        validators=[RegexValidator(r"^1[3-9]\d{9}$", "请填入正确的手机号")]
    )

    email = forms.EmailField(
        label="邮箱",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
        },
        widget=forms.widgets.EmailInput(attrs={"class": "form-control", "placeholder": "邮箱"}, ),
        validators=[RegexValidator(r"[1-9][0-9]{4,12}@qq\.com", "请输入正确的qq邮箱")]
    )
    hobby = forms.fields.MultipleChoiceField(
        # choices=((1, "篮球"), (2, "足球"), (3, "兵乓球")),
        label="爱好",
        initial=1,
        widget=forms.widgets.SelectMultiple()
    )
    def clean(self):
        # 校验密码
        pwd = self.cleaned_data.get("password")
        re_pwd = self.cleaned_data.get("re_password")
        if pwd == re_pwd:
            return self.cleaned_data
        else:
            self.add_error("re_password", "两次密码不一致")
            raise ValidationError("两次密码不一致")
        
    def __init__(self, *args, **kwargs):
        super(Regform, self).__init__(*args, **kwargs)
        self.fields['hobby'].choices = Hobby.objects.all().values_list('id', 'name')
