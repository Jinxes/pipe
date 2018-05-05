from .user import User
from .info import UserInfo
from boot.extensions import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional
from validator import EmailExsits
from werkzeug.security import generate_password_hash

class UserForm(FlaskForm):
    id = IntegerField('id', validators=[Optional()])
    email = StringField('email', validators=[
        DataRequired('电子邮件不能为空'),
        Email('电子邮件格式不正确'),
        EmailExsits('这个电子邮件已经被注册了')
    ])
    nickname = StringField('nickname', validators=[
        DataRequired('昵称不能为空')
    ])
    password = StringField('password', validators=[
        DataRequired('密码不能为空'),
        Length(min=6, max=16, message='密码长度不正确')
    ])
    gender = IntegerField('gender', validators=[
        NumberRange(min=0, max=2, message='请输入正确的值')
    ])

    def create(self):
        try:
            user = User(
                email=self.email.data,
                nickname=self.nickname.data,
                password=self.createPassword(),
                gender=self.gender.data
            )
            db.session.add(user)
            db.session.commit()
            return user
        except Exception:
            return False

    def update(self):
        try:
            user = User.query.filter_by(id=self.id.data)
            user.update(self.data)
            db.session.commit()
            return True
        except Exception:
            return False

    def createPassword(self):
        return generate_password_hash(self.password.data)
