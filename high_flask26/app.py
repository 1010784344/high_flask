# -*- coding: UTF-8 -*-
from flask import Flask,g,session,render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'wangzherongyao'



@app.route('/')
def hello_world():
    # 使用所有模板共享的变量 username
    return render_template('regist.html')


@app.route('/regist/')
def regist():
    session['user_id'] = 1
    return 'regist'


# 定义所有模板共享的变量 username
@app.context_processor
def context_processor():

    if hasattr(g,'user'):
        return {'username':'zhangfei'}
    else:
        return {}




@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        g.user = 'louna'




if __name__ == '__main__':
    app.run(debug=True)
