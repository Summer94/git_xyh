# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 15:15
# @Author  : summer
# @File    : demo.py
# @Software: PyCharm

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dya_11_5.settings")
    import django
    from django.db.models import Q,F,Avg,Max,Min,Count

    django.setup()
    from app01 import models

    # obj = models.t1.objects.filter(id=1)[0]
    # print(obj.name, obj.create_time, obj.edit_time)
    # obj.name = "summer1234"
    # obj.save()
    # print("*" * 120)
    # print(obj.name, obj.create_time, obj.edit_time)
    # models.t1.objects.filter(id__lt=2).update(sex=2)
    # models.t1.objects.filter(create_time__day=4).update(sex=2)
    # obj = models.t1.objects.filter(id=1)[0]
    # print(obj.get_sex_display())
    # obj = models.t1.objects.filter(id__lt=2)
    # obj = models.t1.objects.filter(id__gt=1,id__lt=4)
    # obj = models.t1.objects.filter(id__range=[1, 3])
    # print(obj)



    # 基于对象的查询
    # 1.正向查询
    # 1.通过id为3的书籍查询相关联的出版社的信息
    # obj = models.Book.objects.filter(id=3)[0]
    # ret = obj.publisher
    # print(ret.name, ret.addr)
    # 2.通过id为1的作者查询相关联的书籍信息
    # obj = models.Author.objects.filter(id=1)[0]
    # ret = obj.book.all()
    # print(ret)
    # 2.反向查询
    # 1.通过id为1的出版社查询相关联的书籍的信息
    # obj = models.Publisher.objects.filter(id=1)[0]
    # ret = obj.book_set.all()
    # print(ret[0].name)
    # 2.通过id为3的书籍查询相关联的作者信息
    # obj = models.Book.objects.first()
    # ret = obj.author_set.all()
    # print(ret)

    # 基于QuerySet的查询
    # 1.正向查询
    # 1.通过id为3的书籍查询相关联的出版社的信息
    # obj = models.Book.objects.filter(id=3).values("publisher__name", "publisher__addr")
    # print(obj)
    # 2.通过id为1的作者查询相关联的书籍信息
    # ret = models.Author.objects.filter(id=1).values("book__name", "book__price")
    # print(ret)

    # 2.反向查询
    # 1.通过id为1的出版社查询相关联的书籍的信息
    # obj = models.Publisher.objects.filter(id=1).values("book__name", "book__price")
    # print(obj)
    # ret = models.Publisher.objects.filter(id=1).values_list("books__name", "books__price")
    # print(ret)
    # 2.通过id为3的书籍查询相关联的作者信息
    # ret = models.Book.objects.filter(id=3).values_list("author__name", "author__birth")
    # print(ret)
    # ret = models.Book.objects.filter(id=3).values("authors__name", "authors__birth")
    # print(ret)

    # 既包含第三张表又包含M2M字段
    from app04 import models as app04_models
    # obj = app04_models.Book.objects.filter(id=1)
    # obj = app04_models.Publisher.objects.filter(id=1)[0].books.all()
    # for i in obj:
    #     print(i.name, i.price)
    # 通过QuerySet查询
    # ret = app04_models.Publisher.objects.filter(id=1).values("books__name", "books__price")
    # for i in ret:
    #     print(i)

    # ret = app04_models.Publisher.objects.filter(id=1).values("books__authors__name", "books__authors__birth")
    # for i in ret:
    #     print(i)

    # 通过对象查询
    # obj = app04_models.Publisher.objects.filter(id=2)[0].books.all()[0].authors.all()
    # print(obj)


    # 新增一条数据
    # obj = app04_models.Book_Author.objects.filter(author_id=1)
    # print(obj)
    # app04_models.Book_Author.objects.create(author_id=1, book_id=7)
    # obj = app04_models.Book_Author.objects.filter(author_id=1)
    # print(obj)
    # 删除一条数据
    # obj = app04_models.Book_Author.objects.filter(author_id=1, book_id=8).delete()
    # 修改多条数据
    # obj = app04_models.Author.objects.filter(id=1)[0]
    # print(obj)

    # ret = app04_models.Book.objects.all().annotate(count=Count("authors")).values("name","count")
    # print(ret)

    obj = app04_models.Publisher.objects.filter(id=1).values("books__name")
    print(obj)
    obj = app04_models.Publisher.objects.filter(id=1)[0].books.all()
    print(obj)










