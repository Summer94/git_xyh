# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 10:51
# @Author  : summer
# @File    : rbac_tag.py
# @Software: PyCharm

"""
根据settings中设置的值动态的返回html代码
"""
from django import template
from django.conf import settings
import re
from copy import deepcopy

register = template.Library()

@register.inclusion_tag(filename="rbac/menu.html")
def show_menu(request):
    menu_key = getattr(settings, "MENU_SESSION_KEY", "menu_list")
    menu_list = request.session.get(menu_key)
    for index, menu in enumerate(menu_list):
        if re.match(r'^{}$'.format(menu['url']), request.path_info):
            menu["class"] = "active"
            break
    return {"menu_list": menu_list}


