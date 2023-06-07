from tkinter import *
from tkinter import ttk
from datetime import datetime
#import mysql.connector
#rom mysql.connector import errorcode
#from RegisterUserWindow import *
from PopupBox import *
from CheckUserNameExists import *
from ResetPassword import *

# Implementation of the Update Profile and Settings window
def createUpdateProfileAndSettingsWindow(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Hide the App window
    parentWindow.grid_forget()

    userProfileInfo = getUserProfileInformation(dbConnection, dbCursor, username)

    fullName = userProfileInfo[0]
    birthdate = userProfileInfo[1].strftime("%m/%d/%y")
    phoneNo = userProfileInfo[2]
    email = userProfileInfo[3]
    gender = userProfileInfo[4]
    height = str(userProfileInfo[5])
    weight = str(userProfileInfo[6])
    imagePath = userProfileInfo[7]

    #imagePath = "/Users/marvinharrison/Documents/Code/Final Summative/GetFit/Marvin.jpeg"

    # Create a frame for the Update Profile & Settings window
    updateProfileAndSettingsWindow = ttk.Frame(mainWindow)

    # Setup the Update Profile & Settings window
    updateProfileAndSettingsWindow.grid(sticky = (N, S, E, W))
    updateProfileAndSettingsWindow.columnconfigure(0, weight = 1)
    updateProfileAndSettingsWindow.columnconfigure(1, weight = 1)
    #updateProfileWindow.rowconfigure(0, weight = 1)
    updateProfileAndSettingsWindow.rowconfigure(1, weight = 1)
    updateProfileAndSettingsWindow.rowconfigure(2, weight = 1)
    updateProfileAndSettingsWindow.rowconfigure(3, weight = 1)
    updateProfileAndSettingsWindow.rowconfigure(4, weight = 1)
    updateProfileAndSettingsWindow.rowconfigure(5, weight = 1)
    updateProfileAndSettingsWindow.rowconfigure(6, weight = 1)
    updateProfileAndSettingsWindow.rowconfigure(7, weight = 1)
    updateProfileAndSettingsWindow.rowconfigure(8, weight = 1)
    updateProfileAndSettingsWindow.rowconfigure(9, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(updateProfileAndSettingsWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    middleFrame = ttk.Frame(updateProfileAndSettingsWindow, width = 300, height = 100, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(updateProfileAndSettingsWindow, width = 300, height = 400, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(updateProfileAndSettingsWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    middleButtonFrame = ttk.Frame(updateProfileAndSettingsWindow, width = 300, height = 100, relief = 'groove', borderwidth = 2)
    bottomButtonFrame = ttk.Frame(updateProfileAndSettingsWindow, width = 300, height = 400, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    middleFrame.grid(column = 0, row = 1, columnspan = 1, rowspan = 2, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomFrame.grid(column = 0, row = 3, columnspan = 1, rowspan = 6, padx = 5, pady = 5, sticky=(N, S, E, W))
    buttonFrame.grid(column = 0, row = 9, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    middleButtonFrame.grid(column = 1, row = 1, columnspan = 1, rowspan = 2, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomButtonFrame.grid(column = 1, row = 3, columnspan = 2, rowspan = 6, padx = 5, pady = 5, sticky=(N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(1, weight = 1)
    middleFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    #bottomFrame.columnconfigure(0, weight = 1)
    #bottomFrame.columnconfigure(1, weight = 1)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(1, weight = 1)
    middleButtonFrame.columnconfigure(1, weight = 1)
    bottomButtonFrame.columnconfigure(1, weight = 1)

    #topFrame.rowconfigure(0, weight = 1)
    middleFrame.rowconfigure(1, weight = 1)
    middleFrame.rowconfigure(2, weight = 1)
    bottomFrame.rowconfigure(3, weight = 1)
    bottomFrame.rowconfigure(4, weight = 1)
    bottomFrame.rowconfigure(5, weight = 1)
    bottomFrame.rowconfigure(6, weight = 1)
    bottomFrame.rowconfigure(7, weight = 1)
    bottomFrame.rowconfigure(8, weight = 1)
    bottomFrame.rowconfigure(9, weight = 1)
    bottomFrame.rowconfigure(10, weight = 1)
    middleButtonFrame.rowconfigure(1, weight = 1)
    middleButtonFrame.rowconfigure(2, weight = 1)
    bottomButtonFrame.rowconfigure(3, weight = 1)
    bottomButtonFrame.rowconfigure(4, weight = 1)
    bottomButtonFrame.rowconfigure(5, weight = 1)
    bottomButtonFrame.rowconfigure(6, weight = 1)
    bottomButtonFrame.rowconfigure(7, weight = 1)
    bottomButtonFrame.rowconfigure(8, weight = 1)
    bottomButtonFrame.rowconfigure(9, weight = 1)
    bottomButtonFrame.rowconfigure(10, weight = 1)

    # Create label widget for Profile & Settings
    profileAndSettingsLabel =ttk.Label(topFrame, text = "Profile & Settings", width = 25, anchor = W)
    profileAndSettingsLabel.grid(column = 0, row = 0, pady = 5, sticky = (N, W))

    # Create label widget for Username
    usernameLabel =ttk.Label(topFrame, text = "Username: " + username, width = 20, anchor = W)
    usernameLabel.grid(column = 1, row = 0, pady = 5, sticky = (N, W))

    # Create label widget for Password & Security
    passwordAndSecurityLabel =ttk.Label(middleFrame,text = "Password & Security", width = "30", anchor = W)
    passwordAndSecurityLabel.grid(column = 0, row = 1, pady = 5, sticky = (N, W))

    # Create label widget for Password & Security information
    passwordAndSecurityInfoLabel =ttk.Label(middleFrame,text = "Manage your GetFit password and edit your Security Question", width = "50", anchor = W)
    passwordAndSecurityInfoLabel.grid(column = 0, row = 2, columnspan = 2, sticky = (N, W))

    # Create button widget for Change password
    updatePasswordAndSecurityButton = ttk.Button(middleButtonFrame, text = "Change password", command = lambda : changePasswordSecurityCheck(mainWindow, updateProfileAndSettingsWindow, dbConnection, dbCursor, username))
    updatePasswordAndSecurityButton.grid(column = 1, row = 1)

    # Create button widget for Change security question password
    updatePasswordAndSecurityButton = ttk.Button(middleButtonFrame, text = "Change security question", command = lambda : changeSecretQuestionSecurityCheck(mainWindow, updateProfileAndSettingsWindow, dbConnection, dbCursor, username))
    updatePasswordAndSecurityButton.grid(column = 1, row = 2)
    
    # Create label widget for Personal Information
    personaInformationLabel =ttk.Label(bottomFrame,text = "Personal Information", width = "30", anchor = W)
    personaInformationLabel.grid(column = 0, row = 3, sticky = (N, W))

    # Create label widget for Name
    nameLabel =ttk.Label(bottomFrame,text = "Name: " + fullName, width = "30", anchor = W)
    nameLabel.grid(column = 0, row = 4, sticky = (N, W))

    # Create label widget for Birthdate
    birthdateLabel =ttk.Label(bottomFrame,text = "Birth date: " + birthdate, width = "30", anchor = W)
    birthdateLabel.grid(column = 0, row = 5, sticky = (N, W))

    # Create label widget for Phone
    phoneNumberLabel =ttk.Label(bottomFrame,text = "Phone: " + phoneNo, width = "30", anchor = W)
    phoneNumberLabel.grid(column = 0, row = 6, sticky = (N, W))

    # Create label widget for Email
    emailLabel =ttk.Label(bottomFrame,text = "Email: " + email, width = "30", anchor = W)
    emailLabel.grid(column = 0, row = 7, sticky = (N, W))

    # Create label widget for Gender
    genderLabel =ttk.Label(bottomFrame,text = "Gender: " + gender, width = "30", anchor = W)
    genderLabel.grid(column = 0, row = 8, sticky = (N, W))

    # Create label widget for Height
    heightLabel =ttk.Label(bottomFrame,text = "Height: " + height + " cm", width = "30", anchor = W)
    heightLabel.grid(column = 0, row = 9, sticky = (N, W))
    
    # Create label widget for Weight
    weightLabel =ttk.Label(bottomFrame,text = "Weight: " + weight + " kg", width = "30", anchor = W)
    weightLabel.grid(column = 0, row = 10, sticky = (N, W))

    # Create button widget for Edit
    updateProfileButton = ttk.Button(bottomButtonFrame, text = "Edit", command = lambda : updateProfile(mainWindow, updateProfileAndSettingsWindow, dbConnection, dbCursor, username))
    updateProfileButton.grid(column = 1, row = 3)

    # Create button widget to Cancel the Update Profile & Settings window
    cancelButton = ttk.Button(buttonFrame, text = "Cancel", command = lambda : 
                                   cancelUpdateProfileAndSettingsWindow(mainWindow, updateProfileAndSettingsWindow, parentWindow))
    cancelButton.grid(column = 1, row = 11, pady = 5)

def changePasswordSecurityCheck(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Create StringVars to hold the user input
    password = StringVar()

    # Create a toplevel window for the Reset Password dialog box
    changePasswordSecurityCheckWindow = Toplevel(parentWindow)
    changePasswordSecurityCheckWindow.title("Enter Your Password")

    # Create an information label widget
    informationLabel =ttk.Label(changePasswordSecurityCheckWindow, text = "Please enter your current password to reset your password")
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create an empty label widget for padding
    emptyLabel1 =ttk.Label(changePasswordSecurityCheckWindow, text = "")
    emptyLabel1.grid(column = 0, row = 1, columnspan = 2)

    # Create label widget for Password
    passwordLabel =ttk.Label(changePasswordSecurityCheckWindow, text = "Password", width = "30", anchor = 'w')
    passwordLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create entry widget for Password
    passwordField = ttk.Entry(changePasswordSecurityCheckWindow, width = 30, textvariable = password, show = '*')
    passwordField.grid(column = 0, row = 3, columnspan = 2)

    # Create button widget for OK
    oKButton = ttk.Button(changePasswordSecurityCheckWindow, text = "OK", width=10, command = lambda : confirmPassword(mainWindow, parentWindow, dbConnection, dbCursor, username, passwordField.get()))
    oKButton.grid(column = 0, row = 7)

    # Create button widget for Cancel
    cancelButton = ttk.Button(changePasswordSecurityCheckWindow, text = "Cancel", width = 10, command = lambda : changePasswordSecurityCheckWindow.destroy())
    cancelButton.grid(column = 1, row = 7)
    
    # Force an update on the mainWindow so the size of the widgets are known
    mainWindow.update()

    # Get width an height of the popup diagog box so we can resize it
    # to fit the contents of the label and button
    w = changePasswordSecurityCheckWindow.winfo_reqwidth()
    h = changePasswordSecurityCheckWindow.winfo_reqheight()

    # Calculate the geometry to center the dialog box on the screen
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    changePasswordSecurityCheckWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    changePasswordSecurityCheckWindow.grab_set()

def changeSecretQuestionSecurityCheck(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Create StringVars to hold the user input
    password = StringVar()

    # Create a toplevel window for the Reset Password dialog box
    changeSecretQuestionSecurityCheckWindow = Toplevel(parentWindow)
    changeSecretQuestionSecurityCheckWindow.title("Enter Your Password")

    # Create an information label widget
    informationLabel =ttk.Label(changeSecretQuestionSecurityCheckWindow, text = "Please enter your current password to reset your password")
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create an empty label widget for padding
    emptyLabel1 =ttk.Label(changeSecretQuestionSecurityCheckWindow, text = "")
    emptyLabel1.grid(column = 0, row = 1, columnspan = 2)

    # Create label widget for Password
    passwordLabel =ttk.Label(changeSecretQuestionSecurityCheckWindow, text = "Password", width = "30", anchor = 'w')
    passwordLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create entry widget for Password
    passwordField = ttk.Entry(changeSecretQuestionSecurityCheckWindow, width = 30, textvariable = password, show = '*')
    passwordField.grid(column = 0, row = 3, columnspan = 2)

    # Create button widget for OK
    oKButton = ttk.Button(changeSecretQuestionSecurityCheckWindow, text = "OK", width=10, command = lambda : confirmPassword(mainWindow, parentWindow, dbConnection, dbCursor, username, passwordField.get()))
    oKButton.grid(column = 0, row = 7)

    # Create button widget for Cancel
    cancelButton = ttk.Button(changeSecretQuestionSecurityCheckWindow, text = "Cancel", width = 10, command = lambda : changeSecretQuestionSecurityCheckWindow.destroy())
    cancelButton.grid(column = 1, row = 7)
    
    # Force an update on the mainWindow so the size of the widgets are known
    mainWindow.update()

    # Get width an height of the popup diagog box so we can resize it
    # to fit the contents of the label and button
    w = changeSecretQuestionSecurityCheckWindow.winfo_reqwidth()
    h = changeSecretQuestionSecurityCheckWindow.winfo_reqheight()

    # Calculate the geometry to center the dialog box on the screen
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    changeSecretQuestionSecurityCheckWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    changeSecretQuestionSecurityCheckWindow.grab_set()


def changePassword(mainWindow, parentWindow, dbConnection, dbCursor, username):
    security(mainWindow, parentWindow, dbConnection, dbCursor, username)

    #if (passwordCheck(mainWindow, parentWindow, dbConnection, dbCursor, username, password)):
    #    resetPassword(mainWindow, parentWindow, dbConnection, dbCursor, username)
    #else:
    #    pass


def changeSecurityQuestion(mainWindow, parentWindow, dbConnection, dbCursor, username, password):
    getPasswordAndCheck(mainWindow, parentWindow, dbConnection, dbCursor, username)

    #if (passwordCheck(mainWindow, parentWindow, dbConnection, dbCursor, username, password)):
    #    resetSecurityQuestion(mainWindow, parentWindow, dbConnection, dbCursor, username)
    #else:
    #    pass

def resetPasswordd():
    i = 1

def resetSecurityQuestion(mainWindow, parentWindow, dbConnection, dbCursor, username):
    i = 1


def updateProfile(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Create a toplevel window for the Update Profile dialog box
    updateProfileWindow = Toplevel(parentWindow)
    updateProfileWindow.title("Update profile")

    # Create an information label
    informationLabel =ttk.Label(updateProfileWindow, text = "Please enter details below to update your profile")
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Add your labels widget, entry widgets, and button widgets below here
    # Add checking for the entry fields
    # Add button event


    # Force an update on the mainWindow so the size of the widgets are known
    mainWindow.update()

    # Get width an height of the popup diagog box so we can resize it
    # to fit the contents of the label and button
    w = updateProfileWindow.winfo_reqwidth()
    h = updateProfileWindow.winfo_reqheight()

    # Calculate the geometry to center the dialog box on the screen
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    updateProfileWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))


# Implementation of the Cancel button for the Update Profile & Settings window
# Closes the Update Profile & Settings window and returns to the App window
def cancelUpdateProfileAndSettingsWindow(mainWindow, parentWindow, appWindow):
    # Hide the Update Profile & Settings window
    parentWindow.grid_forget()
    
    # Show the App window
    appWindow.grid(sticky = (N, S, E, W))


def getUserProfileInformation(dbConnection, dbCursor, username):
        selectStatement = """SELECT * FROM UserInfo WHERE username = %s"""
        vals = (username,)
        dbCursor.execute(selectStatement, vals)

        userInfo = dbCursor.fetchone()

        # Create the userProfileInfo tuple
        # userProfileInfo = (fullname, birthdate, phone_number, email, gender, height, weight, image_path)
        userProfileInfo = (userInfo[2], userInfo[3], userInfo[4], userInfo[5], userInfo[6], userInfo[7], userInfo[8], userInfo[9])

        # Return the tuple (fullname, birthdate, phone_number, email, gender, height, weight, image_path)
        return userProfileInfo
