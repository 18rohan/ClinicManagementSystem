import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    passwd = "rohan$198",
    database = 'testdb',
    
)

my_cursor = mydb.cursor()

#CREATING A DATABASE
#my_cursor.execute("CREATE DATABASE testdb")

#SQL COMMAND TO DISPLAY THE DATABASES
#my_cursor.execute("SHOW DATABASES")

#CREATING A TABLE
#my_cursor.execute("CREATE TABLE users (name VARCHAR(200), email VARCHAR(255), age INTEGER(4), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
	print(table[0])

#INSERTING VALUES INTO A TABLE
sqlstuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("Rohan", "rohan@email.com", 23)

my_cursor.execute(sqlstuff, record1)
mydb.commit()


#PRINTING EACH DATABASE
#for db in my_cursor:
#	print(db)

