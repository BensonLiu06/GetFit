from tkinter import *
#from tkinter import ttk
#from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
from PopupBox import *
from CheckUserNameExists import *

# Implementation for user registration window
def registerUserWindow(mainWindow, userRegistrationWindow, userLoginWindow, dbConnection, dbCursor):
    # Create StringVars to hold the user input
    username = StringVar()
    password = StringVar()
    confirmPassword = StringVar()
    securityQuestion = StringVar()
    securityResponse = StringVar()
    
    # Hide the user login window
    userLoginWindow.grid_forget()

    # Setup the user registarion window
    userRegistrationWindow.grid(sticky='nsew')

    userRegistrationWindow.columnconfigure(0, weight = 1)
    userRegistrationWindow.columnconfigure(1, weight = 1)
    userRegistrationWindow.rowconfigure(0, weight = 1)
    userRegistrationWindow.rowconfigure(1, weight = 1)
    userRegistrationWindow.rowconfigure(2, weight = 1)
    userRegistrationWindow.rowconfigure(3, weight = 1)
    userRegistrationWindow.rowconfigure(4, weight = 1)
    userRegistrationWindow.rowconfigure(5, weight = 1)
    userRegistrationWindow.rowconfigure(6, weight = 1)
    userRegistrationWindow.rowconfigure(7, weight = 1)
    userRegistrationWindow.rowconfigure(8, weight = 1)
    userRegistrationWindow.rowconfigure(9, weight = 1)
    userRegistrationWindow.rowconfigure(10, weight = 1)
    userRegistrationWindow.rowconfigure(11, weight = 1)
    userRegistrationWindow.rowconfigure(12, weight = 1)
    userRegistrationWindow.rowconfigure(13, weight = 1)

    # Create all the main frame containers
    topFrame = Frame(userRegistrationWindow, width=590, height = 100, padx = 15, pady = 5)
    leftFrame = Frame(userRegistrationWindow, width = 290, height = 400, padx = 15, pady = 5, relief='groove', borderwidth = 2)
    rightFrame = Frame(userRegistrationWindow, width = 290, height = 400, padx = 15, pady =5)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, sticky = "ew")
    leftFrame.grid(column = 0, row = 3, sticky = "ew")
    rightFrame.grid(column = 1, row = 3, sticky = "ew")

    # Create an information label 
    informationLabel = Label(topFrame, text = "To register for a GetFit profile, please enter details below")
    informationLabel.grid(column = 0, row = 0, columnspan = 2)
    emptyLabel = Label(topFrame, text = "")
    emptyLabel.grid(column = 0, row = 1, columnspan = 2)

    # Create label widget for Username
    usernameLabel = Label(leftFrame, text = "Username", width = "30", anchor = 'w')
    usernameLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create entry widget for Username
    usernameField = Entry(leftFrame, bd = 3, width = 30,textvariable = username)
    usernameField.grid(column = 0, row = 3, columnspan = 2)
    
    # Set focus on Username field
    usernameField.focus_force() 

    # Create label widget for Password
    passwordLabel = Label(leftFrame, text = "Password", width = "30", anchor = 'w')
    passwordLabel.grid(column = 0, row = 4, columnspan = 2)

    # Create entry widget for Password
    passwordField = Entry(leftFrame, bd = 3, width = 30, textvariable = password, show = '*')
    passwordField.grid(column = 0, row = 5, columnspan = 2)

    # Create label widget for Confirm Password
    confirmPasswordLabel = Label(leftFrame, text = "Confirm password", width = "30", anchor = 'w')
    confirmPasswordLabel.grid(column = 0, row = 6, columnspan = 2)

    # Create entry widget for Confirm Password
    confirmPasswordField = Entry(leftFrame, bd = 3, width = 30, textvariable = confirmPassword, show = '*')
    confirmPasswordField.grid(column = 0, row = 7, columnspan = 2)

    # Create label widget for Security Question
    securityQuestionLabel = Label(leftFrame, text = "Enter a security question", width = "30", anchor = 'w')
    securityQuestionLabel.grid(column = 0, row = 8, columnspan = 2)

    # Creat entry widget for Security Question
    securityQuestionField = Entry(leftFrame, bd = 3, width = 30, textvariable = securityQuestion)
    securityQuestionField.grid(column = 0, row = 9, columnspan = 2)

    # Create label widget for Security Response
    securityResponseLabel = Label(leftFrame, text = "Enter a response to the security question", width = "30", anchor = 'w')
    securityResponseLabel.grid(column = 0, row = 10, columnspan = 2)

    # Create an entry widget for Security Response
    securityResponseField = Entry(leftFrame, bd = 3, width = 30, textvariable = securityResponse)
    securityResponseField.grid(column = 0, row = 11, columnspan = 2)

    # Create label for padding
    emptyLabel = Label(leftFrame, text = "", width = "30", anchor = 'w')
    emptyLabel.grid(column = 0, row = 12, columnspan = 2)

    # Create button widget for Register - registers a new user
    registerUserButton = Button(leftFrame, text = "Register", width=10, height=1, bg="blue", command = lambda : registerUser(mainWindow, userRegistrationWindow, userLoginWindow, dbConnection, dbCursor, usernameField.get(), passwordField.get(), confirmPasswordField.get(), securityQuestionField.get(), securityResponseField.get(), usernameField, passwordField, securityQuestionField, securityResponseField))
    registerUserButton.grid(column = 0, row = 13)

    # Create button widget for Cancel - cancels user registration
    cancelButton = Button(leftFrame, text = "Cancel", width = 10, height=1, bg="blue", command = lambda : cancelUserRegistration(userRegistrationWindow, userLoginWindow, usernameField, passwordField, securityQuestionField, securityResponseField))
    cancelButton.grid(column = 1, row = 13)

