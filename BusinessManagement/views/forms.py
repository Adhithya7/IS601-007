from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo

class Employee(FlaskForm):
    first_name = StringField("First_name", [InputRequired()])
    last_name = StringField("Last_name", [InputRequired()])
    company = IntegerField("Company")
    email = EmailField("Email", [InputRequired(), Email()])
class Company(FlaskForm):
    name = StringField("name", [InputRequired()])
    address = StringField("address", [InputRequired()])
    city = StringField("city", [InputRequired()])
    country = StringField("country", [InputRequired()])
    state = StringField("state", [InputRequired()])
    zip_code = StringField("zip_code", [InputRequired()])
    website = StringField("website")