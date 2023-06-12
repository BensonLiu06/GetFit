from PopupBox import *
# Implementation of Track Activity window
def createTrackActivityWindow(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Hide the App window
    parentWindow.grid_forget()

    # Create a frame for the Track Activity window
    trackActivityWindow = ttk.Frame(mainWindow, padding=(3,3,12,12))
    trackActivityWindow.grid(sticky = (N, S, E, W))

    # Setup the User Registration window
    trackActivityWindow.columnconfigure(0, weight = 1)
    trackActivityWindow.columnconfigure(1, weight = 1)
    trackActivityWindow.rowconfigure(0, weight = 1)
    trackActivityWindow.rowconfigure(1, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(trackActivityWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(trackActivityWindow, width = 300, height = 700, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(trackActivityWindow, width = 300, height = 50, relief = 'groove', borderwidth = 2)

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
    buttonFrame.rowconfigure(12, weight = 1)

    # Create an information label 
    informationLabel =ttk.Label(topFrame, text = "Track your activity")
    informationLabel.grid(column = 0, row = 0, columnspan = 2)

    # Create an information label 
    informationLabel2 =ttk.Label(bottomFrame, text = "Danger - Construction Area - Keep Out")
    informationLabel2.grid(column = 0, row = 1, columnspan = 2)


    popupBox(mainWindow, trackActivityWindow, "Warning", "Track Activity Window implementation incomplete")
    
    # Create button widget to Cancel the Update Profile & Settings window
    cancelButton = ttk.Button(buttonFrame, text = "Cancel", command = lambda : 
                                   cancelTrackActivityWindow(mainWindow, trackActivityWindow, parentWindow))
    cancelButton.grid(column = 1, row = 12, pady = 5)

# Implementation of the Cancel button for the Track Activity window
# Closes the Track Activity window and returns to the App window
def cancelTrackActivityWindow(mainWindow, parentWindow, appWindow):
    # Hide the Track Progress window
    parentWindow.grid_forget()

    # Show the App window
    appWindow.grid(sticky = (N, S, E, W))