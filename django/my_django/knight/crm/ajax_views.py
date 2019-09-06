# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 20:44
# @Author  : summer
# @File    : ajax_views.py
# @Software: PyCharm
from crm import models
from django.http import JsonResponse

def ajax_class(request):
    res = {'code': 0, 'data': []}
    sid = request.GET.get('sid')
    # 根据前端发送的校区id找出该校区下面所有的班级
    query_set = models.ClassList.objects.filter(campuses_id=sid)
    for c in query_set:
        res['data'].append({'id': c.id, 'name': '{}-{}'.format(c.get_course_display(), c.semester)})
    return JsonResponse(res)

