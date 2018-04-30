# -*- coding:utf8 -*-
from flask.views import View
from flask import Response, request, jsonify
from flask_cors import cross_origin

class Controller(View):

    methods = ['DELETE']

    @cross_origin()
    def dispatch_request(self):
        return Response(status=205)
