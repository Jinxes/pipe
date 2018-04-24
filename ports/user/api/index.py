#-*- coding:utf8 -*-
from flask.views import View
from flask import request, Response, jsonify
from opt.validator import Validator
from ports.user.service import Service as UserService
from opt.auth import auth_dependent
from ports.user.model.user_form import UserForm

class Controller(View):

    methods = ['GET']

    def __init__(self):
        self.userService = UserService()

    # @auth_dependent
    def dispatch_request(self):

        # print(self.userService.get_curent_user())
        # validator = self.validate()
        # if validator.invalid():
        #     resp = jsonify(validator.get_errors())
        #     return resp, 422
        #
        # email = request.args.get('email')
        # nickname = request.args.get('nickname')
        # password = request.args.get('password')
        # gender = request.args.get('gender')
        #
        # if (self.userService.add(email, password, nickname, gender)):
        #     return Response(status=201)
        # return Response(status=500)
        form = UserForm(request.args)
        if form.validate():
            form.update()
            return '201', 201

        return jsonify(form.data), 422
