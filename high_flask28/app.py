# -*- coding: UTF-8 -*-
from flask import Flask,g,request
from signal_demo import nake_signal

app = Flask(__name__)




@app.route('/')
def hello_world():

    return '欢迎来到王者荣耀'



@app.route('/login/')
def login():
    # http://127.0.0.1:5000/login/?user=bajie
    user = request.args.get('user')

    if user:
        g.user = user
        # 触发信号
        nake_signal.send()
        return '登录成功'
    else:
        return '请输入用户名'







if __name__ == '__main__':
    app.run(debug=True)
