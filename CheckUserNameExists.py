# Create a function to check if the username already exists
def checkUserNameExists(username, dbCursor):
    selectQuery = """SELECT * FROM Users WHERE username = %s"""
    vals = (username,)
    dbCursor.execute(selectQuery, vals)

    user = dbCursor.fetchone()
    if user is not None:
        return True
    else:
        return False
