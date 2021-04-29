from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='User name:')
    email = StringField(label='E-mail:')
    password = PasswordField(label='Password:')
    password_confirmation = PasswordField(label='Confirm your password:')
    submit = SubmitField(label='OK')