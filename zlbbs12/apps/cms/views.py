# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,views,request,redirect,url_for,session,g,jsonify
from apps.cms.forms import LoginForm,ResetpwdForm,ResetemailForm
from apps.cms.models import CMSUser
import config
from apps.cms.decorators import LoginRequired
from exts import db,mail
from flask_mail import Message
import string
import random

# 定义 cms 的蓝图
cms_bp = Blueprint('cms',__name__,url_prefix='/cms')

# cms 首页
@cms_bp.route('/index/')
@LoginRequired
def index():
    return render_template('/cms/cms_index.html')

# cms 注销
@cms_bp.route('/logout/')
@LoginRequired
def logout():
    session.pop(config.CMS_USER_ID)
    return redirect(url_for('cms.login'))


# cms 个人中心
@cms_bp.route('/profile/')
@LoginRequired
def profile():

    return render_template('cms/cms_profile.html')


# cms 给指定邮箱发送验证码（ajax 调用）
@cms_bp.route('/sendcaptcha/')
def sendcaptcha():

    #/cms/sendcaptcha/?email=1010784344@qq.com

    # 获取邮箱（给谁发）
    email = request.args.get('email')
    if not email:
        return jsonify({'code': '400', 'message': '请输入邮箱！'})
    else:


        # 获取验证码（内容）
        allcaptcha = list(string.ascii_letters)
        allcaptcha.extend(map(lambda x:str(x),range(0,10)))
        captcha = ''.join(random.sample(allcaptcha,6))


        #发送验证码
        message = Message('王者荣耀论坛邮箱验证码', recipients=[email], body='您的邮箱验证码是：%s'%captcha)
        try:
            mail.send(message)
        except:
            return jsonify({'code': '400', 'message': '网络错误！'})

        return jsonify({'code': '200', 'message': '验证码已经发送至您的邮箱，请确认！'})



# 发送邮件测试
@cms_bp.route('/emailbug/')
def emailbug():
    # 邮件主题，收件人列表，邮件正文
    message = Message('邮件发送',recipients=['1010784344@qq.com'],body='测试')
    mail.send(message)
    return 'success'




# cms 登录
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

                session[config.CMS_USER_ID] = user.id

                # 对应页面的 remember me 功能
                # 如果设置 session.permanet = True，那么过期时间是 31天
                if remember:
                    session.permanent = True

                # 蓝图使用 url_for ，记得把蓝图的名字给加上。
                # 使用 url_for 反转蓝图的普通视图函数
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


# cms 修改密码
class ResetPwd_View(views.MethodView):

    # 基于调度方法添加装饰器
    decorators = [LoginRequired]

    def get(self):
        # 渲染具有层级目录的书写方法
        return render_template('/cms/cms_resetpwd.html')
    def post(self):
        # 将页面提交的数据导入 wtforms 进行验证
        form = ResetpwdForm(request.form)

        if form.validate():

            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            print(oldpwd)
            # 这个就不需要获取了，因为关于和新密码不一致的问题，
            # forms.py 里面的 wt-form 验证器已经帮我们验证过了
            # newpwd2 = form.newpwd2.data

            # user 对象在钩子函数里面已经提前获取过了
            user = g.cms_user

            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()

                # 返回json数据
                return jsonify({'code': '200', 'message': '密码修改成功！'})
            else:
                return jsonify({'code':'400','message':'旧密码输入错误！'})
        else:
            # 返回具体的错误验证信息
            # form.errors : {'password': ['请输入正确格式的密码']}
            message = form.errors.popitem()[1][0]
            # 表单验证错误（数据格式不对）

            return jsonify({'code': '400', 'message': message})

# cms 修改邮箱
class ResetEmail_View(views.MethodView):

    # 基于调度方法添加装饰器
    decorators = [LoginRequired]

    def get(self):
        return render_template('/cms/cms_resetemail.html')

    def post(self):
        # 将页面提交的数据导入 wtforms 进行验证
        form = ResetemailForm(request.form)

        if form.validate():
            pass

        else:
            pass

# 基于调度方法的类视图和蓝图的结合使用（以前一直以为自己不会的东西）
# 特别注意这有个东西，as_view ，给 view_func 起个名字，相当于非类写法里面的视图函数
cms_bp.add_url_rule('/login/',view_func=Login_View.as_view('login'))
cms_bp.add_url_rule('/resetpwd/',view_func=ResetPwd_View.as_view('resetpwd'))
cms_bp.add_url_rule('/resetemail/',view_func=ResetEmail_View.as_view('resetemail'))





















