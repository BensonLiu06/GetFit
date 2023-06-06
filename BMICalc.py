import tkinter as Tk

def bmiIndexCalc():
    weight = ""
    height = ""
    bmiIndex = float("")

    bmiIndex = weight/(height**2) * 703


    if bmiIndex > "30":
        print("placeholder")

    elif bmiIndex < "18.5":
        print("placeholder")

    elif bmiIndex > "18.5" and bmiIndex < "24.9":
        print("placeholder")

    elif bmiIndex > "25.0" and bmiIndex < "29.9":
        print("placeholder")




