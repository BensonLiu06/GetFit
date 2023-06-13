from tkinter import *

# Create the main application window
mainWindow = Tk()

# Create the leftFrame
leftFrame = Frame(mainWindow)
leftFrame.pack(side=LEFT)

# Function to display weight lifting goals
def displayWeightLiftingGoals():
    # Create a new window for weight lifting goals
    goalsWindow = Toplevel()
    goalsWindow.title("Weight Lifting Goals")

    # Create Entry widgets for the user to input goals
    goal1Entry = Entry(goalsWindow, width=50)
    goal1Entry.pack()
    goal2Entry = Entry(goalsWindow, width=50)
    goal2Entry.pack()
    goal3Entry = Entry(goalsWindow, width=50)
    goal3Entry.pack()

    def saveGoals():
        goal1 = goal1Entry.get()
        goal2 = goal2Entry.get()
        goal3 = goal3Entry.get()
        print("Saved goals:")
        print("Goal 1:", goal1)
        print("Goal 2:", goal2)
        print("Goal 3:", goal3)

    # Add a button to save the goals
    saveButton = Button(goalsWindow, text="Save Goals", command=saveGoals)
    saveButton.pack(pady=10)

# Add the "Goals" button to the existing code
goalsButton = Button(leftFrame, text="Goals", command=displayWeightLiftingGoals)
goalsButton.grid(column=0, row=3, pady=5)

# Start the main event loop
mainWindow.mainloop()
