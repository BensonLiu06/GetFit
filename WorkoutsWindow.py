import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import tkinter.font as tkFont
from WorkoutsShowText import *


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


    workout2 = ttk.Button(bottomFrame, text = " Advanced Workout", command = lambda: showWorkout2())
    workout2.grid(column = 0, row = 2, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout3 = ttk.Button(bottomFrame, text = " HIIT Workout")
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
    global Start
    global End

    top = Tk()
    top.geometry("1680x720")
    top.title("Beginner Workout")

    introduction = Label(top, text = "Press Start to start the workout.")
    introduction.grid()

    Label(top, text = "Tips"  )

    Start = Button(top, text = "Start", command = lambda: [buttonClicked(), timer()] )
    Start.grid(column = 1, row= 1, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(top, text = "End", command = top.destroy)
    End.grid(column = 1, row= 2, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    buttonClicked()
    top.mainloop()


def buttonClicked():
    

    global airSquats
    global inbetweenBreaks
    global walkingLunges
    global pushUps
    global plank
    global jumpingJacks
    global breakTime
    global i
    
    i = 0
    for i in range(5):  
        fontObj = ('Times New Roman',30,'bold')

        
        
        airSquats = Label(top, text = "Air Squats x 20", width = 20, font = fontObj, anchor=CENTER)
        airSquats.after(1000 , showtext1 )
        airSquats.after(31000, airSquats.destroy)

        
        inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
        inbetweenBreaks.after(31000, showtext2)
        inbetweenBreaks.after(41000, inbetweenBreaks.destroy)



        walkingLunges = Label(top, text = "Lunges x 10 on each leg", width = 20, font = fontObj, anchor=CENTER)
        walkingLunges.after(41000, showtext3)
        walkingLunges.after(71000, walkingLunges.destroy)


        inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
        inbetweenBreaks.after(71000, showtext2)
        inbetweenBreaks.after(81000, inbetweenBreaks.destroy)
        


        pushUps = Label(top, text = "Push-Ups x 10", width = 20, font = fontObj, anchor=CENTER)
        pushUps.after(81000 , showtext4)
        pushUps.after(111000, pushUps.destroy)
        

        inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
        inbetweenBreaks.after(111000, showtext2)
        inbetweenBreaks.after(121000, inbetweenBreaks.destroy)
        

        plank = Label(top, text = "Plank x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
        plank.after(121000, showtext5)
        plank.after(151000, plank.destroy)

        inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
        inbetweenBreaks.after(151000, showtext2)
        inbetweenBreaks.after(161000, inbetweenBreaks.destroy)
        
            
        jumpingJacks = Label(top, text = "Jumping Jacks x 30", width = 20, font = fontObj, anchor=CENTER)
        jumpingJacks.after(161000, showtext6)
        jumpingJacks.after(191000, jumpingJacks.destroy)


        breakTime = Label(top, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
        breakTime.after(191000, showtext7)
        breakTime.after(221000, breakTime.destroy)

        repeat = Label(top, text = "This workout is to be repeated 5 times to complete, Finish before the time runs out.", font = fontObj, anchor=CENTER)
        repeat.grid(column=6, row = 12)

    

    
def finished():
    if i == 5:
        finished = Tk()

        congratsMessage = Label(finished, text = "Congrats, you made it, the workout has finished!", anchor=CENTER)
        congratsMessage.grid()

        finished.mainloop()
    
    else:
        return

    
def countdown(count):
    global Font_tuple
    
    Font_tuple = ('Impact',20, 'bold')
    # change text in label        
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    elif count == 0:
        alarm = Label(root, text = "20 minutes is up.", font = Font_tuple)
        alarm.grid()

def timer():
    global label
    global root

    root = tk.Tk()

    label = tk.Label(root, font = ('Impact', 20, 'bold'), anchor=CENTER)
    label.place(x=35, y=15)

    # call countdown first time   
    countdown(1200)
    # root.after(0, countdown, 5)

    root.mainloop()

#-----------------------------------------------------------------
def showWorkout2():
    global workout2

    workout2 = Tk()
    workout2.geometry("1380x720")
    workout2.title("Advanced Workout")
    
    introduction2 = Label(workout2, text = "Press start to start the workout")
    introduction2.grid()

    Start = Button(workout2, text = "Start", command = lambda: [buttonClicked2(), timer()] )
    Start.grid(column = 1, row= 1, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(workout2, text = "End", command = top.destroy)
    End.grid(column = 1, row= 2, ipadx = 30, ipady = 20, padx = 15, pady = 15)


def buttonClicked2():
    global airSquats
    global inbetweenBreaks
    global walkingLunges
    global pushUps
    global plank
    global breakTime
    global i
    global pistolSquats
    global tricepDips


    i = 0
    while i < 5:
        i += 1
        fontObj = ('Times New Roman',30,'bold')
        airSquats = Label(workout2, text = "Air Squats x 20", width = 20, font = fontObj, anchor=CENTER)
        airSquats.after(1000 , showtext1)
        airSquats.after(61000, airSquats.destroy)

        
        inbetweenBreaks = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
        inbetweenBreaks.after(61000, showtext2)
        inbetweenBreaks.after(71000, inbetweenBreaks.destroy)



        walkingLunges = Label(workout2, text = "Lunges x 20 on each leg", width = 20, font = fontObj, anchor=CENTER)
        walkingLunges.after(71000, showtext3)
        walkingLunges.after(131000, walkingLunges.destroy)


        inbetweenBreaks = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
        inbetweenBreaks.after(131000, showtext2)
        inbetweenBreaks.after(141000, inbetweenBreaks.destroy)
        


        pushUps = Label(workout2, text = "Push-Ups x 20", width = 20, font = fontObj, anchor=CENTER)
        pushUps.after(141000 , showtext4)
        pushUps.after(201000, pushUps.destroy)
        

        inbetweenBreaks = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
        inbetweenBreaks.after(201000, showtext2)
        inbetweenBreaks.after(211000, inbetweenBreaks.destroy)
        
        pistolSquats = Label(workout2, text = "pistol Squats x 10 on each side", width = 20, font = fontObj, anchor=CENTER)
        pistolSquats.after(251000, showtext8)
        pistolSquats.after(311000, pistolSquats.destroy)

        inbetweenBreaks = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
        inbetweenBreaks.after(241000, showtext2)
        inbetweenBreaks.after(251000, inbetweenBreaks.destroy)

        tricepDips = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
        tricepDips.after(200000, showtext9)
        tricepDips.after(300000, tricepDips.destroy)

        inbetweenBreaks = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
        inbetweenBreaks.after(311000, showtext2)
        inbetweenBreaks.after(321000, inbetweenBreaks.destroy)

        plank = Label(workout2, text = "Plank x 1 minute", width = 20, font = fontObj, anchor=CENTER)
        plank.after(211000, showtext5)
        plank.after(241000, plank.destroy)
        

        breakTime = Label(workout2, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
        breakTime.after(321000, showtext7)
        breakTime.after(381000, breakTime.destroy)

        repeat = Label(workout2, text = "This workout is to be repeated 5 times to complete, Finish before the time runs out.", font = fontObj, anchor=CENTER)
        repeat.grid(column=6, row = 12)

def showWorkout3():
    top = Tk()
    top.geometry("720x250")
    top.title("HIIT Workout")
    
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




#------------------------------------------------------------

def showtext1():
    airSquats.grid(column = 6, row = 1)

def showtext2():
    inbetweenBreaks.grid(column = 6, row = 2)

def showtext3():
    walkingLunges.grid(column = 6, row = 3)

def showtext4():
    pushUps.grid(column = 6, row = 5)

def showtext5():
    plank.grid(column = 6, row = 7)

def showtext6():
    jumpingJacks.grid(column = 6, row = 9)

def showtext7():
    breakTime.grid(column = 6, row = 11)

def showtext8():
    pistolSquats.grid(column = 6, row = 6)

def showtext9():
    tricepDips.grid(column = 6, row = 8)
