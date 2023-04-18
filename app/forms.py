from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class PokemonLookUpForm(FlaskForm):
    name = StringField('Name', validators= [DataRequired()])
    ability = StringField('Ability', validators= [DataRequired()])
    base_experience = StringField('Base_experience', validators= [DataRequired()])
    attack = StringField('Attack', validators= [DataRequired()])
    defense = StringField('Defense', validators= [DataRequired()])