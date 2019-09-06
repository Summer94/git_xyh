from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.http import HttpResponse
from utils.geetest import GeetestLib
import json
from utils.redis_pool import pool
import redis
from Course.models import Account
from utils.base_response import BaseResponse
import uuid


# 请在官网申请ID使用，示例ID不可使用
pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"
import datetime

# 创建一个redis连接池
REDIS_CONN = redis.Redis(connection_pool=pool)


#用户注册
class RegisterView(APIView):
    def post(self, request):
        # 获取前端传过来注册数据
        data = request.data
        # 验证 用序列化器
        ser_obj = UserSerializer(data=data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response("注册成功")

#滑动验证码登录
class GeetestView(APIView):
    def get(self, request):
        user_id = 'test'
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        status = gt.pre_process(user_id)
        # request.session[gt.GT_STATUS_SESSION_KEY] = status
        # request.session["user_id"] = user_id
        REDIS_CONN.set(gt.GT_STATUS_SESSION_KEY, status)
        REDIS_CONN.set("geetest_user_id", user_id)
        response_str = gt.get_response_str()
        return HttpResponse(response_str)

    def post(self, request):
        res = BaseResponse()
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.data.get(gt.FN_CHALLENGE, '')
        validate = request.data.get(gt.FN_VALIDATE, '')
        seccode = request.data.get(gt.FN_SECCODE, '')
        # status = request.session[gt.GT_STATUS_SESSION_KEY]
        # user_id = request.session["user_id"]
        status = REDIS_CONN.get(gt.GT_STATUS_SESSION_KEY)
        user_id = REDIS_CONN.get("geetest_user_id")
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        # 判断result是0,1
        # 1 代表验证码通过
        if not result:
            res.code = 1001
            res.error = "验证码未通过"
            return Response(res.dict)
        username = request.data.get("username", "")
        pwd = request.data.get("password", "")
        # 判断用户名和密码是否正确
        user_obj = Account.objects.filter(username=username, password=pwd).first()
        if not user_obj:
            res.code = 1002
            res.error = "用户名或密码错误"
            return Response(res.dict)
        token = uuid.uuid4()
        print("token",token)
        # 用redis存token
        REDIS_CONN.set(str(token), user_obj.id, ex=datetime.timedelta(days=7))
        user_obj.token = token
        user_obj.save()
        res.data = token
        res.username = username
        res.token = str(token)
        return Response(res.dict)
