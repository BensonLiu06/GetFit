from tkinter import *
from tkinter import ttk
from PopupBox import *
import mysql.connector

# Establish a database connection
dbConnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="GetFitDB"
)

# Create a cursor object
dbCursor = dbConnection.cursor()

# Implementation of Set Goals window
def createSetGoalsWindow(mainWindow, parentWindow, dbConnection, dbCursor, username):
    # Hide the App window
    parentWindow.grid_forget()

    # Function to add a goal
    def addGoal(entry, frame):
        goal = entry.get()
        if goal and len(frame.winfo_children()) < 50:
            entry.delete(0, END)
            insertGoal(goal, frame)
    # Create a frame for the Set Goals window
    setGoalsWindow = ttk.Frame(mainWindow, padding=(3, 3, 12, 12))
    setGoalsWindow.grid(sticky=(N, S, E, W))

    # Setup the Set Goals window
    setGoalsWindow.columnconfigure(0, weight=1)
    setGoalsWindow.rowconfigure(0, weight=1)

    # Create a top frame for the heading and goal input
    topFrame = ttk.Frame(setGoalsWindow)
    topFrame.grid(row=0, column=0, sticky=(N, W, E))

    # Create a label for the heading
    headingLabel = ttk.Label(topFrame, text="Goals", font=('TkDefaultFont', 30, 'bold'))
    headingLabel.grid(row=0, column=0, padx=10, pady=10)

    # Create an entry box for goal input
    goalEntry = ttk.Entry(topFrame)
    goalEntry.grid(row=1, column=0, padx=10, pady=10, sticky=(W, E))

    # Create a confirm button to add the goal
    confirmButton = ttk.Button(topFrame, text="Confirm", command=lambda: addGoal(goalEntry, goalsFrame))
    confirmButton.grid(row=1, column=1, padx=10, pady=10, sticky=(W, E))

    # Create a bottom frame for displaying goals and the Save button
    bottomFrame = ttk.Frame(setGoalsWindow)
    bottomFrame.grid(row=1, column=0, sticky=(N, S, E, W))

    # Create a scrollable frame for displaying goals
    scrollFrame = ScrollableFrame(bottomFrame)
    scrollFrame.grid(sticky=(N, S, E, W))

    # Function to insert a goal into the database and update the display
    def insertGoal(goal, frame):
        sql = "INSERT INTO goals (goal_text, completed) VALUES (%s, %s)"
        values = (goal, False)
        dbCursor.execute(sql, values)
        dbConnection.commit()
        goalId = dbCursor.lastrowid

        goalLabel = ttk.Label(frame, text=f"{goalId}. {goal}", foreground="red")
        goalLabel.grid(row=goalId-1, column=0, sticky='w')

        completeButton = ttk.Button(frame, text="Complete", command=lambda idx=goalId: markGoalComplete(idx, frame))
        completeButton.grid(row=goalId-1, column=1, padx=5)

    # Function to update the completion status of a goal in the database and update the display
    def markGoalComplete(goalId, frame):
        sql = "UPDATE goals SET completed = %s WHERE goal_id = %s"
        values = (True, goalId)
        dbCursor.execute(sql, values)
        dbConnection.commit()

        goalLabel = frame.grid_slaves(row=goalId-1, column=0)[0]
        goalLabel.configure(foreground="green")

    # Function to load goals from the database and populate the display
    def loadGoals(frame):
        sql = "SELECT goal_id, goal_text, completed FROM goals"
        dbCursor.execute(sql)
        goals = dbCursor.fetchall()

        for goal in goals:
            goalId, goalText, completed = goal
            goalLabel = ttk.Label(frame, text=f"{goalId}. {goalText}", foreground="green" if completed else "red")
            goalLabel.grid(row=goalId-1, column=0, sticky='w')

            completeButton = ttk.Button(frame, text="Complete", command=lambda idx=goalId: markGoalComplete(idx, frame))
            completeButton.grid(row=goalId-1, column=1, padx=5)

    # Create the goals frame
    goalsFrame = ttk.Frame(scrollFrame.scrollable_frame)
    goalsFrame.grid(sticky=(N, W, E))

    # Configure the goals frame
    goalsFrame.columnconfigure(0, weight=1)
    goalsFrame.columnconfigure(1, weight=0)
    goalsFrame.rowconfigure(0, weight=1)

    # Load goals from the database
    loadGoals(goalsFrame)

    # Function to save goals and return to the main window
    def saveGoals():
        # Hide the Set Goals window
        setGoalsWindow.grid_forget()

        # Show the App window
        parentWindow.grid(sticky=(N, S, E, W))

    # Create a button frame for Save and Cancel buttons
    buttonFrame = ttk.Frame(setGoalsWindow)
    buttonFrame.grid(row=2, column=0, sticky=(N, W, E))

    # Create a Save button
    saveButton = ttk.Button(buttonFrame, text="Save", command=saveGoals)
    saveButton.grid(row=0, column=0, padx=10, pady=10, sticky=(W, E))

    # Create a Cancel button
    cancelButton = ttk.Button(buttonFrame, text="Cancel", command=lambda: cancelSetGoalsWindow(mainWindow, setGoalsWindow, parentWindow))
    cancelButton.grid(row=0, column=1, padx=10, pady=10, sticky=(W, E))

# Implementation of the Cancel button for the Set Goals window
# Closes the Set Goals window and returns to the App window
def cancelSetGoalsWindow(mainWindow, parentWindow, appWindow):
    # Hide the Set Goals window
    parentWindow.grid_forget()

    # Show the App window
    appWindow.grid(sticky=(N, S, E, W))

# A custom scrollable frame class
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # Create a vertical scrollbar
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.grid(row=0, column=1, sticky=(N, S))

        # Create a canvas to hold the scrollable frame
        canvas = Canvas(self, yscrollcommand=vscrollbar.set)
        canvas.grid(row=0, column=0, sticky=(N, S, E, W))

        # Link the scrollbar to the canvas
        vscrollbar.config(command=canvas.yview)

        # Create a scrollable frame inside the canvas
        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Add the scrollable frame to the canvas
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configure the grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

# Create the main window and other necessary components
mainWindow = Tk()
parentWindow = ttk.Frame(mainWindow)
dbConnection = None  # Replace with your database connection
dbCursor = None  # Replace with your database cursor
username = ""  # Replace with the user's username

# Call the function to create the Set Goals window
createSetGoalsWindow(mainWindow, parentWindow, dbConnection, dbCursor, username)

# Start the main loop
mainWindow.mainloop()
