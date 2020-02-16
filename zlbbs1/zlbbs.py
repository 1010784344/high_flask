from flask import Flask

from apps.cms.views import cms_bp
from apps.common.views import common_bp
from apps.front.views import front_bp


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
