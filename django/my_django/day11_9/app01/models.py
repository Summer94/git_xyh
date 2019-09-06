from django.db import models


# Create your models here.
# 课程表
class MyClass(models.Model):
    cname = models.CharField(max_length=12)

# 教师表
class Teacher(models.Model):
    tname = models.CharField(max_length=12)
    myclass = models.ManyToManyField(to='MyClass')

#学生表
class Student(models.Model):
    sname = models.CharField(max_length=12)
    myclass = models.ForeignKey(to='MyClass')

    def __str__(self):
        return self.sname



# 自关联表
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255)
    push_time = models.DateTimeField(auto_now_add=True)
    # 父评论：自关联,一个评论可以没有父评论所以null=True
    pcomment = models.ForeignKey(to='self', null=True)

    def __str__(self):
        return self.content


