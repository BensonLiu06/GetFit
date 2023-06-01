from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode


import os

# Implementation for user registration window
def registerUserWindow(parentWindow):
    #global userRegistrationWindow
    userRegistrationWindow = Toplevel(parentWindow)
    userRegistrationWindow.title("Register")

    w = 300
    h = 400
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    print(w, h, x, y)
    userRegistrationWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    global usernameField
    global passwordField
    global securityQuestionField
    global securityResponseField

    username = StringVar()
    password = StringVar()
    securityQuestion = StringVar()
    securityResponse = StringVar()

    Label(userRegistrationWindow, text = "To register for a GetFit profile,", bg="blue").pack()
    Label(userRegistrationWindow, text = "please enter details below", bg="blue").pack()
    Label(userRegistrationWindow, text = "").pack()
    usernameLabel = Label(userRegistrationWindow, text = "Username")
    usernameLabel.pack()
    usernameField = Entry(userRegistrationWindow, textvariable = username)
    usernameField.pack()
    passwordLabel = Label(userRegistrationWindow, text = "Password")
    passwordLabel.pack()
    passwordField = Entry(userRegistrationWindow, textvariable = password, show = '*')
    passwordField.pack()
    securityQuestionLabel = Label(userRegistrationWindow, text = "Enter a security question")
    securityQuestionLabel.pack()
    securityQuestionField = Entry(userRegistrationWindow, textvariable = securityQuestion)
    securityQuestionField.pack()
    securityResponseLabel = Label(userRegistrationWindow, text = "Enter a response to the security question")
    securityResponseLabel.pack()
    securityResponseField = Entry(userRegistrationWindow, textvariable = securityResponse)
    securityResponseField.pack()
    Label(userRegistrationWindow, text = "").pack()
    registerUserButton = Button(userRegistrationWindow, text = "Register", width=10, height=1, bg="blue",
           command = lambda : registerUser(parentWindow, usernameField.get(), passwordField.get(), securityQuestionField.get(), securityResponseField.get()))
    registerUserButton.pack()

# Implementation for forgot your password button event
def forgotPassword(parentWindow):
    global forgotPasswordWindow
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
    
    global verifyForgotPasswordUsername
    verifyForgotPasswordUsername = StringVar()

    global forgotUsernameField

    Label(forgotPasswordWindow, text = "Username").pack()
    forgotUsernameField = Entry(forgotPasswordWindow, textvariable = verifyForgotPasswordUsername)
    forgotUsernameField.pack()
    Label(forgotPasswordWindow, text = "").pack()
    Button(forgotPasswordWindow, text = "Reset", width=10, height=1, command = lambda : 
           resetPassword(forgotPasswordWindow, forgotUsernameField.get())).pack()

# Implemention for register button event
def registerUser(parentWindow, username, password, securityQuestion, securityResponse):

    if not username:
        #userNameIsNull(parentWindow)
        popupBox(parentWindow, "Error", "Username is null. Please provide a valid user name")
    elif not password:
        #passwordIsNull(parentWindow)
        popupBox(parentWindow, "Error", "Password is null. Please provide a valid password")

    elif not securityQuestion:
        popupBox(parentWindow, "Error", "You must provide a security question")
        #messagebox.showwarning('Error','You must provide a security question')
    elif not securityResponse:
        #messagebox.showwarning('Error', 'You must provide a response to the security question')
        popupBox(parentWindow, "Error", "You must provide a security response")
    else:
        if checkUserNameExists(username) == False:
            vals = (username, password, securityQuestion, securityResponse)
            insert_query = "INSERT INTO `users`(`username`, `password`, `security_question`, `security_response`) VALUES (%s,%s,%s,%s)"
            dbCursor.execute(insert_query, vals)
            dbConnection.commit()

            usernameField.delete(0, END)
            passwordField.delete(0, END)
            securityQuestionField.delete(0, END)

            parentWindow.destroy()
            #userRegistrationSucessful(parentWindow)
            popupBox(parentWindow, "Information", "User registration was successful")
        else:
            #messagebox.showwarning('Duplicate Username','This Username Already Exists, try another Username')
            popupBox(parentWindow, "Error", "This username already exits. Please try another username")

# Implementation for login button event

def verifyLogin(parentWindow, username, password):
    #username1 = verifyUsername.get().strip()
    #password1 = verifyPassword.get().strip()
    #parentWindow.usernameLoginField.delete(0, END)
    #parentWindow.passwordLoginField.delete(0, END)

    if checkUserNameExists(username):
        vals = (username, password,)
        select_query = "SELECT * FROM `users` WHERE `username` = %s and `password` = %s"
        dbCursor.execute(select_query, vals)
        user = dbCursor.fetchone()
        if user is not None:
            #loginSucessful(parentWindow)
            popupBox(parentWindow,"Information", "User login was successful")
        else:
            #invalidPassword(parentWindow)
            popupBox(parentWindow, "Error", "Password was invalid")
    else:
        #userNotFound(parentWindow)
        popupBox(parentWindow, "Error", "Username was not found")
    
