# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for,views
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


class ListView(views.View):
    def dispatch_request(self):
        return 'list view'

# view_func：类如何变成一个函数，不需要用类名初始化一个对象，直接使用类的名字调用他的类方法 as_view，
#  as_view 会返回一个函数， as_view 参数给 view_func 起个名字。
# as_view 底层是把 dispatch_request 分发给 view_func
app.add_url_rule('/list/',endpoint='list',view_func=ListView.as_view('list'))


@app.route('/myworld/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

