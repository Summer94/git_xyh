# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 16:36
# @Author  : summer
# @File    : mdwr.py
# @Software: PyCharm

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render,redirect
from django.http import JsonResponse


# class MD1(MiddlewareMixin):
#     def process_request(self, request):
#         print("MD1中的request", request)
#         request.xyh = {"name": "summer", "age": 18}
#         print("MD1里面的 process_request")
#         # return HttpResponse("夏雨豪真他吗的帅")
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print("-" * 80)
#         print("MD1 中的process_view")
#         print(view_func, view_func.__name__)
#
#     def process_exception(self, request, exception):
#         print(exception)
#         print("MD1 中的process_exception")
#
#     def process_response(self, request, response):
#         print("MD1里面的 process_response")
#         return response
#
# class MD2(MiddlewareMixin):
#     def process_request(self, request):
#         print("MD2中的request", request)
#         print("MD2里面的 process_request")
#         print(request.xyh)
#         # return HttpResponse("夏雨豪真他吗的帅22222")
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print("-" * 80)
#         print("MD2 中的process_view")
#         print(view_func, view_func.__name__)
#
#
#     def process_response(self, request, response):
#         print("MD2里面的 process_response")
#         # return JsonResponse(request.xyh)
#         return response
#
#     def process_exception(self, request, exception):
#         print(exception)
#         print("MD2 中的process_exception")
import time
from threading import Timer


class Login_middleware(MiddlewareMixin):
    user_info = ["/app02/login/",'/login/']
    black_info = ['/app02/xyh/']
    session_dic = {}
    def process_request(self, request):
        url_info = request.path_info
        print(url_info,"---------")
        if url_info in self.user_info or request.session.get("user"):
            return
        elif url_info in self.black_info:
            return HttpResponse('您处于黑名单内!垃圾！')
        else:
            if not url_info.startswith("/app02/"):
                # app01中的url
                return redirect("/login/?return_url={}".format(url_info))
            return redirect("/app02/login/?return_url={}".format(url_info))

        # return HttpResponse("夏雨豪真他吗的帅22222")

limit_dic = {
    "127.0.0.1": [1542252426.783346, 1542252426.23423]
}
class Limit(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META["REMOTE_ADDR"]
        if not ip in limit_dic:
            limit_dic[ip] = []
        history = limit_dic[ip]
        now = time.time()
        while history and now - history[-1] > 60:
            history.pop()
        history.insert(0, now)
        print(history)
        if len(history) > 3:
            return HttpResponse("滚")





