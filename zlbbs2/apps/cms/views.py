# -*- coding: utf-8 -*-
from flask import Blueprint

cms_bp = Blueprint('cms',__name__,url_prefix='/cms')

@cms_bp.route('/index/')
def index():
    return 'This is cms'