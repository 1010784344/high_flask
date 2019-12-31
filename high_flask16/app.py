# -*- coding: UTF-8 -*-
from flask import Flask
import config
from exts import db
# 没有这一行的话，执行 python manage.py db migrate，会报错
from models import Haxi

app = Flask(__name__)


# 从外部引入配置文件到 app
app.config.from_object(config)


#防止循环引用，db 连接 app
db.init_app(app)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
