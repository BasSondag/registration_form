
from flask import Flask, render_template, request, redirect, session, flash
import re
import datetime
		
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z\.\-_]*$')
app = Flask(__name__)
app.secret_key = 'whatdoessecret'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods= ['POST'])
def users():
	temp = request.form['password'].lower()

	if len(request.form['first_name']) < 1:
		flash('first name must be filled','first_name')
	elif not NAME_REGEX.match(request.form['first_name']):
		flash('No numbers ','first_name')
	elif len(request.form['last_name']) < 1:
		flash('last name must be filled','last_name')
	elif not NAME_REGEX.match(request.form['last_name']):
		flash('No numbers ','last_name')
	elif len(request.form['email']) < 1:
		flash('email required','email') 
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email address','email')
	elif temp == request.form['password']:
			flash('one upercase required','password')
	elif len(request.form['password']) < 9:
		flash('you need to fill in password','password')
	elif len(request.form['conf_password']) < 1:
		flash('you need to confirm password','conf_password')
	elif request.form['password'] != request.form['conf_password']:
		flash('you have diverend passwords','password')
	# elif request.form['date'] != datetime.date.strftime(request.form['date'],' %m-%d-%y'):	
	# 	flash('mm-dd-yyyy','date')
	else:
		flash('You registreted','succes')
		
	return redirect('/')	



app.run(debug = True)
 