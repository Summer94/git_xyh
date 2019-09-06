# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 11:05
# @Author  : summer
# @File    : class_views.py
# @Software: PyCharm

"""
班主任相关的视图
"""

from django import views
from django.shortcuts import reverse, render, redirect, HttpResponse
from .models import ClassList, CourseRecord, StudyRecord
from .forms import ClassListForm, CourseRecordForm, StudyRecordForm
from utils.my_paginatons import Pagination
from django.http import QueryDict
from django.forms import modelformset_factory


# 班级列表
class ClassListView(views.View):
    def get(self, request):
        query_set = ClassList.objects.all()
        total_count = query_set.count()
        url_prefix = request.path_info
        current_page = request.GET.get("page", 1)
        qd = request.GET.copy()  # 复制QuerySet, 默认qd._mutable = True
        # 生成一个分页的实例
        page_obj = Pagination(current_page, total_count, url_prefix, qd, per_page=4, show_page=7)
        # 获取当前的页面数据
        data = query_set[page_obj.start: page_obj.stop]
        # 获取分页的html代码
        page_html = page_obj.page_html()
        return render(request, "class_list.html", {"class_list": data, "page_html": page_html})


# 添加与编辑编辑
def op_class(request, edit_id=None):
    # 现根据edit_id查找对象，对象不存在则说明是添加操作
    class_obj = ClassList.objects.filter(id=edit_id).first()
    form_obj = ClassListForm(instance=class_obj)
    if request.method == "POST":
        form_obj = ClassListForm(request.POST, instance=class_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("class_list"))

    return render(request, "op_class.html", {"form_obj": form_obj})


# 课程记录
class CourseListView(views.View):
    def get(self, request, class_id):
        # 根据班级id查询出所有的上课记录
        query_set = CourseRecord.objects.filter(re_class_id=class_id)
        current_url = request.get_full_path()
        qd = QueryDict(mutable=True)
        qd['next'] = current_url
        return render(request, 'course_list.html',
                      {'course_record_list': query_set, 'next_url': qd.urlencode(), 'class_id': class_id})

    def post(self, request, class_id):
        # 从POST提交的数据中筛选出action和被勾选中的id
        action = request.POST.get("action")
        cid = request.POST.getlist("cid")
        # 根据反射执行相应的函数
        if hasattr(self, "_{}".format(action)):
            ret = getattr(self, "_{}".format(action))(cid)
        else:
            return HttpResponse("404 not found!")
        if ret:
            return ret
        else:
            return redirect(reverse('course_record_list', kwargs={"class_id": class_id}))

    def _multi_init(self, cid):
        # 根据cid找到要初始化学习记录的那些课程
        courser_objs = CourseRecord.objects.filter(id__in=cid)
        # 针对每个课程 挨个初始化学习记录
        # 创建学习记录
        for course_record in courser_objs:
            # 找到一个班级中的所有的学生
            all_student = course_record.re_class.customer_set.all()  # 找学生--> 根据课程记录找 re_class --> 反向查找这个班级的所有学生
            # 创建学习记录
            studentreord_objs = (StudyRecord(course_record=course_record, student=student) for student in all_student)
            # 一次性将学生对象创建
            StudyRecord.objects.bulk_create(studentreord_objs)
        return HttpResponse('初始化好了')


# 课程添加和编辑
def course_record(request, class_id=None, course_record_id=None):
    class_obj = ClassList.objects.filter(id=class_id).first()
    edit_obj = CourseRecord.objects.filter(id=course_record_id).first() or CourseRecord(re_class=class_obj)
    form_obj = CourseRecordForm(instance=edit_obj, initial={'re_class': class_obj})
    if request.method == 'POST':
        form_obj = CourseRecordForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            next_url = request.GET.get('next', '/crm/class_list/')
            return redirect(next_url)
    return render(request, 'course_record.html', {'form_obj': form_obj, 'edit_id': course_record_id})


# 学习记录表
def study_record_list(request, course_record_id):
    FormSet = modelformset_factory(StudyRecord, StudyRecordForm, extra=0)  # 返回值是一个类
    # 拿到这一个课程记录的所有同学的学习记录
    query_set = StudyRecord.objects.filter(course_record_id=course_record_id)
    #将所有学生的form表单集合起来，提交是一起提交
    formset_obj = FormSet(queryset=query_set)
    if request.method == 'POST':
        formset_obj = FormSet(request.POST, queryset=query_set)
        if formset_obj.is_valid():
            formset_obj.save()

    return render(request, 'study_record_list.html', {'formset_obj': formset_obj})
