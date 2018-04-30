from flask import Response
from flask import request
from ports.user.service.user import UserService
from ports.user.service.auth import AuthService


def dependent(cls):
    '''
    判定 token 的正确性, 不正确返回 401, token 格式错误 400
    '''
    def decorator(f):
        auth_field = request.headers.environ.get('HTTP_AUTHORIZATION')
        if not auth_field:
            Response(status=403)
        auth_pack = auth_field.split(' ')
        auth_type = auth_pack[0]
        if auth_type != 'Bearer':
            Response(status=400)

        token = auth_pack[1]
        if token is not None:
            auth = AuthService()
            payload = auth.decode_token(token)
            userService = UserService()
            user = userService.findById(payload['identity'])
            if user is not None:
                userService.set_curent_user(user)
                return cls(f)
        return Response(status=401)

    return decorator
