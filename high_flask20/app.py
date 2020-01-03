# -*- coding: UTF-8 -*-
from flask import Flask,Response
from blueprints.allcook import abouttag

app = Flask(__name__)

app.config['SERVER_NAME'] = 'hy.com:5000'

app.register_blueprint(abouttag)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 设置cookie
@app.route('/regist/',methods=['GET','POST'])
def regist():
    resp = Response('regist')

    # domain 设置 cookie 有效域名
    resp.set_cookie('username','wangzhe',domain='.hy.com')
    return resp





if __name__ == '__main__':
    app.run(debug=True)
