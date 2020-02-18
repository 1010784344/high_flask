# -*- coding: utf-8 -*-

import os
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/zlbbs?charset=utf8'
# SQLALCHEMY 里面的模型一有变动，那么他都会给我们发送一个信号，没有必要会浪费性能
SQLALCHEMY_TRACK_MODIFICATIONS = True
# session 加密
SECRET_KEY = os.urandom(24)