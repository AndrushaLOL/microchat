from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class IrisForm(FlaskForm):
    sepal_length = IntegerField('Petal length', validators=[DataRequired()])
    sepal_width = IntegerField('Petal width', validators=[DataRequired()])
    petal_length = IntegerField('Petal length', validators=[DataRequired()])
    petal_width = IntegerField('Petal width', validators=[DataRequired()])
    submit = SubmitField('Predict')