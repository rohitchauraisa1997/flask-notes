"""
auth.py contains the routes to 
all the pages in our web app
that need authorization tokens.
"""
from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route("/login")
def login():
    return "<p>Login</p>"

@auth.route("/sign_up")
def signup():
    return "<p>Sign Up</p>"

@auth.route("/logout")
def logout():
    return "<p>Log out</p>"

