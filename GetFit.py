from tkinter import *
#from tkinter import ttk
import mysql.connector
from mysql.connector import errorcode
from GetFitDB import *
from LoginWindow import *
from RegisterUserWindow import *
from AppWindow import *
from PopupBox import *
from CheckUsernameExists import *
from PasswordHash import *

# Implementation of the main window
def mainAppWindow():
    #global mainWindow
    # Create an instance of tkinter frame or window
    mainWindow = Tk()

    # Set the width and height of the main window
    w = 800 # Width 
    h = 600 # Height
 
    # Determine the size of the screen
    screen_width =  mainWindow.winfo_screenwidth()  # Width of the screen
    screen_height = mainWindow.winfo_screenheight() # Height of the screen
 
    # Calculate starting x and y coordinates to center the main window on the screen
    x = (screen_width / 2) - (w / 2)
    y = (screen_height / 2) - (h / 2)
 
    mainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    mainWindow.title("GetFit")

    mainWindow.columnconfigure(0, weight = 1)
    mainWindow.rowconfigure(0, weight = 1)

    # Setup parameters to access the mySQL server
    dbHostname = "localhost"
    dbUsername = "root"
    dbPort = "3306"
    dbPassword = ""
    dbName = "GetFitDB"

    # Connect to the GetFit database
    accessDatabase(mainWindow, dbHostname, dbUsername, dbPort, dbPassword, dbName)
    
    try:
        # Connect to the GetFit database
        dbConnection = mysql.connector.connect(
            host = dbHostname,
            user = dbUsername,
            port = dbPort,
            password = dbPassword,
            database = dbName
        )
        dbCursor = dbConnection.cursor()

        # Show the Login window
        createLoginWindow(mainWindow, dbConnection, dbCursor)
    except mysql.connector.Error as error:
        errorMessage = "Error Code: " + str(error.errno) + "\n" + "SQLSTATE: " + error.sqlstate + "\n" + "Message: " + error.msg  
        popupBox(mainWindow, mainWindow, "Error", errorMessage)

    mainWindow.mainloop()

mainAppWindow()
