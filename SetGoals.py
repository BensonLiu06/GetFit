import mysql.connector
from PopupBox import *

# Function to connect to the database and return the connection and cursor objects
def accessDatabase(hostname, username, port, password, dbname):
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            port=port,
            password=password,
            database=dbname
        )
        cursor = connection.cursor()
        return connection, cursor
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Please check your credentials.")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Error: The specified database does not exist.")
        else:
            print(f"Error: {err}")
        return None, None

# Update the code to call the accessDatabase function with the appropriate parameters
dbHostname = "your_hostname"
dbUsername = "your_username"
dbPort = "your_port"
dbPassword = "your_password"
dbName = "your_database_name"

dbConnection, dbCursor = accessDatabase(dbHostname, dbUsername, dbPort, dbPassword, dbName)

# Function to retrieve goals from the database for a specific user
def getGoals(dbCursor, username):
    dbCursor.execute("SELECT goal, completed FROM goals WHERE username = %s", (username,))
    goals = dbCursor.fetchall()
    return goals

# Function to display the goals in the goals window
def displayGoals(goalsList, goalsFrame):
    for widget in goalsFrame.winfo_children():
        widget.destroy()

    for index, (goal, completed) in enumerate(goalsList):
        goalLabel = ttk.Label(goalsFrame, text=f"{index+1}. {goal}")
        goalLabel.grid(row=index, column=0, sticky='w')
        if completed:
            completedLabel = ttk.Label(goalsFrame, text="Completed")
            completedLabel.grid(row=index, column=1, sticky='e')

# Function to add a new goal
def addGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, goalsFrame):
    goal = popupInputBox(mainWindow, goalsWindow, "Add Goal", "Enter the goal:")
    if goal:
        goalsList.append((goal, False))
        dbCursor.execute("INSERT INTO goals (username, goal, completed) VALUES (%s, %s, %s)", (username, goal, False))
        dbConnection.commit()
        displayGoals(goalsList, goalsFrame)

# Function to change a goal
def changeGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, goalsFrame):
    oldGoal = popupOptionBox(mainWindow, goalsWindow, "Change Goal", "Select the goal to change:", goalsList)
    if oldGoal:
        newGoal = popupInputBox(mainWindow, goalsWindow, "Change Goal", "Enter the new goal:")
        if newGoal:
            goalsList.remove(oldGoal)
            goalsList.append((newGoal, oldGoal[1]))
            dbCursor.execute("UPDATE goals SET goal = %s WHERE username = %s AND goal = %s", (newGoal, username, oldGoal[0]))
            dbConnection.commit()
            displayGoals(goalsList, goalsFrame)

# Function to mark a goal as complete
def completeGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, goalsFrame):
    goal = popupOptionBox(mainWindow, goalsWindow, "Complete Goal", "Select the goal to mark as complete:", goalsList)
    if goal:
        completedGoal = (goal[0], True)
        goalsList.remove(goal)
        goalsList.append(completedGoal)
        dbCursor.execute("UPDATE goals SET completed = %s WHERE username = %s AND goal = %s", (True, username, goal[0]))
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
    backButton.grid(row=0, column=0, sticky='w')

    goalsList = getGoals(dbCursor, username)
    displayGoals(goalsList, scrollFrame.scrollable_frame)

    addButton = ttk.Button(mainFrame, text="Add Goal", command=lambda: addGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, scrollFrame.scrollable_frame))
    addButton.grid(row=1, column=0, sticky='w')

    changeButton = ttk.Button(mainFrame, text="Change Goal", command=lambda: changeGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, scrollFrame.scrollable_frame))
    changeButton.grid(row=2, column=0, sticky='w')

    completeButton = ttk.Button(mainFrame, text="Complete Goal", command=lambda: completeGoal(mainWindow, goalsWindow, dbConnection, dbCursor, username, goalsList, scrollFrame.scrollable_frame))
    completeButton.grid(row=3, column=0, sticky='w')

    def backButtonClicked(mainWindow, currentWindow, parentWindow):
        currentWindow.grid_forget()
        parentWindow.grid()

    goalsWindow.grid()

# Usage:
createGoalsWindow(mainWindow, setGoalsWindow, dbConnection, dbCursor, username)
