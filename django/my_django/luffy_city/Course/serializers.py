# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 20:01
# @Author  : summer
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from . import models


# 课程分类
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


# 课程
class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source="get_level_display")
    price = serializers.SerializerMethodField()
    course_img = serializers.SerializerMethodField()

    def get_price(self, obj):
        return obj.price_policy.all().order_by("price").first().price

    def get_course_img(self, obj):
        return "http://127.0.0.1:8100/media/" + str(obj.course_img)

    class Meta:
        model = models.Course
        fields = ["id", "title", "course_img", "brief", "level", "study_num", "price"]


class CourseDetailSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source="get_level_display")
    hours = serializers.SerializerMethodField()
    video_brief_link = serializers.SerializerMethodField()

    def get_hours(self, obj):
        return obj.coursedetail.hours

    def get_video_brief_link(self, obj):
        return obj.coursedetail.video_brief_link

    class Meta:
        model = models.Course
        fields = ["id", "title", "study_num", "level",
                  "hours", "is_free", "video_brief_link"]

class ChapterSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    def get_title(self, obj):
        return {"title": obj.title,"setion": [setion.title for setion in obj.course_sections.all()]}
    class Meta:
        model = models.CourseChapter
        fields = "__all__"

