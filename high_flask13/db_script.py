# -*- coding: UTF-8 -*-
from flask_script import Manager

# 初始化一个 子命令 manager 对象
db_manager = Manager()



@db_manager.command
def init():
    print('迁移仓库创建完毕')

@db_manager.command
def revision():
    print('迁移脚本生产成功')

@db_manager.command
def upograde():
    print('脚本映射到数据库成功')