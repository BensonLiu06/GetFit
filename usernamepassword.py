from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode

# Implementation for user registration window
def registerUserWindow(userRegistrationWindow, userLoginWindow, dbConnection, dbCursor):

    userLoginWindow.grid_forget()
    userRegistrationWindow.grid(sticky='nsew')

    username = StringVar()
    password = StringVar()
    securityQuestion = StringVar()
    securityResponse = StringVar()

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

    # Create all the main frame containers
    topFrame = Frame(userRegistrationWindow, width=590, height = 100, pady = 5)
    leftFrame = Frame(userRegistrationWindow, width = 290, height = 400, pady = 5, relief='groove', borderwidth = 2)
    rightFrame = Frame(userRegistrationWindow, width = 290, height = 400, pady = 5)

    # Layout all of the main frame containers
    topFrame.grid(row = 0, columnspan = 2, sticky = "ew")
    leftFrame.grid(column = 0, row = 3, sticky = "ew")
    rightFrame.grid(column = 1, row = 3, sticky = "ew")

    Label(topFrame, text = "To register for a GetFit profile, please enter details below").grid(row = 0, columnspan = 2)
    Label(topFrame, text = "").grid(row = 1, columnspan = 2)

    usernameLabel = Label(leftFrame, text = "Username", width = "30", anchor = 'w')
    usernameLabel.grid(column = 0, row = 2)
    usernameField = Entry(leftFrame, bd = 3, width = 30, textvariable = username)
    usernameField.grid(column = 0, row = 3)
    usernameField.focus_force() 

    passwordLabel = Label(leftFrame, text = "Password", width = "30", anchor = 'w')
    passwordLabel.grid(column = 0, row = 4)
    passwordField = Entry(leftFrame, bd = 3, width = 30, textvariable = password, show = '*')
    passwordField.grid(column = 0, row = 5)
    securityQuestionLabel = Label(leftFrame, text = "Enter a security question", width = "30", anchor = 'w')
    securityQuestionLabel.grid(column = 0, row = 6)
    securityQuestionField = Entry(leftFrame, bd = 3, width = 30, textvariable = securityQuestion)
    securityQuestionField.grid(column = 0, row = 7)
    securityResponseLabel = Label(leftFrame, text = "Enter a response to the security question", width = "30", anchor = 'w')
    securityResponseLabel.grid(column = 0, row = 8)
    securityResponseField = Entry(leftFrame, bd = 3, width = 30, textvariable = securityResponse)
    securityResponseField.grid(column = 0, row = 9)
    emptyLabel = Label(leftFrame, text = "", width = "30", anchor = 'w')
    emptyLabel.grid(column = 0, row = 10)
    registerUserButton = Button(leftFrame, text = "Register", width=10, height=1, bg="blue", command = lambda : registerUser(userRegistrationWindow, userLoginWindow, dbConnection, dbCursor, usernameField.get(), passwordField.get(), securityQuestionField.get(), securityResponseField.get(), usernameField, passwordField, securityQuestionField, securityResponseField))
    registerUserButton.grid(column = 0, row = 11)
    cancelButton = Button(leftFrame, text = "Quit", width = 10, height=1, bg="blue", command = lambda : cancelUserRegistration(userRegistrationWindow, userLoginWindow, usernameField, passwordField, securityQuestionField, securityResponseField))
    cancelButton.grid(column = 0, row = 12)

# Implementation for forgot your password button event
def forgotPassword(parentWindow):
    forgotPasswordWindow = Toplevel(parentWindow)
    forgotPasswordWindow.title("Forgot your password")

    w = 350
    h = 250
    ws = parentWindow.winfo_screenwidth()
    hs = parentWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    print(w, h, x, y)
    forgotPasswordWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Label(forgotPasswordWindow, text = "Please enter details below to reset your password", padx = 3, pady = 3).pack()
    Label(forgotPasswordWindow, text = "").pack()
    
    verifyForgotPasswordUsername = StringVar()

    Label(forgotPasswordWindow, text = "Username").pack()
    forgotUsernameField = Entry(forgotPasswordWindow, textvariable = verifyForgotPasswordUsername)
    forgotUsernameField.pack()
    Label(forgotPasswordWindow, text = "").pack()
    Button(forgotPasswordWindow, text = "Reset", width=10, height=1, command = lambda : 
           resetPassword(forgotPasswordWindow, forgotUsernameField.get())).pack()

