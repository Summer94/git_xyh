# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 15:09
# @Author  : summer
# @File    : crm_urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views, ajax_views, class_views

urlpatterns = [
    # url(r'customer_list/', views.customer_list, name='customer_list'),
    # url(r'customer_list_new/', views.customer_list_new, name='customer_list_new'),
    url(r'customer_list/', views.CustomerListView.as_view(), name='CustomerListView'),  # 客户信息表
    url(r'login_out/', views.login_out, name='login_out'),  # 注销账号
    # url(r'add_customer/', views.add_customer, name='add_customer'),
    # url(r'edit_customer/(\d+)/', views.edit_customer, name='edit_customer'),
    url(r'add_customer/', views.customer, name='add_customer'),  # 添加客户信息
    url(r'edit_customer/(\d+)/', views.customer, name='edit_customer'),  # 编辑客户信息
    url(r'my_customer/', views.CustomerListView.as_view(), name='my_customer'),  # 我的客户表

    # 沟通记录表
    url(r'consultrecord_list/(\d+)/', views.ConsultRecordView.as_view(), name='consultrecord_list'),  # 沟通记录表
    url(r'add_consult_record/', views.consult_record, name='add_consult_record'),  # 添加沟通记录信息
    url(r'edit_consult_record/(\d+)/', views.consult_record, name='edit_consult_record'),  # 编辑沟通记录

    # 报名表
    url(r'enrollment_list/(?P<customer_id>\d+)/', views.enrollment_list, name='enrollment_list'),  # 报名表
    url(r'add_enrollment/(?P<customer_id>\d+)/', views.enrollment, name='add_enrollment'),  # 添加报名信息，在我的客户中显示
    url(r'edit_enrollment/(?P<edit_id>\d+)/', views.enrollment, name='edit_enrollment'),  # 编辑报名信息
    url(r'del_enrollment/(?P<del_id>\d+)/', views.del_enrollment, name='del_enrollment'),  # 删除报名信息

    # AJAX
    url(r'^ajax_class/$', ajax_views.ajax_class),

    # 班级管理表
    url(r'class_list/', class_views.ClassListView.as_view(), name='class_list'),
    url(r'add_class/', class_views.op_class, name='add_class'),
    url(r'edit_class/(\d+)/', class_views.op_class, name='edit_class'),
    # 课程记录
    # 因为查询课程记录 一定是指定查询某个班级的上课记录
    url(r'^course_record_list/(?P<class_id>\d+)/', class_views.CourseListView.as_view(), name='course_record_list'),
    #添加课程记录
    url(r'^add_course_record/(?P<class_id>\d+)/', class_views.course_record, name='add_course_record'),
    #编辑课程记录
    url(r'^edit_course_record/(?P<course_record_id>\d+)/', class_views.course_record, name='edit_course_record'),

    #学习记录表
    url(r'study_record_list/(?P<course_record_id>\d+)/', class_views.study_record_list, name='study_record_list'),

    # 学习记录
    url(r'^study_record_list/(?P<course_record_id>\d+)/', class_views.study_record_list, name='study_record_list'),
    #缴费记录表
    url(r'^payment_list/', views.payment_list, name='payment_list'),
    url(r'^add_payment/', views.payment_record, name='add_payment'),
    url(r'^edit_payment/(\d+)/', views.payment_record, name='edit_payment'),
]
