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

class Circle:
    """A class to represent a circle"""
    
    def __init__(self, radius=1):
        """Initialize a Circle with a given radius"""
        self.set_radius(radius)
        
    def set_radius(self, radius):
        """Set the radius of the circle"""
        if radius <= 0:
            raise ValueError("Radius must be greater than zero")
        self.radius = radius
        self.diameter = radius * 2
        self.area = round(radius**2 * 3.14, 2)
    
    def get_radius(self):
        """Return the radius of the circle"""
        return self.radius
    
    def get_diameter(self):
        """Return the diameter of the circle"""
        return self.diameter
    
    def get_area(self):
        """Return the area of the circle"""
        return self.area
    
circle1 = Circle()
circle2 = Circle(5)

print(f"Circle 1: \nRadius = {circle1.get_radius()} \nDiameter = {circle1.get_diameter()} \nArea = {circle1.get_area()}")
print(f"\nCircle 2: \nRadius = {circle2.get_radius()} \nDiameter = {circle2.get_diameter()} \nArea = {circle2.get_area()}")

