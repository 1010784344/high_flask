# -*- coding: UTF-8 -*-
from app import app
from exts import db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand


# 创建主 manager 对象
manager = Manager(app)
#用来绑定 app 和 db 到 flask_migrate
Migrate(app,db)
#添加 Migrate 的所有子命令到 主 manager 对象
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()