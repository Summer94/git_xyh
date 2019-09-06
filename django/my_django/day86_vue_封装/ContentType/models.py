from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=32)
    coupon = GenericRelation("Coupon")


class Fruit(models.Model):
    title = models.CharField(max_length=32)
    coupon = GenericRelation("Coupon")


class Coupon(models.Model):
    title = models.CharField(max_length=64)
    content_type = models.ForeignKey(to=ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField("绑定商品", blank=True, null=True)  # 代表哪张表中的对象id
    content_obj = GenericForeignKey("content_type", "object_id")  # 不会生成额外的列
