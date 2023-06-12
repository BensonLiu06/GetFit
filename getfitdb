def accessDatabase(mainWindow, dbHostname, dbUsername, dbPort, dbPassword, dbName):
    # Call the function to check if the database exists
    dbExists = checkDatabaseExists(mainWindow, dbHostname, dbUsername, dbPort, dbPassword, dbName)

    if dbExists:
        pass
    else:
        # Create the GetFit database if it does not exist
        dbConnection = mysql.connector.connect(
            host=dbHostname,
            user=dbUsername,
            port=dbPort,
            password=dbPassword,
        )
        dbCursor = dbConnection.cursor()

        try:
            dbCursor.execute(f"CREATE DATABASE {dbName}")

            dbConnection = mysql.connector.connect(
                host=dbHostname,
                user=dbUsername,
                port=dbPort,
                password=dbPassword,
                database=dbName
            )
            dbCursor = dbConnection.cursor()
            dbCursor.execute("CREATE TABLE User (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), password_hash CHAR(60), security_question VARCHAR(256), security_response VARCHAR(64))")
            dbCursor.execute("CREATE TABLE UserInfo (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), fullname VARCHAR(256), birthdate DATE DEFAULT(CURRENT_DATE), phone_number VARCHAR(50), email VARCHAR(256), gender VARCHAR(10), height DECIMAL(4,1) DEFAULT 0, weight DECIMAL (4,1) DEFAULT 0, image_path VARCHAR(256))")
            dbCursor.execute("CREATE TABLE goals (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), goal1 VARCHAR(256), goal2 VARCHAR(256), goal3 VARCHAR(256))")
            dbConnection.commit()
            dbConnection.close()
        except mysql.connector.Error as error:
            errorMessage = "Error Code: " + str(error.errno) + "\n" + "SQLSTATE: " + error.sqlstate + "\n" + "Message: " + error.msg
            popupBox(mainWindow, mainWindow, "Error", errorMessage)
