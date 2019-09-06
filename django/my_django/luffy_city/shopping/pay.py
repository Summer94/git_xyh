# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 21:28
# @Author  : summer
# @File    : pay.py
# @Software: PyCharm
import redis
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.base_response import BaseResponse
from utils.authentication import LoginAuth
from Course import models
from utils.redis_pool import pool
from django.utils.timezone import now
from .shoppingViews import SHOPPING_CAR_KEY
from .models import CouponRecord, Coupon
from .settlementViews import SETTLEMENT_KEY, GLOBAL_COUPON_KEY




class PayView(APIView):
    pass
