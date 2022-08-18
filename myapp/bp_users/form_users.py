from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from werkzeug.security import generate_password_hash, check_password_hash


class ProfileForm(FlaskForm):
    firstname = StringField('Firstname', id='profile_firstname')
    lastname =StringField('Lastname',id='profile_lastname')
    email = EmailField('Email', id='profile_email')
    submit = SubmitField('Save', id='profile_submit')
