from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers


# 获取标签
class CategoryView(APIView):

    def get(self, request):
        queryset = models.Category.objects.all()
        ser_obj = serializers.CategorySerializer(queryset, many=True)
        return Response(ser_obj.data)


# 获取课程
class CourseView(APIView):

    def get(self, request, id):
        if id == "0":
            queryset = models.Course.objects.all()
        else:
            queryset = models.Course.objects.filter(category_id=id)
        ser_obj = serializers.CourseSerializer(queryset, many=True)
        return Response(ser_obj.data)


# 获取课程详情
class CourseDetailView(APIView):

    def get(self, request, id):
        queryset = models.Course.objects.filter(id=id).first()
        ser_obj = serializers.CourseDetailSerializer(queryset)
        return Response(ser_obj.data)
#获取章节
class ChapterView(APIView):

    def get(self, request, id):
        #根据课程id获取课程的所有章节
        queryset = models.CourseChapter.objects.filter(course_id=id).order_by("order").all()
        ser_obj = serializers.ChapterSerializer(queryset, many=True)
        return Response(ser_obj.data)

