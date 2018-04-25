from flask import Response
from flask import request
from ports.user.service.user import UserService
from ports.user.service.auth import AuthService


def dependent(cls):

    def decorator(f):
        auth = AuthService()
        auth_field = request.authorization
        auth_pack = auth_field.split(' ')
        auth_type = auth_pack[0]
        if auth_type != 'Bearer':
            Response(status=400)

        token = auth_pack[1]
        if token is not None:
            payload = auth.decode_token(token)
            userService = UserService()
            user = userService.findById(payload['identity'])
            if user is not None:
                userService.set_curent_user(user)
                return cls(f)
        return Response(status=401)

    return decorator