# Create a funciton to reset the users password
def resetPassword(parentWindow, username):
    i = 1

# Create a function to check if the username already exists
def checkUserNameExists(username):
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
def createLoginWindow(loginWindow):

    loginWindow.columnconfigure(0, weight = 1)
    loginWindow.columnconfigure(1, weight = 1)
    loginWindow.rowconfigure(0, weight = 1)
    loginWindow.rowconfigure(1, weight = 1)
    loginWindow.rowconfigure(2, weight = 1)
    loginWindow.rowconfigure(3, weight = 1)
    loginWindow.rowconfigure(4, weight = 1)
    loginWindow.rowconfigure(5, weight = 1)
    loginWindow.rowconfigure(6, weight = 1)
    loginWindow.rowconfigure(7, weight = 1)
    loginWindow.rowconfigure(8, weight = 1)

    # Create all the main frame containers
    topFrame = Frame(loginWindow, width=590, height = 100, pady = 5)
    leftFrame = Frame(loginWindow, width = 290, height = 300, pady = 5, relief='groove', borderwidth = 2)
    rightFrame = Frame(loginWindow, width = 290, height = 300, pady = 5, relief='groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(row = 0, columnspan = 2, sticky = "ew")
    leftFrame.grid(column = 0, row = 1, sticky = "nsew")
    rightFrame.grid(column = 1, row = 1, sticky = "nsew")

    # Create label widget
    label1 = Label(topFrame, text = "Sign in to GetFit", width = 20, anchor = 'center')
    label1.grid(row = 0, columnspan = 2)

    # Create label widget
    label2 = Label(leftFrame, text = "Username", width = "30", anchor = 'w')
    label2.grid(column = 0, row = 1)

    global verifyUsername
    global verifyPassword

    verifyUsername = StringVar()
    verifyPassword = StringVar()

    global userNameField
    global usernameLoginField

    # Create entry widget
    userNameField = Entry(leftFrame, textvariable = verifyUsername, bd = 3, width = 30)
    userNameField.grid(column = 0, row = 2)
    userNameField.anchor = 'w'
    userNameField.focus_force() 
    usernameLoginField = userNameField

    # Create label widget
    label3 = Label(leftFrame, text = "Enter your username", width = "30", anchor = 'w')
    label3.grid(column = 0, row = 3)
    
    # Create label widget
    label4 = Label(leftFrame,text = "", width = "30", anchor = 'w')
    label4.grid(column = 0,row = 4)

    # Create label widget
    label5 = Label(leftFrame,text = "Password", width = "30", anchor = 'w')
    label5.grid(column = 0, row = 5)

    global passwordField
    global passwordLoginField

    # Create entry widget
    passwordField = Entry(leftFrame, bd = 3, width = 30, textvariable = verifyPassword, show = '*')
    passwordField.grid(column = 0, row = 6)
    passwordLoginField = passwordField

    # Create button widget for forgot your password
    forgotYourPasswordButton = Button(leftFrame, text = "Forgot your password?", command = lambda : 
                                      forgotPassword(loginWindow))
    forgotYourPasswordButton.grid(column = 0, row = 7)

    # Create label widget
    label6 = Label(leftFrame,text = "", width = "30", anchor = 'w')
    label6.grid(column = 0, row = 8)

    # Create button widget for sign in
    signinButton = Button(leftFrame, text = "Sign in", command = lambda : 
                          verifyLogin(loginWindow, verifyUsername.get(), verifyPassword.get()))
    signinButton.grid(column = 0, row = 9)
    
    # Create button widget to register a new user
    registerNewUserbutton = Button(rightFrame, text = "Register a new user", command = lambda : 
                                   registerUserWindow(loginWindow))
    registerNewUserbutton.grid(column = 1, row = 8)


# Implementation of main window

def mainAppWindow():
    global mainWindow
    # Create an instance of tkinter frame or window
    mainWindow = Tk()

    try:
        global dbConnection
        dbConnection = mysql.connector.connect(host='localhost', user='root', port='3306', password='', database='GetFitdb')
        global dbCursor
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
    h = 400 # Height
 
    # Determine the size of the screen
    screen_width =  mainWindow.winfo_screenwidth()  # Width of the screen
    screen_height = mainWindow.winfo_screenheight() # Height of the screen
 
    # Calculate starting x and y coordinates to center the main window on the screen
    x = (screen_width/2) - (w/2)
    y = (screen_height/2) - (h/2)
 
    mainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    mainWindow.resizable(True, True)
    mainWindow.title("GetFit")

    # Create two frames in the window
    appWindow = Frame(mainWindow)
    appWindow.pack(fill='both', expand=1)
    appWindow.forget()

    loginWindow = Frame(mainWindow)
    loginWindow.pack(fill='both', expand=1)

    createLoginWindow(loginWindow)


    mainWindow.mainloop()

mainAppWindow()
