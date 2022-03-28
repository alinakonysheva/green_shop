from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_htmlmin import HTMLMIN
from flask_debugtoolbar import DebugToolbarExtension
from flask_compress import Compress


db = SQLAlchemy()

htmlmin = HTMLMIN()

compress = Compress()


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object('configuration.BaseConfiguration')

    db.init_app(app)

    # htmlmin.init_app(app)
    compress.init_app(app)
    do_register_blueprint(app)

    do_register_error_handlers(app)

    if app.config['DEBUG']:
        app.debug = True
        toolbar = DebugToolbarExtension()
        toolbar.init_app(app)

    return app


def do_register_blueprint(flaskapp):
    from bp_general.views_general import bp_general_app
    #from bp_users import bp_users

    flaskapp.register_blueprint(bp_general_app)
    #§flaskapp.register_blueprint(bp_users)


def do_register_error_handlers(flaskapp):
    from .bp_general.views_general import do_not_authorized, do_not_found, do_server_error

    flaskapp.register_error_handler(404, do_not_found)
    flaskapp.register_error_handler(403, do_not_authorized)
    flaskapp.register_error_handler(406, do_not_authorized)
    flaskapp.register_error_handler(500, do_server_error)
