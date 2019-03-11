from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class InventoryForm(FlaskForm):
    """
    Form to add a new inventory
    """
    pid = IntegerField('Product Id', validators=[DataRequired(message='Please enter product ID')])
    name = StringField('Name', validators=[DataRequired(message='Please enter name')])
    price = StringField('Price')
    quantity = IntegerField('Quantity')

    submit = SubmitField()