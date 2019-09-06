# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 21:06
# @Author  : summer
# @File    : settlementViews.py
# @Software: PyCharm
import redis
import json
from rest_framework.views import APIView
from utils.authentication import LoginAuth
from utils.base_response import BaseResponse
from rest_framework.response import Response
from django.utils.timezone import now
from utils.redis_pool import pool
from .shoppingViews import SHOPPING_CAR_KEY
from .models import Coupon, CouponRecord

# 创建redis连接
REDIS_CONN = redis.Redis(connection_pool=pool)
SETTLEMENT_KEY = "settlement_%s_%s"
GLOBAL_COUPON_KEY = "gloabl_coupon_%s"


class SettlementViews(APIView):
    # 登录验证
    authentication_classes = [LoginAuth, ]

    def post(self, request):
        """优惠券可以绑定给用户使用，同时还可以绑定给课程，绑定到课程的是专用优惠券，没有绑定课程的是通用优惠券"""
        # 生成包含信号的字典给前端
        res = BaseResponse()
        try:
            # 获取前端传过来的课程id列表，首先验证课程id的合法性
            course_list = request.data.get("course_list", [])
            # 获取用户id
            user_id = request.user.id
            if not course_list:
                res.code = 1500
                res.error = "请携带课程过来"
                return Response(res.dict)
            # 根据课程id判断是否在redis中,在redis里面的购物车里判断课程是否存在
            print("course_list", course_list)
            for course_id in course_list:
                # 生成一个key
                shopping_car_key = SHOPPING_CAR_KEY % (course_id, user_id)
                print("shopping_car_key", shopping_car_key)
                if not REDIS_CONN.exists(shopping_car_key):
                    res.code = 1501
                    res.error = "课程不合法"
                    return Response(res.dict)
                # 课程合法的话则构建结算单redis数据
                # 获取该用户所有的有效优惠券
                user_all_coupon_record = CouponRecord.objects.filter(
                    account_id=user_id, status=0,
                    coupon__valid_begin_date__lte=now(),  # 优惠券的有效开始时间在当前时间的前面
                    coupon__valid_end_date__gt=now()  # 优惠券的结束时间在当前时间后面
                ).all()
                print("user_all_coupon_record",user_all_coupon_record)
                # 优惠券有两种，一种是绑定给一部分课程使用的，另一种是给所有课程使用的
                # 判断优惠券是否含有课程id，有就代表是给部分课程用的，没有则表示是通用优惠券
                # 构建优惠券信息
                course_coupon_dict = {}
                global_coupon_info = {}
                # 循环
                for coupon_recored in user_all_coupon_record:
                    coupon_obj = coupon_recored.coupon
                    print(coupon_obj)
                    if coupon_obj.object_id and coupon_obj.object_id == course_id:
                        # 课程优惠券
                        course_coupon_dict[coupon_obj.id] = {
                            "id": coupon_obj.id,
                            "name": coupon_obj.name,
                            "money_equivalent_value": coupon_obj.money_equivalent_value or "",
                            "off_percent": coupon_obj.off_percent or "",
                            "minimum_consume": coupon_obj.minimum_consume or ""
                        }
                    elif not coupon_obj.object_id:
                        # 全局优惠券
                        global_coupon_info[str(coupon_obj.id)] = json.dumps({
                            "id": coupon_obj.id,
                            "name": coupon_obj.name,
                            "money_equivalent_value": coupon_obj.money_equivalent_value or "",
                            "off_percent": coupon_obj.off_percent or "",
                            "minimum_consume": coupon_obj.minimum_consume or ""
                        }, ensure_ascii=False)
                # 去redis中购物车中获取课程信息
                course_info_dict = REDIS_CONN.hgetall(shopping_car_key)
                # 获取所有的价格策略
                price_policy_dict = json.loads(course_info_dict["price_policy_dict"])

                default_policy_id = course_info_dict["default_price_policy"]

                period = price_policy_dict[default_policy_id]["valid_period"]

                price = price_policy_dict[default_policy_id]["price"]

                # 构建结算中心的数据结构
                settlement_info = {
                    "id": course_info_dict["id"],
                    "title": course_info_dict["title"],
                    "course_img": str(course_info_dict["course_img"]),
                    "period": period,
                    "price": price,
                    "course_coupon_dict": json.dumps(course_coupon_dict, ensure_ascii=False)
                }
                # 拼接key
                settlement_key = SETTLEMENT_KEY % (user_id, course_id)
                global_coupon_key = GLOBAL_COUPON_KEY % (user_id,)

                REDIS_CONN.hmset(settlement_key, settlement_info)

                REDIS_CONN.hmset(global_coupon_key, global_coupon_info)
            res.data = "加入结算中心成功"
        except Exception as e:
            res.code = 1502
            res.error = "加入结算中心失败"
            return Response(res.dict)
        return Response(res.dict)

    def get(self, request):
        print(1111)
        res = BaseResponse()
        user_id = request.user.id
        #模糊匹配该用户所有结算中心的key
        settlement_key = SETTLEMENT_KEY %(user_id, "*")
        global_key = GLOBAL_COUPON_KEY %(user_id,)
        all_keys = REDIS_CONN.scan_iter(settlement_key)
        #循环每个key去redis的结算中心取数据,该用户可能结算多个课程，获取所有课程的信息以及对应的优惠券
        course_info = []
        for key in all_keys:
            setlement_dict = REDIS_CONN.hgetall(key)
            course_info.append(setlement_dict)
        global_coupon_info = REDIS_CONN.hgetall(global_key)

        #构建数据结构返回给前端
        res.data = {
            "course_info": course_info,
            "global_info": global_coupon_info
        }
        return Response(res.dict)

    def put(self, request):
        res = BaseResponse()
        # 1 获取前端传过来的数据以及user_id
        course_id = request.data.get("course_id", "")
        coupon_id = request.data.get("coupon_id", "")
        user_id = request.user.id
        if not coupon_id:
            res.code = 1060
            res.error = "优惠券id必须携带"
            return Response(res.dict)
        # 2, 校验数据的合法性
        # 3，给redis中加入默认选中的优惠券id
        # 2.1 判断是否有course_id 如果没有去全局优惠券校验coupon_id
        if not course_id:
            global_coupon_key = GLOBAL_COUPON_KEY % user_id
            if not REDIS_CONN.hexists(global_coupon_key, coupon_id):
                res.code = 1061
                res.error = "全局优惠券不合法"
                return Response(res.dict)
            # 3.1 全局优惠券合法 写入redis
            REDIS_CONN.hset(global_coupon_key, "default_global_coupon_id", coupon_id)
        # 2.1 如果有course_id 就去课程结算中心去校验coupon_id
        else:
            # 判断course_id 是否合法
            settlement_key = SETTLEMENT_KEY % (user_id, course_id)
            if not REDIS_CONN.exists(settlement_key):
                res.code = 1062
                res.error = "课程id不合法"
                return Response(res.dict)
            # 拿到这个课程的course_coupons_dict 判断coupon_id 是否存在
            course_coupon_dict = json.loads(REDIS_CONN.hget(settlement_key, "course_coupon_dict"))
            if str(coupon_id) not in course_coupon_dict:
                res.code = 1063
                res.error = "课程优惠券不合法"
                return Response(res.dict)
            # 3.2 课程id以及优惠券id都合法写入redis
            REDIS_CONN.hset(settlement_key, "default_course_coupon_id", coupon_id)
        res.data = "更新优惠券成功"
        return Response(res.dict)


