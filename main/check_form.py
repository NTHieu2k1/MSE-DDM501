from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class LoanCheckForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    age = IntegerField('Age:', validators=[DataRequired(), NumberRange(min=18)])
    gender = SelectField('Gender:', choices=['', 'Male', 'Female'], validators=[DataRequired()])
    education = SelectField('Education:', validators=[DataRequired()],
                            choices=['', 'High school', 'Bachelor', 'Master', 'Doctorate'])
    income = FloatField('Monthly income (in millions VND):', validators=[DataRequired(), NumberRange(min=0)])
    exp = IntegerField('Years of employment experience:', validators=[DataRequired(), NumberRange(min=0)])
    home_ownership = SelectField('Home ownership:', validators=[DataRequired()],
                                 choices=['', 'Rent', 'Mortgage', 'Own', 'Other'])
    amount = FloatField('Loan amount (in millions VND):', validators=[DataRequired(), NumberRange(min=0)])
    intent = SelectField('This loan is for:', validators=[DataRequired()],
                         choices=['', 'Education', 'Medical', 'Venture', 'Personal', 'Debt consolidation',
                                  'Home improvement'])
    interest_rate = FloatField('Interest rate (%):', validators=[DataRequired(), NumberRange(min=0)])
    credit_score = IntegerField('Credit score:', validators=[DataRequired(), NumberRange(min=0)])
    credit_hist_len = IntegerField('Credit history length (years):', validators=[DataRequired(), NumberRange(min=0)])
    prev_loan_default = BooleanField('Previous loan default')
    submit = SubmitField('Submit')
