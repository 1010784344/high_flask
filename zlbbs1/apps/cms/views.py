# -*- coding: utf-8 -*-
from apps.cms import bp

@bp.route('/index/')
def index():
    return 'This is cms'