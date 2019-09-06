# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 16:22
# @Author  : summer
# @File    : pull_icons.py
# @Software: PyCharm
"""
从fongtawesome中爬去图标
"""
import requests
from bs4 import BeautifulSoup


def get_icon():

    response = requests.get("http://www.fontawesome.com.cn/faicons/")
    response.encoding = "utf-8"
    html_list = BeautifulSoup(response.text, "html.parser")
    web = html_list.find(attrs={'id': 'web-application'})
    icon_list = []
    for item in web.find_all(attrs={'class': 'fa-hover'}):
        tag = item.find('i')
        class_name = tag.get('class')[1]
        icon_list.append([class_name, str(tag)])

    return icon_list




