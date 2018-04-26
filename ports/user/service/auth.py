# -*- coding:utf8 -*-
import jwt
from flask import request
from boot.kernel import app
from common.singleton import singleton
from ports.user.model.user import User
from werkzeug.security import check_password_hash


@singleton
class AuthService:
    algorithm = 'HS256'

    def __init__(self):
        self.secret_key = app.config.get('SECRET_KEY')

    def make_auth_token(self, user):
        '''
        跟觉用户信息创建 JWT Token
        :param user: User
        :return: string
        '''
        payload = {
            'identity': user.id.data,
            'id': user.id.data,
            'nickname': user.nickname.data,
            'gender': user.gender.data
        }
        token = jwt.encode(payload, self.secret_key, self.algorithm)
        return token

    def decode_token(self, token):
        '''
        解析 JWT Token
        :param token: string
        :return: dict
        '''
        return jwt.decode(token, self.secret_key, self.algorithm)

    def auth_check_by_email(self, email, password):
        '''
        通过email检测用户是否有权限登录
        :param email: string
        :param password: string
        :return: User|False
        '''
        user = User.query.filter_by(email=email).first()
        if user:
            if self.check_password(password, user.password):
                return user
        return False

    def auth_check_by_id(self, id, password):
        '''
        通过用户 id 检测用户是否有权限登录
        :param email: string
        :param password: string
        :return: User|False
        '''
        user = User.query.get(id)
        if user:
            if self.check_password(password, user.password):
                return user
        return False

    def check_password(self, password, password_hash):
        '''
        检测密码
        :param password: string
        :param password_hash: string
        :return: bool
        '''
        return check_password_hash(password_hash, password)
