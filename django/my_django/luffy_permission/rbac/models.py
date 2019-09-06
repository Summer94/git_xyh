from django.db import models


# Create your models here.

#菜单表
class Menu(models.Model):
    title = models.CharField(max_length=32, verbose_name="菜单名称", unique=True)
    icon = models.CharField(max_length=24, null=True, blank=True)
    weight = models.PositiveIntegerField(default=50, verbose_name='菜单权重')
    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 权限表
class Permission(models.Model):
    title = models.CharField(max_length=32, verbose_name="标题") #标题
    url = models.CharField(max_length=64) #对应的url
    show = models.BooleanField(default=False) #是否能在菜单上显示
    p_name = models.CharField(max_length=24, verbose_name="路由别名", null=True, blank=True)  # url别名
    menu = models.ForeignKey(to="Menu", verbose_name="所属菜单", null=True, blank=True) #所属的菜单


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "权限表" #在admin端显示
        verbose_name_plural = verbose_name


# 用户表
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    roles = models.ManyToManyField(to='Role')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


# 角色表
class Role(models.Model):
    title = models.CharField(max_length=32)
    permissions = models.ManyToManyField(to='Permission', null=True, blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "角色表"
        verbose_name_plural = verbose_name

