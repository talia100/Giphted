from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

db = SQLAlchemy()
login = LoginManager()

class UserModel(UserMixin, db.Model):
        __tablename__ = "teachers"

        id = db.Column(db.Integer, primary_key = True)
        username = db.Column(db.String(20), unique = True, nullable = False)
        email = db.Column(db.String(80), unique = True, nullable = False)
        password_hash = db.Column(db.String(255), nullable = False)

        def set_password(self, password):
                self.password_hash = generate_password_hash(password)

        def check_password(self, password):
                return check_password_hash(self.password_hash, password)

class StudentModel(UserMixin, db.Model):
        __tablename__ = "students"

        id = db.Column(db.Integer, primary_key = True)
        username = db.Column(db.String(20), unique = True, nullable = False)
        password_hash = db.Column(db.String(255), nullable = False)

        def set_password(self, password):
                self.password_hash = generate_password_hash(password)

        def check_password(self, password):
                return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
        return UserModel.query.get(int(id))
        return StudentModel.query.get(int(id))

