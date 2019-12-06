# -*- coding: utf-8 -*-
from flask import Flask,render_template,views,request
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

class Login(views.MethodView):
    def get(self):
        return render_template('login.html')
    def post(self):
        username =  request.form.get('username')
        password =  request.form.get('password')
        print(username)
        print(password)
        if username == 'wangzhe' and password == '123456':
            return '登录成功'
        else:
            return render_template('login.html',error = '用户名或者密码错误')




@app.route('/myworld/')
def index():
    return render_template('index.html')


app.add_url_rule('/login/',view_func=Login.as_view('login'))


if __name__ == '__main__':
    app.run(debug=True)

