# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 16:29
# @Author  : summer
# @File    : user.py
# @Software: PyCharm

from flask import Blueprint

userBlue = Blueprint("userBlue", __name__)

@userBlue.route("/index/", endpoint="index")
def index():
    return "index"

