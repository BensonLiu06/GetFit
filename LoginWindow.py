from tkinter import *
from tkinter import ttk
import re
from RegisterUserWindow import *
from AppWindow import *
from PopupBox import *
from CheckUserNameExists import *
from ResetPassword import *
from PasswordHash import *

# Implementation of the User Login window
def createLoginWindow(mainWindow, dbConnection, dbCursor):
    # Create StringVars for text from Entry fields
    username = StringVar()
    password = StringVar()

    # Create a frame for the User Login window
    userLoginWindow = ttk.Frame(mainWindow, padding=(3,3,12,12))
    userLoginWindow.grid(sticky = (N, S, E, W))

    # Setup the main User Login window
    userLoginWindow.columnconfigure(0, weight = 1)
    userLoginWindow.columnconfigure(1, weight = 1)
    #userLoginWindow.rowconfigure(0, weight = 1)
    #userLoginWindow.rowconfigure(1, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(userLoginWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    leftFrame = ttk.Frame(userLoginWindow, width = 300, height = 550, relief = 'groove', borderwidth = 2)
    rightFrame = ttk.Frame(userLoginWindow, width = 300, height = 550, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    leftFrame.grid(column = 0, row = 1, rowspan = 9, padx = 5, pady = 5, sticky=(N, S, E, W))
    rightFrame.grid(column = 1, row = 1, rowspan = 9, padx = 5, pady = 5, sticky=(N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(0, weight = 1)
    leftFrame.columnconfigure(0, weight = 1)
    rightFrame.columnconfigure(1, weight = 1)
    topFrame.rowconfigure(0, weight = 0)
    leftFrame.rowconfigure(1, weight = 1)
    leftFrame.rowconfigure(2, weight = 1)
    leftFrame.rowconfigure(3, weight = 1)
    leftFrame.rowconfigure(4, weight = 1)
    leftFrame.rowconfigure(5, weight = 1)
    leftFrame.rowconfigure(6, weight = 1)
    leftFrame.rowconfigure(7, weight = 1)
    leftFrame.rowconfigure(8, weight = 1)
    leftFrame.rowconfigure(9, weight = 1)
    rightFrame.rowconfigure(1, weight = 1)
    rightFrame.rowconfigure(2, weight = 1)
    rightFrame.rowconfigure(3, weight = 1)
    rightFrame.rowconfigure(4, weight = 1)
    rightFrame.rowconfigure(5, weight = 1)
    rightFrame.rowconfigure(6, weight = 1)
    rightFrame.rowconfigure(7, weight = 1)
    rightFrame.rowconfigure(8, weight = 1)
    rightFrame.rowconfigure(9, weight = 1)

    # Create label widget for Sign In window
    signinLabel = ttk.Label(topFrame, text = "Sign in to GetFit", anchor = W)
    signinLabel.grid(column = 0, row = 0, columnspan = 2, sticky = (N, W))

    # Create label widget for Username
    usernameLabel1 = ttk.Label(leftFrame, text = "Username", anchor = W)
    usernameLabel1.grid(column = 0, row = 1, sticky = (N, W))

    # Create entry widget for Username
    usernameField = ttk.Entry(leftFrame, textvariable = username)
    usernameField.grid(column = 0, row = 2, sticky = (N, W))
    usernameField.anchor = 'w'
    usernameField.focus_force() 

    # Create label widget for Username hint
    usernameLabel2 = ttk.Label(leftFrame, text = "Enter your username", anchor = 'w')
    usernameLabel2.grid(column = 0, row = 3, sticky = (N, W))
    
    # Create label widget
    emptyLabel1 = ttk.Label(leftFrame,text = "", anchor = 'w')
    emptyLabel1.grid(column = 0, row = 4, sticky = (N, W))

    # Create label widget for Password
    passwordLabel = ttk.Label(leftFrame,text = "Password", anchor = 'w')
    passwordLabel.grid(column = 0, row = 5, sticky = (N, W))

    # Create entry widget for Password
    passwordField = ttk.Entry(leftFrame, textvariable = password, show = '*')
    passwordField.grid(column = 0, row = 6, sticky = (N, W))

    # Create label widget for Password hint
    passwordLabel = ttk.Label(leftFrame,text = "Enter your password", anchor = 'w')
    passwordLabel.grid(column = 0, row = 7, sticky = (N, W))

    # Create empty label widget for padding
    emptyLabel2 = ttk.Label(leftFrame,text = "", anchor = 'w')
    emptyLabel2.grid(column = 0, row = 8, sticky = (N, W))

    # Create button widget for sign in
    signinButton = ttk.Button(leftFrame, text = "Sign in", command = lambda : 
                          verifyLogin(mainWindow, userLoginWindow, dbConnection, dbCursor, username.get(), password.get(), usernameField, passwordField))
    signinButton.grid(column = 0, row = 9)

    # Create button widget for forgot your password
    forgotYourPasswordButton = ttk.Button(rightFrame, text = "Forgot your password?", command = lambda : 
                                      forgotYourPassword(mainWindow, userLoginWindow, dbConnection, dbCursor))
    forgotYourPasswordButton.grid(column = 1, row = 5)
    
    # Create button widget to register a new user
    registerNewUserButton = ttk.Button(rightFrame, text = "Register a new user", command = lambda : 
                                   createRegisterUserWindow(mainWindow, userLoginWindow, dbConnection, dbCursor))
    registerNewUserButton.grid(column = 1, row = 7)

    # Create button widget to Exit the application
    exitButton = ttk.Button(rightFrame, text = "Exit", command = lambda : 
                                    exitApp(mainWindow, dbConnection))
    exitButton.grid(column = 1, row = 9)

# Implementation for the Forgot your password button event
# Obtains the username for which the password is to be reset
def forgotYourPassword(mainWindow, parentWindow, dbConnection, dbCursor):
    # Create StringVars to hold the user input
    username = StringVar()

    # Create a toplevel window for the Forgot Your Password dialog box
    forgotYourPasswordWindow = Toplevel(parentWindow)
    forgotYourPasswordWindow.title("Forgot your password")

    # Create an information label
    informationLabel =ttk.Label(forgotYourPasswordWindow, text = "Please enter details below to reset your password")
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create an empty label for padding
    emptyLabel1 =ttk.Label(forgotYourPasswordWindow, text = "")
    emptyLabel1.grid(column = 0, row = 1, columnspan = 2)

    # Create a label widget for Username
    usernameLabel =ttk.Label(forgotYourPasswordWindow, text = "Username")
    usernameLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create an entry widget for Username
    usernameField = ttk.Entry(forgotYourPasswordWindow, textvariable = username)
    usernameField.grid(column = 0, row = 3, columnspan = 2)

    # Create an empty label for padding
    emptyLabel2 =ttk.Label(forgotYourPasswordWindow, text = "")
    emptyLabel2.grid(column = 0, row = 4, columnspan = 2)

    # Create button widget for OK
    oKButton = ttk.Button(forgotYourPasswordWindow, text = "OK", width = 10, command = lambda : verifyUserResetPassword(mainWindow, parentWindow, forgotYourPasswordWindow, dbConnection, dbCursor, usernameField.get()))
    oKButton.grid(column = 0, row = 5)

    # Create button widget for Cancel
    cancelButton = ttk.Button(forgotYourPasswordWindow, text = "Cancel", width = 10, command = lambda : forgotYourPasswordWindow.destroy())
    cancelButton.grid(column = 1, row = 5)
    
    # Force an update on the mainWindow so the size of the widgets are known
    mainWindow.update()

    # Get width an height of the popup diagog box so we can resize it
    # to fit the contents of the label and button
    w = forgotYourPasswordWindow.winfo_reqwidth()
    h = forgotYourPasswordWindow.winfo_reqheight()

    # Calculate the geometry to center the dialog box on the screen
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    forgotYourPasswordWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    forgotYourPasswordWindow.grab_set()
    
# Implementation for the Sign in button event
# Check that the provided user name exists and that the provided password matches
# the password for that username. If it matches, open the main app window
def verifyLogin(mainWindow, parentWindow, dbConnection, dbCursor, username, password, usernameLoginField, passwordLoginField):
    usernameLoginField.delete(0, END)
    passwordLoginField.delete(0, END)

    if checkUserNameExists(username, dbCursor):
        selectStatement = """SELECT * FROM User WHERE username = %s"""
        vals = (username,)
        dbCursor.execute(selectStatement, vals)

        user = dbCursor.fetchone()
        passwordHash = user[2]

        if (comparePassword(password,passwordHash)):
            createAppWindow(mainWindow, parentWindow, dbConnection, dbCursor, username)
        else:
            popupBox(mainWindow, parentWindow, "Error", "Password was invalid")
    else:
        popupBox(mainWindow, parentWindow, "Error", "Username was not found")

# Implementation of the OK button event for the Forgot Your Password window
# Create a function to check that the provided username exists and obtain the
# security question and response for that user's username
def verifyUserResetPassword(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username):
    # Check the GetFit database to ensure the Username exists
    if checkUserNameExists(username, dbCursor):
        selectQuery = """SELECT security_question, security_response FROM User WHERE username = %s"""

        vals = (username,)
        dbCursor.execute(selectQuery, vals)
        result = dbCursor.fetchone()

        # Parse the results of the database query
        # Field 1 = Security Question
        # Field 2 = Security Response
        securityQuestion = result[0]
        securityResponse = result[1]

        callingWindow.destroy()
        askSecurityQuestion(mainWindow, parentWindow, dbConnection, dbCursor, username, securityQuestion, securityResponse)
    else:
        popupBox(mainWindow, parentWindow, "Error", "Username was not found")

# Create a function that obtains the user's response to the security question
def askSecurityQuestion(mainWindow, parentWindow, dbConnection, dbCursor, username, securityQuestion, securityResponse):
    # Create StringVars to hold the user input
    inputSecurityResponse = StringVar()

    # Create a toplevel window for the Security Question dialog box
    askSecurityQuestionWindow = Toplevel(parentWindow)
    askSecurityQuestionWindow.title("Security Question")

    # Create an information label widget
    informationLabel =ttk.Label(askSecurityQuestionWindow, text = "Please enter details below to reset your password")
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create an empty label widget for padding
    emptyLabel1 =ttk.Label(askSecurityQuestionWindow, text = "")
    emptyLabel1.grid(column = 0, row = 1, columnspan = 2)

    # Create a label widget to display the Security Question
    securityQuestionLabel =ttk.Label(askSecurityQuestionWindow, text = securityQuestion)
    securityQuestionLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create an entry field widget to obtain the user's response to the Security Question
    securityResponseField = ttk.Entry(askSecurityQuestionWindow, textvariable = inputSecurityResponse)
    securityResponseField.grid(column = 0, row = 3, columnspan = 2)

    # Create a label widget to prompt the user for response
    securityReponselabel =ttk.Label(askSecurityQuestionWindow, text = "Enter your response")
    securityReponselabel.grid(column = 0, row = 4, columnspan = 2)

    # Create an empty label widget for padding
    emptyLabel2 =ttk.Label(askSecurityQuestionWindow, text = "")
    emptyLabel2.grid(column = 0, row = 5, columnspan = 2)

    # Create an OK button widget
    okButton = ttk.Button(askSecurityQuestionWindow, text = "OK", width=10, command = lambda : 
           verifySecurityResponse(mainWindow, parentWindow, askSecurityQuestionWindow, dbConnection, dbCursor, username, securityResponse, inputSecurityResponse.get()))
    okButton.grid(column = 0, row = 6)

    # Create button widget for Cancel
    cancelButton = ttk.Button(askSecurityQuestionWindow, text = "Cancel", width = 10, command = lambda : askSecurityQuestionWindow.destroy())
    cancelButton.grid(column = 1, row = 6)

    # Force an update on the mainWindow so the size of the widgets are known
    mainWindow.update()

    # Get width an height of the popup diagog box so we can resize it
    # to fit the contents of the label and button
    w = askSecurityQuestionWindow.winfo_reqwidth()
    h = askSecurityQuestionWindow.winfo_reqheight()

    # Calculate the geometry to center the dialog box on the screen
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    askSecurityQuestionWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    askSecurityQuestionWindow.grab_set()

# Implementation of the OK button event for the Ask Security Question window
# Create a function to verify that the response to the security question matches
# before resetting the user's password
def verifySecurityResponse(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username, securityResponse, inputSecurityResponse):
    if inputSecurityResponse == securityResponse:
        callingWindow.destroy()

        resetPassword(mainWindow, parentWindow, dbConnection, dbCursor, username)
    else:
        popupBox(mainWindow, parentWindow, "Error", "Your security response was invalid")

# Implementation of the Exit button event for the User Login window
# Create a function to exit the GetFit application
def exitApp(mainWindow, dbConnection):
    # Close the connection to the GetFit database
    dbConnection.close()

    # Close the main window
    mainWindow.quit()
