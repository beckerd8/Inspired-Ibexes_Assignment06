# File Name : cat.py
# Student Name: Matthew Boutros
# email: boutromw@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Model a real world item using OOP with 4 classes from each team member

# Brief Description of what this module does: Defines the Cat class with attributes, getters/setters, and methods for behavior
# Citations:

class Cat(object):
    """
    Model a Cat with properties such as name, breed, age, and color.
    """

    def __init__(self, name, breed, age, color):
        """
        Constructor
        @param name String: name of the cat
        @param breed String: breed of the cat
        @param age Int: age of the cat
        @param color String: color of the cat
        """
        self.set_name(name)
        self.set_breed(breed)
        self.set_age(age)
        self.set_color(color)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Name cannot be empty")

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        if breed and len(breed) > 0:
            self.__breed = breed
        else:
            raise ValueError("Breed cannot be empty")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer")

    def get_color(self):
        return self.__color

    def set_color(self, color):
        if color and len(color) > 0:
            self.__color = color
        else:
            raise ValueError("Color cannot be empty")

    def meow(self):
        """Simulate the cat meowing"""
        print(f"{self.__name} meows: Meow! Meow!")

    def scratch(self, item):
        """Simulate the cat scratching an item"""
        print(f"{self.__name} scratches the {item}!")

    def __str__(self):
        """
        @return String: Representation of the current object
        """
        return f"Cat name: {self.__name}, breed: {self.__breed}, age: {self.__age}, color: {self.__color}"

