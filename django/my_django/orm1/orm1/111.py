# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 21:00
# @Author  : summer
# @File    : 111.py
# @Software: PyCharm
# def func1():
#     name = '张三'
#
#     def func2(arg):
#         print(arg)
#     func2(name)
#
# func1()
# def func1():
#     name = '张三'
#
#     def func2():
#         print(name)  # 能够访问到外层作用域的变量
#     func2()
#
# func1()

# def func1(name):
#
#     def func2():
#         print(name)  # 能够访问到外层作用域的变量
#     func2()
#
# func1('张三')

# def func1():
#     a = 1
#     def func2():
#         def func3():
#             print('func3')
#             print(a)
#         return func3
#     return func2
#
# ret1 = func1()  # func2
# ret2 = ret1()  # func3
# ret2()


# def func(m):
#     def foo(n):
#         return m*n
#     return foo
# foo = func(8)
# print(foo(8))
# print(foo(-1))

# a = 1
# b = a
# c = b
# print(id(a))
# print(id(b))
# print(id(c))

# a = 1
# def f1():
#     a = 2
#     def f2():
#         print(a)
#     return f2
# f1()()
# from functools import wraps
# def wrapper(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         print("夏雨豪")
#         func(*args,**kwargs)
#         print("袁承明")
#     return inner
#
# @wrapper
# def a(name):
#     print("{}是大帅比！".format(name))
#
# a("夏雨豪")
# print(a.__name__)
#
# def fib(n):
#     a,b = 0,1
#     while a<n:
#         print(a)
#         a,b = b,a+b
# fib(100)
# l1 = ["a","b","c"]
# l2 = [1,2,3,4,5,6]
# print(zip(l1,l2))
# print(list(zip(l1,l2)))
# print(dict(zip(l1,l2)))
# for i,j in zip(l1,l2):
#     print(i,"---->",j)

# l1 = ["summer","age1111","rian","ayar"]

# l1.sort()
# print(l1)
# l2 = sorted(l1)
# print(l2)
# print(sorted(l1,key=len))