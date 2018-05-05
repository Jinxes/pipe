from flask import current_app
from boot.extensions import db
from datetime import datetime
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT, DATETIME
from .info import UserInfo
from ports.blog.model.blog import Blog

class User(db.Model):

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    email = db.Column(VARCHAR(length=128), unique=True, nullable=False)
    nickname = db.Column(VARCHAR(length=128), nullable=False)
    password = db.Column(VARCHAR(length=255), nullable=False)
    gender = db.Column(TINYINT(), nullable=False, default=0)
    state = db.Column(TINYINT(), nullable=False, default=1)
    active = db.Column(TINYINT(), nullable=False, default=0)
    manager = db.Column(TINYINT(), nullable=False, default=0)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    info = db.relationship(UserInfo, uselist=False, backref='user', lazy=True)
    blogs = db.relationship(Blog, uselist=True, backref='user', lazy=True)

    def __str__(self):
        return '<User {0}>'.format(self.id)
