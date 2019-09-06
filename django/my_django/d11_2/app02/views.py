from django.shortcuts import render,HttpResponse,redirect,reverse
from . import models
from django.http import JsonResponse

# Create your views here.

# 母版
def index(request):
    return render(request, "book_list.html")


# 学生列表
def student_list(request):
    # 获取所有的学生对象
    data = models.Student.objects.all()
    student_info = models.Student.objects.all().count()
    # for i in student_info:
    #     print(i["id"], i["name"])
    # print(student_info.keys())
    # print(student_info.values())
    print(student_info)
    return render(request, "app02/student_list.html" ,{"student_list": data, "page": "student"})

# 添加学生
def add_student(request):
    # 返回一个form表单
    # 找到所有的班级对象
    data = models.Myclass.objects.all()
    if request.method == "POST":
        # post请求
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex_id = request.POST.get("sex")
        go_date = request.POST.get("date")
        class_id = request.POST.get("class")
        # 将数据添加到学生表中
        models.Student.objects.create(name=name, age=age, sex=sex_id, go_school=go_date, sclass_id=class_id)
        return redirect(reverse('app02:student_list'))

    return render(request, "app02/add_student.html", {"class_list": data})

# 删除
def del_student(request):
    # 获取被删除的id
    sid = request.GET.get("id")
    # 从学生表中找到这个学生并删除
    models.Student.objects.get(id=sid).delete()
    return redirect(reverse('app02:student_list'))

# 编辑
def edit_student(request):
    # 获取被编辑的学生id
    sid = request.GET.get("id")
    # 根据id获取这个对象
    student_obj = models.Student.objects.get(id=sid)
    # 获取所有班级的对象
    class_list = models.Myclass.objects.all()
    # 返回form表单
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex_id = request.POST.get("sex")
        go_date = request.POST.get("date")
        class_id = request.POST.get("class")
        models.Student.objects.filter(id=sid).update(
            name=name,
            age=age,
            sex = sex_id,
            go_school = go_date,
            sclass_id = class_id
        )
        return redirect(reverse('app02:student_list'))

    return render(request, "app02/edit_student.html", {"student": student_obj, "class_list": class_list})



# 教师表
def teacher_list(request):
    # 获取所有教师对象
    data = models.Teacher.objects.all()
    return render(request, "app02/teacher_list.html", {"teacher_list": data, "page": "teacher"})

# 添加教师
def add_teacher(request):
    # 找到所有的班级对象
    data = models.Myclass.objects.all()
    if request.method == "POST":
        # post请求
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex_id = request.POST.get("sex")
        class_id = request.POST.getlist("class")
        # 将教师数据添加到教师表中
        obj = models.Teacher.objects.create(name=name, age=age, sex= sex_id)
        # 将教师与班级对应关系添加到班级与教师第三张表中
        obj.myclass_set.add(*class_id)
        return redirect(reverse('app02:teacher_list'))

    return render(request, "app02/add_teacher.html", {"class_list": data})

# 删除一条数据
def del_teacher(request):
    tid = request.GET.get("id")
    # 从学生表中找到这个学生并删除
    models.Teacher.objects.get(id=tid).delete()
    return redirect(reverse('app02:teacher_list'))

# 编辑教师信息
def edit_teacher(request):
    # 获取被编辑的教师id
    tid = request.GET.get("id")
    # 根据id获取这个对象
    teacher_obj = models.Teacher.objects.get(id=tid)
    # 获取所有班级的对象
    class_list = models.Myclass.objects.all()
    # 返回form表单
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex_id = request.POST.get("sex")
        class_id = request.POST.getlist("class")
        models.Teacher.objects.filter(id=tid).update(
            name=name,
            age=age,
            sex=sex_id,
        )
        teacher_obj.myclass_set.set(class_id)
        return redirect(reverse('app02:teacher_list'))
    return render(request, "app02/edit_teacher.html", {"teacher": teacher_obj, "class_list": class_list})

# 班级列表
def class_list(request):
    # 获取所有的班级对象
    data = models.Myclass.objects.all()
    return render(request, "app02/class_list.html", {"class_list": data, "page": "class"})

# 添加班级
def add_class(request):
    # 找到所有的教师对象
    data = models.Teacher.objects.all()
    if request.method == "POST":
        # post请求
        name = request.POST.get("name")
        teacher_id = request.POST.getlist("teacher")
        # 将班级数据添加到班级表中
        obj = models.Myclass.objects.create(name=name)
        # 将教师与班级对应关系添加到班级与教师第三张表中
        obj.teacher.add(*teacher_id)
        return redirect(reverse('app02:class_list'))

    return render(request, "app02/add_class.html", {"teacher_list": data})

# 删除班级的一行数据
def del_class(request):
    # 获取被删除的班级的id
    cid = request.GET.get("id")
    # 根据id从班级表中删除
    models.Myclass.objects.get(id=cid).delete()
    # 返回到班级列表
    return redirect(reverse('app02:class_list'))

# 编辑班级信息
def edit_class(request):
    # 获取被编辑的班级id
    cid = request.GET.get("id")
    # 根据id获取这个对象
    class_obj = models.Myclass.objects.get(id=cid)
    # 获取所有教师的对象
    teacher_list = models.Teacher.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        teacher_id = request.POST.getlist("teacher")
        models.Myclass.objects.filter(id=cid).update(name=name,)
        class_obj.teacher.set(teacher_id)
        return redirect(reverse('app02:class_list'))
    return render(request, "app02/edit_class.html", {"class": class_obj, "teacher_list": teacher_list})



from django.forms import Form,fields,widgets

class StudentForm(Form):
    name = fields.CharField(min_length=2,max_length=32,
                            widget=widgets.TextInput(attrs={"class":"form-control"}))
    age = fields.IntegerField(min_value=18,max_value=30,
                              widget=widgets.TextInput(attrs={"class": "form-control"}))


# form组件测试
def student_form(request):
    stu_list = models.Student.objects.values("id", "name", "age")
    for row in stu_list:
        print(row["name"])

    stu_obj = models.Student.objects.all()
    return render(request, "app02/student_form.html", {"stu_list": stu_list, "stu_obj": stu_obj})

