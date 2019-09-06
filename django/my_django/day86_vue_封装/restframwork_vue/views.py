from django.shortcuts import render, HttpResponse
# from django.core import serializers
from django import views
from rest_framework import serializers
from rest_framework.response import Response

from rest_framework.views import APIView
from app01 import models
from .serialize import BookSerializer, PublisherSerializer, AuthorSerializer
from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import ModelViewSet


class GenericAPIView(APIView):
    query_set = None
    serializer_class = None

    def get_queryset(self):
        return self.query_set

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)


class ListModelMixin(object):
    def list(self, request):
        queryset = self.get_queryset()
        ser_obj = self.get_serializer(queryset, many=True)
        return Response(ser_obj.data)


class CreateModelMixin(object):
    def create(self, request):
        # 获取前端传过来的数据
        obj = request.data
        # 用序列化器做校验
        ser_obj = self.get_serializer(data=obj)
        if ser_obj.is_valid():
            ser_obj.save()
            print(ser_obj.validated_data)
            return Response(ser_obj.data)
        return Response(ser_obj.errors)


class RetrieveModelMixin(object):
    def retrieve(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        ser_obj = self.get_serializer(book_obj)
        return Response(ser_obj.data)


class UpdateModelMixin(object):
    def update(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        ser_obj = self.get_serializer(instance=book_obj, data=request.data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors)

class DestroyModelMixin(object):
    def destroy(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        if book_obj:
            book_obj.delete()
            return Response("")
        return Response("删除的对象不存在")


# 书籍列表及添加书籍
class BookView(GenericAPIView, ListModelMixin, CreateModelMixin):
    query_set = models.Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# 编辑删除书籍
class EditBookView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    query_set = models.Book.objects.all()
    serializer_class = BookSerializer
    def get(self, request, id):
        return self.retrieve(request, id)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

# 出版社列表及添加出版社
class PublisherView(APIView):
    def get(self, request):
        publisher_querySet = models.Publisher.objects.all()
        ser_obj = PublisherSerializer(publisher_querySet, many=True)
        return Response(ser_obj.data)

    def post(self, request):
        publisher_obj = request.data
        # print(publisher_obj)
        ser_obj = PublisherSerializer(data=publisher_obj)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        else:
            return Response(ser_obj.errors)


# 作者列表及添加作者
class AuthorView(APIView):
    def get(self, request):
        author_queryset = models.Author.objects.all()
        ser_obj = AuthorSerializer(author_queryset, many=True)
        return Response(ser_obj.data)

    def post(self, request):
        author_obj = request.data
        ser_obj = AuthorSerializer(data=author_obj)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        else:
            return Response(ser_obj.errors)


# 更新、删除作者信息
class EditAuthorView(APIView):
    def get(self, request, id=None):
        print(id)
        # print(request.parser_context['kwargs'].get("id"))
        obj = models.Author.objects.filter(pk=id).first()
        ser_obj = AuthorSerializer(obj)
        return Response(ser_obj.data)

    def put(self, request, id=None):
        print(request.data)
        author_obj = models.Author.objects.filter(pk=id).first()
        ser_obj = AuthorSerializer(author_obj, data=request.data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
        return Response(ser_obj.data)

    def delete(self, request, id=None):
        models.Author.objects.filter(pk=id).delete()
        return Response("删除成功")


class ModelViewSet(ViewSetMixin, GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin,RetrieveModelMixin, DestroyModelMixin):
    pass

#########所有的视图类###########
from rest_framework import views
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics

######## 用框架提供的ModelViewSet
from rest_framework.viewsets import ModelViewSet


class BookModelView(ModelViewSet):
    queryset=models.Book.objects.all()
    serializer_class = BookSerializer

# 框架默认会把queryset结果进行缓存