import tkinter as tk
from tkinter.ttk import Entry, Label



def user_profile(profileWindow):
    profileWindow = tk()

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


def userErrors(nameEntry, genderEntry, weightEntry, heightEntry):
    if len(nameEntry > 50):
        print("Name cannot be more than 50 letters, Use a nickname if you must.")
    elif len(nameEntry < 1):
        print("Please Enter a Name.")


    