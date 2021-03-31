from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "databse.db"

def create_app():
    # __name__ represents name of file
    app = Flask(__name__)
    # encrypts and secures cookies and session data
    # in ouur app.
    app.config['SECRET_KEY'] = 'rohit'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")
    
    return app
    