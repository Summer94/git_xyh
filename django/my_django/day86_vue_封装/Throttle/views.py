from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from utils.throttle import MyThrottle, MyVisit


class TestView(APIView):
    throttle_classes = [MyVisit, ]

    def get(self, request):
        return Response("频率测试接口")
