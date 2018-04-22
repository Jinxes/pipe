from flask import Blueprint
from ports.user.api.index import Controller as Index
from ports.user.api.addition import Controller as Addition

blueprint = Blueprint('user', __name__, url_prefix='/user')
blueprint.add_url_rule('/', 'index', Index.as_view('user'), methods=['GET'])
blueprint.add_url_rule('/', 'add', Addition.as_view('add'), methods=['POST'])