from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user

views = Blueprint("views",__name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html.j2")

@views.route("/login")
def login():
    return render_template("login.html.j2")

@views.route("/sign-up")
def sign_up():
    return render_template("sign-up.html.j2")