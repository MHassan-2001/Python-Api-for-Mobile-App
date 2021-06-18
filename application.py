# from os import name
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql.expression import true
# from sqlalchemy.sql.schema import PrimaryKeyConstraint
# from flask import request

# app=Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///hostelmanagement.db'
# db=SQLAlchemy(app)

# class Drinks(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(80),unique=True,nullable=False)
#     description=db.Column(db.String(120))
    
#     def __repr__(self):
#         return f"{self.name}-{self.description}" 


# @app.route('/')
# def index():
#     return 'Hello!'

# @app.route('/drinks')
# def get_drinks():
#     drink=Drinks.query.all()
#     output=[]
#     for data in drink:
#         dictionary={"name ":data.name,"descritopn":data.description}
#         output.append(dictionary)
#     return {"drink":output}

# @app.route("/drinks/<id>")
# def get_id(id):
#     drink=Drinks.query.get_or_404(id)
#     return {"name":drink.name,"description":drink.description}

# @app.route("/drinks",methods=['POST'])
# def add_drink():
#     drink=Drinks(name=request.form['name'],description=request.form['value'])
#     db.session.add(drink)
#     db.session.commit()
#     return {'id':drink.id}

# @app.route("/drinks/<id>",methods=['DELETE'])
# def delete_drink(id):
#     drink=Drinks.query.get(id)
#     if drink is None:
#         return {"error":"Not Found"}
#     db.session.delete(drink)
#     db.session.commit()
#     return id
    

# if(__name__)=="__main__":
#     app.run(host='0.0.0.0')


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///hostelmanagement.db'
db=SQLAlchemy(app)


#Student Table#
    # id=db.Column(db.Integer,primary_key=True)
    # name=db.Column(db.String(80),unique=True,nullable=False)
    # description=db.Column(db.String(120))
class Student(db.Model):
    std_id=db.Column(db.Integer,primary_key=True)
    std_name=db.Column(db.String(30),nullable=False)
    std_prog=db.Column(db.String(30),nullable=False)
    std_room_id=db.Column(db.String(30),nullable=False)
    std_hostel_name=db.Column(db.String(30),nullable=False)

    def __repr__(self):
        return f"{self.std_name}-{self.std_id}-{self.std_prog}-{self.std_room_id}-{self.std_hostel_name}"

class Hostel(db.Model):
    hostel_name=db.Column(db.String(30),nullable=False,primary_key=True)
    hostel_type=db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"{self.hostel_name}-{self.hostel_type}"

class Room(db.Model):
    room_id=db.Column(db.String(30),nullable=False,primary_key=True)
    # room_space=db.Column(db.Integer)

    def __repr__(self):
        return f"{self.room_id}"

class HostelWarden(db.Model):
    std_id=db.Column(db.Integer,primary_key=True)
    std_name=db.Column(db.String(30),nullable=False)
    std_prog=db.Column(db.String(30),nullable=False)
    std_room_id=db.Column(db.String(30),nullable=False)
    std_hostel_name=db.Column(db.String(30),nullable=False)

    def __repr__(self):
        return f"{self.std_name}-{self.std_id}-{self.std_prog}-{self.std_room_id}-{self.std_hostel_name}"

class Complaints(db.Model):

    std_id=db.Column(db.Integer,nullable=False)
    std_room_id=db.Column(db.String(30),nullable=False)
    std_complaint=db.Column(db.String(200),nullable=False)
    date_time=db.Column(db.String(20),nullable=False,primary_key=True)

    def __repr__(self):
        return f"{self.std_id}-{self.std_room_id}-{self.std_complaint}-{self.date_time}"
    

@app.route('/')
def get_index():

    return "<h1>Welcome to UNIVERSITY OF GUJRAT HOSTEL</h1>"
    # student=Student(std_name="Hassan",
    # std_id="18321519128",std_prog="BSCS",std_room_id="C-29",
    # std_hostel_name="Usman Hostel")
    # db.session.add(student)
    # db.session.commit()
   
@app.route('/student')
def get_student():
    std_DATA=Student.query.all()
    output=[]
    for data in std_DATA:
        std_dic={"id":data.std_id,"name":data.std_name,"prog":data.std_prog,
        "room_id":data.std_room_id,"hostel_name": data.std_hostel_name}
        output.append(std_dic)
    return {"Student":output}

