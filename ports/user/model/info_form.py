from .user import User
from .info import UserInfo
from boot import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional


class InfoForm(FlaskForm):
    id = IntegerField('id', validators=[Optional()])
    address = StringField('address', validators=[
        Length(max=255), Optional()
    ], default='')
    sign = StringField('address', validators=[
        Length(max=500), Optional()
    ], default='这家伙很懒，什么都没留下...')
    intro = StringField('address', validators=[
        Length(max=1024), Optional()
    ], default='')

    def init(self, user_id):
        try:
            info = UserInfo(
                user_id=user_id,
                address=self.address.default,
                sign=self.sign.default,
                intro=self.intro.default
            )
            db.session.add(info)
            db.session.commit()
            return info
        except Exception:
            return False

    def create(self):
        try:
            user = UserInfo(**self.data)
            db.session.add(user)
            db.session.commit()
            return True
        except Exception:
            return False