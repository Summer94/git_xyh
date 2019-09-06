# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 17:24
# @Author  : summer
# @File    : middleware.py
# @Software: PyCharm
"""
中间件里处理跟权限有关的事务

"""

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.conf import settings
import re

class RBACMiddleware(MiddlewareMixin):
    def process_request(self, request):
        #获取当前请求的url
        current_url = request.path_info
        #判断当前请求的url在不在白名单中
        for url in getattr(settings, "WHITE_URLS", []):
            #匹配得上就通过
            if re.match("^{}$".format(url), current_url):
                return
        # 获取权限列表
        key = getattr(settings, "PERMISSION_SESSION_KEY", "permission_list")
        permission_dict = request.session.get(key, {})
        # 从session中取到菜单的字典，取出菜单信息
        menu_key = getattr(settings, 'MENU_SESSION_KEY', 'menu_dict')
        menu_dict = request.session[menu_key]
        # print(permission_dict)
        #{'web:customer_list': {'url': '/customer/list/', 'menu_id': 1}, 'web:customer_add': {'url': '/customer/add/', 'menu_id': 1},
        #  'web:customer_edit': {'url': '/customer/edit/(?P<cid>\\d+)/', 'menu_id': 1},
        # 'web:payment_list': {'url': '/payment/list/', 'menu_id': 2},
        # 'web:payment_add': {'url': '/payment/add/', 'menu_id': 2}}

        # print(menu_dict)
        #{'1': {'id': 1, 'title': '客户管理', 'icon': 'fa-cc', 'weight': 50, 'children': [{'title': '客户列表', 'url': '/customer/list/', 'show': True}, {'title': '添加客户', 'url': '/customer/add/', 'show': True}, {'title': '编辑客户', 'url': '/customer/edit/(?P<cid>\\d+)/', 'show': False}]},
        # '2': {'id': 2, 'title': '账单管理', 'icon': 'fa-heart', 'weight': 50, 'children': [{'title': '账单管理', 'url': '/payment/list/', 'show': True}, {'title': '添加账单', 'url': '/payment/add/', 'show': True}]}}

        # 为面包屑导航获取数据
        request.bread_crumb = [{"title": "首页", "url": "#"}]
        #根据url匹配权限
        for item in permission_dict.values():
            #根据请求过来的url对当前用户所有的权限url进行验证
            if re.match('^{}$'.format(item['url']), current_url):
                # 匹配成功，有权限，通过
                #获取权限名，并添加到面包屑列表中
                menu_title = menu_dict[str(item['menu_id'])]['title']
                request.bread_crumb.append({'title': menu_title})
                return None
        #匹配不到则没有权限，直接返回
        else:
            return HttpResponse('没有权限!!!!')

