# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 19:18
# @Author  : summer
# @File    : forms.py
# @Software: PyCharm

from wtforms import Form, widgets, validators
from wtforms.fields import simple, core, html5
from .models import Book


class RegisterForm(Form):
    name = simple.StringField(
        label="用户名",
        validators=[validators.DataRequired(message="用户名不能为空")]
    )
    pwd = simple.PasswordField(
        label="密码",
        validators=[validators.DataRequired(message="密码不能为空")],
        widget=widgets.PasswordInput()
        # render_kw={'class': 'form-control'}  给标签加样式
    )
    re_pwd = simple.PasswordField(
        label="确认密码",
        validators=[validators.DataRequired(message="密码不能为空"),
                    validators.EqualTo('pwd', message="两次密码不一致")],
        widget=widgets.PasswordInput()
        # render_kw={'class': 'form-control'}  给标签加样式
    )
    email = html5.EmailField(
        label="邮箱",
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
    )
    gender = core.RadioField(
        label='性别',
        choices=(
            (1, '男'),
            (2, '女'),
        ),
        coerce=int
    )
    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )
    city = core.SelectField(
        label='城市',
        choices=(
            ('bj', '北京'),
            ('sh', '上海'),
        )
    )
    hobby = core.SelectMultipleField(
        label='爱好',
        choices=Book.TYPE,
        coerce=int
    )

    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     # 从数据库获取数据 做到实时更新
    #     # 当我们每次实例化Form的时候都去获取一遍数据
    #     self.favor.choices = "数据库中的数据"
