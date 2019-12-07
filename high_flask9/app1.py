# -*- coding: utf-8 -*-
from flask import Flask,render_template,views,request
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

class Login(views.MethodView):
    # 为了保持 get 函数书写格式的标准性，就把这个有传参处理的 render_template 函数抽取出来
    def __render(self,error=None):
        return render_template('login.html', error=error)

    def get(self):
        self.__render()

    def post(self):
        username =  request.form.get('username')
        password =  request.form.get('password')
        print(username)
        print(password)
        if username == 'wangzhe' and password == '123456':
            return '登录成功'
        else:
            self.__render(error='用户名或者密码错误')


@app.route('/myworld/')
def index():
    if request.method == 'GET':
        return render_template('index.html')


app.add_url_rule('/login/',view_func=Login.as_view('login'))


if __name__ == '__main__':
    app.run(debug=True)

