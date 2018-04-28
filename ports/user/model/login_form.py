from .user import User
from .info import UserInfo
from boot import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional
from validator import EmailExsits
from werkzeug.security import generate_password_hash

class LoginForm(FlaskForm):

    email = StringField('email', validators=[
        DataRequired('电子邮件不能为空'),
        Email('电子邮件格式不正确')
    ])

    password = StringField('password', validators=[
        DataRequired('密码不能为空'),
        Length(min=6, max=16, message='密码长度不正确')
    ])
