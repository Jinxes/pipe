from .extensions import cors
from ports.user import blueprint as user
from ports.session import blueprint as session
from ports.blog import blueprint as blog

def register_blueprints(app):
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(user, origins=origins)
    cors.init_app(session, origins=origins)
    cors.init_app(blog, origins=origins)

    app.register_blueprint(user)
    app.register_blueprint(session)
    app.register_blueprint(blog)
