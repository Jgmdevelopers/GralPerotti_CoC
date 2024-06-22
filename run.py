from app import create_app, db
from app.auth.models import User
from flask_mysqldb import MySQL, MySQLdb
from config import config


app = create_app()

if __name__ == "__main__":
     app.run(debug=True)