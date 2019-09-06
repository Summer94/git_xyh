from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from Course.models import Account
import datetime
from django.utils.timezone import now
from utils.redis_pool import pool
import redis

# 基于MySQL认证
# class LoginAuth(BaseAuthentication):
#     def authenticate(self, request):
#         # 认证通过 （request.user, request.auth）
#         # 不通过抛异常
#         # 1 拿到前端带过来的token
#         # 2 判断token是否存在
#         # 3 以及token是否过期
#         token = request.META.get('HTTP_AUTHENTICATION', "")
#         if not token:
#             raise AuthenticationFailed("没有携带token")
#         user_obj = Account.objects.filter(token=token).first()
#         if not user_obj:
#             raise AuthenticationFailed("token不合法")
#         create_time = user_obj.token_create_time
#         if (now() - create_time).days >7:
#             raise AuthenticationFailed("token过期")
#         return (user_obj, user_obj.token)

# 基于redis
conn = redis.Redis(connection_pool=pool)


class LoginAuth(BaseAuthentication):
    def authenticate(self, request):
        # 认证通过 （request.user, request.auth）
        # 不通过抛异常
        # 1 拿到前端带过来的token
        # 2 判断token是否存在
        # 3 以及token是否过期
        if request.method == "OPTIONS":
            return None
        token = request.META.get('HTTP_AUTHENTICATION', "")
        print("token", token)
        if not token:
            raise AuthenticationFailed("没有携带token")
        # token
        if not conn.exists(token):
            raise AuthenticationFailed("token过期")
        user_id = conn.get(token)
        user_obj = Account.objects.filter(id=user_id).first()
        return (user_obj, token)
