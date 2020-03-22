from flask import Flask,render_template
from ueditor import bp as ued_bp
import config


app = Flask(__name__)

app.config.from_object(config)
app.register_blueprint(ued_bp)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
