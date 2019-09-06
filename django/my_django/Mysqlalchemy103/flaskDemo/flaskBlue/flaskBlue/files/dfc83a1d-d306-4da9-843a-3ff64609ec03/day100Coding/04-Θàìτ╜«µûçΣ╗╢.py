from flask import Flask
/Users/summer/Desktop/qq接受文件/day100Coding/settings.py
app = Flask(__name__)
# app.config["DEBUG"] = True
# app.config.from_object("settings.DEVConfig")
app.config.from_object("settings.ProConfig")

@app.route("/")
def index():
    print(app.config)
    # app.config["DEBUG"] = True
    # print(app.config)
    return "主页~~"

if __name__ == '__main__':
    app.run()
