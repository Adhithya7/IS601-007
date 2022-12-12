from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from wtforms.validators import ValidationError

def is_valid_username(username):
    import re
    r = re.fullmatch("^[a-z0-9_-]{2,30}$", username)
    print("re",r)
    if not r:
        print("validation errr")
        raise ValidationError("Invalid username format")

class AuthForm(FlaskForm):
    # shared form that groups most of our validations together to reduce repetition
    username = StringField("username", validators=[DataRequired(), Length(2, 30)])
    email = EmailField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), EqualTo('confirm', message='Passwords must match'), Length(8)])
    confirm = PasswordField("confirm", validators=[DataRequired(),  EqualTo('password', message='Passwords must match'),Length(8)])
    def validate_username(form, field):
        print("checking ", field.data)
        is_valid_username(field.data)
class RegisterForm(AuthForm):
    submit = SubmitField("Register")
