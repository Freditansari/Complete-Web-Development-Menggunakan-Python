from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return "<h1> Hello world</h1>"

@app.route('/')
def blog_home():
    headline = 'World Peace Achieved!'
    lead = 'abc laughed a lot and all the world leaders grown a sense of humor'
    customer_lists = [{'name': 'John', 'upvote': 20, 'downvote': 10},
                      {'name': 'Banana', 'upvote': 50, 'downvote': 10},
                      {'name': 'Susan', 'upvote': 15, 'downvote': 17}]
    return render_template('home.html', headline=headline, lead=lead, is_true = True, customers = customer_lists)


if __name__ == 'main':
    app.run(debug=True)
