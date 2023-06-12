import mysql.connector
from mysql.connector import errorcode
from PopupBox import *

# Create a function to check if the username already exists
def checkUsernameExists(mainWindow, callingWindow, dbConnection, dbCursor, username):
    try:
        # Check to see if the username already exists
        selectQuery = """SELECT * FROM User WHERE username = %s"""
        vals = (username,)

        # Execute the SQL SELECT statement
        dbCursor.execute(selectQuery, vals)

        # Fetch the results of the query
        user = dbCursor.fetchone()
        if user is not None:
            # If a record exists return True, username found
            return True
        else:
            # Else return False, username not found
            return False 
    except mysql.connector.Error as error:
        # Format the database error message for displaying in the popup box
        errorMessage = "Error Code: " + str(error.errno) + "\n" + "SQLSTATE: " + error.sqlstate + "\n" + "Message: " + error.msg  
        popupBox(mainWindow, mainWindow, "Error", errorMessage)
