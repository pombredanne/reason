from datetime import datetime
from sqlalchemy import desc
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from reason import db
from sqlalchemy.util import KeyedTuple

class User(db.Model, UserMixin):
    __bind_key__ = 'userDb'
    __tablename__ = 'User' 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String)
    reports = db.relationship('Report', backref='User', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        print username
        return User.query.filter_by(username=username).first()

    def __repr__(self):
        return " {} ".format(self.username)


class Report(db.Model):
    __bind_key__ = 'userDb'
    __tablename__ = 'Report'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    description = db.Column(db.String(300))    


    def __repr__(self):
	return "Report ID{} for UserID {}".format(self.id, self.uid)

