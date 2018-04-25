# -*- coding:utf8 -*-
import jwt
from flask import request
from boot.kernel import app
from opt.singleton import singleton


@singleton
class AuthService:
    algorithm = 'HS256'

    def __init__(self):
        self.secret_key = app.config.get('SECRET_KEY')

    def make_auth_token(self, payload):
        token = jwt.encode(payload, self.secret_key, self.algorithm)
        return token

    def decode_token(self, token):
        return jwt.encode(token, self.secret_key, self.algorithm)
