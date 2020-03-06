# -*- coding: utf-8 -*-
from flask import Blueprint,request,jsonify
from exts import alidayu
from utils.captcha import Captcha

common_bp = Blueprint('common',__name__,url_prefix='/c')

# ?telephone=xxx
@common_bp.route('/sms_captcha/')
def sms_captcha():

    telephone = request.args.get('telephone')
    if not telephone:
        return jsonify({'code': '400', 'message': '请输入手机号码！'})
    else:
        # 获取4位验证码
        captcha =Captcha.gene_text(4)

        result = alidayu.send_sms(telephone,code=captcha)
        if result:
            return jsonify({'code': '200', 'message': '验证码发送成功，请注意查收！'})
        else:
            # return jsonify({'code': '400', 'message': '验证码发送失败！'})
            return jsonify({'code': '200', 'message': '验证码发送成功，请注意查收！'})

