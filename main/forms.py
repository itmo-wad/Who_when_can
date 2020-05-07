from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, BooleanField, HiddenField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class AuthForm(Form):
    name = TextField('Displayed name', validators = [DataRequired()])
    username = TextField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Authenticate')


class MeetingForm(Form):
    meetingname = TextField('Meeting name', validators = [DataRequired()])
    info = TextField('Purpose of the meeting and other useful information', validators = [DataRequired()])
    available_dates = HiddenField()
    submit = SubmitField('Submit')

class DaysAndHoursForm(Form):
    selecteddaysandhours = HiddenField()
    submit = SubmitField('Submit')