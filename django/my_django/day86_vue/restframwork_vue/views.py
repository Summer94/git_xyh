from django.shortcuts import render, HttpResponse
# from django.core import serializers
from django import views
from rest_framework import serializers
from rest_framework.response import Response

from rest_framework.views import APIView
from app01 import models
from .serialize import BookSerializer, PublisherSerializer, AuthorSerializer

# Create your views here.

# 普通的django视图序列化
# class BookView(views.View):
#     def get(self, request):
#         book_querySet = models.Book.objects.all()
#         ret = serializers.serialize('json', book_querySet, ensure_ascii = False)
#         return HttpResponse(ret)

# 基于restframe
class BookView(APIView):
    def get(self, request):
        book_querySet = models.Book.objects.all()
        #序列化
        ser_obj = BookSerializer(book_querySet, many=True)
        return Response(ser_obj.data)

    def post(self, request):
        #获取前端传过来的数据
        book_obj = request.data
        print(book_obj)
        #用序列化器进行校验
        ser_obj = BookSerializer(data=book_obj)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        else:
            return Response(ser_obj.errors)


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

