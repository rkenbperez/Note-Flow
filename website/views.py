from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html.j2", user=current_user)

@views.route("/flow")
@login_required
def flow():
    return render_template("flow.html.j2", user=current_user)