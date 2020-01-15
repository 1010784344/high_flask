# -*- coding: UTF-8 -*-
from flask import Flask,g,request
from utils import log_a,log_b,log_c

app = Flask(__name__)


@app.route('/')
def hello_world():
    g.username = request.args.get('username')
    log_a()
    log_b()
    log_c()
    return 'Hello World!'



if __name__ == '__main__':
    app.run(debug=True)
