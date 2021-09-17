from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1> Hello world</h1>"


@app.route('/hello/<string:name>', methods=['PUT'])  # won't work
def say_hello(name):
    return f'Hello {name}, welcome to my basic website.'


