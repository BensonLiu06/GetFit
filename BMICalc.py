from tkinter import *
from tkinter import ttk

def bmiTab():
    global bmiWindow
    global userWeight
    global userHeight
    global bottomFrame

    weight = ""
    height = ""

    bmiWindow = Tk()

    bmiWindow.geometry("1200x800")
    bmiWindow.title("BMI Calculator")
    appWindow = ttk.Frame(bmiWindow, padding=(3,3,12,12))
    appWindow.grid(sticky=N+S+E+W)

    # Setup the main App window
    bmiWindow.columnconfigure(0, weight = 1)
    bmiWindow.columnconfigure(1, weight = 1)
    #appWindow.rowconfigure(0, weight = 1)
    bmiWindow.rowconfigure(1, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(bmiWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(bmiWindow, width = 300, height = 700, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(bmiWindow, width = 300, height = 50, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 5, padx = 5, pady = 5, sticky=(N, S, E, W))
    buttonFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(0, weight = 1)
    bottomFrame.rowconfigure(1, weight = 1)
    bottomFrame.rowconfigure(2, weight = 1)
    bottomFrame.rowconfigure(3, weight = 1)
    bottomFrame.rowconfigure(4, weight = 1)
    buttonFrame.rowconfigure(5, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(bmiWindow, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(bmiWindow, width = 600, height = 650, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(bmiWindow, width = 600, height = 100, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 9, padx = 5, pady = 5, sticky=(N, S, E, W))
    buttonFrame.grid(column = 0, row = 5, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))

    weightText = Label(bottomFrame, width = 20, text = "Weight (in Kg)")
    weightText.grid(column = 4, row = 4, padx = 20, pady = 20 )

    heightText = Label(bottomFrame, width = 20, text = "Height (in Meters)")
    heightText.grid(column = 8, row = 4, padx = 20, pady = 20)

    userWeight = Entry(bottomFrame, width = 20, text = "Weight (in Kg)", textvariable = weight)
    userWeight.grid(column = 4, row = 3, padx = 20, pady = 20 )

    userHeight = Entry(bottomFrame, width = 20, text = "Height (in Meters)", textvariable = height)
    userHeight.grid(column = 8, row = 3, padx = 20, pady = 20)

    userCalculate = Button(bottomFrame, width = 20, text = "Calculate BMI", command = lambda: bmiIndexCalc(height, weight))
    userCalculate.grid(column = 5, row = 6, padx = 20,pady = 20, ipadx = 40, ipady=10)


    bmiWindow.mainloop()


def bmiIndexCalc(height,weight):


    weight = userWeight.get()
    height = userHeight.get()
    
    convertedWeight = float(weight)
    convertedHeight = float(height)

    bmiIndex = convertedWeight/(convertedHeight**2)


    

    showBMI = Label(bottomFrame, text = f"BMI = {bmiIndex}")
    showBMI.grid(column = 5, row = 7, padx = 10, pady = 10)

    if bmiIndex >= 30:
        obeseStatus = Label(bottomFrame, text = "You are considered obese but we can work on it!")
        obeseStatus.grid( column = 5, row = 8)
        obeseStatus.after(10000, obeseStatus.destroy)
    elif bmiIndex < 18.59:
        underWeightStatus = Label(bottomFrame, text = "You are considered underweight, consider consuming more calories and having more protein")
        underWeightStatus.grid(column = 5, row = 8)
        underWeightStatus.after(10000, underWeightStatus.grid)
    elif bmiIndex > 18.59 and bmiIndex < 24.99:
        healthyStatus = Label(bottomFrame, text = "You are in the healthy range! Keep balancing your diet with how much you workout!")
        healthyStatus.grid(column = 5, row = 8)
        healthyStatus.after(10000, healthyStatus.destroy)
    elif bmiIndex > 25.0 and bmiIndex < 29.99:
        overWeightStatus = Label(bottomFrame, text = "You are considered slightly Overweight, less calorie intake and more exercise is suggested!")
        overWeightStatus.grid(column = 5, row = 8)
        healthyStatus.after(10000,overWeightStatus.destroy)
    







