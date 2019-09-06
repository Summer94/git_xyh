from django.shortcuts import render, redirect, HttpResponse, reverse

from . import models
# Create your views here.
from rbac.forms.rbac_forms import RoleForm, MenuForm, PermissionForm
from rbac.utils import permission, reload_routes
from django.forms import formset_factory, modelformset_factory


# 登录
def login(request):
    error_msg = ""
    if request.method == "POST":
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        obj = models.UserInfo.objects.filter(username=name, password=pwd).first()
        if obj:
            # 根据用户找到他的所有的权限
            permission.init(request, obj)
            return redirect("/customer/list/")

        else:
            error_msg = "用户名或密码错误"
    return render(request, "login.html", {"error_msg": error_msg})


def logout(request):
    request.session.flush()
    return redirect(reverse("login"))


# 角色列表
def role_list(request):
    data = models.Role.objects.all()
    return render(request, "role_list.html", {"role_list": data})


# 添加和编辑角色
def role(request, edit_id=None):
    edit_obj = models.Role.objects.filter(id=edit_id).first()
    form_obj = RoleForm(instance=edit_obj)
    if request.method == "POST":
        form_obj = RoleForm(request.POST, instance=edit_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:role_list'))


# 删除角色
def role_del(request, del_id=None):
    models.Role.objects.filter(id=del_id).delete()
    return redirect(reverse('rbac:role_list'))


# 菜单管理
def menu_list(request):
    #在页面上点击菜单表里的菜单(a标签)时，会将当前的菜单id通过get的形式传递过来
    menu_id = request.GET.get("menu_id")
    # 根据菜单查询对应的权限
    if menu_id:
        permission_data = models.Permission.objects.filter(menu_id=menu_id)
    else:
        # 没有就默认查询所有的权限
        permission_data = models.Permission.objects.all()
    # 查询所有的菜单
    menu_data = models.Menu.objects.all()
    return render(request, "menu_list.html", {"menu_list": menu_data, "permission_list": permission_data})


# 添加编辑菜单
def menu(request, eidt_id=None):
    menu_obj = models.Menu.objects.filter(id=eidt_id).first()
    form_obj = MenuForm(instance=menu_obj)
    if request.method == "POST":
        form_obj = MenuForm(request.POST, instance=menu_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:menu_list'))
    return render(request, "menu.html", {"form_obj": form_obj})


# 删除菜单
def menu_del(request, del_id=None):
    models.Menu.objects.filter(id=del_id).delete()
    return redirect(reverse('rbac:menu_list'))


# 添加编辑权限
def po_permission(request, edit_id=None):
    edit_obj = models.Permission.objects.filter(id=edit_id).first()
    form_obj = PermissionForm(instance=edit_obj)
    if request.method == "POST":
        form_obj = PermissionForm(request.POST, instance=edit_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:menu_list'))
    return render(request, "po_permission.html", {"form_obj": form_obj, "edit_id": edit_id})


# 删除权限
def permission_del(request, del_id=None):
    models.Permission.objects.filter(id=del_id).delete()
    next_url = request.GET.get("next", reverse("rbac:menu_list"))
    return redirect(next_url)

#批量操作权限
def permission_entry(request):
    # 项目(urls.py)里面所有的路由信息
    all_urls = reload_routes.get_all_url_dict(ignore_namespace_list=['admin', ])
    # 数据库中权限表中存储的所有路由信息
    all_permissions = models.Permission.objects.all()

    # 项目中所有路由的集合
    project_url_set = set(all_urls.keys())
    # 数据库中permission表中的路由集合
    db_url_set = set([i.p_name for i in all_permissions])
    # 项目中有，数据库中没有
    only_in_project = project_url_set - db_url_set
    # 这些路由应该是等待添加到数据库中权限表里面的数据
    AddFormset = formset_factory(PermissionForm, extra=0)
    add_formset_obj = AddFormset(initial=[v for k, v in all_urls.items() if k in only_in_project])

    # 获取项目中存在，Permission表中也存在的路由数据
    project_db_set = project_url_set & db_url_set
    # 从Permission数据库中查询出符合要求的路由信息
    urls = models.Permission.objects.filter(p_name__in=project_db_set)
    # 造一个ModelFormet
    ModelFormSet = modelformset_factory(models.Permission, PermissionForm, extra=0)
    edit_formset_obj = ModelFormSet(queryset=urls)

    # 获取只在permission表中存在但是不在项目中的那些路由
    only_in_db = db_url_set - project_url_set
    del_urls = models.Permission.objects.filter(p_name__in=only_in_db)
    del_formset_obj = ModelFormSet(queryset=del_urls)

    if request.method == 'POST':
        # 取出URL中的post_type参数
        post_type = request.GET.get('post_type', None)
        if post_type == 'add':
            add_formset_obj = AddFormset(request.POST)
            if add_formset_obj.is_valid():
                # 手动创建permission
                objs = (models.Permission(**item) for item in add_formset_obj.cleaned_data)
                models.Permission.objects.bulk_create(objs)
                return redirect(reverse('rbac:permission_entry'))
        if post_type == 'edit':
            edit_formset_obj = ModelFormSet(request.POST, queryset=urls)
            if edit_formset_obj.is_valid():
                edit_formset_obj.save()
                return redirect(reverse('rbac:permission_entry'))

    return render(
        request,
        'permission_entry.html',
        {
            'add_formset_obj': add_formset_obj,
            'edit_formset_obj': edit_formset_obj,
            'del_formset_obj': del_formset_obj,
        }
    )


# 权限批量更新
def permission_update(request):
    #取出所有的用户数据
    all_user = models.UserInfo.objects.all()
    #取出所有的角色数据
    all_role = models.Role.objects.all()
    #取出所有的菜单数据
    all_menu = models.Menu.objects.all()
    #当点击页面上的用户表里面的数据是会携带user_id发来请求
    user_id = request.GET.get("user_id", None)
    user_obj = models.UserInfo.objects.filter(id=user_id).first()
    #当点击页面上的角色里面的角色是会携带role_id发来请求
    role_id = request.GET.get("role_id")
    role_obj = models.Role.objects.filter(id=role_id).first()
    if request.method == "POST":
        post_type = request.GET.get("post_type", None)
        #选中用户则更新其对应的角色
        if user_id and post_type == "role":
            role_ids = request.POST.getlist("role_id")
            user_obj.roles.set(models.Role.objects.filter(permissions__menu_id__in=role_ids))
            return redirect(reverse("rbac:permission_update"))
        #选中角色则更新对应的权限
        if role_id and post_type == "permission":
            permisson_ids = request.POST.getlist("permission_id")
            role_obj.permissions.set(models.Permission.objects.filter(id__in=permisson_ids))
            return redirect(reverse("rbac:permission_update"))
    return render(request, "permission_update.html", {
        "all_user": all_user,
        "all_role": all_role,
        "all_menu": all_menu,
        "user_obj": user_obj,
        "role_obj": role_obj,
    })

