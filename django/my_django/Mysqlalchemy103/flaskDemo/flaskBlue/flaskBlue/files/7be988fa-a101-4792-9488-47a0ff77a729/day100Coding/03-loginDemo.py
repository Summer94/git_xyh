from flask import Flask, render_template, request, redirect

# template_folder = "templates"
# static_folder='static',
app = Flask(__name__, template_folder='template', static_url_path="/xxxx")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        if username == "yu" and pwd == "123":
            return redirect("/")
    return render_template("login.html")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()