from flask import request, Response
from flask.views import View
from flask import request, jsonify
from flask_jwt import current_identity, jwt_required
from flask_apispec import use_kwargs, marshal_with
from ports.blog.blog_schema import blog_schemas


class Controller(View):

    methods = ['GET']

    @jwt_required()
    @marshal_with(blog_schemas)
    def dispatch_request(self):
        user = current_identity
        data = user.blogs
        return data, 200
