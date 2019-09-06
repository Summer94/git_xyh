from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(verbose_name="登录名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

class Class_list(models.Model):
    name = models.CharField(verbose_name="班级名", max_length=32)
    