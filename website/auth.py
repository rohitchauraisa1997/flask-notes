"""
auth.py contains the routes to 
all the pages in our web app
that need authorization tokens.
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from . import db
auth = Blueprint('auth',__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    return render_template("login.html",text="testing",boolean=True)

@auth.route("/sign_up",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email)<5:
            flash("Email id should be more than 5 chars",category='error')
        elif len(first_name) <=2:
            flash("First name should be greater than 2 letters", category='error')
        elif password1 != password2:
            flash("The password doesnt match.",category='error')
        elif len(password1)<7:
            flash("The password must be atleast 7 characters.",category='error')
        else:
            new_user = User(email=email,first_name=first_name,password=generate_password_hash(password1,method='sha256'))
            # print("*"*100)
            # print(new_user)
            # print("*"*100)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created',category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")

@auth.route("/logout")
def logout():
    return "<p>Log out</p>"

