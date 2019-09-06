# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 09:53
# @Author  : summer
# @File    : rbac_forms.py
# @Software: PyCharm

from django import forms
from rbac.models import Role, Menu, Permission
from django.utils.safestring import mark_safe
from rbac.utils.pull_icons import get_icon

ICON_CHOICES = get_icon()
#添加编辑角色
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"
        labels = {
            "title": "角色名",
            "permissions": "权限",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

#添加编辑菜单
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
        labels = {
            "title": "菜单名",
            "icon": "图标",
            "weight": "权重"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        self.fields["icon"] = forms.ChoiceField(
            widget = forms.widgets.RadioSelect,
            choices=((i[0], mark_safe(i[1])) for i in ICON_CHOICES)
        )


#添加编辑权限
class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = "__all__"
        labels = {
            "title": "菜单名",
            "show": "是否显示",
            "p_name": "路由别名",
            "menu": "菜单"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})




