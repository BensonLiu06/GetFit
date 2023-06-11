import tkinter as tk
from tkinter import *
from tkinter import ttk
import time



def workoutsTab():

    workoutsTab = Tk()
    workoutsTab.geometry("1000x800")
    workoutsTab.title("Workouts")

    appWindow = ttk.Frame(workoutsTab, padding=(3,3,12,12))
    appWindow.grid(sticky=N+S+E+W)

    # Setup the main App window
    workoutsTab.columnconfigure(0, weight = 1)
    workoutsTab.columnconfigure(1, weight = 1)
    #appWindow.rowconfigure(0, weight = 1)
    workoutsTab.rowconfigure(1, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(workoutsTab, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(workoutsTab, width = 300, height = 700, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(workoutsTab, width = 300, height = 50, relief = 'groove', borderwidth = 2)

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
    topFrame = ttk.Frame(workoutsTab, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(workoutsTab, width = 600, height = 650, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(workoutsTab, width = 600, height = 100, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 9, padx = 5, pady = 5, sticky=(N, S, E, W))
    buttonFrame.grid(column = 0, row = 5, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))

    #Creates buttons for different types of workouts

    workout1 = ttk.Button(bottomFrame, text = " Beginner Workout", command = lambda: showWorkout1())
    workout1.grid(column = 0, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout2 = ttk.Button(bottomFrame, text = " Advanced Workout")
    workout2.grid(column = 0, row = 2, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout3 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout3.grid(column = 1, row = 1, ipadx= 40, ipady = 80 , padx = 30, pady = 30)


    workout4 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout4.grid(column = 1, row = 2, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout5 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout5.grid(column = 2, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout6 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout6.grid(column = 2, row = 2, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout7 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout7.grid(column = 3, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout8 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout8.grid(column = 3, row = 2, ipadx= 40, ipady = 80, padx = 30, pady = 30)



    workoutsTab.mainloop()

def showWorkout1():
    global top
    
    top = Tk()
    top.geometry("800x600")
    top.title("Beginner Workout")

    
    inbetweenBreaks = Label(top, text = "10 second break")

    Label(top, text = "Press Start to start the workout.")
    Label(top, text = "Tips"  )

    Start = Button(top, text = "Start", command = lambda: buttonClicked() )
    Start.grid(column = 0, row= 2, ipadx = 30, ipady = 20)

    

def buttonClicked():
    inbetweenBreaks = Label(top, text = "10 second break")


    airSquats = Label(top, text = "Air Squats x 20", font = "Arial")
    airSquats.grid()
    time.sleep(60)

    inbetweenBreaks.grid()
    time.sleep(10)


    walkingLunges = Label(top, text = "Walking Lunges x 10 on each leg", font = "Arial")
    walkingLunges.grid()
    time.sleep(60)

    inbetweenBreaks.grid()
    time.sleep(10)

    pushUps = Label(top, text = "Push-Ups x 10")
    pushUps.grid()
    time.sleep(60)

    inbetweenBreaks.grid()
    time.sleep(10)

    plank = Label(top, text = "Plank x 30 Seconds")
    plank.grid()
    time.sleep(30)

    inbetweenBreaks.grid()
    time.sleep(10)
        
    jumpingJacks = Label(top, text = "Jumping Jacks x 30")
    jumpingJacks.grid()
    time.sleep(60)

    breakTime = Label(top, text = "Grab some water and take a break for 30 seconds")
    breakTime.grid()
    time.sleep(30)





    
def showWorkout2():
    top = Tk()
    top.geometry("720x250")
    top.title("Intermediate Workout")
    
    Label(top, text = "")

def showWorkout3():
    top = Tk()
    top.geometry("720x250")
    top.title("Advanced Workout")
    
    Label(top, text = "")

def showWorkout4():
    top = Tk()
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    Label(top, text = "")

def showWorkout5():
    top = Tk()
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    Label(top, text = "")

def showWorkout6():
    top = Tk()
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    Label(top, text = "")

def showWorkout7():
    top = Tk()
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    Label(top, text = "")

def showWorkout8():
    top = Tk()
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    Label(top, text = "")
