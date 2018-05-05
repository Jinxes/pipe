from boot.extensions import db
from flask import current_app
from datetime import datetime
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT, DATETIME, TEXT

class UserInfo(db.Model):

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    sign = db.Column(TEXT(), nullable=False, default='')
    intro = db.Column(TEXT(), nullable=False, default='')
    address = db.Column(VARCHAR(length=255), nullable=False, default='')
    birthday = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    avatar = db.Column(VARCHAR(length=255), nullable=False, default='')
    state = db.Column(TINYINT(), nullable=False, default=1)
    user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('user.id'), nullable=False)

    def __str__(self):
        return '<UserInfo {0}>'.format(self.user.id)
