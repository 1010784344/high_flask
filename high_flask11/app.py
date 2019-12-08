# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for
from blueprints.user import user_bp
from blueprints.news import news_bp
from blueprints.cms import cms_bp

app = Flask(__name__)
# 第二步 ：app 绑定蓝图
app.register_blueprint(user_bp)
app.register_blueprint(news_bp)
app.register_blueprint(cms_bp)


app.config['TEMPLATES_AUTO_RELOAD'] = True
# 修改域名
app.config['SERVER_NAME'] = 'lirui.com:5000'



@app.route('/myworld/')
def index():
    # 使用 url_for 反转蓝图
    print(url_for('news.newslist'))
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

