# -*- coding: utf-8 -*-
from wtforms import Form,StringField,IntegerField
from wtforms.validators import Email,input_required,length


class LoginForm(Form):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'),input_required(message='请输入邮箱')])
    password = StringField(validators=[length(6,15,message='请输入正确格式的密码'),input_required(message='请输入密码')])
    remember = IntegerField()



if __name__ == '__main__':
    print
    1