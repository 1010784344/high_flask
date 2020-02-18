# -*- coding: utf-8 -*-
from exts import db
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash

class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key= True,autoincrement= True)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50),nullable=False, unique= True)
    join_time = db.Column(db.DateTime,default=datetime.now)

    def __init__(self,username,password,email):
        self.username = username
        # 这里的 self.password 其实执行的 @property.setter 里的方法,其实是给 _password 赋了值
        self.password = password
        self.email = email

    # password属性（方法）获取值
    @property
    def password(self):
        return self._password

    # password属性（方法）赋值
    @password.setter
    def password(self, rawpassword):
        self._password = generate_password_hash(rawpassword)

    def check_password(self,rawpassword ):
        result = check_password_hash(self.password,rawpassword)
        return result


if __name__ == '__main__':
    print
    1