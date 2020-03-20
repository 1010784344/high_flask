# -*- coding: UTF-8 -*-
from exts import db
from datetime import datetime

# 添加 轮播图弹窗 的数据模型

class BannersModel(db.Model):

    __tablename__ = 'banner'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(255),nullable=False)
    image_url = db.Column(db.String(255),nullable=False)
    link_url = db.Column(db.String(255),nullable=False)
    priority = db.Column(db.Integer,default=0)
    creat_time = db.Column(db.DateTime,default=datetime.now)


# 添加 板块管理 的数据模型
class BoardModel(db.Model):

    __tablename__ = 'board'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(255),nullable=False)
    creat_time = db.Column(db.DateTime,default=datetime.now)



if __name__ == '__main__':
    pass