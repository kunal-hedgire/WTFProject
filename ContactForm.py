from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField


class Contactform(Form):
    firstname = StringField("Name Of Student")
    lastname = StringField("Name Of Student")
    gender = RadioField('gender', choices=[('M', 'Male'), ('F', 'Female')])
    address = TextAreaField("Address")
    #email = TextField("Email")
    age = IntegerField("age")
    skill = SelectField('Languages', choices=[('cpp', 'C++'),('py', 'Python')])
    submit = SubmitField("Send")
