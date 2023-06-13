from tkinter import *
from tkinter import ttk





def bmiTab():
    global userWeight
    global userHeight
    global bottomFrame

    weight = ""
    height = ""

    bmiWindow = Tk()

    bmiWindow.geometry("1600x700")
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
    heightText.grid(column = 6, row = 4, padx = 20, pady = 20)

    userWeight = Entry(bottomFrame, width = 20, text = "Weight (in Kg)", textvariable = weight)
    userWeight.grid(column = 4, row = 3, padx = 20, pady = 20 )

    userHeight = Entry(bottomFrame, width = 20, text = "Height (in Meters)", textvariable = height)
    userHeight.grid(column = 6, row = 3, padx = 20, pady = 20)

    userCalculate = Button(bottomFrame, width = 20, text = "Calculate BMI", command = lambda: bmiIndexCalc(height, weight))
    userCalculate.grid(column = 5, row = 4, padx = 20,pady = 20, ipadx = 40, ipady=10)


    bmiWindow.mainloop()


def bmiIndexCalc(height,weight):


    weight = userWeight.get()
    height = userHeight.get()
    
    convertedWeight = float(weight)
    convertedHeight = float(height)

    bmiIndex = convertedWeight/(convertedHeight**2)


    
    blankLabel = Label(bottomFrame, text = "                                                                                                                                                        ")
    blankLabel.grid(column = 5, row = 6, padx=5,pady=5)
    
    BMItext = "BMI = " + str(bmiIndex)
    labelText = ""
    

    if bmiIndex > 30.0:
        labelText = "You are considered obese, but balancing your diet with more greens and fruits can help improve your BMI!"

    elif bmiIndex < 18.5:
        labelText = "You are considered underweight, consider consuming more calories and having more protein to improve BMI!"
        

    elif bmiIndex > 18.5 and bmiIndex < 24.9:
        labelText = "You are in the healthy range! Keep balancing your diet with how much you workout to stay within the range of healthy BMI!"
        

    elif bmiIndex > 25.0 and bmiIndex < 29.9:
        labelText = "You are considered slightly Overweight, less calorie intake and more exercise is suggested to achieve better BMI!"
        
    
    blankLabel = Label(bottomFrame, text = "                                                                                                                                                                                                                                                                                                                                                                              ")
    blankLabel.place(x = 50, y = 190)

    showBMI = Label(bottomFrame, text = BMItext)
    showBMI.grid(column = 5, row = 6, padx = 5, pady = 5)

    status = Label(bottomFrame, text = labelText)
    status.grid(column = 5, row = 7)