# Implemention for register button event
def registerUser(mainWindow, parentWindow, userLoginWindow, dbConnection, dbCursor, username, password, confirmPassword, securityQuestion, securityResponse, usernameField, passwordField, securityQuestionField, securityResponseField):
    if not username:
        popupBox(mainWindow, parentWindow, "Error", "Username is null. Please provide a valid user name")
    elif not password:
        popupBox(mainWindow, parentWindow, "Error", "Password is null. Please provide a valid password")
    elif not securityQuestion:
        popupBox(mainWindow, parentWindow, "Error", "You must provide a security question")
    elif not securityResponse:
        popupBox(mainWindow, parentWindow, "Error", "You must provide a security response")
    else:
        if checkUserNameExists(username, dbCursor) == False:
            if password == confirmPassword:
                # Add new user into the GetFit database
                insertStatement = """INSERT INTO Users (username, password, security_question, security_response) VALUES (%s, %s, %s, %s)"""
                vals = (username, password, securityQuestion, securityResponse)
                dbCursor.execute(insertStatement, vals)

                dbConnection.commit()

                usernameField.delete(0, END)
                passwordField.delete(0, END)
                securityQuestionField.delete(0, END)
                securityResponseField.delete(0, END)

                parentWindow.grid_forget()
                userLoginWindow.grid(sticky='nsew')
                popupBox(mainWindow, userLoginWindow, "Information", "User registration was successful")
            else:
                popupBox(mainWindow, userLoginWindow, "Error", "Passwords do not match")

        else:
            popupBox(mainWindow, parentWindow, "Error", "This username already exits. Please try another username")

# Implemtation for cancel user registration button event
def cancelUserRegistration(parentWindow, userLoginWindow, usernameField, passwordField, securityQuestionField, securityResponseField):
    usernameField.delete(0, END)
    passwordField.delete(0, END)
    securityQuestionField.delete(0, END)
    securityResponseField.delete(0, END)

    parentWindow.grid_forget()
    userLoginWindow.grid(sticky='nsew')