@app.route('/student',methods=['POST'])
def add_student():
    std=Student(std_id=request.form['sid'],std_name=request.form['sname'],std_prog=request.form['sprog']
    ,std_room_id=request.form['srid'],std_hostel_name=request.form['shname'])
    db.session.add(std)
    db.session.commit()
    return {'id':std.std_id}

@app.route('/hostel')
def get_hostel():
    hostel_DATA=Hostel.query.all()
    output=[]
    for data in hostel_DATA:
        hostel_dic={"hostel_name": data.hostel_name,"hostel_type":data.hostel_type}
        output.append(hostel_dic)
    return {"Hostel":output}

@app.route('/hostel',methods=['POST'])
def add_hostel():
    hostel=Hostel(hostel_name=request.form['hname'],hostel_type=request.form['htype'])
    db.session.add(hostel)
    db.session.commit()
    return {'hname':hostel.hostel_name}

@app.route('/room')
def get_room():
    room=Room.query.all()
    output=[]
    for data in room:
        room_dic={"room_id":data.room_id}
        output.append(room_dic)
    return {"Room":output}

@app.route('/room',methods=['POST'])
def add_room():
    room=Room(room_id=request.form('rid'))
    db.session.add(room)
    db.session.commit()
    return {'rid':room.room_id}
 
@app.route('/warden')
def get_studentfromwarden():
    warden_DATA=HostelWarden.query.all()
    output=[]
    for data in warden_DATA:
        warden_dic={"id":data.std_id,"name":data.std_name,"prog":data.std_prog,
        "room_id":data.std_room_id,"hostel_name": data.std_hostel_name}
        output.append(warden_dic)
    return {"HostelWarden":output}

@app.route('/warden',methods=['POST'])
def add_studentintowarden():
    warden=HostelWarden(std_id=request.form['sid'],std_name=request.form['sname'],std_prog=request.form['sprog']
    ,std_room_id=request.form['srid'],std_hostel_name=request.form['shname'])
    db.session.add(warden)
    db.session.commit()
    return {'id':warden.std_id}

@app.route('/warden/<id>',methods=['DELETE'])
def delete_student_from_warden_List(id):
    warden=HostelWarden.query.get(id)

    if warden is None:
        return {"error":"Not Found"}
    db.session.delete(warden)
    db.session.commit()
    return id

@app.route('/complaint')
def get_complaint():
    complain_DATA=Complaints.query.all()
    output=[]
    for data in complain_DATA:
        complain_dic={"sid":data.std_id,"srid":data.std_room_id,"dateTime":data.date_time,"complaint":data.std_complaint}
        output.append(complain_dic)
    return {"Complaints":output}

@app.route('/complaint',methods=['POST'])
def add_complaint():
    add_cmpl=Complaints(std_id=request.form['sid'],std_complaint=request.form['scomplain'],date_time=request.form['date_time']
    ,std_room_id=request.form['srid'])
    db.session.add(add_cmpl)
    db.session.commit()
    return {'id':add_cmpl.std_id}

@app.route('/complaint/<id>',methods=['DELETE'])
def delete_complaint(id):
    complaint=Complaints.query.get(id)
    print(complaint.date_time)
    if complaint is None:
        return {"error":"Not Found"}
    db.session.delete(complaint)
    db.session.commit()
    return id

class Admin(db.Model):
    username=db.Column(db.String(50),primary_key=True)
    password=db.Column(db.String(50))
    
    def __repr__(self):
        return f"{self.username}-{self.password}"

@app.route('/admin')
def get_admin():
    admin_DATA=Admin.query.all()
    output=[]
    for data in admin_DATA:
        admin_dic={"user":data.username,"pass":data.password}
        output.append(admin_dic)
    return {"Admin":output}

###############################
class User(db.Model):
    username=db.Column(db.String(50),primary_key=True)
    password=db.Column(db.String(50))
    
    def __repr__(self):
        return f"{self.username}-{self.password}"

@app.route('/user')
def get_user():
    user_DATA=User.query.all()
    output=[]
    for data in user_DATA:
        user_dic={"user":data.username,"pass":data.password}
        output.append(user_dic)
    return {"User":output}

if(__name__)=="__main__":
    app.run(host='0.0.0.0')

