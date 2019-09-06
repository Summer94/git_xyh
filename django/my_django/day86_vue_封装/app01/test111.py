# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 16:41
# @Author  : summer
# @File    : test111.py
# @Software: PyCharm
author_dic = {'summer': {'name': 'summer', 'age': 24, 'books__name': ['论语', ]}}
# print(author_dic['summer']['books__name'])
# author_dic['summer']['books__name'].append("222")
# print(author_dic)
print(list(author_dic))