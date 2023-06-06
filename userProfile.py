import tkinter as Tk
from tkinter.ttk import Entry, Label


def updateProfileWindow(profileWindow):

    profileWindow = Tk()
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
    nameLabel.grid(column = 0, row = 2, columnspan = 2)

    nameEntry = Entry(profileWindow , bd = 3, width = 30, textvariable = name)
    nameEntry.grid(column = 0, row = 3, columnspan = 2 )

    genderLabel = Label(profileWindow  , text = "Gender", width = "30")
    genderLabel.grid (column = 0 , row = 2, columnspan = 2)

    genderEntry = Entry(profileWindow  , bd = 3, width = 30 , textvariable = gender)
    genderEntry.grid(column = 0, row = 3, columnspan = 2)

    weightLabel = Label(profileWindow  , text = "Weight", width = "30")
    weightLabel.grid(column = 0 , row = 3, columnspan = 2)

    weightEntry = Entry(profileWindow, bd = 3, width = 30 , textvariable = weight)
    weightEntry.grid(column = 0 , row = 3, columnspan = 2)

    heightLabel = Label(profileWindow, text = "Height", width = "30")
    heightLabel.grid(column = 0, row = 2, columnspan = 2)

    heightEntry = Entry(profileWindow, bd = 3, width = 30, textvariable = height)
    heightEntry.grid(column = 0, row = 3, columnspan = 2)

