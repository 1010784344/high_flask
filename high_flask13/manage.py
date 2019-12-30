# -*- coding: UTF-8 -*-
from flask_script import Manager
from app import app,Haxi,db


# 引入隔壁的 manager 对象
from db_script import db_manager



# 初始化一个 manager 对象（主manager对象）
manager = Manager(app)


# 将隔壁的 manager 对象，添加到这个主 manager 对象里面，构成子命令
manager.add_command('db',db_manager)



# 命令行不需要参数
@manager.command
def greet():
    print('你好')



# 命令行传递参数
@manager.option('-n','--name',dest='name')
def hello(name):
    print('hello',name)



# 命令行相关的数据库操作
@manager.option('-u','--username',dest='username')
@manager.option('-a','--age',dest='age')
def add_user(username,age):
    haxi = Haxi(username=username,age=age)
    db.session.add(haxi)
    db.session.commit()

if __name__ == '__main__':
    manager.run()