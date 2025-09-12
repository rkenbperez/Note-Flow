from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash("Login successful!", category="success")
            return redirect(url_for("views.flow"))
        else:
            flash("Invalid email or password.", category="error")

    return render_template("login.html.j2", user=current_user)

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")  # Capture username
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already exists.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        else:
            new_user = User(
                email=email,
                username=username,  # Save username
                password=generate_password_hash(password1, method="pbkdf2:sha256")
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully!", category="success")
            return redirect(url_for("auth.login"))

    return render_template("sign-up.html.j2", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))