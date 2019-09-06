# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 21:20
# @Author  : summer
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask
from flask_session import Session
#第一步，导入SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
#第二步，实例化,注意在导入蓝图前实例化
db = SQLAlchemy()
from .views.user import userBlue

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.DevConfig")
    Session(app)
    app.register_blueprint(userBlue)
    #第三步，初始化db
    db.init_app(app)
    return app



