import mysql.connector
from PopupBox import *

# Connect to the database and create the necessary tables
dbConnection, dbCursor = accessDatabase(mainWindow, dbHostname, dbUsername, dbPort, dbPassword, dbName)

# Function to retrieve goals from the database for a specific user
def getGoals(dbCursor, username):
    dbCursor.execute("SELECT goal FROM goals WHERE username = %s", (username,))
    goals = dbCursor.fetchall()
    return goals

# Function to display the goals in the goals window
def displayGoals(goalsList, goalsFrame):
    for widget in goalsFrame.winfo_children():
        widget.destroy()

    for index, goal in enumerate(goalsList):
        goalLabel = ttk.Label(goalsFrame, text=f"{index+1}. {goal}")
        goalLabel.pack(anchor='w')

# Function to add a new goal
def addGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, goalsFrame):
    goal = popupInputBox(mainWindow, goalsWindow, "Add Goal", "Enter the goal:")
    if goal:
        goalsList.append(goal)
        dbCursor.execute("INSERT INTO goals (username, goal) VALUES (%s, %s)", (username, goal))
        dbConnection.commit()
        displayGoals(goalsList, goalsFrame)

# Function to change a goal
def changeGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, goalsFrame):
    oldGoal = popupOptionBox(mainWindow, goalsWindow, "Change Goal", "Select the goal to change:", goalsList)
    if oldGoal:
        newGoal = popupInputBox(mainWindow, goalsWindow, "Change Goal", "Enter the new goal:")
        if newGoal:
            goalsList.remove(oldGoal)
            goalsList.append(newGoal)
            dbCursor.execute("UPDATE goals SET goal = %s WHERE username = %s AND goal = %s", (newGoal, username, oldGoal))
            dbConnection.commit()
            displayGoals(goalsList, goalsFrame)

# Function to delete a goal
def deleteGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, goalsFrame):
    goal = popupOptionBox(mainWindow, goalsWindow, "Delete Goal", "Select the goal to delete:", goalsList)
    if goal:
        goalsList.remove(goal)
        dbCursor.execute("DELETE FROM goals WHERE username = %s AND goal = %s", (username, goal))
        dbConnection.commit()
        displayGoals(goalsList, goalsFrame)

# Function to mark a goal as complete
def completeGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, goalsFrame):
    goal = popupOptionBox(mainWindow, goalsWindow, "Complete Goal", "Select the goal to mark as complete:", goalsList)
    if goal:
        goalsList.remove(goal)
        dbCursor.execute("DELETE FROM goals WHERE username = %s AND goal = %s", (username, goal))
        dbConnection.commit()
        displayGoals(goalsList, goalsFrame)

# Function to create the goals window
def createGoalsWindow(mainWindow, parentWindow, dbConnection, dbCursor, username):
    parentWindow.grid_forget()

    goalsWindow = ttk.Frame(mainWindow, padding=(3, 3, 12, 12))
    goalsWindow.grid(sticky=(N, S, E, W))

    goalsWindow.columnconfigure(0, weight=1)
    goalsWindow.rowconfigure(0, weight=1)

    scrollFrame = ScrollableFrame(goalsWindow)
    scrollFrame.grid(row=0, column=0, sticky=(N, S, E, W))

    mainFrame = ttk.Frame(goalsWindow)
    mainFrame.grid(row=1, column=0, pady=10)

    backButton = ttk.Button(mainFrame, text="Back", command=lambda: backButtonClicked(mainWindow, goalsWindow, parentWindow))
    backButton.pack()

    goalsList = getGoals(dbCursor, username)
    displayGoals(goalsList, scrollFrame.scrollable_frame)

    addButton = ttk.Button(mainFrame, text="Add Goal", command=lambda: addGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, scrollFrame.scrollable_frame))
    addButton.pack()

    changeButton = ttk.Button(mainFrame, text="Change Goal", command=lambda: changeGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, scrollFrame.scrollable_frame))
    changeButton.pack()

    deleteButton = ttk.Button(mainFrame, text="Delete Goal", command=lambda: deleteGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, scrollFrame.scrollable_frame))
    deleteButton.pack()

    completeButton = ttk.Button(mainFrame, text="Complete Goal", command=lambda: completeGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, scrollFrame.scrollable_frame))
    completeButton.pack()

    def backButtonClicked(mainWindow, currentWindow, parentWindow):
        currentWindow.grid_forget()
        parentWindow.grid()

    goalsWindow.grid()

# Usage:
createGoalsWindow(mainWindow, setGoalsWindow, dbConnection, dbCursor, username)
