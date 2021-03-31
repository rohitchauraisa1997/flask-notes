"""
views.py contains the routes to 
all the pages in our web app.
"""
from flask import Blueprint

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return "<h1>test</h1>"

