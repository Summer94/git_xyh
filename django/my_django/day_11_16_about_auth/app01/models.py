from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class UserInfo(AbstractUser):
    """
    用户信息表
    """
    nid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, unique=True)
    hobby = models.CharField(default=1, max_length=10)

    def __str__(self):
        return self.username


class Hobby(models.Model):
    name = models.CharField(max_length=32, verbose_name="爱好" ,unique=True)