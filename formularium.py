from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class growth(FlaskForm):

    deposit = StringField('Deposit')
    interest = StringField('Yield')
    submit = SubmitField('Submit')
