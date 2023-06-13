from tkinter import *
from tkinter import ttk
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
    confirmButton = ttk.Button(topFrame, text="Confirm", command=lambda: addGoal(goalEntry, goalsList, goalsFrame))
    confirmButton.grid(row=1, column=1, padx=10, pady=10, sticky=(W, E))

    # Create a bottom frame for displaying goals and the Save button
    bottomFrame = ttk.Frame(setGoalsWindow)
    bottomFrame.grid(row=1, column=0, sticky=(N, S, E, W))

    # Create a scrollable frame for displaying goals
    scrollFrame = ScrollableFrame(bottomFrame)
    scrollFrame.grid(sticky=(N, S, E, W))

    # Create a list to store goals
    goalsList = []

    # Function to add a goal
    def addGoal(entry, goals, frame):
        goal = entry.get()
        if goal and len(goals) < 50:
            goals.append([goal, False])  # Store goal and completion status
            entry.delete(0, END)
            updateGoalsDisplay(goals, frame)

    # Function to update the goals display
    def updateGoalsDisplay(goals, frame):
        # Clear the frame
        for widget in frame.winfo_children():
            widget.destroy()

        # Display the goals
        for index, goal in enumerate(goals):
            goalLabel = ttk.Label(frame, text=f"{index+1}. {goal[0]}", foreground="green" if goal[1] else "red")
            goalLabel.grid(row=index, column=0, sticky='w')

            completeButton = ttk.Button(frame, text="Complete", command=lambda idx=index: markGoalComplete(idx, goals, frame))
            completeButton.grid(row=index, column=1, padx=5)

    # Function to mark a goal as complete
    def markGoalComplete(index, goals, frame):
        goals[index][1] = True  # Update completion status
        goalLabel = frame.grid_slaves(row=index, column=0)[0]
        goalLabel.configure(foreground="green")

    # Create the goals frame
    goalsFrame = ttk.Frame(scrollFrame.scrollable_frame)
    goalsFrame.grid(sticky=(N, W, E))

    # Configure the goals frame
    goalsFrame.columnconfigure(0, weight=1)
    goalsFrame.columnconfigure(1, weight=0)
    goalsFrame.rowconfigure(0, weight=1)

    # Update the goals display
    updateGoalsDisplay(goalsList, goalsFrame)

# Function to save goals and return to the main window
    def saveGoals(mainWindow, setGoalsWindow, parentWindow):
            # Create a button frame for Save and Cancel buttons
        buttonFrame = ttk.Frame(setGoalsWindow)
        buttonFrame.grid(row=2, column=0, sticky=(N, W, E))

        # Create a Save button
        saveButton = ttk.Button(buttonFrame, text="Save", command=lambda: saveGoals(mainWindow, setGoalsWindow, parentWindow))
        saveButton.grid(row=0, column=0, padx=10, pady=10, sticky=(W, E))

        # Create a Cancel button
        cancelButton = ttk.Button(buttonFrame, text="Cancel", command=lambda: cancelSetGoalsWindow(mainWindow, setGoalsWindow, parentWindow))
        cancelButton.grid(row=0, column=1, padx=10, pady=10, sticky=(W, E))

        # Hide the Set Goals window
        setGoalsWindow.grid_forget()

        # Show the App window
        parentWindow.grid(sticky=(N, S, E, W))

    # Create a button frame for Save and Cancel buttons
    buttonFrame = ttk.Frame(setGoalsWindow)
    buttonFrame.grid(row=2, column=0, sticky=(N, W, E))

    # Create a Save button
    saveButton = ttk.Button(buttonFrame, text="Save", command=lambda: saveGoals(mainWindow, setGoalsWindow, parentWindow))
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

        # Attach the scrollbar to the canvas
        vscrollbar.config(command=canvas.yview)

        # Create a scrollable frame inside the canvas
        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a window into the scrollable frame
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configure the canvas to expand with the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Configure the scrollable frame to expand with the canvas
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(width=e.width))