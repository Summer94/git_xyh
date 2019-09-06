from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    CHOICE = ((1, "普通用户"), (2, "黄金vip"), (3, "钻石vip"))
    type = models.IntegerField(choices=CHOICE, default=3)
