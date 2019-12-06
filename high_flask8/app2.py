# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for,views,jsonify
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
# 有几个 url 需要返回 json 数据

class ADSView(views.View):

    def __init__(self):
        self.context = {'ads':'j'}


class LoginView(ADSView):

    def dispatch_request(self):
        return jsonify(self.get_data())



class RegistView(ADSView):


    def dispatch_request(self):
        return jsonify(self.get_data())


app.add_url_rule('/list/',endpoint='list',view_func=ListView.as_view('list'))


@app.route('/myworld/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

