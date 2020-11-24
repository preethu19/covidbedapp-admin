from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,TextAreaField,SelectField
from wtforms.validators import DataRequired

#class hospitalform(FlaskForm):
#    hospitalname = StringField('Hospital Name', validators=[DataRequired()])
#    submit = SubmitField('Enter')
    
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
    
class edithospitalform(FlaskForm):
    total_beds = IntegerField('total_beds', validators=[DataRequired()])
    total_ward_beds = IntegerField('total_ward_beds', validators=[DataRequired()])
    total_ward_beds_with_oxygen = IntegerField('total_ward_beds_with_oxygen', validators=[DataRequired()])
    total_icu_beds = IntegerField('total_icu_beds', validators=[DataRequired()])
    total_icu_beds_with_oxygen = IntegerField('total_icu_beds_with_oxygen', validators=[DataRequired()])
    submit = SubmitField('Enter')    
        
class InfoForm(FlaskForm):
    name = SelectField('Name', choices=[('Please Select','Please Select'),('Preetham emergency','Preetham emergency'),('Nandan clinic','Nandan clinic'),('Siddarth multispeciality','Siddarth multispeciality'),('Father Muller Hospital','Father Muller Hospital')])
    district = SelectField('District: ', choices=[('Please Select','Please Select'),('D.K','D.K'),('Banglore','Banglore')])
    state = SelectField('State: ', choices=[('Please Select','Please Select'),('Andra','Andra'),('Karnataka','Karnataka')])
    area = SelectField('Area: ', choices=[('Please Select','Please Select'),('badyar','badyar'),('mattikere','mattikere')])
    beds = SelectField('Sort bed results by ', validators=[DataRequired()], choices=[('total_beds','total_beds'),('available_beds','available_beds'),('available_ward_beds','available_ward_beds'),('available_ward_beds_with_oxygen','available_ward_beds_with_oxygen'),('available_icu_beds','available_icu_beds'),('available_icu_beds_with_oxygen','available_icu_beds_with_oxygen')], default='total_beds')
    submit = SubmitField('Search')    