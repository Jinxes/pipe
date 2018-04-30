from flask import Blueprint
from ports.session.api.signout import Controller as Signout

blueprint = Blueprint('session', __name__, url_prefix='/api/session')
blueprint.add_url_rule('', 'signout', Signout.as_view('user'), methods=['DELETE'])
