import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import tkinter.font as tkFont



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

    Start = Button(top, text = "Start", command = lambda: [buttonClicked(), timer()] )
    Start.grid(column = 1, row= 1, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    top.mainloop()

    

def buttonClicked():
    fontObj = tkFont.Font(size=30)
    inbetweenBreaks = Label(top, text = "10 second break", font = fontObj)
    #font= ('Times New Roman',17,'bold')

    airSquats = Label(top, text = "Air Squats x 20", width = 20, anchor = 'center', font = fontObj)
    airSquats.grid(column = 6, row = 1)
   
    

    inbetweenBreaks.grid(column = 6, row = 2)
 


    walkingLunges = Label(top, text = "Lunges x 10 on each leg", width = 20, anchor = 'center', font = fontObj)
    walkingLunges.grid(column = 6, row = 3)
  


    inbetweenBreaks.grid(column = 6, row = 4)
   

    pushUps = Label(top, text = "Push-Ups x 10", width = 20, anchor = 'center', font = fontObj)
    pushUps.grid(column = 6, row = 5)
    #top.after(60000)


    inbetweenBreaks.grid(column = 6, row = 6)
    #top.after(10000)

    plank = Label(top, text = "Plank x 30 Seconds", width = 20, anchor = 'center', font = fontObj)
    plank.grid(column = 6, row = 7)
    #top.after(60000)


    inbetweenBreaks.grid(column = 6, row = 8)
    #top.after(10000)
        
    jumpingJacks = Label(top, text = "Jumping Jacks x 30", width = 20, anchor = 'center', font = fontObj)
    jumpingJacks.grid(column = 6, row = 9)
    #top.after(60000)

    inbetweenBreaks.grid(column = 6, row = 10)


    breakTime = Label(top, text = "Grab some water and take a break for 30 seconds", font = fontObj)
    breakTime.grid(column = 6, row = 11)
    #top.after(30000)

    repeat = Label(top, text = "Repeat the workout 5 times to complete, Finish before the time runs out.", font = fontObj)
    repeat.grid(column=6, row = 12)



def countdown(count):
    # change text in label        
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    elif count == 0:
        alarm = Label(root, text = "60 seconds is up.", font = ('Digital-7', 40))
        alarm.grid()

def timer():
    global label
    global root

    root = tk.Tk()

    label = tk.Label(root)
    label.place(x=35, y=15)

    # call countdown first time   
    countdown(1200)
    # root.after(0, countdown, 5)

    root.mainloop()


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
