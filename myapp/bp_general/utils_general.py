from flask import current_app
from flask.cli import with_appcontext
from myapp import db
import myapp.bp_general


@myapp.bp_general.cli.command("create-db")
@with_appcontext
def do_create_db():
    if current_app.config['DEBUG']:
        db.drop_all()
    db.create_all()

