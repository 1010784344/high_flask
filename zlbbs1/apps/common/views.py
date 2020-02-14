# -*- coding: utf-8 -*-
from apps.common import bp


@bp.route('/index/')
def index():
    return 'This is commmon'


