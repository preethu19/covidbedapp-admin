from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,TextAreaField
from wtforms.validators import DataRequired

class hospitalform(FlaskForm):
    hospitalname = StringField('Hospital Name', validators=[DataRequired()])
    submit = SubmitField('Enter')
    
class addhospitalform(FlaskForm):
    hospitalname = StringField('Hospital Name', validators=[DataRequired()])
    area = StringField('area', validators=[DataRequired()])
    district = StringField('district', validators=[DataRequired()])
    state = StringField('state', validators=[DataRequired()])
    total_beds = IntegerField('total_beds', validators=[DataRequired()])
    total_ward_beds = IntegerField('total_ward_beds', validators=[DataRequired()])
    total_ward_beds_with_oxygen = IntegerField('total_ward_beds_with_oxygen', validators=[DataRequired()])
    total_icu_beds = IntegerField('total_icu_beds', validators=[DataRequired()])
    total_icu_beds_with_oxygen = IntegerField('total_icu_beds_with_oxygen', validators=[DataRequired()])
    submit = SubmitField('Enter')    
    