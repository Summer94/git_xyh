# -*- coding: utf-8 -*-.
# @Time    : 2019/1/3 16:12
# @Author  : summer
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


db = SQLAlchemy()
from .views.user import userBlue


def create_app():
    app = Flask(__name__)
    Session(app)
    app.config.from_object("settings.DevConfig")
    app.register_blueprint(userBlue)
    db.init_app(app)
    return app