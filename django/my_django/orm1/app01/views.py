from django.shortcuts import render, HttpResponse, redirect, reverse

from . import models


# Create your views here.


# def login(request):
# res = models.Student.objects.filter(name='ssummer')[0]
# res1 = models.Student.objects.filter(name='ssummer')
# res3 = models.Student.objects.filter(id__lt=3)
# print(res3)
# for item in res3:
#     print(item.name)
# res2 = models.Student.objects.get(id=1)
# models.Student.objects.create(name="张瑞阳",password="1234")
# print(res1,"------->") #QuerySet
# print(res.id, res.name, res.password)
# print(res2)  #返回的是对象


# ret = models.Student.objects.first() #得到的是第一个对象
# print(ret.name)
# ret1 = models.Student.objects.exclude(id=1) #不包含id=1的对象
# for item in ret1:
#     print(item.name)
# obj = models.Student(**{"name":"alex","password":"1234"})
# obj.save()
# res = models.Student.objects.filter(id__gt=3)
# for item in res:
#     print(item.name)
# models.Student.objects.filter(name='ssummer').update(name='summer')
# res = models.Student.objects.filter(name='summer')[0]
# print(res.name,res.id)

# res = models.Student.objects.filter(id__gt=1).values()
# res1 = models.Student.objects.filter(id__gt=1).values_list()
# for i in res:
#     print(i)
#
# for i in res1:
#     print(i)


# return HttpResponse(1111)
# return redirect(reverse("login"))


def login(request):
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        ret = models.Student.objects.filter(name=user, password=pwd)
        if ret:
            return redirect("https://www.baidu.com")
        else:
            error_msg = "账号或密码错误"
    # get请求过来时
    return render(request, "login.html", {"error_msg": error_msg})


# 显示出版社的所有信息
def publisher_list(request):
    # 重数据库中获取所有的数据
    publisher_list = models.Publisher.objects.all()

    return render(request, "publisher_list.html", {"publisher_list": publisher_list, "page": "publisher"})


# 添加出版社
def add_publisher(request):
    # 首先返回一个表单
    if request.method == "POST":
        # 以post的方式请求，先获取表单的数据
        name = request.POST.get("publisher_name")
        # 将数据添加到数据库中
        models.Publisher.objects.create(name=name)
        # 返回出版社列表
        return redirect(reverse('app01:publisher_list1'))
    # get请求过来时
    return render(request, "add_publisher.html")


# 删除一条出版社信息
def del_publisher(request):
    # 获取被删除的出版社的id
    id = request.GET.get("id")
    # 找出要删除的数据进行删除并返回最初的列表
    models.Publisher.objects.filter(id=id).delete()
    return redirect(reverse('app01:publisher_list1'))


# 编辑出版社信息
def edit_publisher(request):
    if request.method == "POST":
        # 获取被修改的出版社的id和出版社名字
        id = request.POST.get("id")
        name = request.POST.get("name")
        # 修改数据库中的数据
        obj = models.Publisher.objects.get(id=id)
        obj.name = name
        obj.save()
        # 返回最初的列表
        return redirect(reverse('app01:publisher_list1'))

    # get请求过来时
    # 首先获取被编辑的id以及出版社名称
    id = request.GET.get("id")
    name = request.GET.get("name")
    # 返回一个带有值得表单
    return render(request, "edit_publisher.html", {"id": id, "name": name})


# 书籍列表
def book_list(request):
    data = models.Book.objects.all()
    # 获取出版社的所有对象
    publisher_list = models.Publisher.objects.all()
    return render(request, "book_list.html", {"book_list": data, "publisher_list": publisher_list, "page": "book"})


# 添加书籍
def add_book(request):
    # 获取书籍名称
    name = request.POST.get("name")
    # 获取选择的出版社的id
    publisher_id = request.POST.get("publisher")
    # 将数据添加到数据库中
    models.Book.objects.create(title=name, publisher_id=publisher_id)
    # 返回到书籍列表页面
    return redirect(reverse("app01:book_list"))


# 删除书籍
def del_book(request):
    # 获取被删除书籍的id
    id = request.GET.get("id")
    models.Book.objects.get(id=id).delete()
    return redirect(reverse("app01:book_list"))


# 修改书籍
def edit_book(request):
    # 获取被修改书籍的id
    book_id = request.GET.get("id")
    book_obj = models.Book.objects.get(id=book_id)
    # 获取所有的出版社对象
    all_publisher = models.Publisher.objects.all()

    if request.method == "POST":
        # 回去新修改的书籍名称
        new_name = request.POST.get("name")
        # 获取选择的出版社id
        publisher_id_select = request.POST.get("publisher")
        # 更新数据库
        book_obj.title = new_name
        book_obj.publisher_id = publisher_id_select
        book_obj.save()
        # 返回到书籍列表页面
        return redirect(reverse("app01:book_list"))

    return render(request, "edit_book.html", {"book": book_obj, "publisher_list": all_publisher})


# 作者列表
def author_list(request):
    # 获取作者表中的所有信息
    data = models.Author.objects.all()
    book_list = models.Book.objects.all()
    return render(request, "author_list.html", {"author_list": data, "book_list": book_list, "page": "author"})


# 添加作者
def add_author(request):
    # 1.提供form表单，显示作者名、年龄、以及作品
    # 1.1将所有的作品信息获取
    data = models.Book.objects.all()
    if request.method == "POST":
        # 获取作者姓名
        new_name = request.POST.get("name")
        # 获取年龄
        new_age = request.POST.get("age")
        # 获取作品id
        book_id_list = request.POST.getlist("book")
        # 将信息添加到作者表中
        obj = models.Author.objects.create(name=new_name, age=new_age)
        # 将信息添加到作者和书籍的第三张表中
        obj.book.add(*book_id_list)
        # 返回作者列表页面
        return redirect(reverse('app01:author_list'))

    return render(request, "add_author.html", {"book_list": data})


# 删除作者信息
def del_author(request):
    # 获取被删除的作者的id
    del_id = request.GET.get("id")
    # 从作者表中找到这行数据删除
    models.Author.objects.get(id=del_id).delete()
    # 返回到作者列表页面
    return redirect(reverse('app01:author_list'))


# 编辑作者信息
def edit_author(request):
    # 1.获取被编辑的作者的id
    edit_id = request.GET.get("id")
    # 2.获取编辑的作者的对象
    edit_obj = models.Author.objects.get(id=edit_id)
    # 3.获取所有书籍的信息
    all_books = models.Book.objects.all()
    # 4.返回编辑页面
    if request.method == "POST":
        # 获取内容
        new_name = request.POST.get("name")
        new_age = request.POST.get("age")
        book_id_list = request.POST.getlist("book")
        # 将数据写入作者表中
        edit_obj.name = new_name
        edit_obj.age = new_age
        edit_obj.save()
        # 将作品添加到第三张表中
        edit_obj.book.set(book_id_list)
        return redirect(reverse('app01:author_list'))

    return render(request, "edit_author.html", {"author": edit_obj, "book_list": all_books})


# 管理页面
def admin(request):
    return redirect(reverse('app01:book_list'))
