# File Name : main.py
# Student Name: David Becker, Evan Bolin <-- ADD NAME AND EMAIL :) - LAST PERSON DELETE THIS
# email:  beckerd8@mail.uc.edu, bolinen@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Model a real world item using OOP with 4 classes from each team member

# Brief Description of what this module does: Creates objects, calls methods, and prints outputs
# Citations: 

# Anything else that's relevant:


from dog_package.dog import *
from mouse_package.mouse import * 


if __name__ == "__main__":
    
    print("\n--------------------")
    
    # Creating a Dog object
    my_dog = Dog(name="Yoki", breed="Chocolate Lab", age=3, color="Chocolate")

    # Printing string representations
    print(my_dog)

    # Demonstrating methods
    my_dog.bark()
    my_dog.fetch("avocado falling off professor's desk")
    my_dog.wag_tail()

    # Updating dog's age
    print("Update dog's age to 4...")
    my_dog.set_age(4)
    print(my_dog)

    print("\n--------------------")

if __name__ == "__main__":

    print("\n--------------------")

    my_Mouse = Mouse(name="Stewart", weight=2, length=6, color="Gray")

    print(my_Mouse)

    my_Mouse.chew()
    my_Mouse.eat("cheese")

    print("Now the mouse is 4 pounds")
    my_Mouse.set_weight(4)
    print(my_Mouse)

    print("\n--------------------")