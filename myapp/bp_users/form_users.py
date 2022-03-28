from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField

class ProfileForm(FlaskForm):
    username = StringField('Gebruikersnaam', id='profile_username')
    email = EmailField('Email', id='profile_email')
    submit = SubmitField('Bewaren', id='profile_submit')
