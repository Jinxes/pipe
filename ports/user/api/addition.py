# -*- coding:utf8 -*-
from flask.views import View
from flask import request, jsonify
from ports.user.service.user import UserService
from ports.user.service.auth import AuthService
from ports.user.model.user_form import UserForm
from ports.user.model.info_form import InfoForm
from flask_cors import cross_origin


class Controller(View):

    methods = ['POST']

    def __init__(self):
        self.userService = UserService()
        self.authService = AuthService()

    @cross_origin()
    def dispatch_request(self):
        user_form = UserForm(request.form)
        if user_form.validate():
            user = user_form.create()
            if user:
                info_form = InfoForm()
                info = info_form.init(user.id)
                if info:
                    token = self.authService.make_auth_token(user)
                    return jsonify(dict(token=token.decode())), 201
                return jsonify({'errors': {'_system': 'system busy'}}), 500
            else:
                return jsonify({'errors': {'_system': 'system busy'}}), 500
        else:
            return jsonify({'errors': user_form.errors}), 422
