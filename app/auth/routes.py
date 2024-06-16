from . import auth
from app.auth.forms import LoginForm, RegistrationForm
from flask import render_template, flash, session, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.models import User


@auth.route('/register', methods=["GET","POST"])
def register_user():
    if current_user.is_authenticated:
        flash("El usuario ya esta registrado en el sistema")
        return redirect(url_for("auth.home"))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        User.create_user(
            username=form.username.date,
            email = form.email.data,
            password = form.password.data
        )
        
        flash("Registro éxitoso!")
        return redirect(url_for("auth.log_in_user"))
    return render_template("registration.html", form=form)


@auth.route('/login', methods=["GET","POST"])
def log_in_user():
    if current_user.is_authenticated:
        flash("El usuario ya se encuentra autenticado en el sistema")
        return redirect(url_for("auth.home"))
     
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if not user or not user.check_password(form.password.data):
            flash("Credenciales no válidas")
            return redirect(url_for("auth.log_in_user"))
        
        login_user(user, form.stay_loggedin.data)
        session["username"] = form.username.data
        flash("Ingreso Correcto al sistema")
        return render_template("login.html", form=form)

    return render_template('login.html', form=form)

@auth.route('/')
def index():
    return render_template("base.html")

@auth.route('/home')
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