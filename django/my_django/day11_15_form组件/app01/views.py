import re

from django.shortcuts import render, HttpResponse, redirect, reverse

from django import forms
from . import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.http import JsonResponse


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
        min_length=3,
        max_length=11,
        label="密码",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "密码最短3位",
            "max_length": "密码最长11位",
        },
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}, )
    )

    re_password = forms.CharField(
        min_length=3,
        max_length=11,
        label="确认密码",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "密码最短3位",
            "max_length": "密码最长11位",
        },
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "确认密码"}, )
    )

    gender = forms.fields.ChoiceField(
        choices=((1, "男"), (2, "女"), (3, "保密")),
        label="性别",
        initial=1,
        widget=forms.widgets.RadioSelect()
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

    email = forms.CharField(
        label="邮箱",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
        },
        widget=forms.widgets.EmailInput(attrs={"class": "form-control", "placeholder": "邮箱"}, ),
        validators=[RegexValidator(r"[1-9][0-9]{4,12}@qq\.com", "请输入正确的qq邮箱")]
    )

    def clean(self):
        pwd = self.cleaned_data.get("password")
        re_pwd = self.cleaned_data.get("re_password")
        if pwd == re_pwd:
            return self.cleaned_data
        else:
            self.add_error("re_password", "两次密码不一致")
            raise ValidationError("；两次密码不一致")


# form表单提交
def register(request):
    print("form")
    form_obj = Regform()
    # print(type(form_obj))
    # print(form_obj.__dict__)
    # print(form_obj["username"], type(form_obj["username"]))
    # print(form_obj["username"].__dict__)
    if request.method == "POST":
        form_obj = Regform(request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data.get("username")
            pwd = form_obj.cleaned_data.get("password")
            gender_id = form_obj.cleaned_data.get("gender")
            phone = form_obj.cleaned_data.get("phone")
            email = form_obj.cleaned_data.get("email")
            models.User_info.objects.create(user=username, password=pwd, gender=gender_id, phone=phone, em=email)
            print("注册成功")
            return redirect(reverse("app01:index"))
        else:
            return render(request, "register.html", {"form": form_obj})
    return render(request, "register.html", {"form": form_obj})


# ajax注册
def summer(request):
    form_obj = Regform()
    if request.method == "POST":
        form_obj = Regform(request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data.get("username")
            pwd = form_obj.cleaned_data.get("password")
            gender_id = form_obj.cleaned_data.get("gender")
            phone = form_obj.cleaned_data.get("phone")
            email = form_obj.cleaned_data.get("email")
            form_obj.cleaned_data.pop("re_password")
            models.User_info.objects.create(user=username, password=pwd, gender=gender_id, phone=phone, em=email)
            print("注册成功")
            return JsonResponse({"status": 1})
        else:
            print(form_obj.errors)
            return JsonResponse({"status": 0, "error_msg": form_obj.errors})
    return render(request, "register.html", {"form": form_obj})


# ajax验证手机号
def check_regist(request):
    if request.method == "POST":
        phone = request.POST.get("phone_val")
        ret = models.User_info.objects.filter(phone=phone)
        if ret:
            return HttpResponse(1)  # 手机号已注册
        else:
            return HttpResponse(2)

def index(request):
    return render(request, "index.html")
