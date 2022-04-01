from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField


class ProfileForm(FlaskForm):
    username = StringField('Name', id='profile_username')
    email = EmailField('Email', id='profile_email')
    submit = SubmitField('Save', id='profile_submit')
