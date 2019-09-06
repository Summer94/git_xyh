from django.shortcuts import render,HttpResponse,reverse,redirect

# Create your views here.
from app01 import models
from functools import wraps
from django import views
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect



# session验证
# def check_session(func):
#     @wraps(func)
#     def inner(request, *args, **kwargs):
#         if request.session.get("user"):
#             # 有session，登录成功
#             ret = func(request, *args, **kwargs)
#             return ret
#         else:
#             return_url = request.path_info
#             return redirect("app02/login/?return_url={}".format(return_url))
#     return inner

# 登录
def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        pwd = request.POST.get("pwd")
        seven = request.POST.get("seven")
        res = models.User_info.objects.filter(username=name, password=pwd)
        if res:
            request.session["user"] = {"name": "summer", "age": 18}
            retrun_url = request.GET.get("return_url", "/app02/app02_publisher/")
            if seven:
                request.session.set_expiry(7*24*60*60)
            return redirect(retrun_url)
        else:
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})
    return render(request, "login.html")


# @check_session
def xyh(request):
    return HttpResponse("xyh")

# @check_session
def app02_publisher(request):
    data = models.Publisher.objects.all()
    return render(request, "app02_publisher.html", {"publisher_list": data})

# 注销账号
def app02_login_out(request):
    request.session.flush()
    return redirect(reverse('app02:login'))


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# CBV
@method_decorator(csrf_exempt, name='dispatch') #不用在form表单中写{% csrf_token %}
class Foo(views.View):
    # @method_decorator(check_session) #对CBV的装饰器
    def dispatch(self, request, *args, **kwargs):
        obj = super(Foo, self).dispatch(request, *args, **kwargs)
        return obj

    def get(self, request):
        return render(request, "foo.html")

    def post(self, request):
        name = request.POST.get("name")
        if name == "summer":
            return HttpResponse("1111")
        else:
            return HttpResponse("滚!")
