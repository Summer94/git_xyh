import random

from django.test import TestCase

# Create your tests here.

# msg = "%s一个人的夜%s我的心"
#
# print(msg %(1, 2))


# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def foo(self):
#         print(self.name + "正在吃饭")
#         return 11
#
# class B(A):
#     def __init__(self, name):
#         super(B, self).__init__(name)
#
# p1 = B("rain")
# p = A("summer")
#
# print(p.__class__.foo(p))
# print(p1.__class__.foo(p1))
# l = [[i*j for j in range(5)] for i in range(4)]
# print(l)
# d = {"name": "summer", "age": 18}
# d1 = d
# d1["a"] = 100
#
# print(d1)
# print(d)
# print(id(d1))
# print(id(d))
# l = [1, 2, [3, [4, 5]], 6, [7, ]]
# def func(l):
#     if isinstance(l,list):
#         return [y for x in l for y in func(x)]
#     else:
#         return [l]
#
# print(func(l))

# l = [y for y in [1,2,3,4]]
# print(l)
# l = ["{}-{}".format(i,j) for i in range() for j in range(5)]
# print(l)

# a = 0
# if not a:
#     print(11)
# else:
#     print(22)

# from functools import wraps
#
#
# def outer(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(func.__name__,11111)
#         return res
#     return inner
#
# @outer
# def f1():
#     print(f1.__name__,22222)
#     return 11
#
# f1()

# 冒泡排序
# def bubble_sort(li):
#     for i in range(len(li)-1):
#         flag = False
#         for j in range(len(li)-i-1):
#             if li[j] > li[j+1]:
#                 li[j], li[j+1] = li[j+1], li[j]
#                 flag = True
#         if not flag:
#             return
#
# l1 = [2,4,1,2,4,8,6,9,1]
# bubble_sort(l1)
# print(l1)


# def select_sort(li):
#     for i in range(len(li)-1):
#         min_index = i
#         for j in range(i,len(li)):
#             if li[j] < li[min_index]:
#                 min_index = j
#
#         li[i], li[min_index] = li[min_index], li[i]
#
# l1 = list(range(100))
# random.shuffle(l1)
# select_sort(l1)
# print(l1)





# import hashlib
#
# m = hashlib.md5()
# s = "summer"
# # m.update(s.encode("utf-8"))
# # m.update("123".encode("utf-8"))
# ss = "summer123"
# m.update(ss.encode("utf-8"))
#
# print(m.hexdigest())

#
# def Singleton(cls):
#     _instance = {}
#
#     def _singleton(*args, **kargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kargs)
#         return _instance[cls]
#
#     return _singleton
#
#
# @Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
print(a1.a)
print(a1.__dict__)
print(a2.a)
print(a2.__dict__)
#
# from threading import RLock,Thread
#
# class A:
#     _instance = None
#     rlock = RLock()
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance:
#             return cls._instance
#         with cls.rlock:
#             if not cls._instance:
#                 cls._instance = object.__new__(cls)
#             return cls._instance
#
#
# def task():
#     a = A()
#     print(a)
#
# for i in range(10):
#     t = Thread(target=task)
#     t.start()
#
#
#
#
# d = {"s": 12, "as": 23, "fds": 22, "adfa": 67}
# l = sorted(d,key=lambda k:d[k])
# print(l)


print(111)
import sys
print(sys.path)

