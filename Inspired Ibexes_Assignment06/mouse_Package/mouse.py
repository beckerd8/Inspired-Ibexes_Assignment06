# File Name : mouse.py
# Student Name: Evan Bolin
# email:  bolinen@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Model a real world item using OOP with 4 classes from each team member

# Brief Description of what this module does: Defines the mouse class with attributes, getters and setters, and methods for behavior

# Anything else that's relevant:

class Mouse(object):
    """
    Models a mouse with a name, weight, length, and color  
    """
    def __init__(self, name, weight, length, color):
        """
        @param name String: mouse's name
        @param weight Int: mouse's weight
        @param length Int: mouse's length
        @param color String: color of the mouse
        """
        self.set_name(name)
        self.set_weight(weight)
        self.set_length(length)
        self.set_color(color)

    def get_name(self):
        """
        @return String: name of the mouse
        """
        return self.__name

    def set_name(self, name):
        """
        Assign a value to the mouse's name
        @param name String: The name of the mouse
        """
        if name and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Name cannot be empty")

    def get_weight(self):
        """
        @return Int: weight of the mouse
        """
        return self.__weight

    def set_weight(self, weight):
        """
        Assign a value to the mouses weight
        @param weight Int: The weight of the mouse
        """
        if isinstance(weight, int) and weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Weight must be a positive integer")

    def get_length(self):
        """
        @return Int: length of the mouse
        """
        return self.__length

    def set_length(self, length):
        """
        Assign a value to the mouses length
        @param length Int: The length of the mouse
        """
        if isinstance(length, int) and length > 0:
            self.__length = length
        else:
            raise ValueError("Length must be a positive integer")

    def get_color(self):
        """
        @return String:color of the mouse
        """
        return self.__color

    def set_color(self, color):
        """
        Assign a value to the mouse's color
        @param color String: The color of the mouse
        """
        if color and len(color) > 0:
            self.__color = color
        else:
            raise ValueError("Color cannot be empty")

    def chew(self):
        """
        Simulates the mouse chewing through something
        """
        print(f"{self.__name} chews through the packaging.")

    def eat(self, item):
        """
        Simulates the mouse eating something
        @param item String: item the mouse is eating
        """
        print(f"{self.__name} eats the {item}.")

    def __str__(self):
        """
        @return String: Representation of the current object
        """
        return f"Dog name: {self.__name}, weith: {self.__weight}pounds, length: {self.__length}inches, color: {self.__color}"