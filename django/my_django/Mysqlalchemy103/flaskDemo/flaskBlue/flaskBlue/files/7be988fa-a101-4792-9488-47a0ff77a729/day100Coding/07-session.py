from flask import Flask, render_template, request, session, redirect, make_response

app = Flask(__name__, template_folder="template")
# flask session 内部md5 加盐
app.config.from_object("settings.DEVConfig")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        pwd = request.form.get("pwd")
        if name == "yu" and pwd=="123":
            # 登陆成功 设置session
            session["userinfo"] = {"name": name}
            return redirect("/")

    return render_template("login.html")


@app.route("/")
def index():
    print(session.get("userinfo"))
    return "首页"


if __name__ == '__main__':
    app.run()