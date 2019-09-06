from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.

from .forms import Regform
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import UserInfo, Hobby

#注册
def register(request):
    if request.method == "POST":
        # 校验数据的格式
        form_obj = Regform(request.POST)
        if form_obj.is_valid():
            # 获取用户提交的数据
            username = request.POST.get("username")
            pwd = request.POST.get("password")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            hobby = request.POST.getlist("hobby")
            hobby_id = "|".join(hobby)
            #数据正确,验证是否存在该数据
            user_obj = authenticate(username=username, password=pwd)
            code = {"status": 0}
            if not user_obj:
                # 说明用户不存在,创建用户
                try:
                    # obj= UserInfo.objects.create(username=username, password=pwd, email=email)
                    form_obj.cleaned_data.pop("re_password")
                    obj = UserInfo.objects.create_user(username=username,password=pwd, phone=phone, email=email, hobby=hobby_id)
                    print(obj,"-"*120)
                    return redirect(reverse("app01:my_login"))
                except Exception as e:
                    print("e"*120)
                    code["error_msg"] = e
            else:
                #用户存在返回错误信息
                print(222)
                code["error_msg"] = "该用户已存在"
            return render(request, "register.html", {"code": code, "form_obj": form_obj})
        else:
            #格式不正确，返回错误信息
            return render(request, "register.html", {"form_obj": form_obj})
    form_obj = Regform()
    return render(request, "register.html", {"form_obj": form_obj})

# 登录
def my_login(request):
    if request.method == "POST":
        # 获取用户提交的数据
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        seven = request.POST.get("seven")
        #验证数据是否存在
        user_obj = authenticate(username=username, password=pwd)
        print(user_obj)
        if user_obj:
            #数据存在，登录成功
            login(request, user_obj)  # 设置session
            if seven == 7: #七天免登陆
                request.session.set_expiry(7 * 24 * 60 * 60)
            return redirect(reverse("app01:index"))
        else:
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})
    return render(request, "login.html")

# 首页
@login_required
def index(request):
    # 将表中的字符串分割成数字id，同时这些id对应的就是爱好表中的id
    hobby_list = [int(i) for i in request.user.hobby.split("|")]
    data = Hobby.objects.all()
    return render(request, "index.html", {"hobby_list": hobby_list, "hobby_obj": data})

# 注销
@login_required
def my_logout(request):
    logout(request)
    return redirect(reverse("app01:my_login"))

# 设置新的密码
@login_required
def set_pwd(request):
    data = {"status": 1}
    if request.method == "POST":
        # 获取旧密码与新密码
        old_pwd = request.POST.get("old_pwd")
        new_pwd = request.POST.get("new_pwd")
        re_new_pwd = request.POST.get("re_new_pwd")
        # 获取当前用户对象
        user = request.user
        #检查原密码是否正确
        if user.check_password(old_pwd):
            if not new_pwd or not re_new_pwd:
                data['err_msg'] = '不能为空'
                data['status'] = "new_password"
            elif new_pwd != re_new_pwd:
                data['err_msg'] = '两次密码不一致'
                data['status'] = "re_password"
            else:
                #所有数据都正确都修改密码
                user.set_password(new_pwd)
                user.save()
        else:
            #原密码输入错误
            data['err_msg'] = "密码错误"
            data['status'] = "password"
        return JsonResponse(data)



# 测试上传文件
def put(request):
    if request.method == "POST":
        print(request.FILES.get("files"))
    return render(request, "put.html")





