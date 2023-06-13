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

    end = Button(bottomButtonFrame, text = "End", command = lambda: finished())
    end.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()


def buttonClicked(bottomFrame):
    
    fontObj = ('Times New Roman',14,'bold')

    
    
    airSquats = Label(bottomFrame, text = "Air Squats x 20", width = 20, font = fontObj, anchor=CENTER)
    airSquats.grid(column = 6, row = 1)

    
    inbetweenBreaks1 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks1.grid(column = 6, row = 2)




    walkingLunges = Label(bottomFrame, text = "Lunges x 10 on each leg", width = 20, font = fontObj, anchor=CENTER)
    walkingLunges.grid(column = 6, row = 3)


    inbetweenBreaks2 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks2.grid(column = 6, row = 4)


    pushUps = Label(bottomFrame, text = "Push-Ups x 10", width = 20, font = fontObj, anchor=CENTER)
    pushUps.grid(column = 6, row = 5)
    

    inbetweenBreaks3 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks3.grid(column = 6, row = 6)
    

    plank = Label(bottomFrame, text = "Plank x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    plank.grid(column = 6, row = 7)

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.grid(column = 6, row = 8)
    
        
    jumpingJacks = Label(bottomFrame, text = "Jumping Jacks x 30", width = 20, font = fontObj, anchor=CENTER)
    jumpingJacks.grid(column = 6, row = 9)


    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.grid(column = 6, row = 10)

    repeat = Label(bottomFrame, text = "This workout is to be repeated 5 times to complete, Finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)

       

def finished():

    label.after(1000, label.destroy())

    finished = Tk()

    congratsMessage = Label(finished, text = "Congrats, you made it, the workout has finished!", anchor=CENTER)
    congratsMessage.grid()

    finished.mainloop()

    
def countdown(count):

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


        
def showWorkout2():

    top = Tk()
    top.geometry("1100x900")
    top.title("Advanced Workout")

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
    

    
    fontObj = ('Times New Roman',14,'bold')
    airSquats = Label(bottomFrame, text = "Air Squats x 20", width = 20, font = fontObj, anchor=CENTER)
    airSquats.grid(column = 6, row = 1)

    
    inbetweenBreaks1 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks1.grid(column = 6, row = 2)



    walkingLunges = Label(bottomFrame, text = "Lunges x 20 on each leg", width = 20, font = fontObj, anchor=CENTER)
    walkingLunges.grid(column = 6, row = 3)


    inbetweenBreaks2 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks2.grid(column = 6, row = 4)
    
    pushUps = Label(bottomFrame, text = "Push-Ups x 20", width = 20, font = fontObj, anchor=CENTER)
    pushUps.grid(column = 6, row = 5)
    

    inbetweenBreaks3 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks3.grid(column = 6, row = 6)
    
    pistolSquats = Label(bottomFrame, text = "pistol Squats x 10 on each side", width = 20, font = fontObj, anchor=CENTER)
    pistolSquats.grid(column = 6, row = 7)

    inbetweenBreaks4 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks4.grid(column = 6, row = 8)

    tricepDips = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    tricepDips.grid(column = 6, row = 9)

    inbetweenBreaks5 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks5.grid(column = 6, row = 10)

    plank = Label(bottomFrame, text = "Plank x 1 minute", width = 20, font = fontObj, anchor=CENTER)
    plank.grid(column = 6, row = 11)
    

    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.grid(column = 6, row = 12)

    repeat = Label(bottomFrame, text = "This workout is to be repeated 5 times to complete, Finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 13)


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
    fontObj = ('Times New Roman',14,'bold')
    sideKickThrough = Label(bottomFrame, text = "side Kick-Through x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    sideKickThrough.grid(column = 6, row = 1)

    
    inbetweenBreaks1 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks1.grid(column = 6, row = 2)




    airSquats = Label(bottomFrame, text = "airSquats x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    airSquats.grid(column = 6, row = 3)


    inbetweenBreaks2 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks2.grid(column = 6, row = 4)


    jumpingLunges = Label(bottomFrame, text = "Jumping Lunges x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    jumpingLunges.grid(column = 6, row = 5)
    

    inbetweenBreaks3 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks3.grid(column = 6, row = 6)

    Frogger = Label(bottomFrame, text = "Frogger x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    Frogger.grid(column = 6, row = 7)

    inbetweenBreaks = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.grid(column = 6, row = 8)
    
        
    bicycleCrunch = Label(bottomFrame, text = "Bicycle Crunches x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    bicycleCrunch.grid(column = 6, row = 9)


    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.grid(column = 6, row = 10)

    repeat = Label(bottomFrame, text = "Now repeat the workout! This workout is to be repeated 6 times to complete, Try your best to finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 11)


def showWorkout4():

    top = Tk()
    top.geometry("1100x900")
    top.title("Full-Body Cardio Workout")

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


    Start = Button(bottomButtonFrame, text = "Start", command = lambda: [buttonClicked4(bottomFrame), timer(bottomButtonFrame)])
    Start.grid(column = 1, row= 4, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(bottomButtonFrame, text = "End", command = lambda: finished() )
    End.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()

def buttonClicked4(bottomFrame):
    fontObj = ('Times New Roman',14,'bold')
    sidePlankTwist = Label(bottomFrame, text = "Side Plank Twist x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    sidePlankTwist.grid(column = 6, row = 1)

    
    inbetweenBreaks1 = Label(bottomFrame, text = "15 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks1.grid(column = 6, row = 2)




    squatPulse = Label(bottomFrame, text = "Squat Pulse x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    squatPulse.grid(column = 6, row = 3)

    #Change to 15 second break between exercise
    inbetweenBreaks2 = Label(bottomFrame, text = "15 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks2.grid(column = 6, row = 4)


    tuckUp = Label(bottomFrame, text = "Tuck Ups x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    tuckUp.grid(column = 6, row = 5)
    

    inbetweenBreaks3 = Label(bottomFrame, text = "15 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks3.grid(column = 6, row = 6)
    

    plankRock = Label(bottomFrame, text = "Plank Rock Back and Fourth x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    plankRock.grid(column = 6, row = 7)

    inbetweenBreaks4 = Label(bottomFrame, text = "15 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks4.grid(column = 6, row = 8)
    
    pushUps = Label(bottomFrame, text = "Push Ups x 30 Seconds")
    pushUps.grid(column = 6, row = 9)
    
    mountainClimbers = Label(bottomFrame, text = "Mountain Climbers x 30 seconds", width = 20, font = fontObj, anchor = CENTER)
    mountainClimbers.grid(column = 6, row = 10)

    inbetweenBreaks5 = Label(bottomFrame, text = "15 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks5.grid(column = 6, row = 11)

    bicycleKicks= Label(bottomFrame, text = "Bicycle Kicks x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    bicycleKicks.grid(column = 6, row = 12)

    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.grid(column = 6, row = 13)

    repeat = Label(bottomFrame, text = "Repeat the workout! This workout is to be repeated 5 times to complete, Try your best to finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 14)

def showWorkout5():
    top = Tk()
    top.geometry("1100x900")
    top.title("Intermediate 7 minute Workout")

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


    Start = Button(bottomButtonFrame, text = "Start", command = lambda: [buttonClicked5(bottomFrame), timer2(bottomButtonFrame)])
    Start.grid(column = 1, row= 4, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(bottomButtonFrame, text = "End", command = lambda: finished2() )
    End.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()

def buttonClicked5(bottomFrame):

    fontObj = ('Times New Roman',14,'bold')

    jumpingJacks = Label(bottomFrame, text = "Jumping Jacks AMRAP", width = 20, font = fontObj, anchor=CENTER)
    jumpingJacks.grid(column = 6, row = 1)

    
    inbetweenBreaks1 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks1.grid(column = 6, row = 2)

    airSquats = Label(bottomFrame, text = "airSquats AMRAP", width = 20, font = fontObj, anchor=CENTER)
    airSquats.grid(column = 6, row = 3)


    inbetweenBreaks2 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks2.grid(column = 6, row = 4)


    wallSit = Label(bottomFrame, text = "Wall Sit AMRAP", width = 20, font = fontObj, anchor=CENTER)
    wallSit.grid(column = 6, row = 5)
    

    inbetweenBreaks3 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks3.grid(column = 6, row = 6)
    

    abdominalCrunch = Label(bottomFrame, text = "Abdominal Crunches AMRAP", width = 20, font = fontObj, anchor=CENTER)
    abdominalCrunch.grid(column = 6, row = 7)

    inbetweenBreaks4 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks4.grid(column = 6, row = 8)
    
    stepUp = Label(bottomFrame, text = "Step-Up onto Chair AMRAP", width = 20, font = fontObj, anchor=CENTER)
    stepUp.grid(column = 6, row = 9)

    inbetweenBreaks5 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks5.grid(column = 6, row = 10)

    tricepDips2 = Label(bottomFrame, text = "Tricep Dips on Chair AMRAP", width = 20, font = fontObj, anchor=CENTER)
    tricepDips2.grid(column = 6, row = 11)

    inbetweenBreaks6 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks6.grid(column = 6, row = 12)

    highKnee2 = Label(bottomFrame, text = "High Knees AMRAP", width = 20, font = fontObj, anchor=CENTER)
    highKnee2.grid(column = 6, row = 13)

    inbetweenBreaks7 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks7.grid(column = 6, row = 14)

    sidePlank = Label(bottomFrame, text = "Side Plank AMRAP", width = 20, font = fontObj, anchor=CENTER)
    sidePlank.grid(column = 6, row = 15)

    repeat = Label(bottomFrame, text = "This workout is to pace yourself and complete as much of each exercise.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 16)

def showWorkout6():
    top = Tk()
    top.geometry("1100x900")
    top.title("Advanced 7 Minute Workout")

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


    Start = Button(bottomButtonFrame, text = "Start", command = lambda: [buttonClicked6(bottomFrame), timer2(bottomButtonFrame)])
    Start.grid(column = 1, row= 4, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(bottomButtonFrame, text = "End", command = lambda: finished2() )
    End.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()

def buttonClicked6(bottomFrame):
    fontObj = ('Times New Roman',14,'bold')

    reverseLunges = Label(bottomFrame, text = "Reverse Lunges, alternating sides per rep AMRAP", width = 20, font = fontObj, anchor=CENTER)
    reverseLunges.grid(column = 6, row = 1)

    
    inbetweenBreaks1 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks1.grid(column = 6, row = 2)

    lateralPillarBridge = Label(bottomFrame, text = "Lateral Pillar bridge, alternate sides per rep AMRAP", width = 20, font = fontObj, anchor=CENTER)
    lateralPillarBridge.grid(column = 6, row = 3)


    inbetweenBreaks2 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks2.grid(column = 6, row = 4)


    rdltoCurlPress = Label(bottomFrame, text = "Single Leg RDL (romainian deadlift), alternating legs per rep AMRAP ", width = 20, font = fontObj, anchor=CENTER)
    rdltoCurlPress.grid(column = 6, row = 5)
    

    inbetweenBreaks3 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks3.grid(column = 6, row = 6)
    

    plankArmlift = Label(bottomFrame, text = "Plank with Armlift AMRAP", width = 20, font = fontObj, anchor=CENTER)
    plankArmlift.grid(column = 6, row = 7)

    inbetweenBreaks4 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks4.grid(column = 6, row = 8)
    
        
    lungetotricep = Label(bottomFrame, text = "Lateral Lunge to overhead tricep extension AMRAP", width = 20, font = fontObj, anchor=CENTER)
    lungetotricep.grid(column = 6, row = 9)

    inbetweenBreaks5 = Label(bottomFrame, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks5.grid(column = 6, row = 10)

    bentoverRow = Label(bottomFrame, text = "Bent Over row, alternating arms per rep AMRAP", width = 20, font = fontObj, anchor=CENTER)
    bentoverRow.grid(column = 6, row = 11)

    repeat = Label(bottomFrame, text = "This workout is to be done once to complete, Try your best to finish as much of each exercise before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)

def showWorkout7():
    top = Tk()
    top.geometry("1100x900")
    top.title("Arm Workout")

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


    Start = Button(bottomButtonFrame, text = "Start", command = lambda: [buttonClicked7(bottomFrame), timer(bottomButtonFrame)])
    Start.grid(column = 1, row= 4, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(bottomButtonFrame, text = "End", command = lambda: finished() )
    End.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()

def buttonClicked7(bottomFrame):
    fontObj = ('Times New Roman',14,'bold')

    tricepDips_chair = Label(bottomFrame, text = "Tricep Dips on Chair x 20", width = 20, font = fontObj, anchor=CENTER)
    tricepDips_chair.grid(column = 6, row = 1)

    
    inbetweenBreaks1 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks1.grid(column = 6, row = 2)

    pushUps2 = Label(bottomFrame, text = "Push Ups x 20", width = 20, font = fontObj, anchor=CENTER)
    pushUps2.grid(column = 6, row = 3)


    inbetweenBreaks2 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks2.grid(column = 6, row = 4)


    shadowBoxing = Label(bottomFrame, text = "Shadow Boxing x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    shadowBoxing.grid(column = 6, row = 5)
    

    inbetweenBreaks3 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks3.grid(column = 6, row = 6)
    

    declinePushUp = Label(bottomFrame, text = "Decline Push Up x 20", width = 20, font = fontObj, anchor=CENTER)
    declinePushUp.grid(column = 6, row = 7)

    inbetweenBreaks4 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks4.grid(column = 6, row = 8)
    
    inclinePushUp = Label(bottomFrame, text = "Incline Push Up x 20", width = 20, font = fontObj, anchor=CENTER)
    inclinePushUp.grid(column = 6, row = 9)

    inbetweenBreaks5 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks5.grid(column = 6, row = 10)

    inchWorm = Label(bottomFrame, text = "Inchworm x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    inchWorm.grid(column = 6, row = 11)

    inbetweenBreaks6 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks6.grid(column = 6, row = 12)

    diamondPushUp = Label(bottomFrame, text = "Diamond Push Up x 10", width = 20, font = fontObj, anchor=CENTER)
    diamondPushUp.grid(column = 6, row = 13)
                        
    inbetweenBreaks7 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks7.grid(column = 6, row = 14)

    burpees = Label(bottomFrame, text = "Burpees x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    burpees.grid(column = 6, row = 15)

    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.grid(column = 6, row = 16)

    repeat = Label(bottomFrame, text = "Repeat the workout! This workout is to be repeated 3 times to complete, Try your best to finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 17)

def showWorkout8():
    top = Tk()
    top.geometry("1100x900")
    top.title("Leg Workout")

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


    Start = Button(bottomButtonFrame, text = "Start", command = lambda: [buttonClicked8(bottomFrame), timer(bottomButtonFrame)])
    Start.grid(column = 1, row= 4, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(bottomButtonFrame, text = "End", command = lambda: finished() )
    End.grid(column = 1, row= 6, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    exit = Button(buttonFrame, text = "Quit", command =  top.destroy )
    exit.grid(column = 1 , row = 3 , ipadx = 30, ipady = 20 , padx = 15, pady = 15)
    
    top.mainloop()

def buttonClicked8(bottomFrame):
    fontObj = ('Times New Roman',14,'bold')

    reverseLunges2 = Label(bottomFrame, text = "Reverse Lunges x 45 seconds", width = 20, font = fontObj, anchor=CENTER)
    reverseLunges2.grid(column = 6, row = 1)

    
    inbetweenBreaks1 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks1.grid(column = 6, row = 2)

    sideLunges = Label(bottomFrame, text = "Side Lunges x 45 seconds", width = 20, font = fontObj, anchor=CENTER)
    sideLunges.grid(column = 6, row = 3)


    inbetweenBreaks2 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks2.grid(column = 6, row = 4)


    highKnees = Label(bottomFrame, text = "High Knees x 30 seconds", width = 20, font = fontObj, anchor=CENTER)
    highKnees.grid(column = 6, row = 5)
    

    inbetweenBreaks3 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks3.grid(column = 6, row = 6)
    

    hipRaises = Label(bottomFrame, text = "Hip Raises x 45 seconds", width = 20, font = fontObj, anchor=CENTER)
    hipRaises.grid(column = 6, row = 7)

    inbetweenBreaks4 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks4.grid(column = 6, row = 8)
    
        
    boxJumps = Label(bottomFrame, text = "Box Jumps x 20", width = 20, font = fontObj, anchor=CENTER)
    boxJumps.grid(column = 6, row = 9)
    
    inbetweenBreaks5 = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks5.grid(column = 6, row = 10)

    airSquats3 = Label(bottomFrame, text = "Air Squats x 45 Seconds", width = 20, font = fontObj, anchor=CENTER)
    airSquats3.grid(column = 6, row = 11)

    inbetweenBreaks = Label(bottomFrame, text = "30 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.grid(column = 6, row = 12)

    burpees2 = Label(bottomFrame, text = "Burpees x 20", width = 20, font = fontObj, anchor=CENTER)
    burpees2.grid(column = 6, row = 13)

    breakTime = Label(bottomFrame, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.grid(column = 6, row = 14)

    repeat = Label(bottomFrame, text = "Repeat the workout!This workout is to be repeated 3 times to complete, Try your best to finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 15)


def finished2():
    label2.after(1000, label2.destroy())

    finished = Tk()

    congratsMessage = Label(finished, text = "Congrats, you made it, the workout has finished!", anchor=CENTER)
    congratsMessage.grid()

    finished.mainloop()
    
def countdown2(count):
    # change text in label        
    label2['text'] = count

    if count > 0:
        bottomButtonFrame.after(1000, countdown, count-1)
    


    

    
def timer2(bottomButtonFrame):
    global label2

    label2 = tk.Label(bottomButtonFrame, font = ('impact', 14, 'bold'))
    label2.grid(column = 1, row= 3, padx = 15, pady = 15)
    
    # call countdown first time   
    countdown2(420)
    # root.after(0, countdown, 5)



#------------------------------------------------------------


