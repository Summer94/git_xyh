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

register = template.Library()

#显示菜单
@register.inclusion_tag(filename="rbac/menu.html")
def show_menu(request):
    # 获取当前用户所有的显示的菜单权限
    menu_key = getattr(settings, "MENU_SESSION_KEY", "menu_dict")
    menu_dict = request.session.get(menu_key)
    menu_list = menu_dict.values()
    #根据权重排序
    menu_list = sorted(menu_list, key=lambda x:x["weight"], reverse=True)
    for menu in menu_list:
        menu["class"] = "hide"
        for child in menu['children']:
            if re.match(r'^{}$'.format(child['url']), request.path_info):
                child["class"] = "active"
                menu["class"] = ""
                break
    return {"menu_list": menu_list}

#生成面包屑导航
@register.inclusion_tag(filename="rbac/bread_crumb.html")
def bread_crumb(request):
    bread_crumb_list = request.bread_crumb
    return {"bread_crumb_list": bread_crumb_list}

# 自定义filter 实现按钮是否显示
@register.filter()
def has_permission(request, value):
    key = getattr(settings, 'PERMISSION_SESSION_KEY', 'permission_dict')
    # 3. 当前登陆的这个人他的权限列表是什么
    permission_dict = request.session.get(key, {})
    return value in permission_dict



#给被选中的一行菜单添加样式
@register.filter()
def add_style(value):
    return str(value)


