from flask import Flask

from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp


import config

app = Flask(__name__)

# 引入配置文件
app.config.from_object(config)

# 注册蓝图到app
app.register_blueprint(cms_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)



if __name__ == '__main__':
    app.run()
