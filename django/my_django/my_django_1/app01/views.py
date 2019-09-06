from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login(request):
    print(request,11111)
    return render(request, "login.html")


def layout(request):
    return render(request,"布局管理.html")


def index(request):
    if request.method == "GET":
        return render(request, "login-1.html")
    elif request.method == "POST":
        emai = request.POST.get("email")
        pwd = request.POST.get("pwd")
        if emai == "xyh@123.com" and pwd == "xyh1234":
            return HttpResponse("登录成功")
        else:
            return render(request, "login-1.html", {"error_msg":"用户名或密码错误"})


def pic(request):
    return render(request, "pic.html")

