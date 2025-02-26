# File Name : bird.py
# Student Name: Zach Bell
# email:  bellzj@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Model a real world item using OOP with 4 classes from each team member

# Brief Description of what this module does: Defines the bird class with attributes, getters/setters, and method for behavior
# Citations: https://stackoverflow.com/questions/35878470/call-a-setter-from-init-in-python - used for setter logic

# Anything else that's relevant:

class Bird(object):
    """
    Model a bird with properties such as name, species, age, and color.
    """

    def __init__(self, name, species, age, color):
        """
        Constructor
        @param name String: The name of the bird
        @param species String: The species of the bird
        @param age Int: The age of the bird
        @param color String: The color of the bird
        """
        self.set_name(name)
        self.set_species(species)
        self.set_age(age)
        self.set_color(color)

    def get_name(self):
        """
        @return String: The name of the bird
        """
        return self.__name

    def set_name(self, name):
        """
        Assign a value to the bird's name
        @param name String: The name to be assigned
        """
        if name and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Name cannot be empty")

    def get_species(self):
        """
        @return String: The species of the bird
        """
        return self.__species

    def set_species(self, species):
        """
        Assign a value to the bird's species
        @param species String: The species to be assigned
        """
        if species and len(species) > 0:
            self.__species = species
        else:
            raise ValueError("Species cannot be empty")

    def get_age(self):
        """
        @return Int: The age of the bird
        """
        return self.__age

    def set_age(self, age):
        """
        Assign a value to the bird's age
        @param age Int: The age to be assigned
        """
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer")

    def get_color(self):
        """
        @return String: The color of the bird
        """
        return self.__color

    def set_color(self, color):
        """
        Assign a value to the bird's color
        @param color String: The color to be assigned
        """
        if color and len(color) > 0:
            self.__color = color
        else:
            raise ValueError("Color cannot be empty")

    def quack(self):
        """
        Simulate the duck quacking
        """
        print(f"{self.__name} speaks: Quack Quack!")

    def __str__(self):
        """
        @return String: Representation of the current object
        """
        return f"Bird's name: {self.__name}, species: {self.__species}, age: {self.__age}, color: {self.__color}"





