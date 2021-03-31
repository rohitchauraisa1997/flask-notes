"""
views.py contains the routes to 
all the pages in our web app.
"""
from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")

