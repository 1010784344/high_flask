# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# 旧方法不指定 endpoint
@app.route('/myworld/')
def index():
    print(url_for('test'))
    return render_template('index.html')


# 旧方法也可以指定 endpoint
@app.route('/myworldtest/',endpoint='test')
def myworld():
    return 'myworldtest'


# 新方法
def mylist():
    return 'mylist'

app.add_url_rule('/mylist/',endpoint='fighting',view_func=mylist)


# 制造请求上下文环境
# 因为 url_for 是 flask 里的函数，而运行 flask 里面的东西，都是必须依赖上下文环境
with app.test_request_context():
    print(url_for('fighting'))


if __name__ == '__main__':
    app.run(debug=True)

