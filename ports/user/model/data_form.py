from .user import User
from .info import UserInfo
from boot.extensions import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional
from datetime import datetime, date

class UserDataForm(FlaskForm):
    id = IntegerField('id', validators=[Optional()])
    email = StringField('email', validators=[
        DataRequired('电子邮件不能为空'),
        Email('电子邮件格式不正确'),
    ])
    nickname = StringField('nickname', validators=[
        DataRequired('昵称不能为空')
    ])
    gender = IntegerField('gender', validators=[
        NumberRange(min=0, max=2, message='请输入正确的值')
    ])
    birthday = StringField('birthday', validators=[
        DataRequired('生日不能为空')
    ])
    sign = StringField('nickname', validators=[
        Length(max=128, message='签名超出长度')
    ])
    address = StringField('nickname', validators=[
        Length(max=255, message='地址超出长度')
    ])
    intro = StringField('nickname', validators=[
        Length(max=2000, message='简介超出长度')
    ])

    def update(self):
        try:
            user = User.query.filter_by(id=self.id.data).first()
            info = user.info
            user.update(
                commit = False,
                email = self.email.data,
                nickname = self.nickname.data,
                gender = self.gender.data
            )

            info.update(
                commit=False,
                sign = self.sign.data,
                intro = self.intro.data,
                address = self.address.data,
                birthday = self.birthday.data,
            )
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False