from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.base_response import BaseResponse
from utils.authentication import LoginAuth
from Course import models
import json
from utils.redis_pool import pool
import redis

# Create your views here.
"""
前端给我传过来的数据  course_id  price_policy_id
购物车的数据放入redis
构建数据结构
{
    shoppingcar_userid_course_id: {
            id: 1，
            "title": "",
            "course_img": "",
            price_policy_dict: {
                price_policy_id: {周期， 价格},

            },
            default_policy_id: 用户选的价格策略id      
    }

}
"""
# 购物车key
SHOPPING_CAR_KEY = "shopping_car_%s_%s"
REDIS_CONN = redis.Redis(connection_pool=pool)


class ShoppingCarView(APIView):
    """
    code = 1000 成功
    code = 1020 以后代表购物车里的错误
    """
    # 用户认证，必须是登录的客户才可以看到购物车
    authentication_classes = [LoginAuth, ]

    def post(self, request):
        print("shopping-post---------------")
        """加入购物车
        course_id
        price_policy_id
        """
        res = BaseResponse()
        try:
            # 1 获取前端传过来的数据以及 user_id
            course_id = request.data.get("course_id", "")
            price_policy_id = request.data.get("price_policy_id", "")
            user_id = request.user.id
            print(course_id, price_policy_id, user_id)
            # 2 校验数据的合法性
            # 2.1 校验course_id
            course_obj = models.Course.objects.filter(id=course_id).first()
            if not course_obj:
                res.code = 1021
                res.error = "课程id不合法"
                return Response(res.dict)
            # 2.2 校验price_policy_id的合法性
            # 拿课程的所有的价格策略对象
            price_policy_queryset = course_obj.price_policy.all()
            print(price_policy_queryset, "价格策略")
            # 构建字典 以价格策略的id为key  详细信息为value
            price_policy_dict = {}
            for price_policy in price_policy_queryset:
                price_policy_dict[price_policy.id] = {
                    "valid_period": price_policy.get_valid_period_display(),  # 课程周期
                    "price": price_policy.price  # 课程价格
                }
            print("price_policy_dict", price_policy_dict)
            # 判断price_policy_id 是否在课程对象所有的价格策略组成的字典里
            if price_policy_id not in price_policy_dict:
                res.code = 1022
                res.error = "课程价格策略不合法"
                return Response(res.dict)
            # 3 数据合法 构建数据结构
            course_info = {
                "id": course_id,
                "title": course_obj.title,
                "course_img": "http://127.0.0.1:8100/media/" + str(course_obj.course_img),
                "price_policy_dict": json.dumps(price_policy_dict, ensure_ascii=False),
                "default_price_policy": price_policy_id
            }

            shopping_car_key = SHOPPING_CAR_KEY % (user_id, course_id)
            # 4 构建好的数据写入redis
            REDIS_CONN.hmset(shopping_car_key, course_info)
            res.data = "加入购物车成功"
        except Exception as e:
            res.code = 1020
            res.error = "加入购物失败"
        print(res.dict)  # {'code': 1000, 'error': None, 'data': '加入购物车成功'}
        return Response(res.dict)

    def get(self, request):
        """
        [{}, {}]
        :param request:
        :return:
        """
        res = BaseResponse()
        print("shopping-get-----------")
        try:
            # 1 获取用户id
            user_id = request.user.id
            # 2 拿到用户购物车里所有key
            user_shopping_key = SHOPPING_CAR_KEY % (user_id, "*")
            # scan_iter模糊匹配 匹配成功对象放入一个生成器
            all_keys = REDIS_CONN.scan_iter(user_shopping_key)
            # 3 去redis获取数据
            ret = []
            for key in all_keys:
                ret.append(REDIS_CONN.hgetall(key))
            res.data = ret
        except Exception as e:
            res.code = 1024
            res.error = "获取购物车失败"
        print(res.dict)

        return Response(res.dict)

    def put(self, request):
        """
        前端传过来什么数据 course_id  price_policy_id
        :param request:
        :return:
        """
        res = BaseResponse()
        try:
            # 1, 获取前端传过来的数据以及user_id
            course_id = request.data.get("course_id", "")
            price_policy_id = request.data.get("price_policy_id", "")
            user_id = request.user.id
            # 2, 校验数据合法性 去redis
            # 2.1 得到redis购物车的key
            key = SHOPPING_CAR_KEY % (user_id, course_id)
            # 2.2 判断key是否在redis
            if not REDIS_CONN.exists(key):
                res.code = 1026
                res.error = "课程id不合法"
                return Response(res.dict)
            # 2.3 判断价格策略id是否合法
            price_policy_dict = json.loads(REDIS_CONN.hget(key, "price_policy_dict"))
            # 2.4 判断price_policy_id 是否在price_policy_dict
            if str(price_policy_id) not in price_policy_dict:
                res.code = 1027
                res.error = "价格策略不合法"
                return Response(res.dict)
            # 3， 更改redis中 default_price_policy
            REDIS_CONN.hset(key, "default_price_policy", price_policy_id)
            res.data = "更新成功"
        except Exception as e:
            res.code = 1025
            res.error = "修改价格策略失败"
        return Response(res.dict)

    def delete(self, request):
        """
        前端传过来的数据 course_list: [1, 2]
        :param request:
        :return:
        """
        res = BaseResponse()
        try:
            # 1, 获取用户传过来的数据
            course_list = request.data.get("course_list", "")
            user_id = request.user.id
            # 2， 校验数据的合法性
            # 2.1 拼接购物车key
            for course_id in course_list:
                key = SHOPPING_CAR_KEY % (user_id, course_id)
                # 2.2 判断key是否在redis
                if not REDIS_CONN.exists(key):
                    res.code = 1029
                    res.error = "课程id不合法"
                    return Response(res.dict)
                # 3， 删除redis中的购物车数据
                REDIS_CONN.delete(key)
            res.data = "删除成功"
        except Exception as e:
            res.code = 1028
            res.error = "删除失败"
        return Response(res.dict)
