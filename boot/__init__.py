#-*- coding:utf8 -*-
from flask import Flask
from .setting import DevConfig, ProdConfig, TestConfig
from .blueprints import register_blueprints
from .extensions import db, migrate, jwt


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)


def create_app(config_object=ProdConfig):
    """
    :param config_object: The configuration object to use.
    :return: Flask
    """
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app

