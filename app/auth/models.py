from datetime import datetime
from app import db, bcrypt
from app import login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.now)
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    @classmethod
    def create_user(cls, username, email, password):
        user = cls(
            username = username,
            email = email,
            password = bcrypt.generate_password_hash(password).decode("utf-8")
        )
        
        db.session.add(user)
        db.session.commit()
        return user
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
