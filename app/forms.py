from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class InputTextForm(FlaskForm):
    text_in = TextAreaField("Input Text", validators=[DataRequired()])
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    number_of_res = IntegerField(
        "How many results?", default=10, validators=[NumberRange(min=1)]
    )
    word = StringField("Input Word", validators=[DataRequired()])
    submit = SubmitField("Submit")
