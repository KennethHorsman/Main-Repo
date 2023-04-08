# Rectangle.py

class Rectangle(object):
    # Declare public methods here
    def __init__(self, length, width):
        # Set class instance variables here
        self.length = length
        self.width = width

    def calculateArea(self):
        # Write calculateArea here
        return self.length * self.width

    def calculatePerimeter(self):
        # Write calculatePerimeter here
        return (2 * self.length) + (2 * self.width)
        
    
# MyRectangleClassProgram.py
 
from Rectangle import Rectangle

rectangle1 = Rectangle(10.0, 5.0)
rectangle2 = Rectangle(7.0, 3.0)

print("Perimeter of rectangle1 is " + str(rectangle1.calculatePerimeter()))
print("Area of rectangle1 is " + str(rectangle1.calculateArea()))
print("Perimeter of rectangle2 is " + str(rectangle2.calculatePerimeter()))
print("Area of rectangle2 is " + str(rectangle2.calculateArea()))
