"""
auth.py contains the routes to 
all the pages in our web app
that need authorization tokens.
"""
from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

@auth.route("/login")
def login():
    return render_template("login.html",text="testing",boolean=True)

@auth.route("/sign_up")
def signup():
    return render_template("sign_up.html")

@auth.route("/logout")
def logout():
    return "<p>Log out</p>"

