from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo

class AddEmployee(FlaskForm):
    first_name = StringField("First_name", [InputRequired()])
    last_name = StringField("Last_name", [InputRequired()])
    company = IntegerField("Company")
    email = EmailField("Email", [InputRequired(), Email()])

class EditEmployee(AddEmployee):
    id = IntegerField("Employee ID", [InputRequired()])