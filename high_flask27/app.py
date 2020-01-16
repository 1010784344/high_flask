# -*- coding: UTF-8 -*-
from flask import Flask,abort

app = Flask(__name__)




@app.route('/')
def hello_world():
    # 手动抛出相应的错误页面
    abort(404)
    return '欢迎来到王者荣耀'


# 定制 404 错误，相当于重写
@app.errorhandler(404)
def catch_cat(error):
    return '恭喜你抓到一只大猫猫'

# 定制 500 错误，相当于重写
@app.errorhandler(500)
def page_not_find(error):
    return '大猫猫'


if __name__ == '__main__':
    app.run(debug=True)
