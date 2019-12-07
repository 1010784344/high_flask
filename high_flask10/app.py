# -*- coding: utf-8 -*-
from flask import Flask,render_template,views,request
from functools import wraps
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# 检验登录装饰器（访问控制）
def user_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_name = request.args.get('user_name')
        if user_name == 'wangzhe':
            return f(*args, **kwargs)
        else:
            return '请先登录！'
    return decorated_function


# 视图函数使用装饰器
@app.route('/myworld/')
@user_login_req
def index():
    if request.method == 'GET':
        return render_template('index.html')


# 标准类视图使用装饰器
class LoginView(views.View):
    decorators = [user_login_req]

    def dispatch_request(self):
        return '我要打篮球'


# 基于调度方法的类视图使用装饰器
class RegistView(views.MethodView):
    decorators = [user_login_req]

    def get(self):
        return '我要吃饭去'


app.add_url_rule('/login/',view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/',view_func=RegistView.as_view('regist'))


if __name__ == '__main__':
    app.run(debug=True)

