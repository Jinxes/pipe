# -*- coding:utf8 -*-
import json
from flask.views import View
from flask import request, jsonify
from ports.user.service.user import UserService
from ports.user.service.auth import AuthService
from ports.user.model.user_form import UserForm
from flask_cors import cross_origin


class Controller(View):

    methods = ['POST']

    def __init__(self):
        self.userService = UserService()
        self.authService = AuthService()

    @cross_origin()
    def dispatch_request(self):
        form = UserForm(request.form)
        if form.validate():
            if form.create():
                payload = {
                    'identity': form.id.data,
                    'id': form.id.data,
                    'nickname': form.nickname.data,
                    'gender': form.gender.data
                }
                token = self.authService.make_auth_token(payload)
                return jsonify(dict(token=token.decode())), 201
            else:
                return jsonify({
                    'errors': {
                        '_system': 'system busy'
                    }
                }), 500
        else:
            return jsonify({
                'errors': form.errors
            }), 422
