from django.shortcuts import render, HttpResponse, reverse, redirect


# Create your views here.
import time
import datetime

def index(request):
    list1 = [111, 222, 333]

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def dream(self):
            return "夏雨豪真的帅!"

    xyh = "summer"

    p1 = Person("p1", 18)
    p2 = Person("p2", 19)
    p3 = Person("p3", 20)

    l2 = [p1, p2, p3]

    d = {"name": "summer", "age": 18}
    return render(request, "index.html", {"list1": list1, "l2": l2, "d": d, "xyh": xyh})


def time_difference(t1,t2):
    t = ""
    t1_struct = time.strptime(t1,"%Y-%m-%d")
    t2_struct = time.strptime(t2,"%Y-%m-%d")
    t1_stamp = time.mktime(t1_struct)
    t2_stamp = time.mktime(t2_struct)
    s = t2_stamp - t1_stamp
    a,b = divmod(s,60*60*24) #多少天
    c,d = divmod(a,365)
    if c>=1:
        e, f = divmod(d, 30)
        if e >= 1:
            # print("{}年{}月{}天".format(int(c), int(e), int(f)))
            t = "{}岁{}个月{}天".format(int(c), int(e), int(f))
        else:
            # print("{}年{}天".format(int(c), int(f)))
            t = "{}岁{}天".format(int(c), int(f))
    else:
        e,f = divmod(d,30)
        if e>=1:
            # print("{}月{}天".format(int(e), int(f)))
            t = "{}个月{}天".format(int(e), int(f))
        else:
            # print("{}天".format(int(f)))
            t = "{}天".format(int(f))
    return t

def re_age(request):
    if request.method == "POST":
        t = ""
        age = ""
        s = ""
        #获取出生年月
        try:
            age = request.POST.get("age")
            now_time = datetime.date.fromtimestamp(time.time())
            t = time_difference(str(age), str(now_time))
            t = "您的年龄为{}".format(t)
        except Exception:
            s = "请输入正确的格式"

        return render(request, "re_age.html", {"t": t, "age": age, "s": s},)


    return render(request, "re_age.html",)



