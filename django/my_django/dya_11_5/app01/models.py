from django.db import models


# Create your models here.

# 自己定义char字段
class MyChar(models.Field):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(MyChar, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        """限定生成的数据表的字段类型为char，长度为max_lenght指定的值"""
        return "char(%s)" % self.max_length
#
#
class t1(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    create_time = models.DateField(auto_now_add=True)
    edit_time = models.DateField(auto_now=True)
    hooby = MyChar(max_length=32,)
    sex = models.SmallIntegerField(choices=((1, "male"), (2, "female"), (3, "none")))
    class Meta:
        # db_table = "t1"
        verbose_name = "app01_t1"

    def __str__(self):
        return self.name


# 出版社表
class Publisher(models.Model):
    name = models.CharField(max_length=64, verbose_name="出版社名称")
    addr = models.CharField(max_length=128, verbose_name="地址")
    create_time = models.DateField(max_length=64, auto_now_add=True, verbose_name="成立日期")
    def __str__(self):
        return self.name

# 书籍表
class Book(models.Model):
    name = models.CharField(max_length=64, verbose_name="书籍名称")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="书籍价格")
    num = models.PositiveIntegerField(verbose_name="编号" ,unique=True)
    publisher = models.ForeignKey(to="Publisher", verbose_name="外键关联Publisher", related_name="books")
    def __str__(self):
        return self.name

# 作者表
class Author(models.Model):
    name = models.CharField(max_length=64, verbose_name="作者名")
    birth = models.DateTimeField(verbose_name="生日")
    sex = models.PositiveSmallIntegerField(choices=((1, "male"), (2, "female")), verbose_name="性别")
    phone = models.BigIntegerField(verbose_name="手机号", unique=True)
    email = models.EmailField(verbose_name="邮箱")
    book = models.ManyToManyField(to="Book", verbose_name="多对多关联Book", related_name="authors",)
    def __str__(self):
        return self.name




