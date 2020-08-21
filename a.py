# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 20:44
# @Author  : summer
# @File    : a.py
# @Software: PyCharm
a = 1
def foo():
    if a == 2:
        print(2222)
    else:
        print(1111)

class A:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("{} is runing ojbk".format(self.name))

    def see(self):
        print("see something")


class B:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("{} is runing ojbk".format(self.name))

    def see(self):
        print("see something")
foo()

aa = A("summer")
aa.run()