# Implemention for register button event
def registerUser(parentWindow, userLoginWindow, dbConnection, dbCursor, username, password, securityQuestion, securityResponse, usernameField, passwordField, securityQuestionField, securityResponseField):
    if not username:
        popupBox(parentWindow, "Error", "Username is null. Please provide a valid user name")
    elif not password:
        popupBox(parentWindow, "Error", "Password is null. Please provide a valid password")

    elif not securityQuestion:
        popupBox(parentWindow, "Error", "You must provide a security question")
    elif not securityResponse:
        popupBox(parentWindow, "Error", "You must provide a security response")
    else:
        if checkUserNameExists(username, dbCursor) == False:
            vals = (username, password, securityQuestion, securityResponse)
            insert_query = "INSERT INTO `users`(`username`, `password`, `security_question`, `security_response`) VALUES (%s,%s,%s,%s)"
            dbCursor.execute(insert_query, vals)
            dbConnection.commit()

            usernameField.delete(0, END)
            passwordField.delete(0, END)
            securityQuestionField.delete(0, END)
            securityResponseField.delete(0, END)

            parentWindow.grid_forget()
            userLoginWindow.grid(sticky='nsew')
            popupBox(userLoginWindow, "Information", "User registration was successful")
            #parentWindow.destroy()

        else:
            popupBox(parentWindow, "Error", "This username already exits. Please try another username")

# Implemtation for cancel user registration button event
def cancelUserRegistration(parentWindow, userLoginWindow, usernameField, passwordField, securityQuestionField, securityResponseField):
    usernameField.delete(0, END)
    passwordField.delete(0, END)
    securityQuestionField.delete(0, END)
    securityResponseField.delete(0, END)

    parentWindow.grid_forget()
    userLoginWindow.grid(sticky='nsew')

# Implementation for login button event

def verifyLogin(parentWindow, appWindow, dbCursor, username, password, usernameLoginField, passwordLoginField):
    usernameLoginField.delete(0, END)
    passwordLoginField.delete(0, END)

    if checkUserNameExists(username, dbCursor):
        vals = (username, password,)
        select_query = "SELECT * FROM `users` WHERE `username` = %s and `password` = %s"
        dbCursor.execute(select_query, vals)
        user = dbCursor.fetchone()
        if user is not None:
            parentWindow.grid_forget()
            appWindow.grid(sticky='nsew')
            createAppWindow(appWindow, parentWindow)
            popupBox(appWindow,"Information", "User login was successful")
            
        else:
            popupBox(parentWindow, "Error", "Password was invalid")
    else:
        popupBox(parentWindow, "Error", "Username was not found")
    
# Create a funciton to reset the users password
def resetPassword(parentWindow, username):
    i = 1

# Create a function to check if the username already exists
def checkUserNameExists(username, dbCursor):
    vals = (username,)
    select_query = "SELECT * FROM `users` WHERE `username` = %s"
    dbCursor.execute(select_query, vals)
    user = dbCursor.fetchone()
    if user is not None:
        return True
    else:
        return False

def changePassword():
    #
    i = 0

# Implementation for a generic popup dialog box
def popupBox(parentWindow, windowTitle, messageText):
    popupBoxWindow = Toplevel(parentWindow)
    popupBoxWindow.title(windowTitle)

    # Calculate the geometry to center the dialog box on the screen
    w = popupBoxWindow.winfo_reqwidth()
    h = popupBoxWindow.winfo_reqheight()
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    popupBoxWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Label(popupBoxWindow, text = messageText, padx = '3', pady = '3').pack(expand = YES, fill = BOTH)
    Button(popupBoxWindow, text = "OK", command = lambda : popupBoxWindow.destroy()).pack()

