from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from config import Config
import os
from flask import Flask, render_template

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicialización de extensiones
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    bootstrap.init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads') 

    with app.app_context():
        db.create_all()
        print("Conexión a la base de datos establecida correctamente.")

    # Importación y registro de blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # Ruta raíz
    @app.route('/')
    def index():
        from app.auth.models import Image
        images = Image.query.all()
        # Envía las imágenes a la plantilla base.html
        return render_template("base.html", images=images)

    # Manejo de errores 404
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app
