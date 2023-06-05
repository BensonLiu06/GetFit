from tkinter import *
import mysql.connector
from mysql.connector import errorcode
from RegisterUserWindow import *
from AppWindow import *
from PopupBox import *
from CheckUserNameExists import *
from PasswordHash import *

# Implementation of login window
def createLoginWindow(mainWindow, userLoginWindow, registrationWindow, appWindow, dbConnection, dbCursor):
    userLoginWindow.grid(sticky='nsew')
    
    userLoginWindow.columnconfigure(0, weight = 1)
    userLoginWindow.columnconfigure(1, weight = 1)
    userLoginWindow.rowconfigure(0, weight = 1)
    userLoginWindow.rowconfigure(1, weight = 1)
    userLoginWindow.rowconfigure(2, weight = 1)
    userLoginWindow.rowconfigure(3, weight = 1)
    userLoginWindow.rowconfigure(4, weight = 1)
    userLoginWindow.rowconfigure(5, weight = 1)
    userLoginWindow.rowconfigure(6, weight = 1)
    userLoginWindow.rowconfigure(7, weight = 1)
    userLoginWindow.rowconfigure(8, weight = 1)

    # Create all the main frame containers
    topFrame = Frame(userLoginWindow, width=590, height = 100, padx = 15,pady = 5)
    leftFrame = Frame(userLoginWindow, width = 290, height = 400, padx = 15, pady = 5, relief='groove', borderwidth = 2)
    rightFrame = Frame(userLoginWindow, width = 290, height = 400, padx = 15, pady = 5, relief='groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, sticky = "ew")
    leftFrame.grid(column = 0, row = 1, sticky = "nsew")
    rightFrame.grid(column = 1, row = 1, sticky = "nsew")

    # Create label widget
    signinLabel = Label(topFrame, text = "Sign in to GetFit", width = 20, anchor = 'center')
    signinLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create label widget
    usernameLabel1 = Label(leftFrame, text = "Username", width = "30", anchor = 'w')
    usernameLabel1.grid(column = 0, row = 1)

    # Create StringVars for text from Entry fields
    username = StringVar()
    password = StringVar()

    # Create entry widget
    usernameField = Entry(leftFrame, textvariable = username, bd = 3, width = 30)
    usernameField.grid(column = 0, row = 2)
    usernameField.anchor = 'w'
    usernameField.focus_force() 

    # Create label widget
    usernameLabel2 = Label(leftFrame, text = "Enter your username", width = "30", anchor = 'w')
    usernameLabel2.grid(column = 0, row = 3)
    
    # Create label widget
    emptyLabel1 = Label(leftFrame,text = "", width = "30", anchor = 'w')
    emptyLabel1.grid(column = 0,row = 4)

    # Create label widget
    passwordLabel = Label(leftFrame,text = "Password", width = "30", anchor = 'w')
    passwordLabel.grid(column = 0, row = 5)

    # Create entry widget
    passwordField = Entry(leftFrame, bd = 3, width = 30, textvariable = password, show = '*')
    passwordField.grid(column = 0, row = 6)

    # Create button widget for forgot your password
    forgotYourPasswordButton = Button(leftFrame, text = "Forgot your password?", command = lambda : 
                                      forgotYourPassword(mainWindow, userLoginWindow, dbConnection, dbCursor))
    forgotYourPasswordButton.grid(column = 0, row = 7)

    # Create label widget
    emptyLabel2 = Label(leftFrame,text = "", width = "30", anchor = 'w')
    emptyLabel2.grid(column = 0, row = 8)

    # Create button widget for sign in
    signinButton = Button(leftFrame, text = "Sign in", command = lambda : 
                          verifyLogin(mainWindow, userLoginWindow, appWindow, dbConnection, dbCursor, username.get(), password.get(), usernameField, passwordField))
    signinButton.grid(column = 0, row = 9)
    
    # Create button widget to register a new user
    registerNewUserButton = Button(rightFrame, text = "Register a new user", command = lambda : 
                                   registerUserWindow(mainWindow, registrationWindow, userLoginWindow, dbConnection, dbCursor))
    registerNewUserButton.grid(column = 1, row = 8)

# Implementation for forgot your password button event
def forgotYourPassword(mainWindow, parentWindow, dbConnection, dbCursor):
    # Create StringVars to hold the user input
    username = StringVar()

    # Create a toplevel window for the Forgot Your Password dialog box
    forgotYourPasswordWindow = Toplevel(parentWindow)
    forgotYourPasswordWindow.title("Forgot your password")

    # Create an information label
    informationLabel = Label(forgotYourPasswordWindow, text = "Please enter details below to reset your password", padx = 3, pady = 3)
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create an empty label for padding
    emptyLabel1 = Label(forgotYourPasswordWindow, text = "")
    emptyLabel1.grid(column = 0, row = 1, columnspan = 2)

    # Create a label widget for Username
    usernameLabel = Label(forgotYourPasswordWindow, text = "Username")
    usernameLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create an entry widget for Username
    usernameField = Entry(forgotYourPasswordWindow, textvariable = username)
    usernameField.grid(column = 0, row = 3, columnspan = 2)

    # Create an empty label for padding
    emptyLabel2 = Label(forgotYourPasswordWindow, text = "")
    emptyLabel2.grid(column = 0, row = 4, columnspan = 2)

    # Create button widget for OK
    oKButton = Button(forgotYourPasswordWindow, text = "OK", width=10, height=1, command = lambda : verifyUserResetPassword(mainWindow, parentWindow, forgotYourPasswordWindow, dbConnection, dbCursor, usernameField.get()))
    oKButton.grid(column = 0, row = 5)

    # Create button widget for Cancel
    cancelButton = Button(forgotYourPasswordWindow, text = "Cancel", width = 10, height=1, bg="blue", command = lambda : forgotYourPasswordWindow.destroy())
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
    
# Implementation for login button event
def verifyLogin(mainWindow, parentWindow, appWindow, dbConnection, dbCursor, username, password, usernameLoginField, passwordLoginField):
    usernameLoginField.delete(0, END)
    passwordLoginField.delete(0, END)

    if checkUserNameExists(username, dbCursor):
        #selectStatement = """SELECT * FROM User WHERE username = %s AND password = %s"""
        #vals = (username, password)

        selectStatement = """SELECT * FROM User WHERE username = %s"""
        vals = (username,)
        dbCursor.execute(selectStatement, vals)

        user = dbCursor.fetchone()
        passwordHash = user[2]

        if (comparePassword(password,passwordHash)):
            parentWindow.grid_forget()
            appWindow.grid(sticky='nsew')
            createAppWindow(mainWindow, appWindow, parentWindow, dbConnection, dbCursor, username)
            popupBox(mainWindow, appWindow,"Information", "User login was successful")
        else:
            popupBox(mainWindow, parentWindow, "Error", "Password was invalid")
    else:
        popupBox(mainWindow, parentWindow, "Error", "Username was not found")

        # Create a funciton to reset the users password

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


def askSecurityQuestion(mainWindow, parentWindow, dbConnection, dbCursor, username, securityQuestion, securityResponse):
    # Create StringVars to hold the user input
    inputSecurityResponse = StringVar()

    # Create a toplevel window for the Security Question dialog box
    askSecurityQuestionWindow = Toplevel(parentWindow)
    askSecurityQuestionWindow.title("Security Question")

    # Create an information label widget
    informationLabel = Label(askSecurityQuestionWindow, text = "Please enter details below to reset your password", padx = 3, pady = 3)
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create an empty label widget for padding
    emptyLabel1 = Label(askSecurityQuestionWindow, text = "")
    emptyLabel1.grid(column = 0, row = 1, columnspan = 2)

    # Create a label widget to display the Security Question
    securityQuestionLabel = Label(askSecurityQuestionWindow, text = securityQuestion)
    securityQuestionLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create an entry field widget to obtain the user's response to the Security Question
    securityResponseField = Entry(askSecurityQuestionWindow, textvariable = inputSecurityResponse)
    securityResponseField.grid(column = 0, row = 3, columnspan = 2)

    # Create a label widget to prompt the user for response
    securityReponselabel = Label(askSecurityQuestionWindow, text = "Enter your response")
    securityReponselabel.grid(column = 0, row = 4, columnspan = 2)

    # Create an empty label widget for padding
    emptyLabel2 = Label(askSecurityQuestionWindow, text = "")
    emptyLabel2.grid(column = 0, row = 5, columnspan = 2)

    # Create an OK button widget
    okButton = Button(askSecurityQuestionWindow, text = "OK", width=10, height=1, command = lambda : 
           verifySecurityResponse(mainWindow, parentWindow, askSecurityQuestionWindow, dbConnection, dbCursor, username, securityResponse, inputSecurityResponse.get()))
    okButton.grid(column = 0, row = 6)

    # Create button widget for Cancel
    cancelButton = Button(askSecurityQuestionWindow, text = "Cancel", width = 10, height=1, bg="blue", command = lambda : askSecurityQuestionWindow.destroy())
    cancelButton.grid(column = 1, row = 6)


def askSecurityQuestion(mainWindow, parentWindow, dbConnection, dbCursor, username, securityQuestion, securityResponse):
    # Create StringVars to hold the user input
    inputSecurityResponse = StringVar()

    # Create a toplevel window for the Security Question dialog box
    askSecurityQuestionWindow = Toplevel(parentWindow)
    askSecurityQuestionWindow.title("Security Question")

    # Create an information label widget
    informationLabel = Label(askSecurityQuestionWindow, text = "Please enter details below to reset your password", padx = 3, pady = 3)
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create an empty label widget for padding
    emptyLabel1 = Label(askSecurityQuestionWindow, text = "")
    emptyLabel1.grid(column = 0, row = 1, columnspan = 2)

    # Create a label widget to display the Security Question
    securityQuestionLabel = Label(askSecurityQuestionWindow, text = securityQuestion)
    securityQuestionLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create an entry field widget to obtain the user's response to the Security Question
    securityResponseField = Entry(askSecurityQuestionWindow, textvariable = inputSecurityResponse)
    securityResponseField.grid(column = 0, row = 3, columnspan = 2)

    # Create a label widget to prompt the user for response
    securityReponselabel = Label(askSecurityQuestionWindow, text = "Enter your response")
    securityReponselabel.grid(column = 0, row = 4, columnspan = 2)

    # Create an empty label widget for padding
    emptyLabel2 = Label(askSecurityQuestionWindow, text = "")
    emptyLabel2.grid(column = 0, row = 5, columnspan = 2)

    # Create an OK button widget
    okButton = Button(askSecurityQuestionWindow, text = "OK", width=10, height=1, command = lambda : 
           verifySecurityResponse(mainWindow, parentWindow, askSecurityQuestionWindow, dbConnection, dbCursor, username, securityResponse, inputSecurityResponse.get()))
    okButton.grid(column = 0, row = 6)

    # Create button widget for Cancel
    cancelButton = Button(askSecurityQuestionWindow, text = "Cancel", width = 10, height=1, bg="blue", command = lambda : askSecurityQuestionWindow.destroy())
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

def verifySecurityResponse(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username, securityResponse, inputSecurityResponse):
    if inputSecurityResponse == securityResponse:
        resetPassword(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username)
    else:
        popupBox(mainWindow, parentWindow, "Error", "Your security response was invalid")

def resetPassword(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username):
    callingWindow.destroy()

    # Create StringVars to hold the user input
    password = StringVar()
    confirmPassword = StringVar()

    # Create a toplevel window for the Reset Password dialog box
    resetPasswordWindow = Toplevel(parentWindow)
    resetPasswordWindow.title("Reset Password")

    # Create an information label widget
    informationLabel = Label(resetPasswordWindow, text = "Please enter details below to reset your password", padx = 3, pady = 3)
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create an empty label widget for padding
    emptyLabel1 = Label(resetPasswordWindow, text = "")
    emptyLabel1.grid(column = 0, row = 1, columnspan = 2)

    # Create label widget for Password
    userLabel = Label(resetPasswordWindow, text = "Resetting password for " + username, width = "30", anchor = 'w')
    userLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create label widget for Password
    passwordLabel = Label(resetPasswordWindow, text = "Password", width = "30", anchor = 'w')
    passwordLabel.grid(column = 0, row = 3, columnspan = 2)

    # Create entry widget for Password
    passwordField = Entry(resetPasswordWindow, bd = 3, width = 30, textvariable = password, show = '*')
    passwordField.grid(column = 0, row = 4, columnspan = 2)

    # Create label widget for Confirm Password
    confirmPasswordLabel = Label(resetPasswordWindow, text = "Confirm password", width = "30", anchor = 'w')
    confirmPasswordLabel.grid(column = 0, row = 5, columnspan = 2)

    # Create entry widget for Confirm Password
    confirmPasswordField = Entry(resetPasswordWindow, bd = 3, width = 30, textvariable = confirmPassword, show = '*')
    confirmPasswordField.grid(column = 0, row = 6, columnspan = 2)

    # Create button widget for OK
    oKButton = Button(resetPasswordWindow, text = "OK", width=10, height=1, command = lambda : verifyAndResetPassword(mainWindow, parentWindow, resetPasswordWindow, dbConnection, dbCursor, username, passwordField.get(), confirmPasswordField.get()))
    oKButton.grid(column = 0, row = 7)

    # Create button widget for Cancel
    cancelButton = Button(resetPasswordWindow, text = "Cancel", width = 10, height=1, bg="blue", command = lambda : resetPasswordWindow.destroy())
    cancelButton.grid(column = 1, row = 7)
    
    # Force an update on the mainWindow so the size of the widgets are known
    mainWindow.update()

    # Get width an height of the popup diagog box so we can resize it
    # to fit the contents of the label and button
    w = resetPasswordWindow.winfo_reqwidth()
    h = resetPasswordWindow.winfo_reqheight()

    # Calculate the geometry to center the dialog box on the screen
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    resetPasswordWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    resetPasswordWindow.grab_set()

def verifyAndResetPassword(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username, password, confirmPassword):

    if password == confirmPassword:
        callingWindow.destroy()
        passwordHash = createPasswordHash(password)

        
        updateStatement = """UPDATE User SET password_hash = %s WHERE username = %s"""
        vals = (passwordHash, username)
        dbCursor.execute(updateStatement, vals)
        dbConnection.commit()
        #
        popupBox(mainWindow, parentWindow, "Information", "Password was successfully reset")
    else:
        popupBox(mainWindow, callingWindow, "Error", "Passwords do not match")
