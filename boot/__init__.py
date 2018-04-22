#-*- coding:utf8 -*-
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from etc.config import dev as config

app = Flask(__name__)
app.config.from_object(config)
CORS(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)