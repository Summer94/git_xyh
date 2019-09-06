from django.shortcuts import render, redirect, reverse
from rbac.utils import permission
from rbac.models import UserProfile


#登录
def login(request):
    print("rbac_login")
    error_msg = ""
    if request.method == "POST":
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        obj = UserProfile.objects.filter(username=name, password=pwd).first()
        if obj:
            #根据用户找到他的所有的权限
            permission.init(request, obj)
            return redirect("/customer/list/")
        else:
            error_msg = "用户名或密码错误"
    return render(request, "login.html", {"error_msg": error_msg})


#注销账户
def logout(request):
    request.session.flush()
    return redirect(reverse("login"))
