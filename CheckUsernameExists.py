import mysql.connector
from mysql.connector import errorcode
from PopupBox import *

# Create a function to check if the username already exists
def checkUsernameExists(username, dbCursor):
    selectQuery = """SELECT * FROM User WHERE username = %s"""
    vals = (username,)
    dbCursor.execute(selectQuery, vals)

    user = dbCursor.fetchone()
    if user is not None:
        return True
    else:
        return False
