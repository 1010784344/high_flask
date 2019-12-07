# -*- coding: utf-8 -*-
from flask import Blueprint
# 定义蓝图
news_bp = Blueprint('news',__name__)

@news_bp.route('/newslist/')
def newslist():
    return '新闻列表'



@news_bp.route('/newsdetail/')
def newsdetail():
    return '新闻详情'



