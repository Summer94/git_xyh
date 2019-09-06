from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder="template")

book_list = [
    {"id": 1, "title": "人类简史"},
    {"id": 2, "title": "时间简史"},
    {"id": 3, "title": "未来简史"},
]

my_dict = {"age": 18}

def my_func():
    return '<h1>自定义函数返回内容</h1>'

# endpoint 默认函数的名字
@app.route("/book")
def book():

    return render_template("book.html", **{"book_list": book_list, "my_dict": my_dict, "my_func": my_func})

@app.route("/")
def index():
    return redirect(url_for("book"))


if __name__ == '__main__':
    app.run()