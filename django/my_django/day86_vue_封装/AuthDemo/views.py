from django.shortcuts import render

# Create your views here.
import uuid


from rest_framework.views import APIView
from rest_framework.views import Response
from .models import User
from utils.auth import MyAuth
from utils.permission import MyPermission



class RegisterView(APIView):
    def post(self, request):
        name = request.data.get("name", "")
        pwd = request.data.get("pwd", "")
        if name and pwd:
            User.objects.create(name=name, pwd=pwd)
            return Response("注册成功")
        return Response("用户名或密码不合法")


class LoginView(APIView):
    def post(self, request):
        name = request.data.get("name", "")
        pwd = request.data.get("pwd", "")
        user_obj = User.objects.filter(name=name, pwd=pwd).first()
        if user_obj:
            # 登录成功 创建一个token并给前端返回
            token = uuid.uuid4()
            user_obj.token = token
            print(user_obj,"=====")
            user_obj.save()
            return Response(token)
        return Response("用户名或密码错误")


class TestView(APIView):
    authentication_classes = [MyAuth,]
    def get(self, request):
        print(request.user)
        print(request.user.name)
        print(request.auth)
        return Response("登录后发送的数据")


class PermissionView(APIView):
    # authentication_classes = [MyAuth, ]
    # permission_classes = [MyPermission, ]

    def get(self, request):
        # 这个接口只能vip或者vvip访问
        return Response("权限测试接口")
