from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoanCheckForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    age = IntegerField('Age:', validators=[DataRequired()])
    gender = SelectField('Gender:', choices=['', 'Male', 'Female'], validators=[DataRequired()])
    education = SelectField('Education:', validators=[DataRequired()],
                            choices=['', 'High school', 'Bachelor', 'Master', 'Doctorate'])
    income = FloatField('Monthly income (in millions VND):', validators=[DataRequired()])
    exp = IntegerField('Years of employment experience:', validators=[DataRequired()])
    home_ownership = SelectField('Home ownership:', validators=[DataRequired()],
                                 choices=['', 'Rent', 'Mortgage', 'Own', 'Other'])
    amount = FloatField('Loan amount (in millions VND):', validators=[DataRequired()])
    intent = SelectField('This loan is for:', validators=[DataRequired()],
                         choices=['', 'Education', 'Medical', 'Venture', 'Personal', 'Debt consolidation',
                                  'Home improvement'])
    interest_rate = FloatField('Interest rate (%):', validators=[DataRequired()])
    credit_score = IntegerField('Credit score:', validators=[DataRequired()])
    credit_hist_len = IntegerField('Credit history length (years):', validators=[DataRequired()])
    prev_loan_default = BooleanField('Previous loan default:')
    submit = SubmitField('Submit')
