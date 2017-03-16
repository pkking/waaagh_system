from flask import Flask
import os
import logging.handlers
import logging
from blog.models import db, migrate
from blog.resources import api

#type define
TESTING='TESTING'
DEVEL='DEVEL'
PRODUCT='PRODUCT'

def configure_logging(app):
    """Configures logging."""
    if not app.config['LOGGING']:
        return
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

def configure_api(app, api):
    api.init_app(app)

def configure_db(app, db):
    # Flask-SQLAlchemy
    db.init_app(app)
    # Flask-Migrate
    migrate.init_app(app, db)

def create_app():
    """Creates the app."""
    app = Flask('blog')
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

    app.config.from_envvar("BLOG_SETTINGS", silent=True)
    configure_logging(app)
    configure_db(app, db)
    configure_api(app, api)

    return app