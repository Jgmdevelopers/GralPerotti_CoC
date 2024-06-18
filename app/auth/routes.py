from . import auth
from app.auth.forms import LoginForm, RegistrationForm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask import render_template, flash, session, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.models import User
from flask import flash, redirect


@auth.route('/register', methods=["GET","POST"])
def register_user():
    if current_user.is_authenticated:
        flash("El usuario ya esta registrado en el sistema")
        return redirect(url_for("auth.home"))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        User.create_user(
            username=form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        
        flash("Registro exitoso!")
        return redirect(url_for("auth.log_in_user"))
    return render_template("registration.html", form=form)

@auth.route('/login', methods=["GET", "POST"])
def log_in_user():
    if current_user.is_authenticated:
        flash("El usuario ya se encuentra autenticado en el sistema")
        return redirect(url_for("auth.home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.stay_loggedin.data)
            session["username"] = form.username.data
            flash("Ingreso Correcto al sistema", "success")
            return redirect(url_for("auth.home"))  # Redirige al usuario después del login

        # Si las credenciales son incorrectas
        flash("Credenciales no válidas. Por favor, verifique su usuario y contraseña.", "error")
        return render_template('login.html', form=form), 400

    return render_template('login.html', form=form)

@auth.route('/home')
@login_required
def home():
    return render_template("home.html")

@auth.route('/logout', methods=["GET"])
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for("auth.log_in_user"))


@auth.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404