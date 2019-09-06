from django.db import models

# Create your models here.

# 出版社表
class Publisher(models.Model):
    name = models.CharField(verbose_name="出版社名", max_length=32)

class User_info(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)