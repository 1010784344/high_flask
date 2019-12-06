# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for,views,jsonify
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
# 有几个视图需要返回相同的变量

class ADSView(views.View):

    def __init__(self):
        # 我自己理解 super 意思是 ：我们是重新定义了__init__ 函数，
        # 但这个__init__ 函数要带上之前父类的初始化操作（父类的代码放到子类来执行），我们再额外添加一些东西进去
        super(ADSView,self).__init__()
        self.context = {'ads':'今年过节不收礼'}


class LoginView(ADSView):
    def dispatch_request(self):
        self.context.update({'username' : 'login'})
        return render_template('login.html',**self.context)



class RegistView(ADSView):
    def dispatch_request(self):
        self.context.update({'username': 'regist'})
        return render_template('regist.html', **self.context)


app.add_url_rule('/login/',endpoint='login',view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/',endpoint='regist',view_func=RegistView.as_view('regist'))


@app.route('/myworld/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

