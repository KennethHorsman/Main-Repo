#pylint: disable=missing-class-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=trailing-whitespace
#pylint: disable=invalid-name

'''
a. Design a class named Circle with fields named radius, area, and diameter. 
Include a constructor that sets the radius to 1. Include get methods for each 
field, but include a set method only for the radius. When the radius is set, 
o not allow it to be zero or a negative number. When the radius is set, calculate the diameter 
(twice the radius) and the area (the radius squared times pi, which is approximately 3.14). 
Create the class diagram and write the pseudocode that defines the class.

b. Design an application that declares two Circles. Set the radius of one 
manually, but allow the other to use the default value supplied by the constructor. 
Then, display each Circle's values.
'''

import math

class Circle:
    "Determines diameter & area based on given r"
    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = None
        self.area = None
        self.set_radius(radius)
        
    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError("The radius must be greater than zero.")
        else:
            self.radius = radius
            self.diameter = self.radius * 2
            self.area = math.pi * (self.radius ** 2)
     
    def get_radius(self):
        return self.radius
    
    def get_diameter(self):
        return self.diameter
    
    def get_area(self):
        return self.area
    
    def display(self):
        print("Circle:")
        for field, value in self.__dict__.items():
            print(f"{field.title()}: {value}")
        print()
        
def is_valid_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_radius_from_user():
    get_input = True
    while get_input is True:
        radius_input = input("Please enter a radius: ")
        if is_valid_number(radius_input):
            if float(radius_input) > 0:
                return float(radius_input)
        else:
            print("The radius must be a number greater than zero.")
        
def print_circles():
    circle_list = []
    circle_list.append(Circle())
    user_radius = get_radius_from_user()
    circle_list.append(Circle(user_radius))
    
    for circle in circle_list:
        print()
        print(f"CIRCLE {circle_list.index(circle) + 1}")
        print(f"Radius: {circle.get_radius():,.2f}")
        print(f"Diameter: {circle.get_diameter():,.2f}")
        print(f"Area: {circle.get_area():,.2f}")
    
print_circles()

