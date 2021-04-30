from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from tasklist.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists.')
    
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email = email_to_check.data).first()
        if email:
            raise ValidationError('E-mail already in use.')

    username = StringField(label='User name:', validators=[Length(min=2,max=30),DataRequired()])
    email = StringField(label='E-mail:', validators=[Email(),DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=2,max=60),DataRequired()])
    password_confirmation = PasswordField(label='Confirm your password:', validators=[EqualTo('password'),DataRequired()])
    submit = SubmitField(label='OK')

class LoginForm(FlaskForm):
    username = StringField(label='User name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Go')