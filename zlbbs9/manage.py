# -*- coding: utf-8 -*-
from zlbbs import app
from exts import db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from apps.cms import models as cms_modles

CMSUser = cms_modles.CMSUser

# flask_script 的 manager 对象是执行所有命令的发号施令者
manager = Manager(app)

#创建命令
Migrate(app,db)

# 将命令添加到发号施令者上面
manager.add_command('db',MigrateCommand)


# 给 manager.py 添加一条命令:在 manage.py 通过 flask-script 给 cms 添加一个用户
@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
def create_cms_user(username,password,email):
    user = CMSUser(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print('cms 用户添加成功！')




if __name__ == '__main__':
    manager.run()