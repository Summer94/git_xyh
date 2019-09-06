# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 10:07
# @Author  : summer
# @File    : p01.py
# @Software: PyCharm
# import time
#
# def wrapper(func):
#     def inner(*args, **kwargs):
#         t = time.time()
#         time.sleep(2)
#         ret = func(*args, **kwargs)
#         s = time.time()
#         print("耗时:%s" %(s-t))
#         return ret
#     return inner
#
# @wrapper
# def f1(*args,**kwargs):
#     print("这是f1")
#     return 111
#
# print(f1())