
# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from flask import flash, _request_ctx_stack
from functools import wraps
from flask_jwt import _jwt
import jwt


def jwt_optional(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            token = _jwt.request_callback()
            try:
                payload = _jwt.jwt_decode_callback(token)
            except jwt.exceptions.DecodeError:
                pass
            else:
                _request_ctx_stack.top.current_identity = _jwt.identity_callback(payload)
            return fn(*args, **kwargs)
        return decorator
    return wrapper


from ports.user.model.user import User
from ports.user.service.auth import AuthService


def jwt_identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()


def authenticate(email, password):
    authService = AuthService()
    user = authService.auth_check_by_email(email, password)
    return user
