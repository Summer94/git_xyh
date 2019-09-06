# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 16:29
# @Author  : summer
# @File    : user.py
# @Software: PyCharm

from flask import Blueprint,render_template, request
from ..forms import RegisterForm


userBlue = Blueprint("userBlue", __name__)

@userBlue.route("/index/", endpoint="index")
def index():
    """展示柱状图"""
    return render_template("index.html")

@userBlue.route("/register/", endpoint="login", methods=["get", "post"])
def register():
    form_obj = RegisterForm()
    if request.method == "POST":
        form_obj = RegisterForm(request.form)
        if form_obj.validate():
            return "注册成功"
    return render_template("register.html", form_obj=form_obj)