from tkinter import *
from tkinter import ttk
import bcrypt
import re
from PopupBox import *
from CheckUsernameExists import *
from PasswordHash import *

# Implementation of the User Registration window
def createRegisterUserWindow(mainWindow, userLoginWindow, dbConnection, dbCursor):

    # Create StringVars to hold the user input
    username = StringVar()
    password = StringVar()
    confirmPassword = StringVar()
    securityQuestion = StringVar()
    securityResponse = StringVar()
    
    # Hide the User Login window
    userLoginWindow.grid_forget()

    # Create a frame for the User Registration window
    userRegistrationWindow = ttk.Frame(mainWindow, padding=(3,3,12,12))
    userRegistrationWindow.grid(sticky = (N, S, E, W))

    # Setup the User Registration window
    userRegistrationWindow.columnconfigure(0, weight = 1)
    userRegistrationWindow.columnconfigure(1, weight = 1)
    userRegistrationWindow.rowconfigure(0, weight = 1)
    userRegistrationWindow.rowconfigure(1, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(userRegistrationWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(userRegistrationWindow, width = 300, height = 700, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(userRegistrationWindow, width = 300, height = 50, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 11, padx = 5, pady = 5, sticky=(N, S, E, W))
    buttonFrame.grid(column = 0, row = 12, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(0, weight = 1)

    topFrame.rowconfigure(0, weight = 0)
    bottomFrame.rowconfigure(1, weight = 1)
    bottomFrame.rowconfigure(2, weight = 1)
    bottomFrame.rowconfigure(3, weight = 1)
    bottomFrame.rowconfigure(4, weight = 1)
    bottomFrame.rowconfigure(5, weight = 1)
    bottomFrame.rowconfigure(6, weight = 1)
    bottomFrame.rowconfigure(7, weight = 1)
    bottomFrame.rowconfigure(8, weight = 1)
    bottomFrame.rowconfigure(9, weight = 1)
    bottomFrame.rowconfigure(10, weight = 1)
    bottomFrame.rowconfigure(11, weight = 1)
    buttonFrame.rowconfigure(11, weight = 1)

    # Create an information label 
    informationLabel =ttk.Label(topFrame, text = "To register for a GetFit profile, please enter details below")
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create label widget for Username
    usernameLabel =ttk.Label(bottomFrame, text = "Username", width = "30", anchor = 'w')
    usernameLabel.grid(column = 0, row = 1, columnspan = 2)

    # Create entry widget for Username
    usernameField = ttk.Entry(bottomFrame, width = 30,textvariable = username)
    usernameField.grid(column = 0, row = 2, columnspan = 2)
    
    # Set focus on Username field
    usernameField.focus_force() 

    # Create label widget for Password
    passwordLabel =ttk.Label(bottomFrame, text = "Password", width = "30", anchor = 'w')
    passwordLabel.grid(column = 0, row = 3, columnspan = 2)

    # Create entry widget for Password
    passwordField = ttk.Entry(bottomFrame, width = 30, textvariable = password, show = '*')
    passwordField.grid(column = 0, row = 4, columnspan = 2)

    # Create label widget for Confirm Password
    confirmPasswordLabel =ttk.Label(bottomFrame, text = "Confirm password", width = "30", anchor = 'w')
    confirmPasswordLabel.grid(column = 0, row = 5, columnspan = 2)

    # Create entry widget for Confirm Password
    confirmPasswordField = ttk.Entry(bottomFrame, width = 30, textvariable = confirmPassword, show = '*')
    confirmPasswordField.grid(column = 0, row = 6, columnspan = 2)

    # Create label widget for Security Question
    securityQuestionLabel =ttk.Label(bottomFrame, text = "Enter a security question", width = "30", anchor = 'w')
    securityQuestionLabel.grid(column = 0, row = 7, columnspan = 2)

    # Creat entry widget for Security Question
    securityQuestionField = ttk.Entry(bottomFrame, width = 30, textvariable = securityQuestion)
    securityQuestionField.grid(column = 0, row = 8, columnspan = 2)

    # Create label widget for Security Response
    securityResponseLabel =ttk.Label(bottomFrame, text = "Enter a response to the security question", width = "30", anchor = 'w')
    securityResponseLabel.grid(column = 0, row = 9, columnspan = 2)

    # Create an entry widget for Security Response
    securityResponseField = ttk.Entry(bottomFrame, width = 30, textvariable = securityResponse)
    securityResponseField.grid(column = 0, row = 10, columnspan = 2)

    # Create label for padding
    emptyLabel =ttk.Label(bottomFrame, text = "", width = "30", anchor = 'w')
    emptyLabel.grid(column = 0, row = 11, columnspan = 2)

    # Create button widget for Register - registers a new user
    registerUserButton = ttk.Button(buttonFrame, text = "Register", width=10, command = lambda : registerUser(mainWindow, userRegistrationWindow, userLoginWindow, dbConnection, dbCursor, usernameField.get(), passwordField.get(), confirmPasswordField.get(), securityQuestionField.get(), securityResponseField.get(), usernameField, passwordField, confirmPasswordField, securityQuestionField, securityResponseField))
    registerUserButton.grid(column = 0, row = 12, sticky = (N, W))

    # Create button widget for Cancel - cancels user registration
    cancelButton = ttk.Button(buttonFrame, text = "Cancel", width = 10, command = lambda : cancelUserRegistration(userRegistrationWindow, userLoginWindow, usernameField, passwordField, confirmPasswordField, securityQuestionField, securityResponseField))
    cancelButton.grid(column = 1, row = 12 ,sticky = (N, W))

# Implemention for the Register button event
# Does error checking on user input values for username, password, confirm password,
# security question and security response. Validates minimum and maximum length of
# username. Validates that provided password follows password rules. Creates a password
# hash to store in the User database. Creates a User and UserInfo database record for
# the user in the GetFit database
def registerUser(mainWindow, parentWindow, userLoginWindow, dbConnection, dbCursor, username, password, confirmPassword, securityQuestion, securityResponse, usernameField, passwordField, confirmPasswordField, securityQuestionField, securityResponseField):
    # Define a regular expression to check that the password meets the following criteria:
    #   - Is a minimum of 8 characters in length. Adjust it by modifying {8,}
    #   - Has at least one uppercase English letter. You can remove this condition by removing (?=.*?[A-Z])
    #   - Has at least one lowercase English letter. You can remove this condition by removing (?=.*?[a-z])
    #   - Has at least one digit. You can remove this condition by removing (?=.*?[0-9])
    #   - Has at least one special character. You can remove this condition by removing (?=.*?[#?!@$%^&*-])
    passwordPattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    
    if not username:
        popupBox(mainWindow, parentWindow, "Error", "Username is null. Please provide a valid user name")
    elif len(username) < 6 or len(username) > 50:
        popupBox(mainWindow,parentWindow, "Error", "Username must be between 6 and 50 characters long")
    elif not password:
        popupBox(mainWindow, parentWindow, "Error", "Password is null. Please provide a valid password")
    elif len(password) < 8 or len(password) > 64:
        popupBox(mainWindow,parentWindow, "Error", "Password must be between 8 and 64 characters long")
    elif (re.match(passwordPattern,password) == None):
        popupBox(mainWindow,parentWindow, "Error", "Password must be a minimum of 8 characters long\nPassword must have at least one uppercase English letter\nPassword must have at least one lowercase English letter\nPassword must have at least one digit\nPassword must have at least one special character such as #?!@$%^&*-\n")
    elif not securityQuestion:
        popupBox(mainWindow, parentWindow, "Error", "You must provide a security question")
    elif len(securityQuestion) > 256:
        popupBox(mainWindow,parentWindow, "Error", "The maximum length of a security question is 256 characters long")
    elif not securityResponse:
        popupBox(mainWindow, parentWindow, "Error", "You must provide a security response")
    elif len(securityResponse) > 64:
        popupBox(mainWindow,parentWindow, "Error", "The maximum length of a security response is 64 characters long")
    else:
        if checkUsernameExists(username, dbCursor) == False:
            if password == confirmPassword:
                passwordHash = createPasswordHash(password)

                # Add new user into the GetFit database
                insertStatement = """INSERT INTO User (username, password_hash, security_question, security_response) VALUES (%s, %s, %s, %s)"""
                vals = (username, passwordHash, securityQuestion, securityResponse)
                dbCursor.execute(insertStatement, vals)

                # Add a UserInfo record for the user
                #fullName = ""
                #phoneNo = ""
                #email = ""
                #gender = ""
                #imagePath = ""
                #insertStatement = """INSERT INTO UserInfo (username, fullname, phone_number, email, gender, image_path) VALUES (%s, %s, %s, %s, %s, %s)"""
                #vals = (username, fullName, phoneNo, email, gender, imagePath)
                insertStatement = """INSERT INTO UserInfo (username) VALUES (%s)"""
                vals = (username,)

                dbCursor.execute(insertStatement, vals)

                dbConnection.commit()

                usernameField.delete(0, END)
                passwordField.delete(0, END)
                confirmPasswordField.delete(0, END)
                securityQuestionField.delete(0, END)
                securityResponseField.delete(0, END)

                # Hide the Register User window
                parentWindow.grid_forget()

                # Show the User Login window
                userLoginWindow.grid(sticky = (N, S, E, W))
                popupBox(mainWindow, userLoginWindow, "Information", "User registration was successful")
            else:
                popupBox(mainWindow, userLoginWindow, "Error", "Passwords do not match")

        else:
            popupBox(mainWindow, parentWindow, "Error", "This username already exits. Please try another username")

# Implementation for the Cancel user registration button event
def cancelUserRegistration(parentWindow, userLoginWindow, usernameField, passwordField, confirmPasswordField, securityQuestionField, securityResponseField):
    usernameField.delete(0, END)
    passwordField.delete(0, END)
    confirmPasswordField.delete(0, END)
    securityQuestionField.delete(0, END)
    securityResponseField.delete(0, END)

    # Hide the User Registration window
    parentWindow.grid_forget()

    # Show the User Login window
    userLoginWindow.grid(sticky = (N, S, E, W))
