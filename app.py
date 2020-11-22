from flask import Flask,render_template,url_for, redirect,flash, request
from models import db,app,Hospital,Bed,Patient,Contact
from forms import hospitalform,addhospitalform
from sqlalchemy import desc



#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

#db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '966da55dc2'

@app.route('/')
def home():
    return "Welcome to Home page"

@app.route('/admin')
def admin():
    return render_template('admin.html')
  
@app.route('/hospital', methods=['POST', 'GET'])  
def hospital():
    form = hospitalform()
    #hlist=dict()
    hlist=[]
    if form.validate_on_submit():
        #flash(f'valid hospital name','success') 
        hlist = Hospital.query.filter_by(name=form.hospitalname.data).all()
    else:
        hlist = Hospital.query.all()
    return render_template('hospital.html', form=form, hlist=hlist, title="Hospital")

@app.route('/hospital/add', methods=['POST', 'GET'])
def addhospital():
    form = addhospitalform()   
    if form.validate_on_submit():
        hospital = Hospital(name=form.hospitalname.data,area=form.area.data,\
                            district=form.district.data,total_beds=form.total_beds.data,\
                            state=form.state.data,total_ward_beds=form.total_ward_beds.data,\
                            total_ward_beds_with_oxygen=form.total_ward_beds_with_oxygen.data,total_icu_beds=form.total_icu_beds.data,\
                            total_icu_beds_with_oxygen=form.total_icu_beds_with_oxygen.data,available_beds=form.total_ward_beds.data,\
                            available_ward_beds=form.total_ward_beds.data,available_ward_beds_with_oxygen=form.total_ward_beds_with_oxygen.data,\
                            available_icu_beds=form.total_icu_beds.data,available_icu_beds_with_oxygen=form.total_icu_beds_with_oxygen.data)
        db.session.add(hospital)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('hospitaladd.html', form=form, title="Add Hospital")

@app.route("/hospital/<int:hospital_id>/remove", methods=['GET', 'POST'])
def removehospital(hospital_id):
    h = Hospital.query.get_or_404(hospital_id)
    db.session.delete(h)
    db.session.commit()
    return redirect(url_for('hospital'))

@app.route("/hospital/<int:hospital_id>/edit", methods=['GET', 'POST'])
def edithospital(hospital_id):
    hospital = Hospital.query.get_or_404(hospital_id)
    form = addhospitalform()
    if request.method=='POST' and form.validate_on_submit():
        if hospital.total_beds <= form.total_beds.data and hospital.total_ward_beds <= form.total_ward_beds.data and\
        hospital.total_ward_beds_with_oxygen <= form.total_ward_beds_with_oxygen.data and hospital.total_icu_beds <= form.total_icu_beds.data and\
        hospital.total_icu_beds_with_oxygen <= form.total_icu_beds_with_oxygen.data:                                                                    
            db.session.query(Hospital).filter_by(id=hospital_id).update({Hospital.total_beds: form.total_beds.data, Hospital.total_ward_beds: form.total_ward_beds.data,\
                                                                  Hospital.total_ward_beds_with_oxygen: form.total_ward_beds_with_oxygen.data, Hospital.total_icu_beds: form.total_icu_beds.data,\
                                                                  Hospital.total_icu_beds_with_oxygen:form.total_icu_beds_with_oxygen.data}, synchronize_session = False) 
            db.session.commit()
            return redirect(url_for('hospital')) 
        else:
            return redirect(url_for('admin'))
    else:
        form.hospitalname.data = hospital.name
        form.area.data = hospital.area
        form.district.data = hospital.district
        form.state.data = hospital.state
        form.total_beds.data = hospital.total_beds
        form.total_ward_beds.data = hospital.total_ward_beds
        form.total_ward_beds_with_oxygen.data = hospital.total_ward_beds_with_oxygen
        form.total_icu_beds.data = hospital.total_icu_beds
        form.total_icu_beds_with_oxygen.data = hospital.total_icu_beds_with_oxygen
    return render_template('hospitaledit.html',hospital=hospital, form=form, title="Edit Hospital")
    
@app.route('/complaint')    
def complaint():
    clist = Contact.query.order_by(desc(Contact.date_posted)).all()
    return render_template('complaint.html', clist=clist, title="Complaint Section")
    

if __name__ == '__main__':
    app.run(debug=True)