# -*- coding:utf8 -*-
from flask.views import View
from flask import request, jsonify
from ports.user.service.user import UserService
from common.authorization import dependent
from ports.user.model.user_form import UserForm


class Controller(View):

    methods = ['GET']

    def __init__(self):
        self.userService = UserService()

    @dependent
    def dispatch_request(self):
        form = UserForm(request.args)
        if form.validate():
            form.update()
            return '201', 201

        return jsonify(form.data), 422
