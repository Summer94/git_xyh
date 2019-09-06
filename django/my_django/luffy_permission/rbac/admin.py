from django.contrib import admin

from .models import Permission, UserInfo, Role, Menu

# Register your models here.

#自定制权限的admin
class PermissonAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'show', 'menu', 'p_name'] #控制admin显示哪些字段
    list_editable = ['url', 'show', 'menu', 'p_name'] #控制admin可以修改哪些字段

# 自定制一个权限类的admin
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'weight']  # 控制admin页面显示哪些字段
    list_editable = ['icon', 'weight']

admin.site.register(Permission, PermissonAdmin)
admin.site.register(UserInfo)
admin.site.register(Role)
admin.site.register(Menu, MenuAdmin)

