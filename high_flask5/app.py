# 宏 有关的demo

from flask import Flask,render_template

app = Flask(__name__)
# 模板中的代码修改之后会自动加载
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/myworld/')
def index():

    return render_template('index.html')


@app.route('/macrotest/')
def macrotest():

    return render_template('macrotest.html')





if __name__ == '__main__':
    app.run(debug=True)
