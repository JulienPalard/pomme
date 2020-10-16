from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search_word = StringField("Word", validators=[DataRequired()])
    submit = SubmitField("Search!")
