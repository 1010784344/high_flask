# -*- coding: UTF-8 -*-
from flask import Flask,render_template,request
from flask_wtf import CSRFProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = r'backup'

# 开启 CSRF 防御的功能
CSRFProtect(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'POST':
        return '登录成功'
    return render_template('regist.html')




if __name__ == '__main__':
    app.run(debug=True)
