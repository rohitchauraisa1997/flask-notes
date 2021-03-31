from flask import Flask

def create_app():
    # __name__ represents name of file
    app = Flask(__name__)
    # encrypts and secures cookies and session data
    # in ouur app.
    app.config['SECRET_KEY'] = 'rohit'
    return app
    