from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return "<h1> Hello world</h1>"

@app.route('/')
def blog_home():
    return render_template('home.html')

if __name__=='main':
    app.run(debug=True)