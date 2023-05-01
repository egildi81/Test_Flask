from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    submit = SubmitField('Submit')

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    author_id = StringField('Author ID', validators=[DataRequired()])
    submit = SubmitField('Submit')
