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


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)  # 在添加的时候不确定id是多少，所以直接设置为不需要填
    name = serializers.CharField(max_length=32)
    publisher = PublisherSerializer(read_only=True)
    publisher_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        obj = models.Book.objects.create(name=validated_data['name'], publisher_id=validated_data['publisher_id'])
        return obj


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=32)
    age = serializers.IntegerField()
    books = BookSerializer(many=True, read_only=True)
    book_id_list = serializers.ListField(write_only=True)

    def create(self, validated_data):
        obj = models.Author.objects.create(
            name=validated_data['name'],
            age=validated_data['age'],
        )
        obj.books.add(*validated_data['book_id_list'])
        return obj

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        if validated_data.get("book_id_list"):
            instance.books.set(validated_data.get("book_id_list"))
        instance.save()
        return instance
