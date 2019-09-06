# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 17:05
# @Author  : summer
# @File    : forms.py
# @Software: PyCharm
from django import forms
from django.core.validators import RegexValidator

from .models import Customer, ConsultRecord, Enrollment, ClassList, CourseRecord, StudyRecord, PaymentRecord

# 注册的form组件
class RegisterForm(forms.Form):

    name = forms.CharField(
        max_length=32,
        label="用户名",
        strip=True,  # 是否移除用户输入空白
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "max_length": "用户名最长32位",
        },
        widget=forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "用户名"})
    )
    password = forms.CharField(
        min_length=8,
        max_length=11,
        label="密码",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "密码最短8位",
            "max_length": "密码最长11位",
        },
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}, )
    )
    re_password = forms.CharField(
        min_length=8,
        max_length=11,
        label="确认密码",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "密码最短8位",
            "max_length": "密码最长11位",
        },
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "确认密码"}, )
    )
    email = forms.CharField(
        label="邮箱",
        error_messages={
            "required": "不能为空",
            "invalid": "请输入正确的邮箱地址",
        },
        widget=forms.widgets.EmailInput(attrs={"class": "form-control", "placeholder": "邮箱"}, ),
        validators=[RegexValidator(r"[1-9][0-9]{4,12}@qq\.com", "请输入正确的qq邮箱")]
    )

    mobile = forms.CharField(
        label="手机号",
        error_messages={
            "required": "不能为空",
            "invalid": "请输入正确的手机号",
            "max_length": "手机号最长11位",
        },
        widget=forms.widgets.TextInput(attrs={"class": "form-control", "placeholder": "手机号"}, ),
        validators=[RegexValidator(r"^1[3-9]\d{9}$", "请填入正确的手机号")]
    )


#客户列表
class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            "course": forms.widgets.SelectMultiple
        }

#沟通记录
class ConsultRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConsultRecordForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        self.fields['customer'] = forms.models.ModelChoiceField(
            queryset=Customer.objects.filter(consultant=self.instance.consultant))
        # 修改跟进人只能是自己
        self.fields['consultant'].choices = [(self.instance.consultant.id, self.instance.consultant.name), ]

    class Meta:
        model = ConsultRecord
        exclude = ['delete_status', ]
        widgets = {
            "course": forms.widgets.SelectMultiple
        }


#报名表
class EnrollMentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
        self.fields['customer'].choices = [(self.instance.customer.id, self.instance.customer.name)]

    class Meta:
        model = Enrollment
        exclude = ['contract_approved', ]


#班级表
class ClassListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    class Meta:
        model = ClassList
        fields = "__all__"

# 课程记录
class CourseRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        self.fields["re_class"].choices = [(self.instance.re_class.id, self.instance.re_class.course)]

    class Meta:
        model = CourseRecord
        fields = '__all__'


# 学习记录的
class StudyRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
    class Meta:
        model = StudyRecord
        fields = ['student', 'attendance', 'score', 'homework_note']


# 支付记录
class PaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        # 缴费的客户只能是自己的客户
        # self.fields['consultant'].choices = [(self.instance.consultant.id, self.instance.consultant.name), ]

    class Meta:
        model = PaymentRecord
        fields = "__all__"