# Implementation of login window
def createLoginWindow(userLoginWindow, registrationWindow, appWindow, dbConnection, dbCursor):
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
    topFrame = Frame(userLoginWindow, width=590, height = 100, pady = 5)
    leftFrame = Frame(userLoginWindow, width = 290, height = 400, pady = 5, relief='groove', borderwidth = 2)
    rightFrame = Frame(userLoginWindow, width = 290, height = 400, pady = 5, relief='groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(row = 0, columnspan = 2, sticky = "ew")
    leftFrame.grid(column = 0, row = 1, sticky = "nsew")
    rightFrame.grid(column = 1, row = 1, sticky = "nsew")

    # Create label widget
    signinLabel = Label(topFrame, text = "Sign in to GetFit", width = 20, anchor = 'center')
    signinLabel.grid(row = 0, columnspan = 2)

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
                                      forgotPassword(userLoginWindow))
    forgotYourPasswordButton.grid(column = 0, row = 7)

    # Create label widget
    emptyLabel2 = Label(leftFrame,text = "", width = "30", anchor = 'w')
    emptyLabel2.grid(column = 0, row = 8)

    # Create button widget for sign in
    signinButton = Button(leftFrame, text = "Sign in", command = lambda : 
                          verifyLogin(userLoginWindow, appWindow, dbCursor, username.get(), password.get(), usernameField, passwordField))
    signinButton.grid(column = 0, row = 9)
    
    # Create button widget to register a new user
    registerNewUserButton = Button(rightFrame, text = "Register a new user", command = lambda : 
                                   registerUserWindow(registrationWindow, userLoginWindow, dbConnection, dbCursor))
    registerNewUserButton.grid(column = 1, row = 8)

# Implementation of app window
def createAppWindow(appWindow, userLoginWindow):
    appWindow.grid(sticky='nsew')
    
    # Create label widget
    label1 = Label(appWindow, text = "Signed in to GetFit", width = 20, anchor = 'center')
    label1.grid(column = 0, row = 0)
    
    # Create button widget to sign out 
    signoutButton = Button(appWindow, text = "Sign out", command = lambda : 
                                   signoutOfApp(appWindow, userLoginWindow))
    signoutButton.grid(column = 0, row = 1)

def signoutOfApp(appWindow, userLoginWindow):
    appWindow.grid_forget()
    userLoginWindow.grid(sticky='nsew')
    popupBox(userLoginWindow, "Information", "User was successfully signed out")

# Implementation of main window

def mainAppWindow():
    global mainWindow
    # Create an instance of tkinter frame or window
    mainWindow = Tk()

    try:
        dbConnection = mysql.connector.connect(host='localhost', user='root', port='3306', password='', database='GetFitdb')
        dbCursor = dbConnection.cursor()
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            dbConnection.close()
        
    # Set the width and height of the main window
    w = 600 # Width 
    h = 500 # Height
 
    # Determine the size of the screen
    screen_width =  mainWindow.winfo_screenwidth()  # Width of the screen
    screen_height = mainWindow.winfo_screenheight() # Height of the screen
 
    # Calculate starting x and y coordinates to center the main window on the screen
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
 
    mainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    mainWindow.resizable(True, True)
    mainWindow.title("GetFit")

    # Create three frames in the window

    # Create a frame for the main app window
    appWindow = Frame(mainWindow)
    appWindow.grid(sticky='nsew')
    appWindow.grid_forget()

    # Create a frame for the user registration window
    userRegistrationWindow = Frame(mainWindow)
    userRegistrationWindow.grid(sticky='nsew')
    userRegistrationWindow.grid_forget()

    # Create a frame for the user login window
    userLoginWindow = Frame(mainWindow)
    userLoginWindow.grid(sticky='nsew')

    createLoginWindow(userLoginWindow, userRegistrationWindow, appWindow, dbConnection, dbCursor)

    mainWindow.mainloop()

mainAppWindow()
