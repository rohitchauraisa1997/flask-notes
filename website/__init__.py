from flask import Flask

def create_app():
    # __name__ represents name of file
    app = Flask(__name__)
    # encrypts and secures cookies and session data
    # in ouur app.
    app.config['SECRET_KEY'] = 'rohit'
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")
    
    return app
    