from django.shortcuts import render, HttpResponse, redirect, reverse
from django import views
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from crm.models import UserProfile, Customer, ConsultRecord, Enrollment, PaymentRecord
from crm.forms import RegisterForm, CustomerForm, ConsultRecordForm, EnrollMentForm, PaymentForm
from utils.my_paginatons import Pagination
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.conf import settings
from django.db import transaction
from rbac.utils import permission



# 登录
class Login_view(views.View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        # 获取用户提交的数据
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        remember = (request.POST.get("remember") == "777")
        # 验证账号密码是否正确
        auth_obj = auth.authenticate(email=email, password=pwd)
        if auth_obj:
            # 登录成功,设置session
            auth.login(request, auth_obj)
            # 执行权限组件的初始化方法
            permission.init(request, auth_obj)
            # 判断是否有7天免登陆
            if remember:
                request.session.set_expiry(7 * 24 * 60 * 60)
            else:
                request.session.set_expiry(0)
            return redirect(reverse('CustomerListView'))
        else:
            return render(request, "login.html", {"error_msg": "邮箱或密码错误"})

# 带有分页功能的客户页面显示
class CustomerListView(views.View):
    @method_decorator(login_required)
    def get(self, request):
        url_prefix = request.path_info
        current_page = request.GET.get("page", 1)
        # 根据url判断是否是共有的客户还是私客
        if request.path_info == reverse("my_customer"):
            # 当为私人客户时，就要将和当前登录的所有相关的客户的信息筛选出来
            query_set = Customer.objects.filter(consultant=request.user)
        else:
            # 公户信息
            query_set = Customer.objects.filter(consultant__isnull=True)

        #数据总共多少条
        total_count = query_set.count()
        #模糊查询
        qd = request.GET.copy()  # 复制QuerySet, 默认qd._mutable = True
        #获得查询条件
        q = self._get_query_q(['name', 'qq', 'qq_name'])
        #筛选查询对象
        query_set = query_set.filter(q)
        # 生成一个分页的实例
        page_obj = Pagination(current_page, total_count, url_prefix, qd, per_page=5, show_page=7)
        # 获取当前的页面数据
        data = query_set[page_obj.start: page_obj.stop]
        # 获取分页的html代码
        page_html = page_obj.page_html()
        return render(request, "customer_list.html", {"customer_list": data, "page_html": page_html})

    @method_decorator(login_required)
    def post(self, request):
        """批量的操作客户转换"""
        url_prefix = request.path_info
        # 获取被操作的客户的id
        cid = request.POST.getlist("cid")
        # 获取操作方式
        action = request.POST.get("action")
        if hasattr(self, "_{}".format(action)):
            ret = getattr(self, "_{}".format(action))(cid)
            if ret:
                return ret
            return redirect(url_prefix)
        else:
            return HttpResponse("404 not found!")

    def _to_public(self, cid):
        # 操作私有客户变为公有客户
        Customer.objects.filter(id__in=cid).update(consultant=None)


    def _to_private(self, cid):
        # 操作公有客户变为私有客户
        # 需要更新的客户数量
        update_num = len(cid)
        # 判断名额是否够用
        valid_num = (self.request.user.customers.count() + update_num) - settings.CUSTOMER_NUM_LIMIT
        if valid_num > 0:
            return HttpResponse("名额已满，最多只能添加{}个".format(
                settings.CUSTOMER_NUM_LIMIT - self.request.user.customers.count()
            ))

        with transaction.atomic():
            #找到所有要操作的客户
            select_objs = Customer.objects.filter(id__in=cid, consultant__isnull=True).select_for_update()
            select_num = select_objs.count()
            #查询出来的数据跟要更新的数据数量不相等，说明有的客户被抢走了
            if select_num != update_num:
                #拿到可以转化为私户的客户id并更新
                select_id = [i[0] for i in select_objs.values_list("id")]
                select_objs.update(consultant=self.request.user)
                #找到没有更新的id
                others = Customer.objects.filter(id__in=cid).exclude(id__in=select_id)
                name_tuple = others.values_list("name")
                name_str = '、'.join([i[0] for i in name_tuple])
                return HttpResponse("手速太慢，{}已经给别人抢走了".format(name_str))
            else:
                select_objs.update(consultant=self.request.user)

    def _get_query_q(self, field_list, op="OR"):
        #从url中获取query参数
        query_value = self.request.GET.get("query", "")
        q = Q()
        #指定q内部的查询方式
        q.connector = op
        #遍历要查询的字段并添加要子Q对象
        for field in field_list:
            q.children.append(Q(('{}__icontains'.format(field), query_value)))
        return q


# def customer_list_new(request):
#     current_page = request.GET.get("page", 1)
#     query_set = Customer.objects.all()
#     total_count = query_set.count()
#     # 生成一个分页的实例
#     page_obj = Pagination(current_page, total_count, per_page=3, show_page=7)
#     # 获取当前的页面数据
#     data = query_set[page_obj.start: page_obj.stop]
#     # 获取分页的html代码
#     page_html = page_obj.page_html()
#     return render(request, "customer_list.html", {"customer_list": data, "page_html": page_html})


#  注册
class Register(views.View):
    def get(self, request):
        obj = RegisterForm()
        return render(request, "register.html", {"form_obj": obj})

    def post(self, request):
        obj = RegisterForm(request.POST)
        if obj.is_valid():
            # 邮箱不存在，创建用户
            obj.cleaned_data.pop("re_password")
            UserProfile.objects.create_user(**obj.cleaned_data)
            return redirect("/login/")
        else:
            return render(request, "register.html", {"form_obj": obj})


@login_required
def index(request):
    return render(request, "index.html")


# ajax检查密码是否一致
def check_paaword(request):
    ret = {"status": 0}
    password = request.POST.get("password")
    re_password = request.POST.get("re_password")
    if password != re_password:
        ret["error_msg"] = "两次密码不一致"
        ret["status"] = 1
    return JsonResponse(ret)


# ajax检查邮箱是否存在
def check_email(request):
    ret = {"status": 0}
    email = request.POST.get("email")
    obj = UserProfile.objects.filter(email=email)
    if obj:
        ret["error_msg"] = "该邮箱已存在"
        ret["status"] = 1
    return JsonResponse(ret)


# 客户列表
@login_required
def customer_list(request):
    data = Customer.objects.all()
    return render(request, "customer_list.html", {"customer_list": data, })


# 注销账户
def login_out(request):
    auth.logout(request)
    return redirect("/login/")


# 添加客户信息
@login_required
def add_customer(request):
    form_obj = CustomerForm()
    if request.method == "POST":
        form_obj = CustomerForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('customer_list'))
    return render(request, "add_customer.html", {"form_obj": form_obj})


