from flask import Flask

app = Flask(__name__)  # create Flask application object


@app.route('/')  # assign this view function to '/' (i.e., the "root: of the web site)
def index():  # define the view function
    return '<h1>Hello, JPMC Flask world!</h1>' # return HTML for the page to display

@app.route('/other')
def other():
    home_page = app.url_for('index')
    return f"""
    <h2>Welcome to the other page</h2>
    <a href="{home_page}">Return to home page</a>
    """

@app.route('/api/wombat')
def get_wombats(id):
    return "ALL WOMBATS"

@app.route('/api/wombat/<int:id>')
def get_wombat(id):
    return """{"name": "Waldo", "color": "brown" }"""


@app.route('/wombats')
def wombats():
    return '<h2>You have found the wombats</h2>'

# app.register_route(index, '/')

if __name__ == '__main__':
    app.run(debug=True) # start the development server
