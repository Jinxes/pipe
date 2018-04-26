from flask import request, Response
from flask.views import View
from ports.user.service.user import UserService


class Controller(View):

    methods = ['GET']

    def __init__(self):
        self.userService = UserService()

    def dispatch_request(self):

        if self.userService.email_exist(request.args.get('email', None)):
            return Response(status=200)
        return Response(status=404)
