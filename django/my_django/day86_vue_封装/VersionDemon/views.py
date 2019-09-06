from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class VersionView(APIView):
    def get(self, request, version):  # 接收路由的匹配信息
        print(request.version)  # 获取版本
        print(request.versioning_scheme)  # 版本实例控制对象

        if request.version == "v1":
            return Response("睁大眼睛看看，这是版本1")
        elif request.version == "v2":
            return Response("看清楚没有！这是版本2")
        return Response("版本不存在")