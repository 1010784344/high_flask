# -*- coding: UTF-8 -*-

SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:123456@localhost/your_test'

# TRUE 数据库里面的数据一变化，sqlalchemy 也会跟着变化
SQLALCHEMY_TRACK_MODIFICATIONS = True