from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return "<h1> Hello world</h1>"

@app.route('/')
def blog_home():
    headline='World Peace Achieved!'
    lead = 'abc laughed a lot and all the world leaders grown a sense of humor'
    return render_template('home.html', headline=headline, lead = lead)

if __name__=='main':
    app.run(debug=True)