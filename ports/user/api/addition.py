#-*- coding:utf8 -*-
from flask.views import View
from flask import request, jsonify, Response
from opt.validator import Validator
from ports.user.service import Service as UserService

class Controller(View):

    methods = ['POST']

    def __init__(self):
        self.userService = UserService()

    def dispatch_request(self):

        validator = self.validate()
        if validator.invalid():
            resp = jsonify(validator.get_errors())
            return (resp, 401)

        email = request.args.get('email')
        password = request.args.get('password')
        nickname = request.args.get('nickname')
        gender = request.args.get('gender')

        if (self.userService.add(email, password, nickname, gender)):
            return Response(status=201)
        return Response(status=500)


    def validate(self):
        validator = Validator()
        validator('email').required().email()
        email = request.args.get('email')
        if self.userService.email_exist(email):
            validator.set_error('email', {'exist': '电子邮件重复了'})

        validator('nickname').required().max_length(16)
        if validator.has('gender'):
            validator('gender').numeric().contain([0, 1, 2])

        return validator
