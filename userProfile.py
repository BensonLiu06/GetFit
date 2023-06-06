import tkinter as tk
from tkinter.ttk import Entry, Label


def updateProfileWindow(profileWindow):

    profileWindow = tk()
    w = 600 # Width 
    h = 500 # Height
 
    # Determine the size of the screen
    screen_width =  profileWindow.winfo_screenwidth()  # Width of the screen
    screen_height = profileWindow.winfo_screenheight() # Height of the screen
 
    # Calculate starting x and y coordinates to center the main window on the screen
    x = (screen_width / 2) - (w / 2)
    y = (screen_height / 2) - (h / 2)
 
    profileWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    profileWindow.resizable(True, True)
    profileWindow.title("User Profile")

    name = ""
    gender = ""
    weight = ""
    height = ""

    
    nameLabel = Label(profileWindow , text = "Full Name", width = "30")
    nameLabel.pack()

    nameEntry = Entry(profileWindow , width = "30", textvariable = name)
    nameEntry.pack()

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

