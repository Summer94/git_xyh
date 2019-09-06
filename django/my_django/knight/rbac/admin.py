from django.contrib import admin

from .models import Permission, Role

# Register your models here.

class PermissonAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'is_menu', 'icon']
    list_editable = ['url', 'is_menu']

admin.site.register(Permission, PermissonAdmin)
admin.site.register(Role)

