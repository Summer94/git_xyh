from django.db import models
from crm.models import UserProfile

# Create your models here.


# 权限表
class Permission(models.Model):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=64)
    is_menu = models.BooleanField(default=False)
    icon = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "权限表"
        verbose_name_plural = verbose_name

# 角色表
class Role(models.Model):
    title = models.CharField(max_length=32)
    #权限与角色多对多关联
    permissions = models.ManyToManyField(to='Permission', null=True, blank=True)
    #将角色与用户关联
    user = models.ManyToManyField(to=UserProfile, related_name='roles')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "角色表"
        verbose_name_plural = verbose_name

