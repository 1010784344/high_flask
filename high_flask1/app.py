from flask import Flask,redirect,url_for,Response,jsonify

app = Flask(__name__)



# code = 301 ,构造永久重定向
@app.route('/')
def hello_world():
    return redirect(url_for('hello_myworld'),code=301)


@app.route('/myworld/')
def hello_myworld():
    return 'Hello  go to myworld!'


if __name__ == '__main__':
    # 在局域网中让其他电脑访问我的网站:host='0.0.0.0'
    app.run(debug=True,host='0.0.0.0')
