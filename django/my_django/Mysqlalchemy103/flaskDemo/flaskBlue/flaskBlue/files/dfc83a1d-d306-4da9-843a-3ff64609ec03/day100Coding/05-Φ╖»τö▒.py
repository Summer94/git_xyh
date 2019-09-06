from flask import Flask, redirect, url_for

app = Flask(__name__)

# endpoint 默认函数的名字
@app.route("/book/<int:nid>", endpoint="book")
def book(nid):
    print(nid)
    print(type(nid))
    return "BOOK~~~"

@app.route("/")
def index():
    return redirect(url_for("book", nid=111))


if __name__ == '__main__':
    app.run()