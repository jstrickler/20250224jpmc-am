from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>try /username/YOURNAME</h1>', 200

@app.route('/username/<username>')
def user_name(username):
    data = {
        'username': username.replace('+', ' '),
        'browser': request.headers.get('User-Agent'),
        'accept_language': request.headers.get('Accept-Language'),
    }
    return render_template(
        'flask_hello.html',
        data=data,
    )

if __name__ == '__main__':
    app.run(debug=True)
