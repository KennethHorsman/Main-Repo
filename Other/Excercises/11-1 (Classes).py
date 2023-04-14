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
    """A class representing a circle."""
    count = 0
    def __init__(self, radius=1):
        """Initialize a Circle object with the given radius."""
        self.radius = radius
        Circle.count += 1
        self.label = f"Circle {Circle.count}"
    
    @property
    def radius(self):
        """Get the radius of the circle."""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Set the radius of the circle to the given value."""
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Radius must be a positive number")
        self._radius = value

    @property
    def diameter(self):
        """Get the diameter of the circle."""
        return self.radius * 2
    
    @property
    def area(self):
        """Get the area of the circle."""
        return (self.radius ** 2) * math.pi
    
    def display(self, *props):
        """Display information about the circle."""
        if not props:
            print(f"{self.label}:\nRadius = {self.radius}\nDiameter = {self.diameter}\nArea = {self.area}\n")
        else:
            valid_props = {"radius": self.radius, "diameter": self.diameter, "area": self.area}
            for prop in props:
                prop = prop.lower()
                if prop not in valid_props:
                    raise ValueError(f"Invalid property name: {prop}")
                print(f"{self.label}:\n{prop.capitalize()} = {valid_props[prop]}\n")

if __name__=='__main__':
    circle1 = Circle()
    circle2 = Circle(5)
    circle1.display("diameter")
    circle2.display()
