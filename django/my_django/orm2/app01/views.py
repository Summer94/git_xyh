from django.shortcuts import render,HttpResponse,redirect,reverse

from . import models
# Create your views here.

def login(request):
    error_msg = ""
    if request.method == "POST":
        name = request.POST.get("username")
        pwd = request.POST.get("pwd")
        ret = models.Login.objects.filter(username=name,password=pwd)
        if ret:
            return HttpResponse("登录成功")
        else:
            error_msg = "用户名或密码错误！"
    return render(request, "login.html", {"error_msg":error_msg})

