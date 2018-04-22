from boot import db
from datetime import datetime
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT, DATETIME

class User(db.Model):

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    email = db.Column(VARCHAR(length=128), unique=True, nullable=False)
    nickname = db.Column(VARCHAR(length=128), nullable=False)
    password = db.Column(VARCHAR(length=64), nullable=False)
    gender = db.Column(TINYINT(), nullable=False, default=0)
    active = db.Column(TINYINT(), nullable=False, default=0)
    manager = db.Column(TINYINT(), nullable=False, default=0)
    create_time = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __str__(self):
        return "User(id='%s')" % self.id
