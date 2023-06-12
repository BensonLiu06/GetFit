from tkinter import *
from tkinter import ttk
import re
from AppWindow import *
from PopupBox import *
from CheckUserNameExists import *
from PasswordHash import *

def createResetPasswordBox(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Create StringVars to hold the user input
    password = StringVar()
    confirmPassword = StringVar()

    # Create a toplevel window for the Reset Password dialog box
    resetPasswordWindow = Toplevel(parentWindow)
    resetPasswordWindow.title("Reset Password")

    # Create an information label widget
    informationLabel =ttk.Label(resetPasswordWindow, text = "Please enter details below to reset your password")
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create an empty label widget for padding
    emptyLabel1 =ttk.Label(resetPasswordWindow, text = "")
    emptyLabel1.grid(column = 0, row = 1, columnspan = 2)

    # Create label widget for Password
    userLabel =ttk.Label(resetPasswordWindow, text = "Resetting password for " + username, width = "30", anchor = 'w')
    userLabel.grid(column = 0, row = 2, columnspan = 2)

    # Create label widget for Password
    passwordLabel =ttk.Label(resetPasswordWindow, text = "Password", width = "30", anchor = 'w')
    passwordLabel.grid(column = 0, row = 3, columnspan = 2)

    # Create entry widget for Password
    passwordField = ttk.Entry(resetPasswordWindow, width = 30, textvariable = password, show = '*')
    passwordField.grid(column = 0, row = 4, columnspan = 2)

    # Create label widget for Confirm Password
    confirmPasswordLabel =ttk.Label(resetPasswordWindow, text = "Confirm password", width = "30", anchor = 'w')
    confirmPasswordLabel.grid(column = 0, row = 5, columnspan = 2)

    # Create entry widget for Confirm Password
    confirmPasswordField = ttk.Entry(resetPasswordWindow, width = 30, textvariable = confirmPassword, show = '*')
    confirmPasswordField.grid(column = 0, row = 6, columnspan = 2)

    # Create button widget for OK
    oKButton = ttk.Button(resetPasswordWindow, text = "OK", width=10, command = lambda : verifyAndResetPassword(mainWindow, parentWindow, resetPasswordWindow, dbConnection, dbCursor, username, passwordField.get(), confirmPasswordField.get()))
    oKButton.grid(column = 0, row = 7)

    # Create button widget for Cancel
    cancelButton = ttk.Button(resetPasswordWindow, text = "Cancel", width = 10, command = lambda : resetPasswordWindow.destroy())
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
    # Define a regular expression to check that the password meets the following criteria:
    #   - Is a minimum of 8 characters in length. Adjust it by modifying {8,}
    #   - Has at least one uppercase English letter. You can remove this condition by removing (?=.*?[A-Z])
    #   - Has at least one lowercase English letter. You can remove this condition by removing (?=.*?[a-z])
    #   - Has at least one digit. You can remove this condition by removing (?=.*?[0-9])
    #   - Has at least one special character. You can remove this condition by removing (?=.*?[#?!@$%^&*-])
    passwordPattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

    if (re.match(passwordPattern,password) == None):
        popupBox(mainWindow,parentWindow, "Error", "Password must be a minimum of 8 characters long\nPassword must have at least one uppercase English letter\nPassword must have at least one lowercase English letter\nPassword must have at least one digit\nPassword must have at least one special character such as #?!@$%^&*-\n")
    elif password == confirmPassword:
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


def confirmPassword(mainWindow, parentWindow, dbConnection, dbCursor, username, password):
    if checkUsernameExists(username, dbCursor):
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

def passwordCheck(mainWindow, parentWindow, dbConnection, dbCursor, username, password):
    if checkUsernameExists(username, dbCursor):
        selectStatement = """SELECT * FROM User WHERE username = %s"""
        vals = (username,)
        dbCursor.execute(selectStatement, vals)

        user = dbCursor.fetchone()
        passwordHash = user[2]

        if (comparePassword(password,passwordHash)):
            return True
        else:
            popupBox(mainWindow, parentWindow, "Error", "Password was invalid")
            return False
    else:
        popupBox(mainWindow, parentWindow, "Error", "Username was not found")
        return False

