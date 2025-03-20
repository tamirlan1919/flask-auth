from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    username = StringField('Username', Length(min=3, max=20), validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', Length(min=6), validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', Length(min=6), validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('Register')


