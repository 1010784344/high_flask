# -*- coding: UTF-8 -*-
from flask import Flask,request,render_template

app = Flask(__name__)

# 字段
from wtforms import Form,StringField,PasswordField
# 验证器(用来对输入的数据进行一些限制)
from wtforms.validators import DataRequired,Length,EqualTo


# 注册表单的一个form
class RegistForm(Form):

    user_name = StringField(label='用户名',
                            validators=[DataRequired(message='用户名不能为空！'),
                                                   Length(min=3,max=15,message='用户名长度在3到15个字符之间！')])

    user_pwd = PasswordField(label='用户密码',
                             validators=[DataRequired(message='用户密码不能为空！'),
                                                     Length(min=3, max=5, message='用户密码长度在3到5个字符之间！')])

    user_equalpwd = StringField(label='确认密码',
                             validators=[DataRequired(message='用户邮箱不能为空！'),
                                         Length(min=3, max=5, message='用户密码长度在3到5个字符之间！'), EqualTo('user_pwd')])


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        #传入需要进行验证的数据(数据保存在 request 对象的 form 属性里)，初始化验证器对象，
        form = RegistForm(request.form)
        #validate ，检查验证数据的情况
        if form.validate():
            return 'success'
        else:
            # 把验证器收集的错误信息输出出来
            print(form.errors)
            return 'fail'



if __name__ == '__main__':
    app.run(debug=True)
