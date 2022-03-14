from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[DataRequired('Username is required.'),
    Length(max=30, message="Username must be < 30 characters."),
    username_exists])

    full_name = StringField('full_name', validators=[DataRequired('Full name is required.')])

    email = StringField('email', validators=[DataRequired('Email is required.'),
    Email(message="Must be a valid email."),
    user_exists])

    password = StringField('password', validators=[DataRequired('Password is required.')])
