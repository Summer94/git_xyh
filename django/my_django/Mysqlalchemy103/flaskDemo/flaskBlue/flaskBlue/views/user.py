# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 21:25
# @Author  : summer
# @File    : user.py
# @Software: PyCharm

from flask import Blueprint, session, render_template, request
from flaskBlue import db
from flask import current_app as app
from ..models import Tag
import shutil
import zipfile
import os
import uuid
from werkzeug.utils import secure_filename

userBlue = Blueprint("userBlue", __name__)


@userBlue.route("/index/")
def index():
    tag_obj = Tag(title="python")
    db.session.add(tag_obj)
    db.session.commit()
    db.session.close()
    session["summer"] = "2019"
    return "index"


@userBlue.route("/see/", endpoint="see")
def see():
    obj = db.session.query(Tag).filter_by(id=1).first()
    print(session["summer"])
    return obj.title


@userBlue.route("/upload/", endpoint="upload", methods=["get", "post"])
def upload_file():
    if request.method == "POST":
        file_obj = request.files.get("myFile")
        print(file_obj)
        if file_obj:
            file_name = file_obj.filename
            if file_name.rsplit('.',1)[-1]=="zip":
                upload_path = os.path.join(app.config.root_path, "files", str(uuid.uuid4()))
                print(upload_path)
                shutil._unpack_zipfile(file_obj, upload_path)
                file_list = []
                for (dirpath,dirname,filenames) in os.walk(upload_path,):
                    print(filenames, "------")
                    for filename in filenames:
                        if not filename.endswith(".py"):
                            continue
                        file_path = os.path.join(dirpath, filename)
                        file_list.append(file_path)

                sum_num = 0
                for file in file_list:
                    with open(file, "r") as f:
                        for line in f:
                            if line.strip().startswith("#"):
                                continue
                            sum_num += 1
                print(sum_num)
                return str(sum_num)






    return render_template("upload.html")
