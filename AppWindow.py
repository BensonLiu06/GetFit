from tkinter import *
from tkinter import ttk
#import mysql.connector
#from mysql.connector import errorcode
from RegisterUserWindow import *
from UpdateProfileWindow import *
from SetGoals import *
from TrackActivity import *
from TrackProgress import *
from PopupBox import *

# Implementation of the app window
def createAppWindow(mainWindow, callingWindow, dbConnection, dbCursor, username):

    # Hide the User Login window
    callingWindow.grid_forget()

    # Create a frame for the main App window
    appWindow = ttk.Frame(mainWindow, padding=(3,3,12,12))
    appWindow.grid(sticky=N+S+E+W)

    # Setup the main App window
    appWindow.columnconfigure(0, weight = 1)
    appWindow.columnconfigure(1, weight = 1)
    #appWindow.rowconfigure(0, weight = 1)
    appWindow.rowconfigure(1, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(appWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(appWindow, width = 300, height = 700, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(appWindow, width = 300, height = 50, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 5, padx = 5, pady = 5, sticky=(N, S, E, W))
    buttonFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(0, weight = 1)
    bottomFrame.rowconfigure(1, weight = 1)
    bottomFrame.rowconfigure(2, weight = 1)
    bottomFrame.rowconfigure(3, weight = 1)
    bottomFrame.rowconfigure(4, weight = 1)
    buttonFrame.rowconfigure(5, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(appWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(appWindow, width = 600, height = 650, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(appWindow, width = 600, height = 100, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 9, padx = 5, pady = 5, sticky=(N, S, E, W))
    buttonFrame.grid(column = 0, row = 5, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))

    # Create label widget for information message
    label1 =ttk.Label(topFrame, text = "Signed in to GetFit", width = 20, anchor = 'center')
    label1.grid(column = 0, row = 0, pady = 5)

    # Create label widget for Username
    label2 =ttk.Label(topFrame, text = "Username: " + username, width = 20, anchor = 'center')
    label2.grid(column = 1, row = 0, pady = 5)

    # Create button widget for Profile & Settings
    updateProfileButton = ttk.Button(bottomFrame, text = "Profile & Settings", command = lambda : createUpdateProfileAndSettingsWindow(mainWindow, appWindow, dbConnection, dbCursor, username))
    updateProfileButton.grid(column = 0, row = 1, pady = 5)

    # Create button widget for Set Goals
    setGoalsButton = ttk.Button(bottomFrame, text = "Set Goals", command = lambda : createSetGoalsWindow(mainWindow, appWindow, dbConnection, dbCursor, username))
    setGoalsButton.grid(column = 0, row = 2, pady = 5)

    # Create button widget for Track Activity
    trackActivityButton = ttk.Button(bottomFrame, text = "Track Activity", command = lambda : createTrackActivityWindow(mainWindow, appWindow, dbConnection, dbCursor, username))
    trackActivityButton.grid(column = 0, row = 3, pady = 5)

    # Create button widget for Track Progress
    trackProgressButton = ttk.Button(bottomFrame, text = "Track Progress", command = lambda : createTrackProgressWindow(mainWindow, appWindow, dbConnection, dbCursor, username))
    trackProgressButton.grid(column = 0, row = 4, pady = 5)

    # Create button widget for Sign out 
    signoutButton = ttk.Button(buttonFrame, text = "Sign out", command = lambda : 
                                   signoutOfApp(mainWindow, callingWindow, appWindow))
    signoutButton.grid(column = 1, row = 5, pady = 5)

    popupBox(mainWindow, appWindow,"Information", "User login was successful")

# Implementation of Sign out button event
def signoutOfApp(mainWindow, callingWindow, appWindow):
    # Hide the App window
    appWindow.grid_forget()

    # Show the User Login window
    callingWindow.grid(sticky = (N, S, E, W))
    popupBox(mainWindow, callingWindow, "Information", "User was successfully signed out")
