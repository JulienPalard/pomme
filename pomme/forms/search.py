from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search_word = StringField("Word", validators=[DataRequired()])
    id_lang = SelectField("Source Language", choices=["en"], default="en")
    str_lang = SelectField("Dest Language", choices=["fr"], default="fr")
    submit = SubmitField("Search!")
