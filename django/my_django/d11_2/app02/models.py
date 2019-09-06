from django.db import models


# Create your models here.

# 学生表
class Student(models.Model):
    name = models.CharField(verbose_name="学生姓名", max_length=32)
    age = models.IntegerField(verbose_name="学生年龄",)
    sex_choice = (
        (0,"female"),
        (1,"male"),
    )
    sex = models.IntegerField(choices=sex_choice)
    go_school = models.DateField(verbose_name="入学日期")
    sclass = models.ForeignKey(to='Myclass', on_delete=models.CASCADE)


# 教师表
class Teacher(models.Model):
    name = models.CharField(verbose_name="教师姓名", max_length=32)
    age = models.IntegerField(verbose_name="教师年龄",)
    sex_choice = (
        (0, "female"),
        (1, "male"),
    )
    sex = models.IntegerField(choices=sex_choice)

# 班级表
class Myclass(models.Model):
    name = models.CharField(verbose_name="班级名称", max_length=32)
    teacher = models.ManyToManyField(to='Teacher',)
    # aaa = models.DateField(auto_now=True) #建立时间
    # bbbb = models.DateField(auto_now_add=True) #修改时间
