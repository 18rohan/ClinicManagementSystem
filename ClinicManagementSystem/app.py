from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime, time


app = Flask(__name__)
config = {
'host': 'localhost',
'user': 'root',
'password': 'rohan$198',
'database': 'clinic_db3',

}
clinic = mysql.connector.connect(**config)
mycursor = clinic.cursor()



#CREATING A DATABASE
#mycursor.execute("CREATE DATABASE clinic_db1")

#CREATING A TABLE
#mycursor.execute("CREATE TABLE Patients1 (firstName VARCHAR(100), lastName VARCHAR(100), email VARCHAR(200), password VARCHAR(50), dateOfbirth DATE, city VARCHAR(100), state VARCHAR(100),user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

#mycursor.execute("CREATE TABLE Patient_details1 (firstName VARCHAR(100), lastName VARCHAR(100), Age INT(4), Disease VARCHAR(100), Medications TEXT, user_id INT PRIMARY KEY, FOREIGN KEY(user_id) REFERENCES Patients1(user_id))")
global patientDetails
@app.route('/', methods =['GET', 'POST'])
def index():
		mycursor = clinic.cursor()
		number_rows = mycursor.execute('select * from Patients3')
		all_data = len(mycursor.fetchall())

		mycursor5 = clinic.cursor()
		number_rows_appt = mycursor5.execute('select * from Appointments3')
		all_data_appt =len(mycursor5.fetchall())

		mycursor = clinic.cursor()
		Valdata = mycursor.execute('select * from Appointments3')
		patient_Details3 = mycursor.fetchall()
		#return render_template('/appointments.html',patient_details = patient_Details3)

		mycursor = clinic.cursor()
		resultVal = mycursor.execute('select * from Patients3')
		patientDetails = mycursor.fetchall()


		return render_template('index.html', number_rows= all_data, numberRowsAppt = all_data_appt, patient_details = patient_Details3, patientDetails = patientDetails)


@app.route('/appointments.html', methods = ['GET', 'POST'])
def appointment():
		mycursor = clinic.cursor()
		Valdata = mycursor.execute('select * from Appointments3')
		patient_Details3 = mycursor.fetchall()
		return render_template('/appointments.html',patient_details = patient_Details3)


@app.route('/add-appointment.html', methods = ['GET', 'POST'])
def add_appointment():
	if request.method =='POST':

		appt_data = request.form
		appt_id = appt_data['appt_id']
		name = appt_data['Patient_name']
		date = appt_data['Date']
		datetimeobject = datetime.strptime(date,'%d/%m/%Y')
		new_date = datetimeobject.strftime('%Y/%m/%d')
		time = appt_data['Time']
		time1 = time.split(' ')[0]
		timeobject = datetime.strptime(time1, '%H:%M')
		new_time = timeobject.strftime('%H:%M')
		email = appt_data['email']
		phone = appt_data['contacts']
		message = appt_data['message']
		#status = appt_data['status']
		mycursor1 = clinic.cursor()
		mycursor1.execute("INSERT INTO Appointments3(appointment_id, patient_name, date,time,email,Contact, Message) VALUES (%s, %s, %s, %s, %s, %s, %s)", (appt_id, name, new_date, new_time, email, phone, message) )
		clinic.commit()

		#return 'success'
		return redirect('/appointments.html')
	return render_template('add-appointment.html')

@app.route('/index.html')
def index1():
	mycursor = clinic.cursor()
	number_rows = mycursor.execute('select * from Patients3')
	all_data = len(mycursor.fetchall())

	mycursor5 = clinic.cursor()
	number_rows_appt = mycursor5.execute('select * from Appointments3')
	all_data_appt =len(mycursor5.fetchall())

	mycursor = clinic.cursor()
	Valdata = mycursor.execute('select * from Appointments3')
	patient_Details3 = mycursor.fetchall()
	#return render_template('/appointments.html',patient_details = patient_Details3)

	mycursor = clinic.cursor()
	resultVal = mycursor.execute('select * from Patients3')
	patientDetails = mycursor.fetchall()


	return render_template('index.html', number_rows = all_data, numberRowsAppt = all_data_appt, patient_details = patient_Details3, patientDetails = patientDetails )

@app.route('/patients.html', methods = ['GET', 'POST'])
def patient():
	mycursor = clinic.cursor()
	resultVal = mycursor.execute('select * from Patients3')
	#global patientDetails
	patientDetails = mycursor.fetchall()
	return render_template('patients.html', patientDetails = patientDetails)

@app.route('/Patient_details.html', methods = ['GET', 'POST'])
def Patient_details():
	mycursor = clinic.cursor()

	resultVal = mycursor.execute('select * from Patients3')
	patient_details1 = mycursor.fetchall()

	return render_template('Patient_details.html', patientdetails1 = patient_details1)


@app.route('/add-patient.html', methods =['GET', 'POST'])
def add_patient():
	if request.method == 'POST':
		user_data  = request.form
		first_name = user_data['first_name'] #0
		last_name = user_data['last_name'] #1
		email = user_data['email']  #2
		age = user_data['age'] #3
		disease = user_data['disease'] #4
		medications = user_data['medications'] #5
		phone = user_data['contacts'] #6
		city = user_data['city'] #7
		#state = user_data['states'] #
		address = user_data['address']  #8
		#firstName VARCHAR(100), lastName VARCHAR(100), email VARCHAR(200), password VARCHAR(50), dateOfbirth DATE, city VARCHAR(100), state VARCHAR(100)
		mycursor.execute("INSERT INTO Patients3(firstName, lastName, email, Age, disease, medications, contacts, city, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, email, age, disease, medications, phone, city, address) )
		#mycursor.execute("INSERT INTO Patient_details1(firstName, lastName, Age, Disease, Medications) VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, age, disease, medications) )
		clinic.commit()
		#mycursor.close()
		#return 'success'
		return redirect('/patients.html')
	else:
		return render_template('add-patient.html')

@app.route('/handle_data')
def handle_data(input):
	for user in patientDetails:
		userid = user[0]
	return userid


def finish():
	mycursor.close()

    #if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else


if __name__ == '__main__':
	app.run(port='5044', debug= True)
	finish()










































