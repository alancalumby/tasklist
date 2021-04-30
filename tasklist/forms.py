from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='User name:', validators=[Length(min=2,max=30),DataRequired()])
    email = StringField(label='E-mail:', validators=[Email(),DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=2,max=60),DataRequired()])
    password_confirmation = PasswordField(label='Confirm your password:', validators=[EqualTo('password'),DataRequired()])
    submit = SubmitField(label='OK')