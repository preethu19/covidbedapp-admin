from flask import Flask,render_template,url_for, redirect,flash, request
from models import db,app,Hospital,Bed,Patient,Contact
from forms import addhospitalform,InfoForm, edithospitalform
from sqlalchemy import desc



#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

#db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '966da55dc2'

#@app.route('/')
#def home():
#    return "Welcome to Home page"

@app.route('/')
def admin():
    return render_template('admin.html')
  
 
"""
def hospital():
    form = hospitalform()
    hlist=[]
    if form.validate_on_submit():
        #flash(f'valid hospital name','success') 
        hlist = Hospital.query.filter_by(name=form.hospitalname.data).all()
    else:
        hlist = Hospital.query.all()
    return render_template('hospital.html', form=form, hlist=hlist, title="Hospital")
"""
@app.route('/hospital', methods=['POST', 'GET']) 
def hospital():
    name=False
    district=False
    state=False
    area=False
    beds= False
    form = InfoForm() 
    page = request.args.get('page', 1, type=int)
    print('page: ', page)
    
    if request.method == 'POST':
        name = form.name.data
        district = form.district.data
        state = form.state.data
        area = form.area.data
        beds = form.beds.data
        page = 1
        print(name)
        print(district)
    
    if request.method == 'GET':
        name = request.args.get('name')
        state = request.args.get('state')
        district = request.args.get('district')
        area = request.args.get('area')
        beds = request.args.get('beds')
    # data = Hospital.query.order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page) 
    if form.validate_on_submit() and request.method == "POST":
        print('POST request')
        
        
        #print(request.form['name'])
        # print(form.name.data)
        
    data = Hospital.query.order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
    # if request.method == "POST":
        
        #print(request.form['name'])
        # if name =='Please Select':
        #     name_avail = False
        # if district =='Please Select':
        #     district_avail = False
        # if state =='Please Select':
        #     state_avail = False
        # if area =='Please Select':
        #     area_avail = False
        
    if(name =='Please Select' and district =='Please Select' and state =='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)        
        elif beds== 'available_beds':
            data = Hospital.query.order_by(Hospital.available_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name !=  'Please Select' and district =='Please Select' and state =='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district !='Please Select' and state =='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district =='Please Select' and state !='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
    
    elif(name ==  'Please Select' and district =='Please Select' and state =='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
    
    elif(name !=  'Please Select' and district !='Please Select' and state =='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name !=  'Please Select' and district =='Please Select' and state !='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name !=  'Please Select' and district =='Please Select' and state =='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district !='Please Select' and state !='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district !='Please Select' and state =='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district =='Please Select' and state !='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)


    elif(name !=  'Please Select' and district !='Please Select' and state !='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name !=  'Please Select' and district !='Please Select' and state =='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)


    elif(name !=  'Please Select' and district =='Please Select' and state !='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district !='Please Select' and state !='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name !=  'Please Select' and district !='Please Select' and state !='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    else:
        data = Hospital.query.order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        print("Get Request")
    form.name.data = name
    form.district.data = district
    form.state.data = state
    form.area.data = area
    form.beds.data = beds
    return render_template('index.html', form=form, name=name, district=district, state=state, area=area, beds=beds, hospitals=data)

@app.route('/hospital/<int:hospital_id>/profile')
def profilehospital(hospital_id):
    hospital = Hospital.query.get_or_404(hospital_id)
    return render_template('hospitalprofile.html' , hospital=hospital) 
    
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
    form = edithospitalform()
    if request.method=='POST' and form.validate_on_submit():
        if (hospital.total_beds-hospital.available_beds) <= form.total_beds.data and (hospital.total_ward_beds-hospital.available_ward_beds) <= form.total_ward_beds.data and\
        (hospital.total_ward_beds_with_oxygen-hospital.available_ward_beds_with_oxygen) <= form.total_ward_beds_with_oxygen.data and (hospital.total_icu_beds-hospital.available_icu_beds) <= form.total_icu_beds.data and\
        (hospital.total_icu_beds_with_oxygen-hospital.available_icu_beds_with_oxygen) <= form.total_icu_beds_with_oxygen.data:                                                                    
            db.session.query(Hospital).filter_by(id=hospital_id).update({Hospital.total_beds: form.total_beds.data, Hospital.total_ward_beds: form.total_ward_beds.data,\
                                                                  Hospital.total_ward_beds_with_oxygen: form.total_ward_beds_with_oxygen.data, Hospital.total_icu_beds: form.total_icu_beds.data,\
                                                                  Hospital.total_icu_beds_with_oxygen:form.total_icu_beds_with_oxygen.data}, synchronize_session = False) 
            db.session.commit()
            return redirect(url_for('hospital')) 
        else:
            flash('the number of beds of category edited should be greater than the occupied number','danger')
            return redirect(url_for('admin'))
    else:
        form.total_beds.data = hospital.total_beds
        form.total_ward_beds.data = hospital.total_ward_beds
        form.total_ward_beds_with_oxygen.data = hospital.total_ward_beds_with_oxygen
        form.total_icu_beds.data = hospital.total_icu_beds
        form.total_icu_beds_with_oxygen.data = hospital.total_icu_beds_with_oxygen
    return render_template('hospitaledit.html',hospital=hospital, form=form, title="Edit Hospital")
    
@app.route('/complaint')    
def complaint():
    page = request.args.get('page', 1, type=int)
    clist = Contact.query.order_by(desc(Contact.date_posted)).paginate(per_page=5, page=page)
    return render_template('complaint.html', clist=clist, title="Complaint Section")
    
@app.route('/complaint/<int:complaint_id>/resolve')    
def resolvecomplaint(complaint_id):
    c = Contact.query.get_or_404(complaint_id)
    db.session.delete(c)
    db.session.commit()
    return redirect(url_for('complaint'))

if __name__ == '__main__':
    app.run(debug=True)