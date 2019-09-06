from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .polyv import polyv_video
import json
from urllib.parse import urlencode
# Create your views here.

class PolyvView(APIView):
    def post(self, request):
        print("Polyv-post")
        # 给前端返回加密的token
        # vid, remote_addr, uid=None, username="", extra_params="HTML5"
        vid = request.data.get("vid")
        remote_addr = request.META.get("REMOTE_ADDR")
        username = "summer"
        token_dict = polyv_video.get_verify_data(vid, remote_addr, uid=1, username=username)
        return Response(token_dict["token"])

    # 播放跑马灯视频的时候给这个接口发get请求 vid code t callback
    def get(self, request):
        print("Polyv-get")
        vid = request.query_params.get("vid", "")
        code = request.query_params.get("code", "")
        t = request.query_params.get("t", "")
        callback = request.query_params.get("callback", "")
        status = 1
        username = "xiayuhao" #跑马灯显示的数据，如果是中文，必须urlencode
        sign = polyv_video.get_play_key(vid, username, code, status, t)
        res_dict = polyv_video.get_resp(status, username, sign)
        if callback != "":
            ret = callback + "(" + json.dumps(res_dict, ensure_ascii=False) + ")"
        else:
            ret = json.dumps(res_dict, ensure_ascii=False)
        return HttpResponse(ret)
