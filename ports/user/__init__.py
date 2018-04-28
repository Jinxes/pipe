from flask import Blueprint
from ports.user.api.index import Controller as Index
from ports.user.api.email import Controller as Email
from ports.user.api.addition import Controller as Addition
from ports.user.api.token import Controller as Signin

blueprint = Blueprint('user', __name__, url_prefix='/api/user')
blueprint.add_url_rule('/', 'index', Index.as_view('user'), methods=['GET'])
blueprint.add_url_rule('/email', 'email', Email.as_view('email'), methods=['GET'])
blueprint.add_url_rule('/', 'add', Addition.as_view('add'), methods=['POST'])
blueprint.add_url_rule('/token', 'token', Signin.as_view('token'), methods=['POST'])
