from flask import Flask,render_template

app = Flask(__name__)
# 模板中的代码修改之后会自动加载
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/myworld/')
def index():

    context={
        'country':['china','usa','japan'],
        'age':'18',
        'destory':'haha',
        'zuhe':{'name1':'baibai','name2':'pangpang'},
        'books':[{'name':'三国演义','author':'张三','price':'110'},
                 {'name':'红楼梦','author':'李四','price':'119'},
                 {'name':'西游记','author':'王五','price':'120'},
                 {'name':'水浒传','author':'李二','price':'110'}]
    }

    return render_template('index.html',**context)








if __name__ == '__main__':
    app.run(debug=True)
