# -*- coding: UTF-8 -*-
from flask import Flask,g,session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'wangzherongyao'



# 视图函数使用 g 对象里的用户模型
@app.route('/')
def hello_world():
    if hasattr(g,'user'):
        print(g.user)
    return 'Hello World!'



# 模拟用户登录：user_id 赋值
@app.route('/regist/')
def regist():
    session['user_id'] = 1
    return 'regist'



# 钩子函数检查用户是否登录，并初始化用户模型放到 g 里面
@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        g.user = 'louna'




if __name__ == '__main__':
    app.run(debug=True)
