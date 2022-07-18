from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField("Name", validators=[
        InputRequired(message="Name is required")])
    
    species = StringField("Species", validators=[
        InputRequired(message="Species is required"), 
        AnyOf(values=dog cat rabbit, message="Species must be dog, cat or rabbit")])
    
    photo_url = StringField("Photo URL", validators=[
        Optional(strip_whitespace=True), 
        URL(message="Must be a valid URL")])
    
    age = IntegerField("Age", validators=[
        Optional(strip_whitespace=True),
        NumberRange(min=0, max=30, message="Age must be between 0-30")])
   
    notes = StringField("Notes", validators=[
        Optional(strip_whitespace=True)])