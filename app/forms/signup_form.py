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
    username = StringField('username', validators=[DataRequired(), Length(max=30, message="Less than 30 characters"), username_exists])
    full_name = StringField('full_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email(message="Must be valid email"), user_exists])

    password = StringField('password', validators=[DataRequired()])
