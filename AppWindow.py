from tkinter import *
from tkinter import ttk
#import mysql.connector
#from mysql.connector import errorcode
from RegisterUserWindow import *
from UpdateProfileWindow import *
from SetGoals import *
from TrackActivity import *
from TrackProgress import *
from PopupBox import *

# Implementation of the app window
def createAppWindow(mainWindow, userLoginWindow, dbConnection, dbCursor, username):

    # Hide the User Login window
    userLoginWindow.grid_forget()

    # Create a frame for the main App window
    appWindow = ttk.Frame(mainWindow, padding=(3,3,12,12))
    appWindow.grid(sticky=N+S+E+W)

    # Setup the main App window
    appWindow.columnconfigure(0, weight = 1)
    appWindow.columnconfigure(1, weight = 1)
    #appWindow.rowconfigure(0, weight = 1)
    appWindow.rowconfigure(1, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(appWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(appWindow, width = 300, height = 700, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(appWindow, width = 300, height = 50, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 5, padx = 5, pady = 5, sticky=(N, S, E, W))
    buttonFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(0, weight = 1)
    bottomFrame.rowconfigure(1, weight = 1)
    bottomFrame.rowconfigure(2, weight = 1)
    bottomFrame.rowconfigure(3, weight = 1)
    bottomFrame.rowconfigure(4, weight = 1)
    buttonFrame.rowconfigure(5, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(appWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(appWindow, width = 600, height = 650, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(appWindow, width = 600, height = 100, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 9, padx = 5, pady = 5, sticky=(N, S, E, W))
    buttonFrame.grid(column = 0, row = 5, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))

    # Create label widget for information message
    label1 =ttk.Label(topFrame, text = "Signed in to GetFit", width = 20, anchor = 'center')
    label1.grid(column = 0, row = 0, pady = 5)

    # Create label widget for Username
    label2 =ttk.Label(topFrame, text = "Username: " + username, width = 20, anchor = 'center')
    label2.grid(column = 1, row = 0, pady = 5)

    # Create button widget for Profile & Settings
    updateProfileButton = ttk.Button(bottomFrame, text = "Profile & Settings", command = lambda : createUpdateProfileAndSettingsWindow(mainWindow, appWindow, dbConnection, dbCursor, username))
    updateProfileButton.grid(column = 0, row = 1, pady = 5)

    # Create button widget for Set Goals
    setGoalsButton = ttk.Button(bottomFrame, text = "Set Goals", command = lambda : createSetGoalsWindow(mainWindow, appWindow, dbConnection, dbCursor, username))
    setGoalsButton.grid(column = 0, row = 2, pady = 5)

    # Create button widget for Track Activity
    trackActivityButton = ttk.Button(bottomFrame, text = "Track Activity", command = lambda : createTrackActivityWindow(mainWindow, appWindow, dbConnection, dbCursor, username))
    trackActivityButton.grid(column = 0, row = 3, pady = 5)

    # Create button widget for Track Progress
    trackProgressButton = ttk.Button(bottomFrame, text = "Track Progress", command = lambda : createTrackProgressWindow(mainWindow, appWindow, dbConnection, dbCursor, username))
    trackProgressButton.grid(column = 0, row = 4, pady = 5)

    # Create button widget for Sign out 
    signoutButton = ttk.Button(buttonFrame, text = "Sign out", command = lambda : 
                                   signoutOfApp(mainWindow, callingWindow, appWindow))
    signoutButton.grid(column = 1, row = 5, pady = 5)

    popupBox(mainWindow, appWindow,"Information", "User login was successful")

# Implementation of Sign out button event
def signoutOfApp(mainWindow, callingWindow, appWindow):
    # Hide the App window
    appWindow.grid_forget()

    # Show the User Login window
    callingWindow.grid(sticky = (N, S, E, W))
    popupBox(mainWindow, callingWindow, "Information", "User was successfully signed out")


def updateProfileWindow(mainWindow, parentWindow, dbConnection, dbCursor, username):
    global profileWindow
    global name, age, gender, weight, height
    global nameEntry, ageEntry, genderEntry, weightEntry, heightEntry
    profileWindow = Tk()
    
    w = 600 # Width 
    h = 500 # Height
 
    # Determine the size of the screen
    screen_width =  profileWindow.winfo_screenwidth()  # Width of the screen
    screen_height = profileWindow.winfo_screenheight() # Height of the screen
     
    x = (screen_width / 2) - (w / 2)
    y = (screen_height / 2) - (h / 2)

    profileWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    profileWindow.resizable(True, True)
    profileWindow.title("User Profile")

    name = ""
    age = ""
    gender = ""
    weight = ""
    height = ""

    
    nameLabel = Label(profileWindow , text = "Full Name", width = "30")
    nameLabel.pack()

    nameEntry = Entry(profileWindow , width = "30", textvariable = name)
    nameEntry.pack()

    ageLabel = Label(profileWindow, text = "Age" , width = "30")
    ageLabel.pack()

    ageEntry = Entry(profileWindow, width = "30",  textvariable = age)
    ageEntry.pack()

    genderLabel = Label(profileWindow  , text = "Gender", width = 30)
    genderLabel.pack()

    genderEntry = Entry(profileWindow  , width = 30 , textvariable = gender)
    genderEntry.pack()

    weightLabel = Label(profileWindow  , text = "Weight", width = "30")
    weightLabel.pack()

    weightEntry = Entry(profileWindow, width = 30 , textvariable = weight)
    weightEntry.pack()

    heightLabel = Label(profileWindow, text = "Height", width = "30")
    heightLabel.pack()

    heightEntry = Entry(profileWindow, width = 30, textvariable = height)
    heightEntry.pack()

    savebutton = Button(profileWindow, text = "Save" , command = clickCommand )
    savebutton.pack()





    profileWindow.mainloop()

def clickCommand():
    nameDisplay = Label(profileWindow, text = "Name:" + nameEntry.get())
    nameDisplay.pack()

    ageDisplay = Label(profileWindow, text = "Age:" + ageEntry.get())
    ageDisplay.pack()

    genderDisplay = Label(profileWindow, text = "Gender:" + genderEntry.get())
    genderDisplay.pack()

    heightDisplay = Label(profileWindow, text = "Height:" + heightEntry.get())
    heightDisplay.pack()

    weightDisplay = Label(profileWindow, text = "Weight:" + weightEntry.get())
    weightDisplay.pack()



def workoutsWindow():
    workoutsTab = Tk()

    workout1 = Button(workoutsTab, text = "Arms Workout", padx=50)
    workout1.pack()

    