# 编辑客户信息
@login_required
def edit_customer(request, page):
    customer_obj = Customer.objects.filter(id=page).first()
    form_obj = CustomerForm(instance=customer_obj)
    if request.method == "POST":
        form_obj = CustomerForm(request.POST, instance=customer_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('customer_list'))
    return render(request, "edit_customer.html", {"form_obj": form_obj})


# 添加与编辑的功能用同一个函数
@login_required
def customer(request, page=None):
    # 获取从上一个页面跳转过来url
    next_url = request.META["HTTP_REFERER"]
    # 当page不存在时也不会报错，而是显示None
    customer_obj = Customer.objects.filter(id=page).first()
    # 当为添加状态时，customer_obj为None，不影响实例，当为编辑状态时，将获取的obj当做实例传入到CustomerForm中
    form_obj = CustomerForm(instance=customer_obj)
    if request.method == "POST":
        form_obj = CustomerForm(request.POST, instance=customer_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(request.POST.get("next_url"))
    return render(request, "customer.html", {"form_obj": form_obj, "next_url": next_url})

#客户跟进沟通表
class ConsultRecordView(views.View):
    @method_decorator(login_required)
    def get(self, request, cid=0):
        #如果是0的话，查询当前用户所有的客户的沟通记录
        if int(cid) == 0:
            query_set = ConsultRecord.objects.filter(consultant=request.user, delete_status=False)
        else:
            #查询当前用户所有的客户的沟通记录
            query_set = ConsultRecord.objects.filter(customer_id=cid, delete_status=False)
        total_count = query_set.count()
        url_prefix = request.path_info
        current_page = request.GET.get("page", 1)
        qd = request.GET.copy()  # 复制QuerySet, 默认qd._mutable = True
        # 生成一个分页的实例
        page_obj = Pagination(current_page, total_count, url_prefix, qd, per_page=3, show_page=7)
        # 获取当前的页面数据
        data = query_set[page_obj.start: page_obj.stop]
        # 获取分页的html代码
        page_html = page_obj.page_html()
        return render(request, "consultrecord_list.html", {"consult_record": data, "page_html": page_html})

#添加和编辑客户跟进记录
@login_required
def consult_record(request, edit_id=None):
    #首先根据id查找
    record_obj = ConsultRecord.objects.filter(id=edit_id).first()
    if not record_obj:
        #不存在就是添加，实例化一个有当前客户的对象
        record_obj = ConsultRecord(consultant=request.user)
    form_obj = ConsultRecordForm(instance=record_obj, initial={"consultant": request.user})
    if request.method == "POST":
        form_obj = ConsultRecordForm(request.POST, instance=record_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("consultrecord_list", args=(0,)))
    return render(request, "consult_record.html", {"form_obj": form_obj, "edit_id": edit_id})


#报名表
@login_required
def enrollment_list(request, customer_id=0):
    if int(customer_id) == 0:
        # 查询当前这个销售所有客户的报名表
        query_set = Enrollment.objects.filter(customer__consultant=request.user, customer__status="signed")
    else:
        query_set = Enrollment.objects.filter(customer_id=customer_id, customer__status="signed")
    total_count = query_set.count()
    url_prefix = request.path_info
    current_page = request.GET.get("page", 1)
    qd = request.GET.copy()  # 复制QuerySet, 默认qd._mutable = True
    # 生成一个分页的实例
    page_obj = Pagination(current_page, total_count, url_prefix, qd, per_page=3, show_page=7)
    # 获取当前的页面数据
    data = query_set[page_obj.start: page_obj.stop]
    # 获取分页的html代码
    page_html = page_obj.page_html()

    return render(request, "enrollment_list.html", {"enrollment_list": data, "page_html": page_html})

#编辑和添加报名信息
@login_required
def enrollment(request, customer_id=None, edit_id=None):
    #根据报名表id去查询，有值就说明是编辑
    enrollment_obj = Enrollment.objects.filter(id=edit_id).first()
    if not enrollment_obj:
        #没有值就说明是添加，根据客户表中传来的数据实例化一个对象，里面包含操作的客户
        customer_obj = Customer.objects.filter(id=customer_id).first()
        enrollment_obj = Enrollment(customer=customer_obj)

    form_obj = EnrollMentForm(instance=enrollment_obj)
    if request.method == "POST":
        form_obj = EnrollMentForm(request.POST, instance=enrollment_obj)
        if form_obj.is_valid():
            new_obj = form_obj.save()
            # 报名成功，更改客户当前的状态
            new_obj.customer.status = 'signed'
            new_obj.customer.save()  # 改的是哪张表的字段就保存哪个对象
            return redirect(reverse('enrollment_list',kwargs={"customer_id": 0}))

    return render(request, "enrollment.html", {"form_obj": form_obj})

#删除
@login_required
def del_enrollment(request, del_id):
    Enrollment.objects.filter(customer_id=del_id).delete()
    return redirect(reverse('enrollment_list'))


#缴费记录表
def payment_list(request):
    data = PaymentRecord.objects.all()
    return render(request, "payment_list.html", {"payment_list": data})

#编辑和添加缴费记录
def payment_record(request, payment_id=None):
    #根据id获取对象，不存在的话说明是添加操作
    payment_obj = PaymentRecord.objects.filter(id=payment_id).first()
    form_obj = PaymentForm(instance=payment_obj)
    if request.method == "POST":
        form_obj = PaymentForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('payment_list'))
    return render(request, "payment_record.html", {"form_obj": form_obj, "edit_id": payment_id})



