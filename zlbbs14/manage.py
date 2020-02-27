# -*- coding: utf-8 -*-
from zlbbs import app
from exts import db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from apps.cms import models as cms_modles

CMSUser = cms_modles.CMSUser
CMSRole = cms_modles.CMSRole
CMPermission = cms_modles.CMPermission

# flask_script 里的 manager（有了这个才会支持在命令行执行代码的行为）
# flask_script 的 manager 对象是执行所有命令的发号施令者（）
manager = Manager(app)

#创建子命令(flask_migrate 说白了就是我们这里另一个文件里配置的子命令，
# flask_migrate 这个模块功能相对来说就是比较简单，就是只是数据库迁移，
# 且封装在一个子命令里面)
Migrate(app,db)

# 将子命令添加到发号施令者（命令行）上面
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




# 运用 flask_script 添加命令的实战（不需要传递参数）
# 给系统添加所有的角色
@manager.command
def add_cms_role():
    # 1.访问者（可以修改个人信息）
    vistors = CMSRole(name='访问者',desc='只能相关数据，不能修改。')
    vistors.permissions = CMPermission.VISITOR

    # 2.运营角色（修改个人信息，管理帖子，管理评论，管理前台用户。）
    operator = CMSRole(name='运营',desc='管理帖子，管理评论，管理前台用户。')
    operator.permissions = CMPermission.VISITOR|CMPermission.POSTER|CMPermission.CMSUSER\
    |CMPermission.COMMENTER|CMPermission.FRONTUSER

    # 3.管理员（拥有绝大部分权限）
    admin = CMSRole(name='管理员', desc='拥有本系统所有权限。')
    admin.permissions = CMPermission.VISITOR | CMPermission.POSTER | CMPermission.CMSUSER \
                           | CMPermission.COMMENTER | CMPermission.FRONTUSER | CMPermission.BOARDER

    # 4.开发者
    developer = CMSRole(name='开发者', desc='开发人员专用角色。')
    developer.permissions = CMPermission.ALL_PERMISSION

    db.session.add_all([vistors,operator,admin,developer])
    db.session.commit()






if __name__ == '__main__':
    manager.run()