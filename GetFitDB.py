from tkinter import *
import mysql.connector
from mysql.connector import errorcode
from PopupBox import *

def accessDatabase(mainWindow, dbHostname, dbUsername, dbPort, dbPassword, dbName):
    # connect() creates a connection to the mysql server an returns a mysql connection object
    # cursor() is a python object that enable you to work with the database
    # execute() is a method we can use to execute SQL queries associated with the cursor object
    #
    
    # Call the function to check if the database exists
    dbExists = checkDatabaseExists(mainWindow, dbHostname, dbUsername, dbPort, dbPassword, dbName)

    if dbExists:
        pass
    else:
        # Create the GetFit database if it does not exist
        
        # Connect to the mysql database server
        dbConnection = mysql.connector.connect(
            host = dbHostname,
            user = dbUsername,
            port = dbPort,
            password = dbPassword,
        )
        # Get a cursor to the database
        dbCursor = dbConnection.cursor()

        try:
            # Create the GetFit databse
            dbCursor.execute(f"CREATE DATABASE {dbName}")

            # Connect to the GetFit database
            dbConnection = mysql.connector.connect(
                host = dbHostname,
                user = dbUsername,
                port = dbPort,
                password = dbPassword,
                database = dbName
            )
            # Get a cursor to the GetFit database
            dbCursor = dbConnection.cursor()

            # Create the User table in the GetFit database
            dbCursor.execute("CREATE TABLE User (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), password_hash CHAR(60), security_question VARCHAR(256), security_response VARCHAR(64))")
            
            # Create the UserInfo table in the GetFit database
            dbCursor.execute("CREATE TABLE UserInfo (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), fullname VARCHAR(256), birthdate DATE DEFAULT(CURRENT_DATE), phone_number VARCHAR(50), email VARCHAR(256), gender VARCHAR(10), height DECIMAL(4,1) DEFAULT 0, weight DECIMAL (4,1) DEFAULT 0, image_path VARCHAR(256))")
            
            # Create the Goals table
            dbCursor.execute("CREATE TABLE Goal (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), goal VARCHAR(256))")

            # Commit the changes
            dbConnection.commit()

            # Close the connection to the GetFit database
            dbConnection.close()
        except mysql.connector.Error as error:
            # Format the database error message for displaying in the popup box
            errorMessage = "Error Code: " + str(error.errno) + "\n" + "SQLSTATE: " + error.sqlstate + "\n" + "Message: " + error.msg  
            popupBox(mainWindow, mainWindow, "Error", errorMessage)

def checkDatabaseExists(mainWindow, dbHostname, dbUsername, dbPort, dbPassword, dbName):
    try:
        # If the GetFit database does not exist return True
        dbConnection = mysql.connector.connect(
            host = dbHostname,
            user = dbUsername,
            port = dbPort,
            password = dbPassword,
            database = dbName
        )
        # Close the connection to the GetFit database
        dbConnection.close()
        return True
    except mysql.connector.Error as error:
        # If the GetFit database does not exist return False
        if error.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            return False
        else:
            # Format the error message for displaying in the popup box
            errorMessage = "Error Code: " + str(error.errno) + "\n" + "SQLSTATE: " + error.sqlstate + "\n" + "Message: " + error.msg
            popupBox(mainWindow, mainWindow, "Error", errorMessage)
            raise
