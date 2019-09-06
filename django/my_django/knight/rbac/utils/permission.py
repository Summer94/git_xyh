# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 12:17
# @Author  : summer
# @File    : permission.py
# @Software: PyCharm
from django.conf import settings

def init(request, user_obj):
    """
    初始化当前登录用户的权限信息以及可显示的菜单信息并保存在session中
    :param request:请求对象
    :param user_obj:登录的用户
    :return:
    """
    #将当前登录用户的所有权限查出来并去重

    permission_querySet = user_obj.roles.values(
        "permissions__url",
        "permissions__title",
        "permissions__is_menu",
        "permissions__icon",
    ).distinct()
    #初始化两个列表分别存放权限信息以及可显示菜单新信息
    permission_list = []
    menu_list = []

    for url in permission_querySet:
        permission_list.append(url["permissions__url"])
        if url.get("permissions__is_menu"):
            menu_list.append({
                "url": url["permissions__url"],
                "title": url["permissions__title"],
                "icon": url["permissions__icon"],
            })
    # 将用户的权限保存在session中
    permisson_key = getattr(settings, "PERMISSION_SESSION_KEY", "permission_url")
    menu_key = getattr(settings, "MENU_SESSION_KEY", "menu_list")
    request.session[permisson_key] = permission_list
    request.session[menu_key] = menu_list