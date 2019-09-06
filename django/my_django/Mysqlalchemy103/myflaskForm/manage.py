# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 16:12
# @Author  : summer
# @File    : manage.py
# @Software: PyCharm

from myflaskForm import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()