from flask import Blueprint
from ports.user.api.index import Controller as Index
from ports.user.api.email import Controller as Email
from ports.user.api.addition import Controller as Addition
from ports.user.api.repemail import Controller as Repemail
from ports.user.api.data import Controller as Data
from ports.user.api.update import Controller as DataUpdate

blueprint = Blueprint('user', __name__, url_prefix='/api/user')
blueprint.add_url_rule('', 'index', Index.as_view('user'), methods=['GET'])
blueprint.add_url_rule('/email', 'email', Email.as_view('email'), methods=['GET'])
blueprint.add_url_rule('', 'add', Addition.as_view('add'), methods=['POST'])
blueprint.add_url_rule('/rep-email', 'repemail', Repemail.as_view('repemail'), methods=['GET'])
blueprint.add_url_rule('/data', 'data', Data.as_view('data'), methods=['GET'])
blueprint.add_url_rule('/data', 'data_update', DataUpdate.as_view('data_update'), methods=['PUT'])
