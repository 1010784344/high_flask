# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for,views,jsonify
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
# 有几个 url 需要返回 json 数据

class JsonView(views.View):

    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())



class ListView(JsonView):
    # 重写以上父类的 get_data 方法，一旦请求‘/list/’,就会直接执行 dispatch_request 这个函数
    def get_data(self):
        return {'username':'wangzhe','password':'123456'}


app.add_url_rule('/list/',endpoint='list',view_func=ListView.as_view('list'))


@app.route('/myworld/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

