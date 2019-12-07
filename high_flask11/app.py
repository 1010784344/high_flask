# -*- coding: utf-8 -*-
from flask import Flask,render_template
from blueprints.user import user_bp
from blueprints.news import news_bp

app = Flask(__name__)
# app 绑定蓝图
app.register_blueprint(user_bp)
app.register_blueprint(news_bp)


app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/myworld/')
def index():

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

