# -*- coding: utf-8 -*-
# from apps.front import bp
from flask import Blueprint

front_bp = Blueprint('front',__name__)

@front_bp.route('/index/')
def index():
    return 'This is front'

