# -*- coding: UTF-8 -*-
from app import db


class Haxi(db.Model):
    # 指定表名
    __tablename__ = 'Haxi'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.String(50), unique=True, nullable=False)

    #规定查询之后的信息呈现
    def __repr__(self):
        return '<User %r>' % self.username