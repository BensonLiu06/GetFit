import tkinter as tk
from tkinter import *
from tkinter import ttk
import time

def callback():
    global buttonClicked
    buttonClicked = not buttonClicked


def workoutsTab():

    workoutsTab = Tk()

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

    workout1 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout1.grid(column = 0, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout2 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout2.grid(column = 0, row = 2, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout3 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout3.grid(column = 0, row = 3, ipadx= 40, ipady = 80 , padx = 30, pady = 30)


    workout4 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout4.grid(column = 0, row = 4, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout5 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout5.grid(column = 1, row = 1, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout6 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout6.grid(column = 1, row = 2, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout7 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout7.grid(column = 1, row = 3, ipadx= 40, ipady = 80, padx = 30, pady = 30)


    workout8 = ttk.Button(bottomFrame, text = " Strength Workout")
    workout8.grid(column = 1, row = 4, ipadx= 40, ipady = 80, padx = 30, pady = 30)



    workoutsTab.mainloop()

def showWorkout1():
    top = Toplevel(workoutsTab)
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    buttonClicked = False
    Label(top, text = "Press Start to start the workout.")
    Label(top, text = "Tips"  )

    Start = Button(top, Text = "Start", command = lambda: [callback(), timer()])
    Start.grid()

    

    if buttonClicked == True:
        airSquats = Label(top, text = "Air Squats x 20", font = "Arial")
        airSquats.grid()
        time.sleep(20)

        walkingLunges = Label(top, text = "Walking Lunges x 10 on each leg", font = "Arial")
        walkingLunges.grid()
        time.sleep(30)

        pushUps = Label(top, text = "Push-Ups x 10")
        pushUps.grid()
        time.sleep(40)

        plank = Label(top, text = "Plank x 30 Seconds")
        plank.grid()
        time.sleep(30)


    
def showWorkout2():
    top = Toplevel(workoutsTab)
    top.geometry("720x250")
    top.title("Intermediate Workout")
    
    Label(top, text = "")
def showWorkout3():
    top = Toplevel(workoutsTab)
    top.geometry("720x250")
    top.title("Advanced Workout")
    
    Label(top, text = "")
def showWorkout4():
    top = Toplevel(workoutsTab)
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    Label(top, text = "")
def showWorkout5():
    top = Toplevel(workoutsTab)
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    Label(top, text = "")
def showWorkout6():
    top = Toplevel(workoutsTab)
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    Label(top, text = "")
def showWorkout7():
    top = Toplevel(workoutsTab)
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    Label(top, text = "")
def showWorkout8():
    top = Toplevel(workoutsTab)
    top.geometry("720x250")
    top.title("Beginner Workout")
    
    Label(top, text = "")

def timer():
    import time
    from tkinter import messagebox
    
    
    # creating Tk window
    root = Tk()
    
    # setting geometry of tk window
    root.geometry("300x250")
    
    # Using title() to display a message in
    # the dialogue box of the message in the
    # title bar.
    root.title("Time Counter")
    
    # Declaration of variables
    hour=StringVar()
    minute=StringVar()
    second=StringVar()
    
    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")
    
    # Use of Entry class to take input from the user
    hourEntry= Entry(root, width=3, font=("Arial",18,""),
                    textvariable=hour)
    hourEntry.place(x=80,y=20)
    
    minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                    textvariable=minute)
    minuteEntry.place(x=130,y=20)
    
    secondEntry= Entry(root, width=3, font=("Arial",18,""),
                    textvariable=second)
    secondEntry.place(x=180,y=20)
    
    
    def submit():
        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)
    
            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
    
            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            time.sleep(1)
    
            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
            
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1
    
    # button widget
    btn = Button(root, text='Set Time Countdown', bd='5',
                command= submit)
    btn.place(x = 70,y = 120)
    
    # infinite loop which is required to
    # run tkinter program infinitely
    # until an interrupt occurs
    root.mainloop()
