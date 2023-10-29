from flask_wtf import FlaskForm
from wtforms import EmailField, StringField
from wtforms.validators import Email, InputRequired

class Employee(FlaskForm):
    first_name = StringField("First_name", [InputRequired()])
    last_name = StringField("Last_name", [InputRequired()])
    email = EmailField("Email", [InputRequired(), Email()])
class Company(FlaskForm):
    name = StringField("name", [InputRequired()])
    address = StringField("address", [InputRequired()])
    city = StringField("city", [InputRequired()])
    zip = StringField("zip_code", [InputRequired()])
    website = StringField("website")