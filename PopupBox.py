from tkinter import *
from tkinter import ttk

# Implementation for a generic popup dialog box
def popupBox(mainWindow, parentWindow, windowTitle, messageText):
    # Create a Toplevel window for the popup dialog box
    popupBoxWindow = Toplevel(parentWindow)
    popupBoxWindow.title(windowTitle)

    # Create lable widget to show the message text
    messageLabel =ttk.Label(popupBoxWindow, text = messageText)
    messageLabel.grid(column = 0, row = 0)
    
    # Create an OK button widget to dismiss the popup dialog box
    okButton = ttk.Button(popupBoxWindow, text = "OK", command = lambda : popupBoxWindow.destroy())
    okButton.grid(column = 0, row = 1)

    # Force an update on the mainWindow so the size of the widgets are known
    mainWindow.update()

    # Get width an height of the popup diagog box so we can resize it
    # to fit the contents of the label and button
    w = popupBoxWindow.winfo_reqwidth()
    h = popupBoxWindow.winfo_reqheight()

    # Calculate the geometry to center the dialog box on the screen
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    popupBoxWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

    popupBoxWindow.grab_set()