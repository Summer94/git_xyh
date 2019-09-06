from django.db import models

# Create your models here.

class User_info(models.Model):
    user = models.CharField(max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=64, verbose_name="密码")
    gender = models.IntegerField(choices=((1, "男"), (2, "女"), (3, "保密")), verbose_name="性别")
    phone = models.CharField(max_length=11, verbose_name="手机号", unique=True, default=1)
    em = models.CharField(verbose_name="邮箱", max_length=24)

