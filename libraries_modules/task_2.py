
class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f"This is a {self.color} shape.")



class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)   
        self.width = width
        self.height = height

    def describe(self):
        area = self.width * self.height
        print(f"Rectangle Details:")
        print(f"Color : {self.color}")
        print(f"Width : {self.width}")
        print(f"Height: {self.height}")
        print(f"Area  : {area}")



rect = Rectangle("Blue", 10, 5)
rect.describe()
