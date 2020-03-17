from flask import Flask,jsonify,render_template
import qiniu

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('qiniu.html')

# 获取 uptoken 的接口
@app.route('/uptoken/')
def uptoken():
    AccessKey = 'PE4avHSNHAKI91mKjk8l7g-DhTQM9KSoxesVf9V3'
    SecretKey = 'nMi3pP0nOEGX2OaC2KiY972UGFZ27wSiWM5qMLFO'
    q = qiniu.Auth(AccessKey,SecretKey)

    # 七牛某个存储空间名称
    bucket = 'dashu666'

    token = q.upload_token(bucket)
    # 方便前端 js 进行调用
    return jsonify({'uptoken':token})

if __name__ == '__main__':
    app.run(debug=True)
