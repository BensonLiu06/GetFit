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


    workout4 = ttk.Button(bottomFrame, text = " 7 Minute Workout (Intermediate)", command = lambda: showWorkout4())
    workout4.grid(column = 3, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout5 = ttk.Button(buttonFrame, text = " 7 Minute Workout (Advanced)", command = lambda: showWorkout5())
    workout5.grid(column = 0, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout6 = ttk.Button(buttonFrame, text = " Arm Workout", command = lambda: showWorkout6())
    workout6.grid(column = 1, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout7 = ttk.Button(buttonFrame, text = " Leg Workout", command = lambda: showWorkout7())
    workout7.grid(column = 2, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout8 = ttk.Button(buttonFrame, text = " Strength Workout", command = lambda: showWorkout8())
    workout8.grid(column = 3, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)



    workoutsTab.mainloop()
   
def showWorkout1():
    global top
    global Start
    global End

    top = Tk()
    top.geometry("1680x720")
    top.title("Beginner Workout")

    introduction = Label(top, text = "Press Start to start the workout.")
    introduction.grid(column = 1, row = 2, padx = 15, pady = 15)


    Start = Button(top, text = "Start", command = lambda: [buttonClicked(), timer2()])
    Start.grid(column = 1, row= 1, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(top, text = "End", command = lambda: [top.destroy])
    End.grid(column = 1, row= 3, ipadx = 30, ipady = 20, padx = 15, pady = 15)

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
    
    
    fontObj = ('Times New Roman',30,'bold')

    
    
    airSquats = Label(top, text = "Air Squats x 20", width = 20, font = fontObj, anchor=CENTER)
    airSquats.after(1000 , showtext1 )

    
    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(31000, showtext2)




    walkingLunges = Label(top, text = "Lunges x 10 on each leg", width = 20, font = fontObj, anchor=CENTER)
    walkingLunges.after(41000, showtext3)


    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(71000, showtext2)


    pushUps = Label(top, text = "Push-Ups x 10", width = 20, font = fontObj, anchor=CENTER)
    pushUps.after(81000 , showtext4)
    

    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(111000, showtext2)
    

    plank = Label(top, text = "Plank x 30 Seconds", width = 20, font = fontObj, anchor=CENTER)
    plank.after(121000, showtext5)

    inbetweenBreaks = Label(top, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(151000, showtext2)
    
        
    jumpingJacks = Label(top, text = "Jumping Jacks x 30", width = 20, font = fontObj, anchor=CENTER)
    jumpingJacks.after(161000, showtext6)


    breakTime = Label(top, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.after(191000, showtext7)

    repeat = Label(top, text = "This workout is to be repeated 5 times to complete, Finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)

    

    
def finished():
    if i == 1200:
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

    if count == 0:
        finished = Tk()

        congratsMessage = Label(finished, text = "Congrats, you made it, the workout has finished!", anchor=CENTER)
        congratsMessage.grid()

        finished.mainloop()
    
    else:
        return

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

    End = Button(workout2, text = "End", command = workout2.destroy)
    End.grid(column = 1, row= 2, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    workout2.mainloop()


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


    
    fontObj = ('Times New Roman',30,'bold')
    airSquats = Label(workout2, text = "Air Squats x 20", width = 20, font = fontObj, anchor=CENTER)
    airSquats.after(1000 , showtext1)

    
    inbetweenBreaks = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(61000, showtext2)



    walkingLunges = Label(workout2, text = "Lunges x 20 on each leg", width = 20, font = fontObj, anchor=CENTER)
    walkingLunges.after(71000, showtext3)


    inbetweenBreaks = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(131000, showtext2)
    


    pushUps = Label(workout2, text = "Push-Ups x 20", width = 20, font = fontObj, anchor=CENTER)
    pushUps.after(141000 , showtext4)
    

    inbetweenBreaks = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(201000, showtext2)
    
    pistolSquats = Label(workout2, text = "pistol Squats x 10 on each side", width = 20, font = fontObj, anchor=CENTER)
    pistolSquats.after(251000, showtext8)

    inbetweenBreaks = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(241000, showtext2)

    tricepDips = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    tricepDips.after(200000, showtext9)

    inbetweenBreaks = Label(workout2, text = "10 second break", width = 20, font = fontObj, anchor=CENTER)
    inbetweenBreaks.after(311000, showtext2)

    plank = Label(workout2, text = "Plank x 1 minute", width = 20, font = fontObj, anchor=CENTER)
    plank.after(211000, showtext5)
    

    breakTime = Label(workout2, text = "Grab some water and take a break for 30 seconds", font = fontObj, anchor=CENTER)
    breakTime.after(321000, showtext7)

    repeat = Label(workout2, text = "This workout is to be repeated 5 times to complete, Finish before the time runs out.", font = fontObj, anchor=CENTER)
    repeat.grid(column=6, row = 12)


def showWorkout3():
    workout3 = Tk()
    workout3.geometry("1380x720")
    workout3.title("HIIT Workout")
    
    introduction3 = Label(workout3, text = "Press Start to start the workout")
    introduction3.grid()

    Start = Button(workout3, text = "Start", command = lambda: [buttonClicked3(), timer ()])
    Start.grid(column = 1, row= 1, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(workout3, text = "End", command = workout3.destroy)
    End.grid(column = 1, row= 2, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    workout3.mainloop()

def buttonClicked3():
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


def showWorkout4():
    workout4 = Tk()
    workout4.geometry("1380x720")
    workout4.title("Full-Body Cardio Workout")
    
    introduction3 = Label(workout4, text = "Press Start to start the workout")
    introduction3.grid()

    Start = Button(workout4, text = "Start", command = lambda: [buttonClicked4(), timer ()])
    Start.grid(column = 1, row= 1, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(workout4, text = "End", command = workout4.destroy)
    End.grid(column = 1, row= 2, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    workout4.mainloop()

def buttonClicked4():
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

def showWorkout5():
    workout5 = Tk()
    workout5.geometry("1380x720")
    workout5.title("Intermediate 7 minute Workout")
    
    introduction4 = Label(workout5, text = "Press Start to start the workout")
    introduction4.grid()

    Start = Button(workout5, text = "Start", command = lambda: [buttonClicked5(), timer2 ()])
    Start.grid(column = 1, row= 1, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    End = Button(workout5, text = "End", command = workout5.destroy)
    End.grid(column = 1, row= 2, ipadx = 30, ipady = 20, padx = 15, pady = 15)

    workout5.mainloop()

def buttonClicked5():
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


def countdown2(count2):
    global Font_tuple
    
    Font_tuple = ('Impact',20, 'bold')
    # change text in label        
    label['text'] = count2

    if count2 > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count2-1)
    elif count2 == 0:
        alarm = Label(root, text = "7 minutes is up.", font = Font_tuple)
        alarm.grid()

    if count2 == 0:
        finished = Tk()

        congratsMessage = Label(finished, text = "Congrats, you made it, the workout has finished!", anchor=CENTER)
        congratsMessage.grid()

        finished.mainloop()
    
    else:
        return

def timer2():
    global label
    global root

    root2 = tk.Tk()

    label = tk.Label(root, font = ('Impact', 20, 'bold'), anchor=CENTER)
    label.place(x=35, y=15)

    # call countdown first time   
    countdown2(4200)
    # root.after(0, countdown, 5)

    root2.mainloop()



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
