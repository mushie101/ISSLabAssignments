from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///lol.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)

class Students(db.Model):
	rn = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))

	def __init__(self, rn, name, email):
		self.rn = rn
		self.name = name
		self.email = email

	def __repr__(self):
		return self.name


class Courses(db.Model):
	code = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))

	def __init__(self, code, name):
		self.code = code
		self.name = name

	def __repr__(self):
		return self.name

@app.route("/")
def show_all():
	return 'Hello world'

@app.route("/students/create", methods = ["POST"])
def student_create():
	db.create_all()
	rn = request.form["rn"]
	name = request.form["name"]
	email = request.form["email"]
	nw = Students(rn, name, email)
	db.session.add(nw)
	db.session.commit()
	temp = {}
	temp['status'] = (type(nw) == Students)
	return jsonify(temp)

@app.route("/students/delete", methods = ["POST"])
def student_delete():
	drn = request.form["rn"]
	delsel = Students.query.filter_by(rn = drn).first()
	db.session.delete(delsel)
	db.session.commit()
	temp = {}
	temp['status'] = (type(delsel) == Students)
	return jsonify(temp)

@app.route("/students", methods = ["POST", "GET"])
def students_fetchall():
	sel = Students.query.all()
	st = {}
	st["students"] = []
	for student in sel:
		st["students"].append({ "Roll Number" : student.rn, "Name" : student.name, "Email" : student.email })
	return jsonify(st)

@app.route("/students/<rollno>", methods = ["POST", "GET"])
def fup(rollno):
	if request.method == "POST":
		urn = rollno
		uname = request.form["name"]
		uemail = request.form["email"]
		delsel = Students.query.filter_by(rn = urn).first()
		db.session.delete(delsel)
		db.session.commit()
		nw = Students(urn, uname, uemail)
		db.session.add(nw)
		db.session.commit()
		return "{ 'status' : True }"
	elif request.method == "GET":
		vsel = Students.query.filter_by(rn = rollno)
		temp = {}
		for student in vsel:
			temp["Roll Number"] = student.rn
			temp["Name"] = student.name
			temp["Email"] = student.email
		return jsonify(temp)

if __name__ == "__main__":
	app.run()
