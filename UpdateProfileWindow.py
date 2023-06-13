from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from datetime import date
from tkcalendar import Calendar, DateEntry
from decimal import Decimal
from PIL import ImageTk
import PIL.Image
import os
import mysql.connector
from mysql.connector import errorcode
from PopupBox import *
from ResetPassword import *

# Implementation of the Update Profile and Settings window
def createUpdateProfileAndSettingsWindow(mainWindow, appWindow, dbConnection, dbCursor, username):
    # Hide the App window
    appWindow.grid_forget()

    # Create a frame for the Update Profile & Settings window
    updateProfileAndSettingsWindow = ttk.Frame(mainWindow)

    # Setup the Update Profile & Settings window
    updateProfileAndSettingsWindow.grid(sticky = (N, S, E, W))

    updateProfileAndSettingsWindow.columnconfigure(0, weight = 1)
    updateProfileAndSettingsWindow.columnconfigure(1, weight = 1)
    updateProfileAndSettingsWindow.columnconfigure(2, weight = 1)

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
    topFrame.grid(column = 0, row = 0, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    middleFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 2, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomFrame.grid(column = 0, row = 3, columnspan = 2, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))
    buttonFrame.grid(column = 0, row = 11, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    middleButtonFrame.grid(column = 2, row = 1, columnspan = 1, rowspan = 2, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomButtonFrame.grid(column = 2, row = 3, columnspan = 1, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(1, weight = 1)
    topFrame.columnconfigure(2, weight = 1)
    middleFrame.columnconfigure(0, weight = 1)
    middleFrame.columnconfigure(1, weight = 5)
    bottomFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(1, weight = 5)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(1, weight = 1)
    middleButtonFrame.columnconfigure(2, weight = 1)
    bottomButtonFrame.columnconfigure(2, weight = 1)

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

    # Get the user profile information for the user from the GetFit database
    userProfileInfo = getUserProfileInformation(mainWindow, updateProfileAndSettingsWindow, dbConnection, dbCursor, username)

    # Create StringVars for the labels
    fullname = StringVar(updateProfileAndSettingsWindow)
    birthdate = StringVar(updateProfileAndSettingsWindow)
    phoneNumber = StringVar(updateProfileAndSettingsWindow)
    email = StringVar(updateProfileAndSettingsWindow)
    gender = StringVar(updateProfileAndSettingsWindow)
    height = StringVar(updateProfileAndSettingsWindow)
    weight = StringVar(updateProfileAndSettingsWindow)
    imagePath = StringVar(updateProfileAndSettingsWindow)

    # Set the StringVars to the values obtained from the GetFit database
    fullname.set(userProfileInfo[0])
    birthdate.set(userProfileInfo[1].strftime("%m/%d/%y"))
    phoneNumber.set(userProfileInfo[2])
    email.set(userProfileInfo[3])
    gender.set(userProfileInfo[4])
    height.set(str(userProfileInfo[5]))
    weight.set(str(userProfileInfo[6]))
    imagePath.set(userProfileInfo[7])

    # Create a tuple for the labels  
    labels = [fullname, birthdate, phoneNumber, email, gender, height, weight, imagePath]

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
    updatePasswordAndSecurityButton = ttk.Button(middleButtonFrame, text = "Change password", command = lambda :
                                                 createChangePasswordSecurityCheckBox(mainWindow, updateProfileAndSettingsWindow, dbConnection, dbCursor, username))
    updatePasswordAndSecurityButton.grid(column = 2, row = 1, sticky = (W, E))

    # Create button widget for Change security question password
    updatePasswordAndSecurityButton = ttk.Button(middleButtonFrame, text = "Change security question", command = lambda :
                                                 createChangeSecretQuestionSecurityCheckBox(mainWindow, updateProfileAndSettingsWindow, dbConnection, dbCursor, username))
    updatePasswordAndSecurityButton.grid(column = 2, row = 2, sticky = (W, E))
    
    # Create label widget for Personal Information
    personaInformationLabel =ttk.Label(bottomFrame, text = "Personal Information", anchor = W)
    personaInformationLabel.grid(column = 0, row = 3, sticky = (N, W))

    # Create label widget for Name
    nameLabel =ttk.Label(bottomFrame, text = "Name:", anchor = W)
    nameLabel.grid(column = 0, row = 4, sticky = (N, W))
    
    # Create label widget for value of Full Name
    nameLabel =ttk.Label(bottomFrame, textvariable = fullname, anchor = W)
    nameLabel.grid(column = 1, row = 4, sticky = (N, W))

    # Create label widget for Birthdate
    birthdateLabel =ttk.Label(bottomFrame, text = "Birth date:", anchor = W)
    birthdateLabel.grid(column = 0, row = 5, sticky = (N, W))

    # Create label widget for value of Birthdate
    birthdateLabel =ttk.Label(bottomFrame, textvariable = birthdate, anchor = W)
    birthdateLabel.grid(column = 1, row = 5, sticky = (N, W))

    # Create label widget for Phone
    phoneNumberLabel =ttk.Label(bottomFrame, text = "Phone:", anchor = W)
    phoneNumberLabel.grid(column = 0, row = 6, sticky = (N, W))

    # Create label widget for value of Phone
    phoneNumberLabel =ttk.Label(bottomFrame, textvariable = phoneNumber, anchor = W)
    phoneNumberLabel.grid(column = 1, row = 6, sticky = (N, W))

    # Create label widget for Email
    emailLabel =ttk.Label(bottomFrame, text = "Email:", anchor = W)
    emailLabel.grid(column = 0, row = 7, sticky = (N, W))

    # Create label widget for value Email
    emailLabel =ttk.Label(bottomFrame, textvariable = email, anchor = W)
    emailLabel.grid(column = 1, row = 7, sticky = (N, W))

    # Create label widget for Gender
    genderLabel =ttk.Label(bottomFrame, text = "Gender:", anchor = W)
    genderLabel.grid(column = 0, row = 8, sticky = (N, W))
    
    # Create label widget for value of Gender
    genderLabel =ttk.Label(bottomFrame, textvariable = gender, anchor = W)
    genderLabel.grid(column = 1, row = 8, sticky = (N, W))

    # Create label widget for Height
    heightLabel =ttk.Label(bottomFrame, text = "Height (in cm): ", anchor = W)
    heightLabel.grid(column = 0, row = 9, sticky = (N, W))
    
    # Create label widget for value of Height
    heightLabel =ttk.Label(bottomFrame, textvariable = height, anchor = W)
    heightLabel.grid(column = 1, row = 9, sticky = (N, W))
    
    # Create label widget for Weight
    weightLabel =ttk.Label(bottomFrame, text = "Weight (in kg):", anchor = W)
    weightLabel.grid(column = 0, row = 10, sticky = (N, W))
        
    # Create label widget for value of Weight
    weightLabel =ttk.Label(bottomFrame, textvariable = weight, anchor = W)
    weightLabel.grid(column = 1, row = 10, sticky = (N, W))

    # Create button widget for Edit Personal Information
    updateProfileButton = ttk.Button(bottomButtonFrame, text = "Edit Personal Information", command = lambda :
                                     createUpdateProfileBox(mainWindow, updateProfileAndSettingsWindow, dbConnection, dbCursor, username, labels))
    updateProfileButton.grid(column = 2, row = 3, sticky = (W, E))

    # Handle special case of empty string; just ignore it
    if not imagePath.get():
        pass
    else:
        # Check if the image file exists
        if(os.path.isfile(imagePath.get())):
            # If the image file exists, open it
            userImage = PIL.Image.open(imagePath.get())

            # Resize the image to fit in the window
            userImage = userImage.resize((250, 250), PIL.Image.Resampling.LANCZOS)
            userImage = ImageTk.PhotoImage(userImage)

            # Create label widget to display the user's image
            userImageLabel = ttk.Label(bottomButtonFrame, image = userImage)
            userImageLabel.image = userImage
            userImageLabel.grid(column = 2, row = 4, sticky = (N, S, E, W))
        else:
            # If the image file does not exist, show an error dialog
            popupBox(mainWindow, updateProfileAndSettingsWindow, "Error", "The file " + imagePath.get() + " was not found")

    # Create button widget to Cancel the Update Profile & Settings window
    updateButton = ttk.Button(bottomButtonFrame, text = "Update image", command = lambda :
                              updateImage(mainWindow, updateProfileAndSettingsWindow, bottomButtonFrame, userImageLabel, imagePath))
    updateButton.grid(column = 2, row = 10, sticky = (W, E))  

    # Create button widget to Cancel the Update Profile & Settings window
    cancelButton = ttk.Button(buttonFrame, text = "Cancel", command = lambda :
                              cancelUpdateProfileAndSettingsWindow(mainWindow, updateProfileAndSettingsWindow, appWindow))
    cancelButton.grid(column = 2, row = 11, pady = 5, sticky = (W, E))

def openImageFile(mainWindow, parentWindow, labels):
    # Specify the file types
    filetypes = (('GIF files', '*.gif'), ('JPEG files', '*.jpeg'), ('PNG files', '*.png'), ('All files', '*.*'))
  
    # Show the open file dialog by specifying path
    file = fd.askopenfile(filetypes = filetypes)
    labels[7].set(file.name)

def updateImage(mainWindow, parentWindow, bottomButtonFrame, userImageLabel, imagePath):
    # Handle special case of empty string; just ignore it
    if not imagePath.get():
        pass
    else:
        # Check if the image file exists
        if(os.path.isfile(imagePath.get())):
            # If the image file exists, open it
            userImage = PIL.Image.open(imagePath.get())

            # Resize the image to fit in the window
            userImage = userImage.resize((250, 250), PIL.Image.Resampling.LANCZOS)
            userImage = ImageTk.PhotoImage(userImage)

            userImageLabel.grid_forget()

            # Create label widget for user's image
            userImageLabel = ttk.Label(bottomButtonFrame, image = userImage)
            userImageLabel.image = userImage
            userImageLabel.grid(column = 2, row = 4, sticky = (N, S, E, W))
        else:
            # If the image file does not exist, show an error dialog
            popupBox(mainWindow, parentWindow, "Error", "The file " + imagePath.get() + " was not found")

def createChangePasswordSecurityCheckBox(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Create a toplevel window for the Reset Password dialog box
    changePasswordSecurityCheckWindow = Toplevel(parentWindow)
    changePasswordSecurityCheckWindow.title("Enter Your Password")

    # Create StringVars to hold the user input
    password = StringVar(changePasswordSecurityCheckWindow)

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
    oKButton = ttk.Button(changePasswordSecurityCheckWindow, text = "OK", width=10, command = lambda :
                          checkPasswordToChangePassword(mainWindow, parentWindow, changePasswordSecurityCheckWindow, dbConnection, dbCursor, username, passwordField.get()))
    oKButton.grid(column = 0, row = 7)

    # Create button widget for Cancel
    cancelButton = ttk.Button(changePasswordSecurityCheckWindow, text = "Cancel", width = 10, command = lambda :
                              changePasswordSecurityCheckWindow.destroy())
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

def createChangeSecretQuestionSecurityCheckBox(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Create a toplevel window for the Reset Password dialog box
    changeSecretQuestionSecurityCheckWindow = Toplevel(parentWindow)
    changeSecretQuestionSecurityCheckWindow.title("Enter Your Password")
    
    # Create StringVars to hold the user input
    password = StringVar(changeSecretQuestionSecurityCheckWindow)

    # Create an information label widget
    informationLabel =ttk.Label(changeSecretQuestionSecurityCheckWindow, text = "Please enter your current password to reset your security question")
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
    oKButton = ttk.Button(changeSecretQuestionSecurityCheckWindow, text = "OK", width=10, command = lambda :
                          checkPasswordToChangeSecretQuestion(mainWindow, parentWindow, changeSecretQuestionSecurityCheckWindow, dbConnection, dbCursor, username, passwordField.get()))
    oKButton.grid(column = 0, row = 7)

    # Create button widget for Cancel
    cancelButton = ttk.Button(changeSecretQuestionSecurityCheckWindow, text = "Cancel", width = 10, command = lambda :
                              changeSecretQuestionSecurityCheckWindow.destroy())
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

def checkPasswordToChangePassword(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username, password):
    try:
        # Get the hashed password for the username from the GetFit database
        selectStatement = """SELECT * FROM User WHERE username = %s"""
        vals = (username,)

        # Execute the SQL SELECT statement
        dbCursor.execute(selectStatement, vals)

        # Fetch the results of the query
        user = dbCursor.fetchone()
        passwordHash = user[2]

        # Compare the hashed password retrieved from the GetFit database to the user supplied password
        if (comparePassword(password,passwordHash)):
            callingWindow.destroy()

            createResetPasswordBox(mainWindow, parentWindow, dbConnection, dbCursor, username)
        else:
            popupBox(mainWindow, parentWindow, "Error", "Password was invalid")
    except mysql.connector.Error as error:
        # Format the database error message for displaying in the popup box
        errorMessage = "Error Code: " + str(error.errno) + "\n" + "SQLSTATE: " + error.sqlstate + "\n" + "Message: " + error.msg  
        popupBox(mainWindow, callingWindow, "Error", errorMessage)

def checkPasswordToChangeSecretQuestion(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username, password):
    # Get the hashed password for the username from the GetFit database
    try:
        # Get the hashed password for the username from the GetFit database
        selectStatement = """SELECT * FROM User WHERE username = %s"""
        vals = (username,)

        # Execute the SQL SELECT statement
        dbCursor.execute(selectStatement, vals)

        # Fetch the results of the query
        user = dbCursor.fetchone()
        passwordHash = user[2]

        # Compare the hashed password retrieved from the GetFit database to the user supplied password
        if (comparePassword(password,passwordHash)):
            callingWindow.destroy()
            createChangeSecretQuestionBox(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username)
        else:
            popupBox(mainWindow, parentWindow, "Error", "Password was invalid")
    except mysql.connector.Error as error:
        # Format the database error message for displaying in the popup box
        errorMessage = "Error Code: " + str(error.errno) + "\n" + "SQLSTATE: " + error.sqlstate + "\n" + "Message: " + error.msg  
        popupBox(mainWindow, callingWindow, "Error", errorMessage)

def createChangeSecretQuestionBox(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username):
    # Create a toplevel window for the Reset Password dialog box
    changeSecretQuestionWindow = Toplevel(parentWindow)
    changeSecretQuestionWindow.title("Reset Secret Question and Response")

    # Create StringVars to hold the user input
    securityQuestion = StringVar(changeSecretQuestionWindow)
    securityResponse = StringVar(changeSecretQuestionWindow)
    
    # Create label widget for Security Question
    securityQuestionLabel =ttk.Label(changeSecretQuestionWindow, text = "Enter a security question", width = "30", anchor = 'w')
    securityQuestionLabel.grid(column = 0, row = 0, columnspan = 2)

    # Creat entry widget for Security Question
    securityQuestionField = ttk.Entry(changeSecretQuestionWindow, width = 30, textvariable = securityQuestion)
    securityQuestionField.grid(column = 0, row = 1, columnspan = 2)

    # Create label widget for Security Response
    securityResponseLabel =ttk.Label(changeSecretQuestionWindow, text = "Enter a response to the security question", width = "30", anchor = 'w')
    securityResponseLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create an entry widget for Security Response
    securityResponseField = ttk.Entry(changeSecretQuestionWindow, width = 30, textvariable = securityResponse)
    securityResponseField.grid(column = 0, row = 3, columnspan = 2)

    # Create label for padding
    emptyLabel =ttk.Label(changeSecretQuestionWindow, text = "", width = "30", anchor = 'w')
    emptyLabel.grid(column = 0, row = 4, columnspan = 2)

    # Create button widget for OK - changes the Security Question and Response for a user
    okButton = ttk.Button(changeSecretQuestionWindow, text = "OK", width=10, command = lambda :
                          changeSecurityQuestion(mainWindow, parentWindow, changeSecretQuestionWindow, dbConnection, dbCursor, username, securityQuestionField.get(), securityResponseField.get()))
    okButton.grid(column = 0, row = 5, sticky = (N, W))

    # Create button widget for Cancel - cancels Security Question window
    cancelButton = ttk.Button(changeSecretQuestionWindow, text = "Cancel", width = 10, command = lambda :
                              changeSecretQuestionWindow.destroy())
    cancelButton.grid(column = 1, row = 5 ,sticky = (N, W))

    # Force an update on the mainWindow so the size of the widgets are known
    mainWindow.update()

    # Get width an height of the popup diagog box so we can resize it
    # to fit the contents of the label and button
    w = changeSecretQuestionWindow.winfo_reqwidth()
    h = changeSecretQuestionWindow.winfo_reqheight()

    # Calculate the geometry to center the dialog box on the screen
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    changeSecretQuestionWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    changeSecretQuestionWindow.grab_set()

def changeSecurityQuestion(mainWindow, parentWindow, callingWindow, dbConnection, dbCursor, username, securityQuestion, securityResponse):
    if not securityQuestion:
        popupBox(mainWindow, parentWindow, "Error", "You must provide a security question")
    elif len(securityQuestion) > 256:
        popupBox(mainWindow,parentWindow, "Error", "The maximum length of a security question is 256 characters long")
    elif not securityResponse:
        popupBox(mainWindow, parentWindow, "Error", "You must provide a security response")
    elif len(securityResponse) > 64:
        popupBox(mainWindow,parentWindow, "Error", "The maximum length of a security response is 64 characters long")
    else:
        try:
            updateStatement = """UPDATE User SET security_question = %s , security_response = %s WHERE username = %s"""
            vals = (securityQuestion, securityResponse, username)
            dbCursor.execute(updateStatement, vals)
            dbConnection.commit()

            callingWindow.destroy()

        except mysql.connector.Error as error:
            # Format the database error message for displaying in the popup box
            errorMessage = "Error Code: " + str(error.errno) + "\n" + "SQLSTATE: " + error.sqlstate + "\n" + "Message: " + error.msg  
            popupBox(mainWindow, callingWindow, "Error", errorMessage)
    
        # Show information message indicating Security question was updated
        popupBox(mainWindow, parentWindow, "Information", "Security Question was successfully updated")

def createUpdateProfileBox(mainWindow, parentWindow, dbConnection, dbCursor, username, labels):    
    # Create a toplevel window for the Update Profile dialog box
    updateProfileWindow = Toplevel(parentWindow)
    updateProfileWindow.title("Update profile")

    # Get user profile information from the GetFit database
    userProfileInfo = getUserProfileInformation(mainWindow, updateProfileWindow, dbConnection, dbCursor, username)

    fullname = StringVar(updateProfileWindow)
    birthdate = StringVar(updateProfileWindow)
    phoneNumber = StringVar(updateProfileWindow)
    email = StringVar(updateProfileWindow)
    gender = StringVar(updateProfileWindow)
    height = StringVar(updateProfileWindow)
    weight = StringVar(updateProfileWindow)
    imagePath = StringVar(updateProfileWindow)
    
    # Create an information label
    informationLabel =ttk.Label(updateProfileWindow, text = "Please enter details below to update your profile")
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create label widget for Full name
    fullnameLabel =ttk.Label(updateProfileWindow, width = 20, text = "Full Name", anchor = E)
    fullnameLabel.grid(column = 0, row = 1, columnspan = 1)

    # Create entry widget for Full name
    fullnameEntry = ttk.Entry(updateProfileWindow, width = 20, textvariable = fullname)
    fullnameEntry.grid(column = 1, row = 1, columnspan = 1)

    # Create label widget for Birth date
    birthdateLabel =ttk.Label(updateProfileWindow, width = 20, text = "Birth Date", anchor = E)
    birthdateLabel.grid(column = 0, row = 2, columnspan = 1)

    # Create date entry widget for birthdate
    #birthdateEntry = DateEntry(updateProfileWindow, width = 12, background = 'darkblue', foreground = 'white', borderwidth = 2, showweeknumbers = False, year = yearVal, month = monthVal, day = dayVal)
    #birthdateEntry = DateEntry(updateProfileWindow, width = 12, background = 'darkblue', foreground = 'white', borderwidth = 2, showweeknumbers = False)
    birthdateEntry = DateEntry(updateProfileWindow, width = 20, borderwidth = 2, showweeknumbers = False, date_pattern='mm/dd/y')
    birthdateEntry.grid(column = 1, row = 2, columnspan = 1)

    # Create label widget for Phone number
    phoneNumberLabel =ttk.Label(updateProfileWindow, width = 20, text = "Phone Number", anchor = E)
    phoneNumberLabel.grid(column = 0, row = 3, columnspan = 1)

    # Creat entry widget for Phone number
    phoneNumberEntry = ttk.Entry(updateProfileWindow, width = 20, textvariable = phoneNumber)
    phoneNumberEntry.grid(column = 1, row = 3, columnspan = 1)

    # Create label widget for Email
    emailLabel =ttk.Label(updateProfileWindow, width = 20, text = "Email", anchor = E)
    emailLabel.grid(column = 0, row = 4, columnspan = 1)

    # Creat entry widget for Email
    emailEntry = ttk.Entry(updateProfileWindow, width = 20, textvariable = email)
    emailEntry.grid(column = 1, row = 4, columnspan = 1)

    # Create label widget for Gender
    genderLabel =ttk.Label(updateProfileWindow, width = 20, text = "Gender", anchor = E)
    genderLabel.grid(column = 0, row = 5, columnspan = 1)

    # Creat entry widget for Gender
    #genderEntry = ttk.Entry(updateProfileWindow, width = 20, textvariable = gender)
    #genderEntry.grid(column = 1, row = 5, columnspan = 1)

    # Create Combobox widget for Gender
    genderCombobox= ttk.Combobox(updateProfileWindow, textvariable = gender)
    genderCombobox['values'] = [
        "Female",
        "Male",
        "Non-binary",
        "Transgender",
        "Other"]
    genderCombobox.grid(column = 1, row = 5)

    # Create label widget for Height
    heightLabel =ttk.Label(updateProfileWindow, width = 20, text = "Height (in cm)", anchor = E)
    heightLabel.grid(column = 0, row = 6, columnspan = 1)

    # Creat entry widget for Height
    heightEntry = ttk.Entry(updateProfileWindow, width = 20, textvariable = height)
    heightEntry.grid(column = 1, row = 6, columnspan = 1)

    # Create label widget for Weight
    weightLabel =ttk.Label(updateProfileWindow, width = 20, text = "Weight (in kg)", anchor = E)
    weightLabel.grid(column = 0, row = 7, columnspan = 1)

    # Creat entry widget for Weight
    weightEntry = ttk.Entry(updateProfileWindow, width = 20, textvariable = weight)
    weightEntry.grid(column = 1, row = 7, columnspan = 1)

    # Create label widget for Image path
    imagePathLabel =ttk.Label(updateProfileWindow, width = 20, text = "Image path", anchor = E)
    imagePathLabel.grid(column = 0, row = 8, columnspan = 1)

    # Creat entry widget for Image path
    imagePathEntry = ttk.Entry(updateProfileWindow, width = 20, textvariable = imagePath)
    imagePathEntry.grid(column = 1, row = 8, columnspan = 1)

    # Create button widget for Open Image File dialog box
    updateProfileButton = ttk.Button(updateProfileWindow, width = 20, text = "Select Image File", command = lambda :
                                     openImageFile(mainWindow, updateProfileWindow, newLabels))
    updateProfileButton.grid(column = 1, row = 9)

    # Create button widget for OK - updates the User profile
    okButton = ttk.Button(updateProfileWindow, text = "OK", width=10, command = lambda :
                          updateProfile(mainWindow, parentWindow, updateProfileWindow, dbConnection, dbCursor, username, labels, newLabels))
    okButton.grid(column = 0, row = 10, sticky = (W, E))

    # Create button widget for Cancel - cancels the Update profile window
    cancelButton = ttk.Button(updateProfileWindow, text = "Cancel", width = 10, command = lambda :
                              updateProfileWindow.destroy())
    cancelButton.grid(column = 1, row = 10 ,sticky = (W, E))

    fullname.set(userProfileInfo[0])
    birthdateEntry.set_date(userProfileInfo[1])
    phoneNumber.set(userProfileInfo[2])
    email.set(userProfileInfo[3])
    gender.set(userProfileInfo[4])
    height.set(userProfileInfo[5])
    weight.set(userProfileInfo[6])
    imagePath.set(userProfileInfo[7])

    newLabels = [fullname, birthdateEntry, phoneNumber, email, gender, height, weight, imagePath]

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

def updateProfile(mainWindow, parentWindow, updateProfileWindow, dbConnection, dbCursor, username, labels, newLabels):
    
    fullname = newLabels[0].get()
    birthdate = newLabels[1].get_date()
    phoneNumber = newLabels[2].get()
    email = newLabels[3].get()
    gender = newLabels[4].get()
    height = newLabels[5].get()
    weight = newLabels[6].get()
    imagePath = newLabels[7].get()    
    decimalHeight = Decimal(height)
    decimalHeight = round(decimalHeight, 1)
    decimalWeight = Decimal(weight)
    decimalWeight = round(decimalWeight, 1)
    
    # Validate entered data and display any errors
    if len(fullname) > 256:
        popupBox(mainWindow, updateProfileWindow, "Error", "The maximum length of a full name is 256 characters")
    elif len(phoneNumber) > 50:
        popupBox(mainWindow, updateProfileWindow, "Error", "The maximum length of a phone number is 50 characters")
    elif len(email) > 256:
        popupBox(mainWindow, updateProfileWindow, "Error", "The maximum length of an email is 256 characters")
    elif len(gender) > 10:
        popupBox(mainWindow, updateProfileWindow, "Error", "The maximum length of gender is 10 characters")
    elif len(imagePath) > 256:
        popupBox(mainWindow, updateProfileWindow, "Error", "The maximum length of image path is 256 characters")
    elif decimalWeight < 0:
            popupBox(mainWindow, updateProfileWindow, "Error", "Weight must be greater that 0 kg")
    elif decimalHeight < 0:
            popupBox(mainWindow, updateProfileWindow, "Error", "Height must be greater that 0 cm")
    elif decimalHeight >= 10000:
            popupBox(mainWindow, updateProfileWindow, "Error", "Height must be less than 10000 cm")
    elif decimalWeight >= 10000:
            popupBox(mainWindow, updateProfileWindow, "Error", "Weight must be less than 10000 kg")
    else:
        try:
            updateStatement = """UPDATE UserInfo SET fullname = %s , birthdate = %s, phone_number = %s, email = %s, gender = %s, height = %s, weight = %s, image_path = %s WHERE username = %s"""
            vals = (fullname, birthdate, phoneNumber, email, gender, decimalHeight, decimalWeight, imagePath, username)
            dbCursor.execute(updateStatement, vals)
            dbConnection.commit()
    
            updateProfileWindow.destroy()
            refreshUpdateProfileAndSettingsWindow(mainWindow, updateProfileWindow, dbConnection, dbCursor, username, labels)
            
            parentWindow.grid_forget()
            parentWindow.grid(sticky = (N, S, E, W))

            #createUpdateProfileAndSettingsWindow(mainWindow, parentWindow, dbConnection, dbCursor, username)
            # Show information message indicating User profile was updated
            popupBox(mainWindow, parentWindow, "Information", "User profile was successfully updated")

        except mysql.connector.Error as error:
            # Format the database error message for displaying in the popup box
            errorMessage = "Error Code: " + str(error.errno) + "\n" + "SQLSTATE: " + error.sqlstate + "\n" + "Message: " + error.msg  
            popupBox(mainWindow, updateProfileWindow, "Error", errorMessage)


def refreshUpdateProfileAndSettingsWindow(mainWindow, callingWindow, dbConnection, dbCursor, username, labels):
    userProfileInfo = getUserProfileInformation(mainWindow, callingWindow, dbConnection, dbCursor, username)
    labels[0].set(userProfileInfo[0])
    labels[1].set(userProfileInfo[1])
    labels[2].set(userProfileInfo[2])
    labels[3].set(userProfileInfo[3])
    labels[4].set(userProfileInfo[4])
    labels[5].set(userProfileInfo[5])
    labels[6].set(userProfileInfo[6])
    labels[7].set(userProfileInfo[7])

# Implementation of the Cancel button for the Update Profile & Settings window
# Closes the Update Profile & Settings window and returns to the App window
def cancelUpdateProfileAndSettingsWindow(mainWindow, parentWindow, appWindow):
    # Hide the Update Profile & Settings window
    parentWindow.grid_forget()
    
    # Show the App window
    appWindow.grid(sticky = (N, S, E, W))

def getUserProfileInformation(mainWindow, callingWindow, dbConnection, dbCursor, username):
    try:
        selectStatement = """SELECT * FROM UserInfo WHERE username = %s"""
        vals = (username,)

        # Execute the SQL SELECT statement
        dbCursor.execute(selectStatement, vals)

        # Fetch the results of the query
        userInfo = dbCursor.fetchone()

        # Create the userProfileInfo tuple
        # userProfileInfo = (fullname, birthdate, phone_number, email, gender, height, weight, image_path)
        userProfileInfo = (userInfo[2], userInfo[3], userInfo[4], userInfo[5], userInfo[6], userInfo[7], userInfo[8], userInfo[9])

        # Return the tuple (fullname, birthdate, phone_number, email, gender, height, weight, image_path)
        return userProfileInfo
    except mysql.connector.Error as error:
        # Format the database error message for displaying in the popup box
        errorMessage = "Error Code: " + str(error.errno) + "\n" + "SQLSTATE: " + error.sqlstate + "\n" + "Message: " + error.msg  
        popupBox(mainWindow, callingWindow, "Error", errorMessage)
