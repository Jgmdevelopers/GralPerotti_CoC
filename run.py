from app import create_app, db
from app.auth.models import User

flask_scrapy_app = create_app("dev")

with flask_scrapy_app.app_context():
    db.create_all()
    if not User.query.filter_by(username="test").first():
        User.create_user(
            username="test",
            email="test-testing@test.com",
            password="123456"
        )

if __name__ == "__main__":
    flask_scrapy_app.run(debug=True)
