# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 21:19
# @Author  : summer
# @File    : manage.py
# @Software: PyCharm

from flaskBlue import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

# 数据库迁移命名
# 依赖 flask-script
# python3 manage.py db init # 初始化
# python3 manage.py db migrate # makemigrations
# python3 manage.py db upgrade # migrate



#自定义命令
@manager.option("-n", "--name", dest="name")
@manager.option("-u", "--url", dest="url")
def cmd(name, url):  # python3 manage.py cmd -n "summer" -u "127.0.0.1"
    print(name, url)

if __name__ == '__main__':
    manager.run()  #python3 manage.py runserver -h 127.0.0.1 -p 5000  启动项目