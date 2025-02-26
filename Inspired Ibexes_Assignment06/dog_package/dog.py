# File Name : dog.py
# Student Name: David Becker 
# email:  beckerd8@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Model a real world item using OOP with 4 classes from each team member

# Brief Description of what this module does: Defines the Dog class with attributes, getters/setters, and methods for behavior
# Citations: https://stackoverflow.com/questions/35878470/call-a-setter-from-init-in-python - used for setter logic

# Anything else that's relevant:


class Dog(object):
    """
    Model a Dog with properties such as name, breed, age, and color.
    """

    def __init__(self, name, breed, age, color):
        """
        Constructor
        @param name String: The name of the dog
        @param breed String: The breed of the dog
        @param age Int: The age of the dog
        @param color String: The color of the dog
        """
        self.set_name(name)
        self.set_breed(breed)
        self.set_age(age)
        self.set_color(color)

    def get_name(self):
        """
        @return String: The name of the dog
        """
        return self.__name

    def set_name(self, name):
        """
        Assign a value to the dog's name
        @param name String: The name to be assigned
        """
        if name and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Name cannot be empty")

    def get_breed(self):
        """
        @return String: The breed of the dog
        """
        return self.__breed

    def set_breed(self, breed):
        """
        Assign a value to the dog's breed
        @param breed String: The breed to be assigned
        """
        if breed and len(breed) > 0:
            self.__breed = breed
        else:
            raise ValueError("Breed cannot be empty")

    def get_age(self):
        """
        @return Int: The age of the dog
        """
        return self.__age

    def set_age(self, age):
        """
        Assign a value to the dog's age
        @param age Int: The age to be assigned
        """
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer")

    def get_color(self):
        """
        @return String: The color of the dog
        """
        return self.__color

    def set_color(self, color):
        """
        Assign a value to the dog's color
        @param color String: The color to be assigned
        """
        if color and len(color) > 0:
            self.__color = color
        else:
            raise ValueError("Color cannot be empty")

    def bark(self):
        """
        Simulate the dog barking
        """
        print(f"{self.__name} barks: Woof! Woof!")

    def fetch(self, item):
        """
        Simulate the dog fetching an item
        @param item String: The item to fetch
        """
        print(f"{self.__name} fetches the {item}!")

    def wag_tail(self):
        """
        Simulate the dog wagging its tail
        """
        print(f"{self.__name} wags its tail happily!")

    def __str__(self):
        """
        @return String: Representation of the current object
        """
        return f"Dog name: {self.__name}, breed: {self.__breed}, age: {self.__age}, color: {self.__color}"

