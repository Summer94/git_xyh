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
    permission_querySet = user_obj.roles.all().values(
        "permissions__url", # 权限的URL
        "permissions__title", # url的名称
        "permissions__show", # 权限是否显示
        "permissions__p_name", # url路由别名
        "permissions__menu_id", # 菜单的id
        "permissions__menu__title",  # 菜单的标题
        "permissions__menu__icon", # 菜单的图标
        "permissions__menu__weight", # 菜单的权重
    ).distinct()
    #初始化分别存放权限信息以及可显示菜单权限的字典
    permission_dict = {}
    menu_dict = {}
    for item in permission_querySet:
        #权限字典中包含当前权限的别名为key，url以及父级标签的id的字典为value
        #以别名来做key可以将权限粒度细分到按钮级别，在html上判断别名是否在权限字典中，不在则不显示相关的操作(如添加，编辑，删除)
        perms_key = item['permissions__p_name']
        permission_dict[perms_key] = {
            "url": item['permissions__url'],
            "menu_id": item['permissions__menu_id']
        }
        #获取菜单权限
        #以菜单的id为key，生成菜单的html标签时判断时根据show判断是否显示二级菜单
        p_id = item['permissions__menu_id']
        if p_id not in menu_dict:
            menu_dict[p_id] = {
                "id": p_id,
                "title": item['permissions__menu__title'],
                "icon": item['permissions__menu__icon'],
                "weight": item['permissions__menu__weight'],
                #保存下级的权限名、url以及是否可以作为菜单显示
                "children": [{"title": item['permissions__title'], "url": item['permissions__url'], "show": item['permissions__show']}]
            }
        else:
            menu_dict[p_id]["children"].append({"title": item['permissions__title'], "url": item['permissions__url'], "show": item['permissions__show']})
    # 将用户的权限保存在session中
    permisson_key = getattr(settings, "PERMISSION_SESSION_KEY", "permission_dict")
    menu_key = getattr(settings, "MENU_SESSION_KEY", "menu_dict")
    request.session[permisson_key] = permission_dict
    request.session[menu_key] = menu_dict