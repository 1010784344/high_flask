# -*- coding: UTF-8 -*-
from flask import Flask,request,Response
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# 设置cookie
@app.route('/regist/',methods=['GET','POST'])
def regist():
    resp = Response('regist')
    resp.set_cookie('username','wangzhe')
    return resp

# 删除cookie
@app.route('/images/',methods=['GET','POST'])
def images():
    resp = Response('images')
    resp.delete_cookie('username')
    return resp



if __name__ == '__main__':
    app.run(debug=True)
