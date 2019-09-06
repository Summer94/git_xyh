# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 11:20
# @Author  : summer
# @File    : 111.py
# @Software: PyCharm

# s = "summer"
# l1 = ["s", "as", "df"]
# print(" ".join(l1))
# print(s.split("m"))



# d1 = datetime.datetime(2005,10,2)
# d2 = datetime.datetime(2006,3,10)
# s = d2-d1
# print(s.days)
# print(s.total_seconds())
# print(datetime.date.today())
import datetime
import time
from dateutil import relativedelta

while 1:
    birthday = input(">>>").strip()

    birth_day = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    print(birth_day, type(birth_day))
    now_day = datetime.datetime.now()
    print(now_day, type(now_day))
    s = relativedelta.relativedelta(now_day, birth_day)
    print(s)
    print("{obj.years}岁{obj.months}个月{obj.days}天".format(obj=s))

