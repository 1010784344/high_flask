# -*- coding: UTF-8 -*-
import os
from flask import Flask,request,render_template,send_from_directory
from forms import RegistForm
from werkzeug.utils import CombinedMultiDict,secure_filename
app = Flask(__name__)

# 获取文件保存路径
IMAGEDIR = os.path.dirname(__file__)
print(IMAGEDIR)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        #传入需要进行验证的数据(数据保存在 request 对象的 form 属性里)，初始化验证器对象，
        # 获取上传的数据和获取上传的文件的方式是不一样的：request.form 和 request.files，这里使用 CombinedMultiDict 将两者结合在一起

        form = RegistForm(CombinedMultiDict([request.form,request.files]))
        #validate ，检查验证数据的情况
        if form.validate():

            print(form.desc.data)

            image =form.avatar.data
            # 文件名检查
            imagename = secure_filename(image.filename)
            image.save(os.path.join(IMAGEDIR,imagename))

            return 'success'

        else:
            # 把验证器收集的错误信息输出出来
            print(form.errors)
            return 'fail'


@app.route('/images/<image>')
def images(image):
    # 文件生成 url
    return send_from_directory(IMAGEDIR,image)

if __name__ == '__main__':
    app.run(debug=True)
