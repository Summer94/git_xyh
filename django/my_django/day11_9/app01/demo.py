# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 09:54
# @Author  : summer
# @File    : demo.py
# @Software: PyCharm

import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day11_9.settings")
    import django
    from django.db.models import Q, F, Max, Min, Avg, Count
    django.setup()

    from app01 import models

    # obj = models.Teacher.objects.filter(myclass__student__id=6)
    # for i in obj:
    #     print(i.tname)


    # obj = models.Teacher.objects.filter(myclass__id=1).values("tname")
    # print(obj)
    # obj = models.Teacher.objects.get(id=1)
    # ret = obj.myclass.all()
    # print(ret)
    # obj = models.MyClass.objects.get(id=1)
    # ret = obj.teacher_set.all()
    # print(ret)

    # ret = models.Student.objects.filter(myclass__teacher__tname="alex")
    # print(ret)
    # obj = mols.Comment.objects.filter(pcomment_id=2)
    # for i in obj:
    #     print(i.id, i.content)de
    # obj = models.Comment.objects.filter(id=2)[0]
    # ret = obj.comment_set.all()
    # print(ret)
    from app02 import models as app02_models

    # 查找所有书名里包含番茄的书
    # obj = app02_models.Book.objects.filter(title__contains="番茄")
    # print(obj)

    # 查找出版日期是2017年的书
    # obj = app02_models.Book.objects.filter(publish_date__year="2017")
    # print(obj)

    # 查找出版日期是2017年的书名
    # obj = app02_models.Book.objects.filter(publish_date__year="2017").values("title")
    # print(obj)

    # 查找价格大于10元的书
    # obj = app02_models.Book.objects.filter(price__gt=10)
    # print(obj)

    # 查找价格大于10元的书名和价格
    # obj = app02_models.Book.objects.filter(price__gt=10).values("title", "price")
    # print(obj)

    # 查找memo字段是空的书
    # obj = app02_models.Book.objects.filter(memo="").values("memo")
    # print(obj)

    # 查找在北京的出版社
    # obj = app02_models.Publisher.objects.filter(city="北京")
    # print(obj)

    # 查找名字以沙河开头的出版社
    # obj = app02_models.Publisher.objects.filter(name__istartswith="沙河")
    # print(obj)

    # 查找作者名字里面带“小”字的作者
    # obj = app02_models.Author.objects.filter(name__contains="小")
    # print(obj)

    # 查找年龄大于30岁的作者
    # obj = app02_models.Author.objects.filter(age__gt=30).values("name", "age")
    # print(obj)

    # 查找手机号是155开头的作者
    # obj = app02_models.Author.objects.filter(phone__istartswith="155").values("name", "phone")
    # print(obj)

    # 查找书名是“番茄物语”的书的出版社
    # obj = app02_models.Publisher.objects.filter(book__title="番茄物语")
    # print(obj)

    # 查找书名是“番茄物语”的书的出版社所在的城市
    # obj = app02_models.Publisher.objects.filter(book__title="番茄物语").values("name", "city")
    # print(obj)

    # 查找书名是“番茄物语”的书的所有作者
    # obj = app02_models.Book.objects.filter(title="番茄物语")[0]
    # print(obj.author.all())
    # obj = app02_models.Author.objects.filter(book__title="番茄物语").values("name", "age", "phone")
    # print(obj)

    # 查找书名是“番茄物语”的书的作者的地址
    # obj = app02_models.Author.objects.filter(book__title="番茄物语").values("detail__addr", "detail__email")
    # print(obj)
