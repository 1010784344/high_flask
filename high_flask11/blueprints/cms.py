# -*- coding: utf-8 -*-
from flask import Blueprint
# 添加子域名：subdomain
cms_bp = Blueprint('cms', __name__, subdomain='cms')

@cms_bp.route('/index/')
def index():
    return 'my is cms index'