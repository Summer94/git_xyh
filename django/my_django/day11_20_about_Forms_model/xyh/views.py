from django.shortcuts import render, HttpResponse, redirect, reverse

from . import models
from .forms import Form
from utils.my_paginatons import Pagination


# Create your views here.


# 出版社列表
def publisher(request):
    data = models.Pub.objects.all()
    # 获取当前页数
    try:
        # 当输入的值不是数字的时候，当前页默认为1
        current_page = int(request.GET.get("page", 1))
    except Exception as e:
        current_page = 1
    # 不能是负数
    if current_page < 1:
        current_page = 1

    # 获取总共的数据
    query_set = data.count()
    # 每页显示多少条数据
    per_page = 10
    # 计算有多少页
    total_page, more = divmod(query_set, per_page)
    # 如果有余数，那么页数加一
    if more:
        total_page += 1
    # 如果访问的页码数超过了总页码数，默认展示最后一页
    current_page = total_page if current_page > total_page else current_page
    # 每次显示多少页
    show_page = 9
    # 显示页数的一半的页数
    show_half_page = show_page // 2
    # 数据切片的开始位置
    start = per_page * (current_page - 1)
    # 数据切片的结束位置
    stop = per_page * current_page
    # 当前页面要显示的数据
    data = data[start:stop]

    # 显示页数
    # 如果显示的总页码小于要显示的页码
    if current_page > total_page:
        show_page_start = 1
        show_page_stop = per_page
    # 防止左边页面溢出
    elif current_page <= show_half_page:
        show_page_start = 1
        show_page_stop = show_page
    # 防止右边页面溢出
    elif current_page + show_half_page > total_page:
        show_page_stop = total_page
        show_page_start = total_page - show_page + 1
    else:
        # 显示页数的开始
        show_page_start = current_page - show_half_page
        # 显示页数的结束
        show_page_stop = current_page + show_half_page
    # 生成html代码
    page_html_list = []
    # 代码的前缀
    page_html_list.append('<nav aria-label="Page navigation"><ul class="pagination">')
    # 添加首页
    page_html_list.append('<li><a href="/publisher/?page=1">首页</a></li>')
    # 添加上一页
    if current_page - 1 < 1:  # 已经到头啦，不让点上一页啦
        page_html_list.append(
            '<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
    else:
        page_html_list.append(
            '<li><a href="/publisher/?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                current_page - 1))
    for i in range(show_page_start, show_page_stop + 1):
        if i == current_page:
            a = '<li class="active"><a href="/publisher/?page={0}">{0}</a></li>'.format(i)
        else:
            a = '<li><a href="/publisher/?page={0}">{0}</a></li>'.format(i)
        page_html_list.append(a)
    # 添加下一页
    if current_page + 1 > total_page:
        page_html_list.append(
            '<li class="disabled"><a href="" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>')
    else:
        page_html_list.append(
            '<li><a href="/publisher/?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                current_page + 1))

    # 添加尾页
    page_html_list.append('<li><a href="/publisher/?page={}">尾页</a></li>'.format(total_page))
    # 给代码增加后缀
    page_html_list.append('</ul></nav>')
    page_html = "".join(page_html_list)
    return render(request, "publisher.html", {"publisher_list": data, "page_html": page_html})


# 根据定义的分页类来显示数据
def publisher_new(request):
    current_page = request.GET.get("page", 1)
    query_set = models.Pub.objects.all()
    total_count = query_set.count()
    # 生成一个分页的实例
    page_obj = Pagination(current_page, total_count, per_page=10, show_page=7)
    # 获取当前的页面数据
    data = query_set[page_obj.start: page_obj.stop]
    # 获取分页的html代码
    page_html = page_obj.page_html()
    return render(request, "publisher.html", {"publisher_list": data, "page_html": page_html})


# 编辑出版社
def edit_pub(request):
    # 获取被编辑的出版社id
    id = request.GET.get("id")
    # 根据id到数据库中找到被编辑的对象
    pub_obj = models.Pub.objects.get(id=id)
    # 将对象当做实例传入到Form组件中，返回页面时会自动将这个对象的数据填充到html页面中
    form_obj = Form(instance=pub_obj)
    if request.method == "POST":
        # 判断获取的值是否都满足条件
        form_obj = Form(request.POST, instance=pub_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("publisher"))
    return render(request, "edit_publisher.html", {"form_obj": form_obj})


def xyh(request):
    return HttpResponse("xyh")
