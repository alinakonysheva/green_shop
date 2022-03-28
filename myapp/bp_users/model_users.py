from myapp import db


class User(db.Model):

    id = db.Column('id', db.Integer, primary_key=True, index=True)
    username = db.Column('username', db.String(200))
    email = db.Column('email', db.String(200))
    