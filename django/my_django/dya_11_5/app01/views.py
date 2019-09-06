from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.



class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, reqeust):
        print(reqeust.path_info)  #不带参数的url
        print(reqeust.get_full_path())  #带参数
        # name = reqeust.POST.get("name")
        # print(reqeust.body)
        file = reqeust.FILES
        print(file)
        print(file.getlist("xx"))
        for i in file.getlist("xx"):
            print(i.name)
        # print(reqeust.POST)
        # filename3 = file.get("file3").name
        # with open(filename3, "wb") as f:
        #     for i in file.get("file3"):
        #         f.write(i)
        return HttpResponse("登录成功")
