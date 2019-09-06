# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 15:58
# @Author  : summer
# @File    : ceshi.py
# @Software: PyCharm
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day11_20_about_Forms_model.settings")
    import django
    django.setup()
    from xyh.models import Pub
    obj_list = (Pub(name="summer{}".format(i),addr="rain{}".format(i)) for i in range(500))
    Pub.objects.bulk_create(obj_list)