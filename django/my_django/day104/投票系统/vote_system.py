# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 10:02
# @Author  : summer
# @File    : vote_system.py
# @Software: PyCharm

from flask import Flask, render_template, request, session, jsonify
import uuid
import queue


app = Flask(__name__)
app.secret_key = "summer"

vote_dict = {
    1: {"name": "summer", "vote": 100},
    2: {"name": "rain", "vote": 200},
    3: {"name": "blue", "vote": 300},
}

q_dict = {}

@app.route("/index/")
def index():
    """默认用户登录的时候给他创建一个唯一标识的uuid，对应一个q对象，保存在sesssion中，下次请求来的时候回携带这个uuid"""
    user_uuid = str(uuid.uuid4())
    q_dict[user_uuid] = queue.Queue()
    session["user_uuid"] = user_uuid
    return render_template("index.html", vote_dict=vote_dict)

@app.route("/vote/", methods=["get", "post"])
def vote():
    uid = request.json.get("uid")
    vote_dict[uid]["vote"] += 1
    for q in q_dict.values():
        q.put(vote_dict)
    return "投票成功"

@app.route("/getVote/")
def getVote():
    user_uuid = session.get("user_uuid")
    q = q_dict.get(user_uuid)
    try:
        res = q.get(timeout=30)
    except queue.Empty as e:
        res = ""
    return jsonify(res)



if __name__ == '__main__':
    app.run()