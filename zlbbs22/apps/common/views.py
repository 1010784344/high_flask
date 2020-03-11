# -*- coding: utf-8 -*-
from flask import Blueprint,request,jsonify,make_response
from exts import alidayu
from utils.captcha import Captcha
from utils import zlmemcache
from io import BytesIO
from apps.common.forms import SMSCaptchaForm

common_bp = Blueprint('common',__name__,url_prefix='/c')

# 加密前
# 注册页面返回手机短信验证
# ?telephone=xxx
# @common_bp.route('/sms_captcha/')
# def sms_captcha():
#
#     telephone = request.args.get('telephone')
#     if not telephone:
#         return jsonify({'code': '400', 'message': '请输入手机号码！'})
#     else:
#         # 获取4位验证码
#         captcha =Captcha.gene_text(4)
#
#         result = alidayu.send_sms(telephone,code=captcha)
#         if result:
#             return jsonify({'code': '200', 'message': '验证码发送成功，请注意查收！'})
#         else:
#             # return jsonify({'code': '400', 'message': '验证码发送失败！'})
#             return jsonify({'code': '200', 'message': '验证码发送成功，请注意查收！'})



# 加密后
# 注册页面返回手机短信验证
@common_bp.route('/sms_captcha/',methods=['POST'])
def sms_captcha():

    form = SMSCaptchaForm(request.form)

    if form.validate():

        telephone = form.telephone.data
        # 获取4位验证码
        captcha =Captcha.gene_text(4)

        result = alidayu.send_sms(telephone,code=captcha)
        if result:
            # 储存短信验证码到内存中（memcached）
            zlmemcache.set(telephone, captcha)
            print(captcha)
            return jsonify({'code': '200', 'message': '验证码发送成功，请注意查收！'})
        else:
            # 储存短信验证码到内存中（memcached）（测试假设短信发送成功）
            zlmemcache.set(telephone, captcha)
            print(captcha)

            # return jsonify({'code': '400', 'message': '验证码发送失败！'})
            return jsonify({'code': '200', 'message': '验证码发送成功，请注意查收！'})
    else:
        return jsonify({'code': '400', 'message': '参数错误！'})




#注册页面返回图片验证
@common_bp.route('/captcha/')
def graph_captcha():
    # 获取验证码
    text,image = Captcha.gene_graph_captcha()

    # 储存图片验证码到内存中（memcached）
    zlmemcache.set(text.lower(), text.lower())

    # 将 image 对象转化为 二进制流
    out = BytesIO()
    image.save(out,'png')
    out.seek(0)

    # 返回请求：二进制流数据
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp




















