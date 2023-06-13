import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import tkinter.font as tkFont
from WorkoutsShowText import *


def workoutsTab():

    workoutsTab = Tk()
    workoutsTab.geometry("1200x800")
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
    buttonFrame = ttk.Frame(workoutsTab, width = 600, height = 300, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))
    bottomFrame.grid(column = 0, row = 1, columnspan = 2, rowspan = 9, padx = 5, pady = 5, sticky=(N, S, E, W))
    buttonFrame.grid(column = 0, row = 5, columnspan = 2, rowspan = 1, padx = 5, pady = 5, sticky=(N, S, E, W))

    #Creates buttons for different types of workouts

    workout1 = ttk.Button(bottomFrame, text = " Beginner Workout", command = lambda: showWorkout1())
    workout1.grid(column = 0, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout2 = ttk.Button(bottomFrame, text = " Advanced Workout", command = lambda: showWorkout2())
    workout2.grid(column = 1, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout3 = ttk.Button(bottomFrame, text = " HIIT Workout", command = lambda: showWorkout3())
    workout3.grid(column = 2, row = 1, ipadx= 40, ipady = 80 , padx = 30, pady = 30)


    workout4 = ttk.Button(bottomFrame, text = " Full-Body Cardio Workout", command = lambda: showWorkout4())
    workout4.grid(column = 3, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout5 = ttk.Button(buttonFrame, text = " 7 Minute Workout (Intermediate)", command = lambda: showWorkout5())
    workout5.grid(column = 0, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout6 = ttk.Button(buttonFrame, text = " 7 Minute Workout (Advanced)", command = lambda: showWorkout6())
    workout6.grid(column = 1, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout7 = ttk.Button(buttonFrame, text = " Arm Workout", command = lambda: showWorkout7())
    workout7.grid(column = 2, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout8 = ttk.Button(buttonFrame, text = " Leg Workout", command = lambda: showWorkout8())
    workout8.grid(column = 3, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)



    workoutsTab.mainloop()
   
def showWorkout1():
    global bottomButtonFrame

    top = Tk()
    top.geometry("1100x900")
    top.title("Beginner Workout")

    # Create a frame for the Update Profile & Settings window
    frame1 = ttk.Frame(top)

    # Setup the Update Profile & Settings window
    frame1.grid(sticky = (N, S, E, W))

    frame1.columnconfigure(0, weight = 1)
    frame1.columnconfigure(1, weight = 1)
    frame1.columnconfigure(2, weight = 1)

    frame1.rowconfigure(1, weight = 1)
    frame1.rowconfigure(2, weight = 1)
    frame1.rowconfigure(3, weight = 1)
    frame1.rowconfigure(4, weight = 1)
    frame1.rowconfigure(5, weight = 1)
    frame1.rowconfigure(6, weight = 1)
    frame1.rowconfigure(7, weight = 1)
    frame1.rowconfigure(8, weight = 1)
    frame1.rowconfigure(9, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(frame1, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(frame1, width = 300, height = 400, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(frame1, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomButtonFrame = ttk.Frame(frame1, width = 300, height = 400, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomFrame.grid(column = 0, row = 3, columnspan = 2, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))
    buttonFrame.grid(column = 0, row = 11, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomButtonFrame.grid(column = 2, row = 3, columnspan = 1, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(1, weight = 1)
    topFrame.columnconfigure(2, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(1, weight = 5)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(1, weight = 1)
    bottomButtonFrame.columnconfigure(2, weight = 1)
    bottomFrame.rowconfigure(3, weight = 1)
    bottomFrame.rowconfigure(4, weight = 1)
    bottomFrame.rowconfigure(5, weight = 1)
    bottomFrame.rowconfigure(6, weight = 1)
    bottomFrame.rowconfigure(7, weight = 1)
    bottomFrame.rowconfigure(8, weight = 1)
    bottomFrame.rowconfigure(9, weight = 1)
    bottomFrame.rowconfigure(10, weight = 1)
    bottomButtonFrame.rowconfigure(3, weight = 1)
    bottomButtonFrame.rowconfigure(4, weight = 1)
    bottomButtonFrame.rowconfigure(5, weight = 1)
    bottomButtonFrame.rowconfigure(6, weight = 1)
    bottomButtonFrame.rowconfigure(7, weight = 1)
    bottomButtonFrame.rowconfigure(8, weight = 1)
    bottomButtonFrame.rowconfigure(9, weight = 1)
    bottomButtonFrame.rowconfigure(10, weight = 1)

    introduction = Label(topFrame, text = "Press Start to start the workout.")
    introduction.grid(column = 1, row = 2, padx = 15, pady = 15)


    Start = Button(bottomButtonFrame, text = "Start", command = lambda: [buttonClicked(bottomFrame), timer(bottomButtonFrame)])
    Start.grid(column = 1, row= 4, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(bottomButtonFrame, text = "End", command = lambda: finished() )
    End.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()


def buttonClicked(bottomFrame):
    

    global airSquats
    global inbetweenBreaks
    global walkingLunges
    global pushUps
    global plank
    global jumpingJacks
    global breakTime
    global i
    
    
    fontObj = ('Times New Roman',14,'bold')

    
    
    airSquats = Label(bottomFrame, text = "Air Squats x 20", width = 20, font = fontObj, anchor=CENTER)
    airSquats.after(1000 , showtext1 )

    
    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(31000, showtext2)




    walkingLunges = Label(bottomFrame, text = "Lunges x 10 on each leg", width = 20, font = fontObj, anchor=CENTER)
    walkingLunges.after(41000, showtext3)


    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(71000, showtext2)


    pushUps = Label(bottomFrame, text = "Push-Ups x 10", width = 20, font = fontObj, anchor=CENTER)
    pushUps.after(81000 , showtext4)
    

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(111000, showtext2)
    

    plank = Label(bottomFrame, text = "Plank x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    plank.after(121000, showtext5)

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(151000, showtext2)
    
        
    jumpingJacks = Label(bottomFrame, text = "Jumping Jacks x 30", width = 20, font = fontObj, anchor=CENTER)
    jumpingJacks.after(161000, showtext6)


    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.after(191000, showtext7)

    repeat = Label(bottomFrame, text = "This workout is to be repeated 5 times to complete, Finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)

       
def finished():
    blankLabel = Label(bottomButtonFrame, text = "                           ")
    blankLabel.grid(column = 1, row= 3, padx = 15, pady = 15)

    finished = Tk()

    congratsMessage = Label(finished, text = "Congrats, you made it, the workout has finished!", anchor=CENTER)
    congratsMessage.grid()

    finished.mainloop()

    
def countdown(count):
    global Font_tuple
    
    
    Font_tuple = ('Impact',20, 'bold')
    # change text in label        
    label['text'] = count

    if count > 0:
        bottomButtonFrame.after(1000, countdown, count-1)
    


    

    
def timer(bottomButtonFrame):
    global label

    label = tk.Label(bottomButtonFrame, font = ('impact', 14, 'bold'))
    label.grid(column = 1, row= 3, padx = 15, pady = 15)
    
    # call countdown first time   
    countdown(1200)
    # root.after(0, countdown, 5)


        


#-----------------------------------------------------------------
def showWorkout2():

    top = Tk()
    top.geometry("1100x900")
    top.title("Beginner Workout")

    # Create a frame for the Update Profile & Settings window
    frame1 = ttk.Frame(top)

    # Setup the Update Profile & Settings window
    frame1.grid(sticky = (N, S, E, W))

    frame1.columnconfigure(0, weight = 1)
    frame1.columnconfigure(1, weight = 1)
    frame1.columnconfigure(2, weight = 1)

    frame1.rowconfigure(1, weight = 1)
    frame1.rowconfigure(2, weight = 1)
    frame1.rowconfigure(3, weight = 1)
    frame1.rowconfigure(4, weight = 1)
    frame1.rowconfigure(5, weight = 1)
    frame1.rowconfigure(6, weight = 1)
    frame1.rowconfigure(7, weight = 1)
    frame1.rowconfigure(8, weight = 1)
    frame1.rowconfigure(9, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(frame1, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(frame1, width = 300, height = 400, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(frame1, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomButtonFrame = ttk.Frame(frame1, width = 300, height = 400, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomFrame.grid(column = 0, row = 3, columnspan = 2, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))
    buttonFrame.grid(column = 0, row = 11, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomButtonFrame.grid(column = 2, row = 3, columnspan = 1, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(1, weight = 1)
    topFrame.columnconfigure(2, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(1, weight = 5)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(1, weight = 1)
    bottomButtonFrame.columnconfigure(2, weight = 1)
    bottomFrame.rowconfigure(3, weight = 1)
    bottomFrame.rowconfigure(4, weight = 1)
    bottomFrame.rowconfigure(5, weight = 1)
    bottomFrame.rowconfigure(6, weight = 1)
    bottomFrame.rowconfigure(7, weight = 1)
    bottomFrame.rowconfigure(8, weight = 1)
    bottomFrame.rowconfigure(9, weight = 1)
    bottomFrame.rowconfigure(10, weight = 1)
    bottomButtonFrame.rowconfigure(3, weight = 1)
    bottomButtonFrame.rowconfigure(4, weight = 1)
    bottomButtonFrame.rowconfigure(5, weight = 1)
    bottomButtonFrame.rowconfigure(6, weight = 1)
    bottomButtonFrame.rowconfigure(7, weight = 1)
    bottomButtonFrame.rowconfigure(8, weight = 1)
    bottomButtonFrame.rowconfigure(9, weight = 1)
    bottomButtonFrame.rowconfigure(10, weight = 1)

    introduction = Label(topFrame, text = "Press Start to start the workout.")
    introduction.grid(column = 1, row = 2, padx = 15, pady = 15)


    Start = Button(bottomButtonFrame, text = "Start", command = lambda: [buttonClicked2(bottomFrame), timer(bottomButtonFrame)])
    Start.grid(column = 1, row= 4, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(bottomButtonFrame, text = "End", command = lambda: finished() )
    End.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()

def buttonClicked2(bottomFrame):
    

    
    fontObj = ('Times New Roman',30,'bold')
    airSquats = Label(bottomFrame, text = "Air Squats x 20", width = 20, font = fontObj, anchor=CENTER)
    airSquats.after(1000 , showtext1)

    
    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(61000, showtext2)



    walkingLunges = Label(bottomFrame, text = "Lunges x 20 on each leg", width = 20, font = fontObj, anchor=CENTER)
    walkingLunges.after(71000, showtext3)


    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(131000, showtext2)
    


    pushUps = Label(bottomFrame, text = "Push-Ups x 20", width = 20, font = fontObj, anchor=CENTER)
    pushUps.after(141000 , showtext4)
    

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(201000, showtext2)
    
    pistolSquats = Label(bottomFrame, text = "pistol Squats x 10 on each side", width = 20, font = fontObj, anchor=CENTER)
    pistolSquats.after(251000, showtext8)

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(241000, showtext2)

    tricepDips = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    tricepDips.after(200000, showtext9)

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(311000, showtext2)

    plank = Label(bottomFrame, text = "Plank x 1 minute", width = 20, font = fontObj, anchor=CENTER)
    plank.after(211000, showtext5)
    

    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.after(321000, showtext7)

    repeat = Label(bottomFrame, text = "This workout is to be repeated 5 times to complete, Finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)


def showWorkout3():
    top = Tk()
    top.geometry("1100x900")
    top.title("HIIT Workout")

    # Create a frame for the Update Profile & Settings window
    frame1 = ttk.Frame(top)

    # Setup the Update Profile & Settings window
    frame1.grid(sticky = (N, S, E, W))

    frame1.columnconfigure(0, weight = 1)
    frame1.columnconfigure(1, weight = 1)
    frame1.columnconfigure(2, weight = 1)

    frame1.rowconfigure(1, weight = 1)
    frame1.rowconfigure(2, weight = 1)
    frame1.rowconfigure(3, weight = 1)
    frame1.rowconfigure(4, weight = 1)
    frame1.rowconfigure(5, weight = 1)
    frame1.rowconfigure(6, weight = 1)
    frame1.rowconfigure(7, weight = 1)
    frame1.rowconfigure(8, weight = 1)
    frame1.rowconfigure(9, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(frame1, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(frame1, width = 300, height = 400, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(frame1, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomButtonFrame = ttk.Frame(frame1, width = 300, height = 400, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomFrame.grid(column = 0, row = 3, columnspan = 2, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))
    buttonFrame.grid(column = 0, row = 11, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomButtonFrame.grid(column = 2, row = 3, columnspan = 1, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(1, weight = 1)
    topFrame.columnconfigure(2, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(1, weight = 5)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(1, weight = 1)
    bottomButtonFrame.columnconfigure(2, weight = 1)
    bottomFrame.rowconfigure(3, weight = 1)
    bottomFrame.rowconfigure(4, weight = 1)
    bottomFrame.rowconfigure(5, weight = 1)
    bottomFrame.rowconfigure(6, weight = 1)
    bottomFrame.rowconfigure(7, weight = 1)
    bottomFrame.rowconfigure(8, weight = 1)
    bottomFrame.rowconfigure(9, weight = 1)
    bottomFrame.rowconfigure(10, weight = 1)
    bottomButtonFrame.rowconfigure(3, weight = 1)
    bottomButtonFrame.rowconfigure(4, weight = 1)
    bottomButtonFrame.rowconfigure(5, weight = 1)
    bottomButtonFrame.rowconfigure(6, weight = 1)
    bottomButtonFrame.rowconfigure(7, weight = 1)
    bottomButtonFrame.rowconfigure(8, weight = 1)
    bottomButtonFrame.rowconfigure(9, weight = 1)
    bottomButtonFrame.rowconfigure(10, weight = 1)

    introduction = Label(topFrame, text = "Press Start to start the workout.")
    introduction.grid(column = 1, row = 2, padx = 15, pady = 15)


    Start = Button(bottomButtonFrame, text = "Start", command = lambda: [buttonClicked3(bottomFrame), timer(bottomButtonFrame)])
    Start.grid(column = 1, row= 4, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(bottomButtonFrame, text = "End", command = lambda: finished() )
    End.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()

def buttonClicked3(bottomFrame):
    fontObj = ('Times New Roman',30,'bold')
    sideKickThrough = Label(bottomFrame, text = "side Kick-Through x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    sideKickThrough.after(1000 , showtext10)

    
    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(31000, showtext2)




    airSquats = Label(bottomFrame, text = "airSquats x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    airSquats.after(41000, showtext1)


    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(71000, showtext2)


    jumpingLunges = Label(bottomFrame, text = "Jumping Lunges x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    jumpingLunges.after(81000 , showtext11)
    

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(111000, showtext2)
    

    Frogger = Label(bottomFrame, text = "Frogger x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    Frogger.after(121000, showtext12)

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(151000, showtext2)
    
        
    bicycleCrunch = Label(bottomFrame, text = "Bicycle Crunches x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    bicycleCrunch.after(161000, showtext13)


    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.after(191000, showtext7)

    repeat = Label(bottomFrame, text = "This workout is to be repeated 6 times to complete, Try your best to finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)


def showWorkout4():

    top = Tk()
    top.geometry("1100x900")
    top.title("Full-Body-Cardio Workout")

    # Create a frame for the Update Profile & Settings window
    frame1 = ttk.Frame(top)

    # Setup the Update Profile & Settings window
    frame1.grid(sticky = (N, S, E, W))

    frame1.columnconfigure(0, weight = 1)
    frame1.columnconfigure(1, weight = 1)
    frame1.columnconfigure(2, weight = 1)

    frame1.rowconfigure(1, weight = 1)
    frame1.rowconfigure(2, weight = 1)
    frame1.rowconfigure(3, weight = 1)
    frame1.rowconfigure(4, weight = 1)
    frame1.rowconfigure(5, weight = 1)
    frame1.rowconfigure(6, weight = 1)
    frame1.rowconfigure(7, weight = 1)
    frame1.rowconfigure(8, weight = 1)
    frame1.rowconfigure(9, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(frame1, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(frame1, width = 300, height = 400, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(frame1, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomButtonFrame = ttk.Frame(frame1, width = 300, height = 400, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomFrame.grid(column = 0, row = 3, columnspan = 2, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))
    buttonFrame.grid(column = 0, row = 11, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomButtonFrame.grid(column = 2, row = 3, columnspan = 1, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(1, weight = 1)
    topFrame.columnconfigure(2, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(1, weight = 5)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(1, weight = 1)
    bottomButtonFrame.columnconfigure(2, weight = 1)
    bottomFrame.rowconfigure(3, weight = 1)
    bottomFrame.rowconfigure(4, weight = 1)
    bottomFrame.rowconfigure(5, weight = 1)
    bottomFrame.rowconfigure(6, weight = 1)
    bottomFrame.rowconfigure(7, weight = 1)
    bottomFrame.rowconfigure(8, weight = 1)
    bottomFrame.rowconfigure(9, weight = 1)
    bottomFrame.rowconfigure(10, weight = 1)
    bottomButtonFrame.rowconfigure(3, weight = 1)
    bottomButtonFrame.rowconfigure(4, weight = 1)
    bottomButtonFrame.rowconfigure(5, weight = 1)
    bottomButtonFrame.rowconfigure(6, weight = 1)
    bottomButtonFrame.rowconfigure(7, weight = 1)
    bottomButtonFrame.rowconfigure(8, weight = 1)
    bottomButtonFrame.rowconfigure(9, weight = 1)
    bottomButtonFrame.rowconfigure(10, weight = 1)

    introduction = Label(topFrame, text = "Press Start to start the workout.")
    introduction.grid(column = 1, row = 2, padx = 15, pady = 15)


    Start = Button(bottomButtonFrame, text = "Start", command = lambda: [buttonClicked3(bottomFrame), timer(bottomButtonFrame)])
    Start.grid(column = 1, row= 4, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(bottomButtonFrame, text = "End", command = lambda: finished() )
    End.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()

def buttonClicked4(bottomFrame):
    fontObj = ('Times New Roman',30,'bold')
    sidePlankTwist = Label(bottomFrame, text = "Side Plank Twist x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    sidePlankTwist.after(1000 , showtext14)

    
    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(31000, showtext2)




    squatPulse = Label(bottomFrame, text = "Squat Pulse x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    squatPulse.after(41000, showtext15)

    #Change to 15 second break between exercise
    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(71000, showtext2)


    tuckUp = Label(bottomFrame, text = "Tuck Ups x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    tuckUp.after(81000 , showtext16)
    

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(111000, showtext2)
    

    plankRock = Label(bottomFrame, text = "Plank Rock Back and Fourth x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    plankRock.after(121000, showtext12)

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(151000, showtext2)
    
    pushUps = Label(bottomFrame, text = "Push Ups x 30 Seconds")
    pushUps.after(161000, showtext19)
    
    mountainClimbers = Label(bottomFrame, text = "Mountain Climbers x 30 seconds", width = 20, font = fontObj, anchor = CENTER)
    mountainClimbers.after(191000, showtext20)

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(201000, showtext2)

    bicycleKicks= Label(bottomFrame, text = "Bicycle Kicks x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    bicycleKicks.after(211000, showtext18)

    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.after(241000, showtext7)

    repeat = Label(bottomFrame, text = "This workout is to be repeated 5 times to complete, Try your best to finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)

def showWorkout5():
    top = Tk()
    top.geometry("1100x900")
    top.title("HIIT Workout")

    # Create a frame for the Update Profile & Settings window
    frame1 = ttk.Frame(top)

    # Setup the Update Profile & Settings window
    frame1.grid(sticky = (N, S, E, W))

    frame1.columnconfigure(0, weight = 1)
    frame1.columnconfigure(1, weight = 1)
    frame1.columnconfigure(2, weight = 1)

    frame1.rowconfigure(1, weight = 1)
    frame1.rowconfigure(2, weight = 1)
    frame1.rowconfigure(3, weight = 1)
    frame1.rowconfigure(4, weight = 1)
    frame1.rowconfigure(5, weight = 1)
    frame1.rowconfigure(6, weight = 1)
    frame1.rowconfigure(7, weight = 1)
    frame1.rowconfigure(8, weight = 1)
    frame1.rowconfigure(9, weight = 1)

    # Create all the main frame containers
    topFrame = ttk.Frame(frame1, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomFrame = ttk.Frame(frame1, width = 300, height = 400, relief = 'groove', borderwidth = 2)
    buttonFrame = ttk.Frame(frame1, width = 600, height = 50, relief = 'groove', borderwidth = 2)
    bottomButtonFrame = ttk.Frame(frame1, width = 300, height = 400, relief = 'groove', borderwidth = 2)

    # Layout all of the main frame containers
    topFrame.grid(column = 0, row = 0, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomFrame.grid(column = 0, row = 3, columnspan = 2, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))
    buttonFrame.grid(column = 0, row = 11, columnspan = 3, rowspan = 1, padx = 5, pady = 5, sticky = (N, S, E, W))
    bottomButtonFrame.grid(column = 2, row = 3, columnspan = 1, rowspan = 8, padx = 5, pady = 5, sticky = (N, S, E, W))

    topFrame.columnconfigure(0, weight = 1)
    topFrame.columnconfigure(1, weight = 1)
    topFrame.columnconfigure(2, weight = 1)
    bottomFrame.columnconfigure(0, weight = 1)
    bottomFrame.columnconfigure(1, weight = 5)
    buttonFrame.columnconfigure(0, weight = 1)
    buttonFrame.columnconfigure(1, weight = 1)
    bottomButtonFrame.columnconfigure(2, weight = 1)
    bottomFrame.rowconfigure(3, weight = 1)
    bottomFrame.rowconfigure(4, weight = 1)
    bottomFrame.rowconfigure(5, weight = 1)
    bottomFrame.rowconfigure(6, weight = 1)
    bottomFrame.rowconfigure(7, weight = 1)
    bottomFrame.rowconfigure(8, weight = 1)
    bottomFrame.rowconfigure(9, weight = 1)
    bottomFrame.rowconfigure(10, weight = 1)
    bottomButtonFrame.rowconfigure(3, weight = 1)
    bottomButtonFrame.rowconfigure(4, weight = 1)
    bottomButtonFrame.rowconfigure(5, weight = 1)
    bottomButtonFrame.rowconfigure(6, weight = 1)
    bottomButtonFrame.rowconfigure(7, weight = 1)
    bottomButtonFrame.rowconfigure(8, weight = 1)
    bottomButtonFrame.rowconfigure(9, weight = 1)
    bottomButtonFrame.rowconfigure(10, weight = 1)

    introduction = Label(topFrame, text = "Press Start to start the workout.")
    introduction.grid(column = 1, row = 2, padx = 15, pady = 15)


    Start = Button(bottomButtonFrame, text = "Start", command = lambda: [buttonClicked3(bottomFrame), timer(bottomButtonFrame)])
    Start.grid(column = 1, row= 4, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(bottomButtonFrame, text = "End", command = lambda: finished() )
    End.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()

def buttonClicked5(bottomFrame):
    fontObj = ('Times New Roman',30,'bold')

    jumpingJacks = Label(bottomFrame, text = "Jumping Jacks AMRAP", width = 20, font = fontObj, anchor=CENTER)
    jumpingJacks.after(1000 , showtext10)

    
    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(31000, showtext2)

    airSquats = Label(bottomFrame, text = "airSquats AMRAP", width = 20, font = fontObj, anchor=CENTER)
    airSquats.after(41000, showtext1)


    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(71000, showtext2)


    wallSit = Label(bottomFrame, text = "Wall Sit A<RAP", width = 20, font = fontObj, anchor=CENTER)
    wallSit.after(81000 , showtext11)
    

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(111000, showtext2)
    

    Frogger = Label(bottomFrame, text = "Frogger x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    Frogger.after(121000, showtext12)

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(151000, showtext2)
    
        
    bicycleCrunch = Label(bottomFrame, text = "Bicycle Crunches x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    bicycleCrunch.after(161000, showtext13)


    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.after(191000, showtext7)

    repeat = Label(bottomFrame, text = "This workout is to be repeated only once to complete\nTry to pace yourself and complete as much of each in 35 seconds.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)

def showWorkout6():
    workout6 = Tk()
    workout6.geometry("1380x720")
    workout6.title("Advanced 7 minute Workout")
    
    introduction5 = Label(workout6, text = "Press Start to start the workout")
    introduction5.grid()

    Start = Button(workout6, text = "Start", command = lambda: [buttonClicked6(), timer2 ()])
    Start.grid(column = 1, row= 1, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(workout6, text = "End", command = workout6.destroy)
    End.grid(column = 1, row= 2, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    workout6.mainloop()

def buttonClicked6():
    fontObj = ('Times New Roman',30,'bold')
    sideKickThrough = Label(workout2, text = "side Kick-Through x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    sideKickThrough.after(1000 , showtext10)

    
    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(31000, showtext2)




    airSquats = Label(top, text = "airSquats x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    airSquats.after(41000, showtext1)


    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(71000, showtext2)


    jumpingLunges = Label(top, text = "Jumping Lunges x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    jumpingLunges.after(81000 , showtext11)
    

    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(111000, showtext2)
    

    Frogger = Label(top, text = "Frogger x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    Frogger.after(121000, showtext12)

    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(151000, showtext2)
    
        
    bicycleCrunch = Label(top, text = "Bicycle Crunches x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    bicycleCrunch.after(161000, showtext13)


    breakTime = Label(top, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.after(191000, showtext7)

    repeat = Label(top, text = "This workout is to be repeated 6 times to complete, Try your best to finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)

def showWorkout7():
    workout7 = Tk()
    workout7.geometry("1380x720")
    workout7.title("Leg Workout")
    
    introduction5 = Label(workout7, text = "Press Start to start the workout")
    introduction5.grid()

    Start = Button(workout7, text = "Start", command = lambda: [buttonClicked7(), timer ()])
    Start.grid(column = 1, row= 1, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(workout7, text = "End", command = workout7.destroy)
    End.grid(column = 1, row= 2, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    workout7.mainloop()

def buttonClicked7():
    fontObj = ('Times New Roman',30,'bold')
    sideKickThrough = Label(workout2, text = "side Kick-Through x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    sideKickThrough.after(1000 , showtext10)

    
    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(31000, showtext2)




    airSquats = Label(top, text = "airSquats x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    airSquats.after(41000, showtext1)


    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(71000, showtext2)


    jumpingLunges = Label(top, text = "Jumping Lunges x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    jumpingLunges.after(81000 , showtext11)
    

    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(111000, showtext2)
    

    Frogger = Label(top, text = "Frogger x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    Frogger.after(121000, showtext12)

    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(151000, showtext2)
    
        
    bicycleCrunch = Label(top, text = "Bicycle Crunches x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    bicycleCrunch.after(161000, showtext13)


    breakTime = Label(top, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.after(191000, showtext7)

    repeat = Label(top, text = "This workout is to be repeated 6 times to complete, Try your best to finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)

def showWorkout8():
    workout8 = Tk()
    workout8.geometry("1380x720")
    workout8.title("Arm Workout")
    
    introduction5 = Label(workout8, text = "Press Start to start the workout")
    introduction5.grid()

    Start = Button(workout8, text = "Start", command = lambda: [buttonClicked8(), timer ()])
    Start.grid(column = 1, row= 1, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(workout8, text = "End", command = workout8.destroy)
    End.grid(column = 1, row= 2, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    workout8.mainloop()

def buttonClicked8():
    fontObj = ('Times New Roman',30,'bold')
    sideKickThrough = Label(workout2, text = "side Kick-Through x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    sideKickThrough.after(1000 , showtext10)

    
    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(31000, showtext2)




    airSquats = Label(top, text = "airSquats x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    airSquats.after(41000, showtext1)


    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(71000, showtext2)


    jumpingLunges = Label(top, text = "Jumping Lunges x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    jumpingLunges.after(81000 , showtext11)
    

    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(111000, showtext2)
    

    Frogger = Label(top, text = "Frogger x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    Frogger.after(121000, showtext12)

    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(151000, showtext2)
    
        
    bicycleCrunch = Label(top, text = "Bicycle Crunches x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    bicycleCrunch.after(161000, showtext13)


    breakTime = Label(top, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.after(191000, showtext7)

    repeat = Label(top, text = "This workout is to be repeated 6 times to complete, Try your best to finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)


def finished():
    blankLabel = Label(bottomButtonFrame, text = "                           ")
    blankLabel.grid(column = 1, row= 3, padx = 15, pady = 15)

    finished = Tk()

    congratsMessage = Label(finished, text = "Congrats, you made it, the workout has finished!", anchor=CENTER)
    congratsMessage.grid()

    finished.mainloop()

    
def countdown2(count):
    global Font_tuple
    
    
    Font_tuple = ('Impact',20, 'bold')
    # change text in label        
    label2['text'] = count

    if count > 0:
        bottomButtonFrame.after(1000, countdown, count-1)
    


    

    
def timer2(bottomButtonFrame):
    global label2

    label2 = tk.Label(bottomButtonFrame, font = ('impact', 14, 'bold'))
    label2.grid(column = 1, row= 3, padx = 15, pady = 15)
    
    # call countdown first time   
    countdown(420)
    # root.after(0, countdown, 5)



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

def showtext10():
    tricepDips.grid(column = 6, row = 8)
def showtext11():
    tricepDips.grid(column = 6, row = 8)
def showtext12():
    tricepDips.grid(column = 6, row = 8)
def showtext13():   
    tricepDips.grid(column = 6, row = 8)
