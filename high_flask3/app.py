from flask import Flask,render_template

app = Flask(__name__)


@app.route('/myworld/')
def hello_world():
    # 模板传递多个参数的技巧：统一放在一个字典里传递进去
    context={
        'country':'china',
        'age':'18',
        'destory':'haha',
        'zuhe':{'name1':'baibai','name2':'pangpang'}
    }

    return render_template('index.html',context=context)


# 过滤器(取绝对值)的使用
@app.route('/position/')
def position():
    return render_template('position.html',position=-9)




# default 过滤器的使用
@app.route('/signup/')
def signup():
    context = {
        'name': 'china',
        'signature': None
    }
    return render_template('signup.html',**context)


# escape/safe 过滤器的使用
@app.route('/escape/')
def escape():
    context = {
        'name': 'china',
        'signature': "<script>alert('hello world')</script>",
        'person':[3,2,1],
        'field':'hello world'
    }
    return render_template('escape.html',**context)


# 自定义过滤器,并在模板进行注册
@app.template_filter('cut')
def cut(value):
    value = value.replace('hello','')
    return value






if __name__ == '__main__':
    app.run(debug=True)
