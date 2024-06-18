from dataclasses import field
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo

from app.auth.models import User

def email_exists(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Email ya registrado. Usa uno diferente.')

def username_exists(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('Nombre de usuario ya registrado. Usa uno diferente.')

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(), 
        Length(min=4, max=16, message="El username debe tener entre 4 a 16 caracteres"),
        username_exists
    ])
    email = StringField("E-mail", validators=[
        DataRequired(), 
        Email(), 
        email_exists
    ])
    password = PasswordField("Password", validators=[
        DataRequired(), 
        EqualTo("confirm", message="Las contraseñas deben coincidir")
    ])
    confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Registrar")
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField("Recordarme")
    submit = SubmitField('Login')