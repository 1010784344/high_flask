# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,views,request,redirect,url_for,session
from apps.cms.forms import LoginForm
from apps.cms.models import CMSUser


# 定义 cms 的蓝图
cms_bp = Blueprint('cms',__name__,url_prefix='/cms')


@cms_bp.route('/index/')
def index():
    return 'This is cms index!'

# 基于调度方法的类视图
class Login_View(views.MethodView):
    def get(self,message=None):
        # 渲染具有层级目录的书写方法
        return render_template('/cms/cms_login.html',message=message)
    def post(self):
        # 将页面提交的数据导入 wtforms 进行验证
        form = LoginForm(request.form)

        email = form.email.data
        password = form.password.data
        remember = form.remember.data

        if form.validate():
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['user_id'] = user.id

                # 对应页面的 remember me 功能
                # 如果设置 session.permanet = True，那么过期时间是 31天
                if remember:
                    session.permanent = True

                # 蓝图使用 url_for ，记得把蓝图的名字给加上。
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='邮箱或者密码错误')
                # return render_template('/cms/cms_login.html', message='邮箱或者密码错误')

        else:
            # 返回具体的错误验证信息
            # form.errors : {'password': ['请输入正确格式的密码']}
            message = form.errors.popitem()[1][0]
            # 表单验证错误（数据格式不对）
            return self.get(message=message)
            # return render_template('/cms/cms_login.html',message='表单验证错误（数据格式不对）')

# 基于调度方法的类视图和蓝图的结合使用（以前一直以为自己不会的东西）
cms_bp.add_url_rule('/login/',view_func=Login_View.as_view('login'))




















