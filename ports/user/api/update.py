# -*- coding:utf8 -*-
from flask.views import View
from flask import request, jsonify, Response
from ports.user.service.user import UserService
from ports.user.model.data_form import UserDataForm
from flask_jwt import current_identity, jwt_required
from werkzeug.datastructures import MultiDict


class Controller(View):

    methods = ['PUT']

    def __init__(self):
        self.userService = UserService()

    @jwt_required()
    def dispatch_request(self):
        user = current_identity
        user_data_form = UserDataForm(MultiDict(request.json))
        user_data_form.id.data = user.id
        if user_data_form.validate():
            if user_data_form.update():
                return Response(status=200)
            return jsonify({'errors': {'_system': 'system busy1'}}), 500
        return jsonify({'errors': user_data_form.errors}), 422
