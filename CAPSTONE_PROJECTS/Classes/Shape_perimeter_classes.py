# **Shape Area and Perimeter Classes**
# Create an abstract class called Shape and then inherit from it other shapes like diamond, rectangle, circle, triangle etc. 
# Then have each class override the area and perimeter functionality to handle each shape type.  
#[[masegaloeh (Python)]](https://github.com/masegaloeh/freetime-projects/blob/master/class/shape/shape.py) 

class Shape:

    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self,height,width)
        
        self.height = height
        self.width = width
        