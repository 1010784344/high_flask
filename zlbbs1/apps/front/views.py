# -*- coding: utf-8 -*-
from apps.front import bp


@bp.route('/index/')
def index():
    return 'This is front'

