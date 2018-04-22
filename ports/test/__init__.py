from boot import app
from flask import Blueprint
from ports.user.api.index import Controller

blueprint = Blueprint('test', __name__, url_prefix='/test/')
blueprint.add_url_rule('/', 'test_index', Controller.as_view('test'))
