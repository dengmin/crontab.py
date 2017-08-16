#!/usr/bin/env python
import os
from flask import Flask, render_template
from config import Config

def create_app(config=None):
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app = Flask(__name__, root_path=ROOT_PATH)
    configure_app(app, config)
    configure_extensions(app)
    configure_blueprints(app)
    configure_template_filters(app)
    configure_logging(app)
    configure_hook(app)
    configure_error_handlers(app)
    return app


def configure_app(app, config):
    if not config:
        config = Config
    app.config.from_object(config)

    app.config.from_pyfile('production.py', silent=True)

def configure_extensions(app):
    from app.scheduler import Scheduler
    app.scheduler = Scheduler()
    app.scheduler.start()

    from flask_peewee.db import Database
    app.db = Database(app)

def configure_blueprints(app):
    from app.views import site
    from app.views import user
    app.register_blueprint(site.bp, url_prefix='')
    app.register_blueprint(user.bp, url_prefix='/user')


def configure_template_filters(app):
    pass

def configure_logging(app):
    if app.debug or app.testing:
        return
    import logging

    log_file = os.path.join(app.config.get('LOG_FOLDER'), 'app.log')
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=100000, backupCount=10)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(pathname)s:%(lineno)d > %(message)s')
    )
    app.logger.addHandler(handler)

def configure_hook(app):

    @app.before_request
    def before_request():
        pass

def configure_error_handlers(app):

    @app.errorhandler(404)
    def page_not_found(self):
        return render_template('errors/404.html'), 404