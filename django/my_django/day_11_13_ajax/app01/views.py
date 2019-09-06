from django.shortcuts import render, HttpResponse, reverse, redirect

# Create your views here.
from . import models
from django.http import JsonResponse
from functools import wraps


# 检查cookie的装饰器
def check_cookie(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if request.COOKIES.get("user") == "summer":
            ret = func(request, *args, **kwargs)
            return ret
        else:
            # 获取被装饰函数的url
            return_url = request.path_info
            return redirect("login/?return_url={}".format(return_url))

    return inner




# 登录
def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        pwd = request.POST.get("pwd")
        seven = request.POST.get("seven")
        res = models.User_info.objects.filter(username=name, password=pwd)
        request.session["user"] = {"name": "summer", "age": 18, "nickname": "c君"}
        if res:
            return_url = request.GET.get("return_url", "/publisher_list/")
            # print(return_url)
            # print("&" * 120)
            obj = redirect(return_url)
            if seven:
                obj.set_cookie("user", "summer", max_age=7 * 24 * 60 * 60)
            else:
                obj.set_cookie("user", "summer")
            return obj
        else:
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})
    return render(request, "login.html")

# 出版社列表
# @check_cookie
def publisher_list(request):
    data = models.Publisher.objects.all()
    return render(request, "publisher_list.html", {"publisher_list": data})


# 删除
# @check_cookie
def del_publisher(request):
    if request.method == "POST":
        data = {"status": 1}
        pid = request.POST.get("pid")
        try:
            models.Publisher.objects.filter(id=pid).delete()
        except Exception as e:
            data["status"] = 0
            data["err_msg"] = str(e)
        return JsonResponse(data)


# @check_cookie
def home(request):
    return render(request, "home.html")


# 注销
def login_out(request):
    ret = redirect("publisher_list")
    ret.delete_cookie("user")
    return ret
