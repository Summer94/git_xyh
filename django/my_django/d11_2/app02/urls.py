# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 17:57
# @Author  : summer
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from . import views as app02_views


urlpatterns = [
    # url('login', views.login, name='login'),
    url(r'index/$', app02_views.index, name='index'),

    url(r'student_form',app02_views.student_form, name='student_form'),

    url(r'student_list', app02_views.student_list, name='student_list'),
    url(r'add_student', app02_views.add_student, name='add_student'),
    url(r'del_student', app02_views.del_student, name='del_student'),
    url(r'edit_student', app02_views.edit_student, name='edit_student'),

    url(r'teacher_list', app02_views.teacher_list, name='teacher_list'),
    url(r'add_teacher', app02_views.add_teacher, name='add_teacher'),
    url(r'del_teacher', app02_views.del_teacher, name='del_teacher'),
    url(r'edit_teacher', app02_views.edit_teacher, name='edit_teacher'),

    url(r'class_list', app02_views.class_list, name='class_list'),
    url(r'add_class', app02_views.add_class, name='add_class'),
    url(r'del_class', app02_views.del_class, name='del_class'),
    url(r'edit_class', app02_views.edit_class, name='edit_class'),



]