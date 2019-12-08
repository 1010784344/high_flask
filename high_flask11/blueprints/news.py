# -*- coding: utf-8 -*-
from flask import Blueprint,render_template
# 第一步：定义蓝图
news_bp = Blueprint('news',__name__)

@news_bp.route('/newslist/')
def newslist():
    # 蓝图中使用模板文件
    return render_template('newslist.html')



@news_bp.route('/newsdetail/')
def newsdetail():
    return '新闻详情'



