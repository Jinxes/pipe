from flask import request, Response
from flask.views import View
from flask import request, jsonify
from ports.user.service.user import UserService
from flask_jwt import current_identity, jwt_required


class Controller(View):

    methods = ['GET']

    def __init__(self):
        self.userService = UserService()

    # @dependent
    @jwt_required()
    def dispatch_request(self):
        # user = self.userService.get_curent_user()
        user = current_identity
        info = user.info
        data = {
            'nickname': user.nickname,
            'email': user.email,
            'sign': info.sign,
            'address': info.address,
            'birthday': {
                'year': info.birthday.year,
                'month': info.birthday.month,
                'day': info.birthday.day
            },
            'gender': user.gender,
            'intro': info.intro
        }
        return jsonify(data), 200
