# -*- coding: UTF-8 -*-
# 字段
from wtforms import Form,StringField,PasswordField,FileField
# 验证器(用来对输入的数据进行一些限制)
from wtforms.validators import InputRequired
#第一次使用 flask_wtf 里面的验证器，flask_wtf 虽然有验证器的功能，我们主要用他来做 CSRF
from flask_wtf.file import FileRequired,FileAllowed

# 注册表单的一个form
class RegistForm(Form):

    avatar = FileField(label='头像',
                            validators=[FileRequired(),FileAllowed(['jpg','png','gif'])])

    desc = PasswordField(label='提交',
                             validators=[InputRequired()])


