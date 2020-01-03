# -*- coding: UTF-8 -*-
# 蓝图生成子域名

from flask import Blueprint,request

abouttag = Blueprint('mytag',__name__,subdomain='tag')



@abouttag.route('/dealcookie/')
def dealcookie():

    # 获取 cookie
    username = request.cookies.get('username')

    return username or '没有获取到cookie'


