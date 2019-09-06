from django.db import models

# Create your models here.

# 登录
class Student(models.Model):
    name = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)


# 出版社表
class Publisher(models.Model):
    name = models.CharField(verbose_name="出版社名", max_length=32)

# 书籍表(外键出版社表)
class Book(models.Model):
    title = models.CharField(verbose_name="书籍名称", max_length=32)
    publisher = models.ForeignKey(to='Publisher',on_delete=models.CASCADE)

# 作者列表(与书籍表多对多关系)
class Author(models.Model):
    name = models.CharField(verbose_name="作者名", max_length=32)
    age = models.IntegerField()
    book = models.ManyToManyField(to="Book")



