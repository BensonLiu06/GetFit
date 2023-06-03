from tkinter import *
import mysql.connector
from mysql.connector import errorcode
from RegisterUserWindow import *
from PopupBox import *
from CheckUserNameExists import *

# Implementation of app window
def createAppWindow(mainWindow, appWindow, userLoginWindow, dbConnection, dbCursor, username):
    # Hide the user login window
    userLoginWindow.grid_forget()

    # Setup the user registarion window
    appWindow.grid(sticky='nsew')
        
    appWindow.columnconfigure(0, weight = 1)
    appWindow.columnconfigure(1, weight = 1)
    appWindow.rowconfigure(0, weight = 1)
    appWindow.rowconfigure(1, weight = 1)
    appWindow.rowconfigure(2, weight = 1)
    appWindow.rowconfigure(3, weight = 1)
    appWindow.rowconfigure(4, weight = 1)
    appWindow.rowconfigure(5, weight = 1)
    appWindow.rowconfigure(6, weight = 1)
    appWindow.rowconfigure(7, weight = 1)
    appWindow.rowconfigure(8, weight = 1)

    # Create all the main frame containers
    topFrame = Frame(appWindow, width=590, height = 100, padx = 15,pady = 5)
    leftFrame = Frame(appWindow, width = 290, height = 400, padx = 15, pady = 5, relief='groove', borderwidth = 2)
    rightFrame = Frame(appWindow, width = 290, height = 400, padx = 15, pady = 5, relief='groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, sticky = "ew")
    leftFrame.grid(column = 0, row = 1, sticky = "nsew")
    rightFrame.grid(column = 1, row = 1, sticky = "nsew")

    # Create label widget
    label1 = Label(topFrame, text = "Signed in to GetFit", width = 20, anchor = 'center')
    label1.grid(column = 0, row = 0, pady = 5)

    # Create label widget
    label2 = Label(topFrame, text = "Username: " + username, width = 20, anchor = 'center')
    label2.grid(column = 1, row = 0, pady = 5)

    updateProfileButton = Button(leftFrame, text = "Profile & Settings", command = lambda : updateProfileWindow(mainWindow, appWindow, dbConnection, dbCursor, username))
    updateProfileButton.grid(column = 0, row = 1, pady = 5)

    # Create button widget to sign out 
    signoutButton = Button(leftFrame, text = "Sign out", command = lambda : 
                                   signoutOfApp(mainWindow, appWindow, userLoginWindow))
    signoutButton.grid(column = 0, row = 2, pady = 5)

def signoutOfApp(mainWindow, appWindow, userLoginWindow):
    appWindow.grid_forget()

    userLoginWindow.grid(sticky='nsew')
    popupBox(mainWindow, userLoginWindow, "Information", "User was successfully signed out")

def updateProfileWindow(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Create a frame for the Profile & Settings window
    parentWindow.gridforget()

    # Create a frame for the Update Profile window

    updateProfileWindow = Frame(mainWindow)
    updateProfileWindow.grid(sticky='nsew')
    #updateProfileWindow.grid_forget()
    
    # Create label widget
    label1 = Label(updateProfileWindow, text = "Profile & Settings", width = 20, anchor = 'center')
    label1.grid(column = 0, row = 0, columnspan = 2, pady = 5)

    # Create label widget
    label2 = Label(updateProfileWindow, text = "Username: " + username, width = 20, anchor = 'center')
    label2.grid(column = 0, row = 1, columnspan = 2, pady = 5)
