from django.db import models

# Create your models here.

# 图书
class Book(models.Model):
    name = models.CharField(max_length=32)
    publisher = models.ForeignKey(to='Publisher')

# 出版社
class Publisher(models.Model):
    name = models.CharField(max_length=64)
    start_time = models.DateField(auto_now_add=True)
    addrss =  models.CharField(max_length=255)

# 作者
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()
    books = models.ManyToManyField(to='Book', related_name='book')




