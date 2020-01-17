# -*- coding: UTF-8 -*-
from flask import Flask,template_rendered,render_template,got_request_exception

app = Flask(__name__)



# 模板渲染完成后的信号实例
def myrender(sender,template,context):
    print(sender)
    print(template)
    print(context)

template_rendered.connect(myrender)






# 视图函数发生异常的信号实例
def myexcept(sender,*args,**kwargs):
    # 当传参为*args,**kwargs，就包含了所有的参数（不管你传什么参数，我都能捕捉）
    print(args)
    print(kwargs)
    print('myexcept')

got_request_exception.connect(myexcept)




@app.route('/')
def hello_world():
    # a = 1/0
    return render_template('regist.html')








if __name__ == '__main__':
    app.run(debug=True)
