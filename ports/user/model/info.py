from boot import db
from datetime import datetime
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT, DATETIME, TEXT


class UserInfo(db.Model):

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    address = db.Column(VARCHAR(length=128), nullable=False, default='')
    sign = db.Column(TEXT(), nullable=False, default='')
    intro = db.Column(TEXT(), nullable=False, default='')
    user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('user.id'), nullable=False)

    def __str__(self):
        return '<UserInfo {0}>'.format(self.user.id)
