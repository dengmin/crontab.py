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
    configure_error_handlers(app)
    configure_cli(app)
    return app


def configure_app(app, config):
    if not config:
        config = Config
    app.config.from_object(config)

    app.config.from_pyfile('production.py', silent=True)

def configure_extensions(app):
    from core.scheduler import Scheduler
    app.scheduler = Scheduler()
    app.scheduler.start()

def configure_blueprints(app):
    from core.views import site
    from core.views import user
    app.register_blueprint(site.bp, url_prefix='')
    app.register_blueprint(user.bp, url_prefix='/user')


def configure_template_filters(app):
    pass

def configure_logging(app):
    if app.debug or app.testing:
        return
    import logging
    from logging.handlers import RotatingFileHandler

    log_file = os.path.join(app.config.get('LOG_FOLDER'), 'core.log')
    handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=10)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(pathname)s:%(lineno)d > %(message)s')
    )
    app.logger.addHandler(handler)


def configure_error_handlers(app):

    @app.errorhandler(404)
    def page_not_found(self):
        return render_template('errors/404.html'), 404

def configure_cli(app):

    @app.cli.command(with_appcontext=True)
    def initdb():
        from core.model import User, Job, Record
        tables = [User, Job, Record]
        for table in tables:
            if not table.table_exists():
                table.create_table()
                print('table {} created!'.format(table.__name__))