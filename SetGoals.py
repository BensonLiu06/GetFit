from PopupBox import *

# Implementation of Set Goals window
def createSetGoalsWindow(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Hide the App window
    parentWindow.grid_forget()

    # Create a frame for the Set Goals window
    setGoalsWindow = ttk.Frame(mainWindow, padding=(3,3,12,12))
    setGoalsWindow.grid(sticky=(N, S, E, W))

    # Setup the Set Goals window
    setGoalsWindow.columnconfigure(0, weight=1)
    setGoalsWindow.columnconfigure(1, weight=1)
    setGoalsWindow.rowconfigure(0, weight=1)
    setGoalsWindow.rowconfigure(1, weight=1)

    # Create all the main frame containers
    topFrame = ttk.Frame(setGoalsWindow, width=600, height=50, relief='groove', borderwidth=2)
    bottomFrame = ttk.Frame(setGoalsWindow, width=300, height=700, relief='groove', borderwidth=2)
    buttonFrame = ttk.Frame(setGoalsWindow, width=300, height=50, relief='groove', borderwidth=2)

    # Layout all of the main frame containers
    topFrame.grid(column=0, row=0, columnspan=2, rowspan=1, padx=5, pady=5, sticky=(N, S, E, W))
    bottomFrame.grid(column=0, row=1, columnspan=2, rowspan=1, padx=5, pady=5, sticky=(N, S, E, W))
    buttonFrame.grid(column=0, row=2, columnspan=2, rowspan=1, padx=5, pady=5, sticky=(N, S, E, W))

    topFrame.columnconfigure(0, weight=1)
    topFrame.columnconfigure(1, weight=1)
    bottomFrame.columnconfigure(0, weight=1)
    bottomFrame.columnconfigure(1, weight=1)
    buttonFrame.columnconfigure(0, weight=1)
    buttonFrame.columnconfigure(1, weight=1)

    topFrame.rowconfigure(0, weight=1)
    bottomFrame.rowconfigure(0, weight=1)
    bottomFrame.rowconfigure(1, weight=1)
    bottomFrame.rowconfigure(2, weight=1)

    # Create an information label
    informationLabel = ttk.Label(topFrame, text="Set your goals")
    informationLabel.grid(column=0, row=0, columnspan=2)

    # Create labels and Entry widgets for goal input
    goal1Label = ttk.Label(bottomFrame, text="Goal 1:")
    goal1Label.grid(column=0, row=0, padx=5, pady=5, sticky=W)
    goal1Entry = ttk.Entry(bottomFrame)
    goal1Entry.grid(column=1, row=0, padx=5, pady=5)

    goal2Label = ttk.Label(bottomFrame, text="Goal 2:")
    goal2Label.grid(column=0, row=1, padx=5, pady=5, sticky=W)
    goal2Entry = ttk.Entry(bottomFrame)
    goal2Entry.grid(column=1, row=1, padx=5, pady=5)

    goal3Label = ttk.Label(bottomFrame, text="Goal 3:")
    goal3Label.grid(column=0, row=2, padx=5, pady=5, sticky=W)
    goal3Entry = ttk.Entry(bottomFrame)
    goal3Entry.grid(column=1, row=2, padx=5, pady=5)

    # Function to save the goals
    def saveGoals():
        goals = [goal1Entry.get(), goal2Entry.get(), goal3Entry.get()]
        # Implement the code to save the goals to the database or file
        # For example, you can use the dbCursor and dbConnection objects to execute an INSERT query
        # dbCursor.execute("INSERT INTO goals (goal1, goal2, goal3) VALUES (%s, %s, %s)", goals)
        # dbConnection.commit()
        # Display a confirmation message
        popupBox(mainWindow, setGoalsWindow, "Success", "Goals saved successfully!")

    # Create button widget to Cancel the Set Goals window
    cancelButton = ttk.Button(buttonFrame, text="Cancel", command=lambda: cancelSetGoalsWindow(mainWindow, setGoalsWindow, parentWindow))
    cancelButton.grid(column=1, row=0, padx=5, pady=5)

    # Create a button widget to save the goals
    saveButton = ttk.Button(buttonFrame, text="Save Goals", command=saveGoals)
    saveButton.grid(column=0, row=0, padx=5, pady=5)


    # Call the saveGoals function
    saveGoals()

# Implementation of the Cancel button for the Set Goals window
 # Closes the Set Goals window and returns to the App window
def cancelSetGoalsWindow(mainWindow, parentWindow, appWindow):
# Hide the Set Goals window
    parentWindow.grid_forget()

    # Show the App window
    appWindow.grid(sticky=(N, S, E, W))
