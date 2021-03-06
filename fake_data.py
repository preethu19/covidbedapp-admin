from models import db, Hospital, Patient, Bed, Contact
from faker import Faker
fakegen = Faker()

h1 = Hospital(name='kle', area='belgaum', district='belgaum', state='Karnataka', total_beds=1000, available_beds=900,\
                 total_ward_beds=250, available_ward_beds=225, total_ward_beds_with_oxygen=300,\
                 available_ward_beds_with_oxygen=275, total_icu_beds=350, available_icu_beds=325,\
                 total_icu_beds_with_oxygen=100, available_icu_beds_with_oxygen=75)
h2 = Hospital(name='kims', area='hubli', district='dharwad', state='Karnataka', total_beds=1000, available_beds=900,\
                 total_ward_beds=250, available_ward_beds=225, total_ward_beds_with_oxygen=300,\
                 available_ward_beds_with_oxygen=275, total_icu_beds=350, available_icu_beds=325,\
                 total_icu_beds_with_oxygen=100, available_icu_beds_with_oxygen=75)
h3 = Hospital(name='lakeview', area='anjaney nagar', district='belgaum', state='Karnataka', total_beds=1000, available_beds=900,\
                 total_ward_beds=250, available_ward_beds=225, total_ward_beds_with_oxygen=300,\
                 available_ward_beds_with_oxygen=275, total_icu_beds=350, available_icu_beds=325,\
                 total_icu_beds_with_oxygen=100, available_icu_beds_with_oxygen=75)    
h4 = Hospital(name='kle', area='basavan nagar', district='dharwad', state='Karnataka', total_beds=1000, available_beds=900,\
                 total_ward_beds=250, available_ward_beds=225, total_ward_beds_with_oxygen=300,\
                 available_ward_beds_with_oxygen=275, total_icu_beds=350, available_icu_beds=325,\
                 total_icu_beds_with_oxygen=100, available_icu_beds_with_oxygen=75) 
db.session.add(h1)
db.session.add(h2)
db.session.add(h3)
db.session.add(h4)
db.session.commit()

b1 = Bed(bed_number=1, bed_type='ward', cost=10000, hospital=h1)
b2 = Bed(bed_number=2, bed_type='ward', cost=10000, hospital=h1)
b3 = Bed(bed_number=3, bed_type='ward', cost=10000, hospital=h1)
b4 = Bed(bed_number=4, bed_type='ward', cost=10000, hospital=h1)
b5 = Bed(bed_number=5, bed_type='ward', cost=10000, hospital=h1)
b6 = Bed(bed_number=1, bed_type='ward with oxygen', cost=20000, hospital=h1)
b7 = Bed(bed_number=2, bed_type='ward with oxygen', cost=20000, hospital=h1)
b8 = Bed(bed_number=3, bed_type='ward with oxygen', cost=20000, hospital=h2)
b9 = Bed(bed_number=4, bed_type='ward with oxygen', cost=20000, hospital=h2)
b10 = Bed(bed_number=5, bed_type='ward with oxygen', cost=20000, hospital=h3)
b11 = Bed(bed_number=1, bed_type='ICU', cost=30000, hospital=h1)
b12 = Bed(bed_number=2, bed_type='ICU', cost=30000, hospital=h2)
b13 = Bed(bed_number=3, bed_type='ICU', cost=30000, hospital=h2)
b14 = Bed(bed_number=4, bed_type='ICU', cost=30000, hospital=h3)
b15 = Bed(bed_number=5, bed_type='ICU', cost=30000, hospital=h3)
b16 = Bed(bed_number=1, bed_type='ICU with oxygen', cost=40000, hospital=h3)
b17 = Bed(bed_number=2, bed_type='ICU with oxygen', cost=40000, hospital=h3)
b18 = Bed(bed_number=3, bed_type='ICU with oxygen', cost=40000, hospital=h1)
b19 = Bed(bed_number=4, bed_type='ICU with oxygen', cost=40000, hospital=h2)
b20 = Bed(bed_number=5, bed_type='ICU with oxygen', cost=40000, hospital=h2)
db.session.add(b1)
db.session.add(b2)
db.session.add(b3)
db.session.add(b4)
db.session.add(b5)
db.session.add(b6)
db.session.add(b7)
db.session.add(b8)
db.session.add(b9)
db.session.add(b10)
db.session.add(b11)
db.session.add(b12)
db.session.add(b13)
db.session.add(b14)
db.session.add(b15)
db.session.add(b16)
db.session.add(b17)
db.session.add(b18)
db.session.add(b19)
db.session.add(b20)
db.session.commit()


p1 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b1)
p2 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b2)
p3 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b3)
p4 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b4)
p5 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b5)
p6 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b6)
p7 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b7)
p8 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b8)
p9 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b9)
p10 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b10)
p11 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b11)
p12 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b12)
p13 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b13)
p14 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b14)
p15 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b15)
p16 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b16)
p17 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b17)
p18 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b18)
p19 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b19)
p20 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b20)
p21 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b1)
p22 = Patient(name='Rahul', age=25, gender='male', status='admitted',\
                 phone=1234567890, address='xyz', blood_group='A positive', bed=b2)
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)
db.session.add(p6)
db.session.add(p7)
db.session.add(p8)
db.session.add(p9)
db.session.add(p10)
db.session.add(p11)
db.session.add(p12)
db.session.add(p13)
db.session.add(p14)
db.session.add(p15)
db.session.add(p16)
db.session.add(p17)
db.session.add(p18)
db.session.add(p19)
db.session.add(p20)
db.session.add(p21)
db.session.add(p22)
db.session.commit()

c1 = Contact(name='Rahul', phone=1234567890, content="hello")
c2 = Contact(name='vijay', phone=9987654321, content="vejiaj")
db.session.add(c1)
db.session.add(c2)
db.session.commit()
