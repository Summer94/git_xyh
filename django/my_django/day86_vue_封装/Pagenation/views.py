from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from app01.models import Book
from restframwork_vue.serialize import BookSerializer
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import parsers
from utils.paginator import MyPagination


# class BookView(APIView):
#     def get(self, request):
#         queryset = Book.objects.all()
#         # 第一步实例化分页器对象
#         paginator = MyPagination()
#         # 第二步调用这个分页器类的分页方法
#         page_queryset = paginator.paginate_queryset(queryset, request)
#         ser_obj = BookSerializer(page_queryset, many=True)
#         # return Response(ser_obj.data)
#         return paginator.get_paginated_response(ser_obj.data)

class BookView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = MyPagination
    parser_classes = [parsers.JSONParser, ]
    # versioning_class = []
    # authentication_classes = []
    # permission_classes = []
    # throttle_classes = []

    def get(self, request):
        print(type(request._request))
        return self.list(request)

