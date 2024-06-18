import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CLAVE SECRETA'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:@localhost/login_perotti"

config = Config()
