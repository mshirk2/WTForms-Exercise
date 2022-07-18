from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField("Name")
    species = StringField("Species")