# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 17:52
# @Author  : summer
# @File    : my_filter.py
# @Software: PyCharm
from django import template
import time

register = template.Library()


@register.filter(name='dsb')
def dsb(value):
    return value + "夏雨豪是大帅比!"

@register.filter()
def my_time(value):
    now_time = time.time()
    pass


