# -*- coding: utf-8 -*-
from flask import Blueprint

common_bp = Blueprint('common',__name__,url_prefix='/common')


@common_bp.route('/index/')
def index():
    return 'This is commmon'


