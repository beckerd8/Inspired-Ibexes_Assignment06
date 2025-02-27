# File Name : main.py

# Student Name: David Becker, Zach Bell, Evan Bolin, Matthew Boutros
# email:  beckerd8@mail.uc.edu,  bellzj@mail.uc.edu, bolinen@mail.uc.edu, boutromw@mail.uc.edu

# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Model a real world item using OOP with 4 classes from each team member

# Brief Description of what this module does: Creates objects, calls methods, and prints outputs
# Citations: 

# Anything else that's relevant:


from bird_package.bird import *
from dog_package.dog import *
from cat_package.cat import *
from mouse_Package.mouse import *


if __name__ == "__main__":
    
    print("\n--------------------\n")
    
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
    print(f"The dog's new age is: {my_dog.get_age()}") 

    print("\n--------------------\n")

    my_Mouse = Mouse(name="Stewart", weight=2, length=6, color="Gray")

    print(my_Mouse)

    my_Mouse.chew()
    my_Mouse.eat("cheese")

    print("Now the mouse is 4 pounds")
    my_Mouse.set_weight(4)
    print(f"The mouse's updated weight is: {my_Mouse.get_weight()} pounds")  

    print("\n--------------------\n")

    # Creating a Bird object
    my_bird = Bird(name="Donald", species="Duck", age=90, color="White")

    # Printing string representations
    print(my_bird)

    # Demonstrating method
    my_bird.quack()
    print(f"The bird's species is: {my_bird.get_species()}") 
   
    print("\n--------------------\n")

 
    # Creating a Cat object
    my_cat = Cat(name="Whiskers", breed="Siamese", age=2, color="Gray")
    
    # Printing string representation of the Cat object
    print(my_cat)
    print(f"The cat's color is: {my_cat.get_color()}")  
    
    # Demonstrating Cat methods
    my_cat.meow()
    my_cat.scratch("sofa")
    
    # Updating Cat's age
    print("Update cat's age to 3...")
    my_cat.set_age(3)
    print(my_cat)

    