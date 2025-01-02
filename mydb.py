# Install Mysql on computer
# https://dev.mysql.com/down/installer
# pip install mysql
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Kji3ll#12345',

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE wish")

print("All Done!")
