from flask import current_app
from boot.extensions import db
from datetime import datetime
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT, DATETIME, TEXT

class Blog(db.Model):

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    title = db.Column(VARCHAR(length=255), index=True, nullable=False)
    subtitle = db.Column(VARCHAR(length=255), nullable=False)
    intro = db.Column(TEXT(), nullable=False, default='')
    content = db.Column(TEXT(), nullable=False, default='')
    logo = db.Column(VARCHAR(length=255), nullable=False, default='')

    update_time = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
    create_time = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
    user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('user.id'), nullable=False)
