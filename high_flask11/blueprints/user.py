# -*- coding: utf-8 -*-
from flask import Blueprint

# 定义蓝图

# url_prefix,因为我们属于 user 模块，使用这个可以给蓝图下面的所有url添加一样的前缀
user_bp = Blueprint('user',__name__,url_prefix='/user')

@user_bp.route('/profile/')
def profile():
    return '个人中心'


@user_bp.route('/setting/')
def setting():
    return '设置'


