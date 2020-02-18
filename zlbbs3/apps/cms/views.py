# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,views

# 定义 cms 的蓝图
cms_bp = Blueprint('cms',__name__,url_prefix='/cms')


# 基于调度方法的类视图
class Login_View(views.MethodView):
    def get(self):
        # 渲染具有层级目录的书写方法
        return render_template('/cms/cms_login.html')
    def post(self):
        pass

# 基于调度方法的类视图和蓝图的结合使用（以前一直以为自己不会的东西）
cms_bp.add_url_rule('/login/',view_func=Login_View.as_view('login'))




















