from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
import logging.handlers
import logging

#type define
TESTING='TESTING'
DEVEL='DEVEL'
PRODUCT='PRODUCT'

def configure_logging(app):
    """Configures logging."""

    logs_folder = os.path.join(app.root_path, os.pardir, "logs")
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')

    info_log = os.path.join(logs_folder, app.config['INFO_LOG'])

    info_file_handler = logging.handlers.RotatingFileHandler(
        info_log,
        maxBytes=100000,
        backupCount=10
    )

    info_file_handler.setLevel(logging.DEBUG)
    info_file_handler.setFormatter(formatter)
    app.logger.addHandler(info_file_handler)

    error_log = os.path.join(logs_folder, app.config['ERROR_LOG'])

    error_file_handler = logging.handlers.RotatingFileHandler(
        error_log,
        maxBytes=100000,
        backupCount=10
    )

    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)

app = Flask(__name__)
try:
    t = os.environ['TYPE']
    if t == DEVEL:
        app.config.from_object('blog.config.DevelopmentConfig')
    elif t == TESTING:
        app.config.from_object('blog.config.TestingConfig')
    elif t == PRODUCT:
        app.config.from_object('blog.config.ProductionConfig')
except KeyError:
    raise TypeError('please specific a TYPE env var which can be: DEVEL, TESTING, PRODUCT')
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)
configure_logging(app)
import blog.models
import blog.resources