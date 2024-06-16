import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask import Blueprint

db = SQLAlchemy()
bootstrap = Bootstrap()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_views = "auth.log_in_user"
login_manager.session_protection = "strong"
login_manager.login_message_category = 'info'

def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), "config", config_type + ".py")
    app.config.from_pyfile(configuration)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    from app.auth import auth
    app.register_blueprint(auth)
    return app