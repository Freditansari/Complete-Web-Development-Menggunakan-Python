from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1> Hello world</h1>"


@app.route('/hello/<string:name>', methods=['GET']) #intentional error
def say_hello(name):
    return f'Hello {name[99]}, welcome to my basic website.'


