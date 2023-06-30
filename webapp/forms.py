from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PatentSearchForm(FlaskForm):
    search_term = StringField('Search Term', validators=[DataRequired()])
    submit = SubmitField('Search')

class CostEstimateForm(FlaskForm):
    patent_id = StringField('Patent ID', validators=[DataRequired()])
    submit = SubmitField('Estimate Cost')