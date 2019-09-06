# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 16:48
# @Author  : summer
# @File    : test.py
# @Software: PyCharm

from flask import Flask

app = Flask(__name__)

@app.route("/index", endpoint="index")
def index():
    return "index"

if __name__ == '__main__':
    app.run()