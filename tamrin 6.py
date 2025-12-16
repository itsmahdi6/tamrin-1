from abc import ABC ,abstractmethod
class Shape(ABC) :
    @abstractmethod
    def calculate_area (self) :
        pass

    @abstractmethod
    def calculate_perimeter(self) :
        pass


class Rectangle (Shape):
    def __init__(self , width ,height):
        self.width = width
        self.height = height 

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2*( self.height + self.width)

class Circle (Shape):
    def __init__(self , radius):
        self.radius = radius 

    def calculate_area(self):
        return self.radius * self.radius * 3.14159      
    
    def calculate_perimeter(self):
        return self.radius * 2 * 3.14159
    

shapes = [Rectangle(2 , 8) , Circle(4)]
for shape in shapes :
    print("Area :", shape.calculate_area())    
    print("Perimeter :" , shape.calculate_perimeter())
    print("***")