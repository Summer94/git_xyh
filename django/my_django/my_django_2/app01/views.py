from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def login(request):
    error_msg = ""
    if request.method == "POST":
        name = request.POST.get("name")
        pwd = request.POST.get("pwd")
        if name == "summer" and pwd == "1234":
            return redirect("https:www.baidu.com")
        else:
            error_msg = "用户名或密码错误"
    return render(request, "login.html", {"error_msg":error_msg})


