# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 18:30
# @Author  : summer
# @File    : text111.py
# @Software: PyCharm
# import os
# s = "/Users/jiangshanchen/Desktop/iosMixTools-master/./target_ios/testMixOC/AppDelegate"
# print(os.path.basename(s))

data = {
    1: {'name': 'alex', 'age': 35},
    2: {'name': 'Gold', 'age': 30},
    3: {'name': 'Eva_J', 'age': 18},
    4: {'name': 'GGGXXX', 'age': 20},
    5: {'name': 'Yuan', 'age': 29},
}


# 给s1上过课的老师
d1 = {
    1: {'name': 'alex', 'age': 35},
    2: {'name': 'Gold', 'age': 30},
    3: {'name': 'Eva_J', 'age': 18},
}

# 给s2上过课的老师id
l2 = [2, 4, 5]


# 1. 找出给s1上过课的，没有给s2上过课的老师
teacher_id = set(data.keys())
# s1_id = set(d1.keys())
# s2_id = set(l2)
# res = s1_id-s2_id
# print(res)
# l = [data[i] for i in res]
# print(l)
#
#
# # 2. 找出既给s1上过课的，也给s2上过课的老师
# res = s1_id & s2_id
# print(res)
# l = [data[i] for i in res]
# print(l)
# # 3. 找出没给s1上过课，但是给s2上过课的老师
# res = s2_id - s1_id
# print(res)
# l = [data[i] for i in res]
# print(l)


# teacher_id.add(1)
# teacher_id.add("summer")
# teacher_id.add((1,2,3,4,))
# # teacher_id.add(["aa", "nn"])
# # teacher_id.add({"name": "summer"})
# # print(teacher_id)
#
# teacher_id.update(["aa", "nn"])
# teacher_id.update({"name": "summer"})
# print(teacher_id)
# print(type(teacher_id))
# teacher_id.discard("summer")
# print(teacher_id)

from importlib import import_module



#
# summer = import_module("os")
# print(summer, type(summer))
# print(summer.path.basename(__file__))
# print(summer.name)
# print(summer.environ)
#import_module只是简单地执行和import相同的步骤，但是返回生成的模块对象
# 。你只需要将其存储在一个变量，然后像正常的模块一样使用。
a = ""
print(len(a))

