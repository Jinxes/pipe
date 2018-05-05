from flask import request, Response
from flask.views import View
from ports.user.service.user import UserService
from flask_jwt import current_identity, jwt_required


class Controller(View):

    methods = ['GET']

    def __init__(self):
        self.userService = UserService()

    @jwt_required()
    def dispatch_request(self):

        user = self.userService.findByEmail(request.args.get('email', None))
        if user:
            if user.id != current_identity.id:
                return Response(status=200)
        return Response(status=404)
