# -*- coding:utf8 -*-
from flask.views import View
from flask import request, jsonify
from ports.user.service.user import UserService
from ports.user.service.auth import AuthService
from ports.user.model.login_form import LoginForm
from ports.user.model.info_form import InfoForm
from flask_cors import cross_origin

class Controller(View):

    methods = ['POST']

    def __init__(self):
        self.userService = UserService()
        self.authService = AuthService()

    @cross_origin()
    def dispatch_request(self):
        login_form = LoginForm(request.form)
        if login_form.validate():
            email = login_form.email.data
            password = login_form.password.data
            user = self.authService.auth_check_by_email(email, password)
            if user:
                token = self.authService.make_auth_token(user)
                return jsonify(dict(token=token.decode())), 200
            else:
                return jsonify({'errors':
                    {'_system': '帐号或密码错误'}
                }), 422
        return jsonify({'errors': login_form.errors}), 422
