# -*- coding: UTF-8 -*-
from flask import Flask,current_app,url_for



app = Flask(__name__)

# 应用上下文使用实例：current_app
# 视图函数外面调用
# # 方法一
# app_context = app.app_context()
# app_context.push()
# print(current_app.name)

# 方法二
with app.app_context():
    print(current_app.name)


@app.route('/')
def hello_world():
    print(current_app.name)
    return 'Hello World!'



# 请求上下文使用实例：url_for

@app.route('/getregist/')
def get_regist():

    return url_for('regist')


@app.route('/regist/')
def regist():
    return 'Please Regist!'

# 视图函数外面调用
with app.test_request_context():
    print(url_for('regist'))





if __name__ == '__main__':
    app.run(debug=True)
