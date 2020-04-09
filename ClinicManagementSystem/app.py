from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
config = {
'host': 'localhost',
'user': 'root',
'password': 'rohan$198',
'database': 'clinic_db1',

}
clinic = mysql.connector.connect(**config)
mycursor = clinic.cursor()


#CREATING A DATABASE
#mycursor.execute("CREATE DATABASE clinic_db1")

#CREATING A TABLE
#mycursor.execute("CREATE TABLE Patients1 (firstName VARCHAR(100), lastName VARCHAR(100), email VARCHAR(200), password VARCHAR(50), dateOfbirth DATE, city VARCHAR(100), state VARCHAR(100),user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")


@app.route('/', methods =['GET', 'POST'])
def index():
	return render_template('index.html')


@app.route('/appointments.html', methods = ['GET', 'POST'])
def appointment():
	   return render_template('appointments.html')


@app.route('/add-appointment.html', methods = ['GET', 'POST'])
def add_appointment():
	return render_template('add-appointment.html')

@app.route('/index.html')
def index1():
	return render_template('index.html')

@app.route('/patients.html', methods = ['GET', 'POST'])
def patient():
	mycursor = clinic.cursor()
	resultVal = mycursor.execute('select * from Patients1')
	patientDetails = mycursor.fetchall()
	return render_template('patients.html', patientDetails = patientDetails)

@app.route('/add-patient.html', methods =['GET', 'POST'])
def add_patient():
	if request.method == 'POST':
		user_data  = request.form
		first_name = user_data['first_name'] #0
		last_name = user_data['last_name'] #1
		email = user_data['email']  #2
		password = user_data['password']  #3
		confirm_pass = user_data['confirm_password']  #4
		dob = user_data['dob']  #5
		city = user_data['city'] #6
		#state = user_data['address'] #7
		address = user_data['address']  #8
		#firstName VARCHAR(100), lastName VARCHAR(100), email VARCHAR(200), password VARCHAR(50), dateOfbirth DATE, city VARCHAR(100), state VARCHAR(100)
		mycursor.execute("INSERT INTO Patients1(firstName, lastName, email, password, city, state) VALUES (%s, %s, %s, %s, %s, %s)", (first_name, last_name, email, confirm_pass, city, address) )
		clinic.commit()
		#mycursor.close()
		#return 'success'
		return redirect('/patients.html')
	else:
		return render_template('add-patient.html')
def finish():
	mycursor.close()

    #if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else


if __name__ == '__main__':
	app.run(port='5018', debug= True)
	finish()



#from flask import Flask, render_template, request, redirect
#import mysql.connector
##from flask_mysqldb import MySQL
#import yaml
#
#app = Flask(__name__)
#
##Configure DB
##db = yaml.load(open('db.yaml'))
#
#config = {
#'host': 'localhost',
#'user': 'root',
#'password': 'rohan$198',
#'database': 'testdb',
#}
#
#mydb = mysql.connector.connect(**config)
#@app.route('/', methods = ['GET', 'POST'])
#def index():
#	if request.method == 'POST':
#		user_data = request.form
#		name = user_data['name']
#		email = user_data['email']
#		cursor = mydb.cursor()
#		cursor.execute("INSERT INTO users(name, email) VALUES (%s, %s)", (name,email) )
#		mydb.commit()
#		cursor.close()
#		return redirect('/users')
#	return render_template('index.html')
#
#@app.route('/users')
#def users():
#	cursor = mydb.cursor()
#	resultVal = cursor.execute("SELECT * FROM users")
#	userDetails = cursor.fetchall()
#	return render_template('users.html', userDetails=userDetails)
#
#if __name__ == '__main__':
#	app.run(port ='5006', debug = True)