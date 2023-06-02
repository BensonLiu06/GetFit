from tkinter import Tk, simpledialog

class UserProfile:
    def __init__(self, name, age, gender, weight, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height

# Create the main tkinter window
root = Tk()
root.withdraw()  # Hide the main window

# Prompt the user for personal information
name = simpledialog.askstring("User Profile", "Enter your name:")
age = simpledialog.askinteger("User Profile", "Enter your age:")
gender = simpledialog.askstring("User Profile", "Enter your gender:")
weight = simpledialog.askfloat("User Profile", "Enter your weight:")
height = simpledialog.askfloat("User Profile", "Enter your height:")

# Create a UserProfile object
user_profile = UserProfile(name, age, gender, weight, height)

# Accessing user profile information
print(user_profile.name)
print(user_profile.age)
print(user_profile.gender)
print(user_profile.weight)
print(user_profile.height)
