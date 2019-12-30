from flask import Flask

from exts import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/alembic_test'

# TRUE 数据库里面的数据一变化，sqlalchemy 也会跟着变化
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


#防止循环引用，db 连接 app
db.init_app(app)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
