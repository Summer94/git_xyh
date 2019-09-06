# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 21:36
# @Author  : summer
# @File    : my_filter.py
# @Software: PyCharm
from django import template

register = template.Library()

@register.filter(name='my_sex')
def my_sex(value):
    return "male" if value == 1 else "female"