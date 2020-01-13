# -*- coding: UTF-8 -*-
from flask import Flask,render_template,request,session
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
        print(11111)
    return render_template('regist.html')

@app.route('/deal_session/',methods=['GET','POST'])
def deal_session():
    # 在 session 获取 csrf_token 的值
    key = session.get('csrf_token')
    return key






if __name__ == '__main__':
    app.run(debug=True)
