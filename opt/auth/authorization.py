#-*- coding:utf8 -*-
from .main import Auth
from flask import Response, request
from ports.user.service import Service as UserService

def auth_dependent(cls):
    def decorator(f):
        auth = Auth()
        token = auth.get_token()
        if token is not None:
            payload = auth.decode_token(token)
            userService = UserService()
            user = userService.findById(payload['identity'])
            if user is not None:
                userService.set_curent_user(user)
                return cls(f)
        return Response(status=401)
    return decorator
