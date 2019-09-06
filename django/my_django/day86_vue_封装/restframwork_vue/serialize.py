# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 17:32
# @Author  : summer
# @File    : serialize.py
# @Software: PyCharm
from rest_framework import serializers
from app01 import models


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=32)
    start_time = serializers.DateField()
    addrss = serializers.CharField(max_length=255)

    def create(self, validated_data):
        obj = models.Publisher.objects.create(
            name=validated_data['name'],
            start_time=validated_data['start_time'],
            addrss=validated_data['addrss'],
        )
        return obj


# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)  # 在添加的时候不确定id是多少，所以直接设置为不需要填
#     name = serializers.CharField(max_length=32)
#     publisher = PublisherSerializer(read_only=True)
#     publisher_id = serializers.IntegerField(write_only=True)
#
#     def create(self, validated_data):
#         obj = models.Book.objects.create(name=validated_data['name'], publisher_id=validated_data['publisher_id'])
#         return obj

class BookSerializer(serializers.ModelSerializer):
    # 自定义
    names = serializers.SerializerMethodField(read_only=True)
    publishers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        # fields = ["id", "title", "pub_time"]
        # exclude = ["authors"]
        # depth = 1
        # depth 让你所有的外键关系变成read_only=True
        # extra_kwargs 给默认字段加额外的参数
        model = models.Book
        fields = "__all__"
        # extra_kwargs = {
        #     "publisher": {"read_only": True},
        # }
        extra_kwargs = {
            "name": {"write_only": True},
            "publisher": {"write_only": True}
        }

    def get_names(self, obj):
        return obj.name

    def get_publishers(self, obj):
        return {"id": obj.publisher_id, "name": obj.publisher.name, }





# 自定义一个验证函数
# def my_validate(value):
#     if "冲田杏梨" in value:
#         raise serializers.ValidationError("不能包含敏感词汇(我爱中国共产党!)")
#     return value
#
#
# class AuthorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     name = serializers.CharField(max_length=32, validators=[my_validate, ])
#     age = serializers.IntegerField()
#     books = BookSerializer(many=True, read_only=True)
#     book_id_list = serializers.ListField(write_only=True)
#
#     # 定义一个局部钩子验证name字段
#     def validate_name(self, value):
#         if "summer" in value:
#             raise serializers.ValidationError("不能包含summer这个大帅比的名字")
#         return value
#
#     # 定义一个全局钩子验证所有的字段，其中attr是一个字典
#     def validate(self, attrs):
#         if "rain" in attrs['name'] and attrs['age'] == 24:
#             raise serializers.ValidationError("这个人存在啦")
#         return attrs
#
#     # 通过orm将新增数据
#     def create(self, validated_data):
#         obj = models.Author.objects.create(
#             name=validated_data['name'],
#             age=validated_data['age'],
#         )
#         obj.books.add(*validated_data['book_id_list'])
#         return obj
#
#     # 更新数据
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.age = validated_data.get("age", instance.age)
#         if validated_data.get("book_id_list"):
#             instance.books.set(validated_data.get("book_id_list"))
#         instance.save()
#         return instance


class AuthorSerializer(serializers.ModelSerializer):
    name_info = serializers.SerializerMethodField(read_only=True)
    age_info = serializers.SerializerMethodField(read_only=True)
    book_info = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = models.Author
        fields = "__all__"
        extra_kwargs = {
            "name": {"write_only": True},
            "age": {"write_only": True},
            "books": {"write_only": True},
        }

    def get_name_info(self, obj):
        return obj.name

    def get_age_info(self, obj):
        return obj.age

    def get_book_info(self, obj):
        return [{"id": book.id, "name": book.name} for book in obj.books.all()]


