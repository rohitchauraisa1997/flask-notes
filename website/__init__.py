import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "databse.db"

def create_database(app):
    if not os.path.exists('website/'+DB_NAME):
        db.create_all(app=app)
        print('Created database')

def create_app():
    # __name__ represents name of file
    from .views import views
    from .auth import auth
    from .models import User,Note
    app = Flask(__name__)
    # encrypts and secures cookies and session data
    # in ouur app.
    app.config['SECRET_KEY'] = 'rohit'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")
    create_database(app)
    
    
    return app
    