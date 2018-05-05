from flask import Blueprint
from .api.showlist import Controller as ShowList

blueprint = Blueprint('blog', __name__, url_prefix='/api/blog')

blueprint.add_url_rule('', 'index', ShowList.as_view('index'), methods=['GET'])