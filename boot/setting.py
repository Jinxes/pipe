# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from datetime import timedelta

class Config(object):
    """Base configuration."""
    SECRET_KEY = '\x00\xad\x1c\xd0\xf1\xc3\xe6\xb9\xda\x80\x8e)\xaaV\x1c-\xbe\xbd4\x85\xcd\xc4\xec'
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = False
    CORS_ORIGIN_WHITELIST = '*'
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_HEADER_PREFIX = 'Bearer'
    JWT_AUTH_URL_RULE = '/api/user/token'
    JWT_EXPIRATION_DELTA = timedelta(seconds=3600)

class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:blldxt@localhost:3306/1984_prod?charset=utf8'

class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:blldxt@localhost:3306/1984_dev?charset=utf8'


class TestConfig(Config):
    """Test configuration."""
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4