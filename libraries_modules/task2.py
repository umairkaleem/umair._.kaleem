import matplotlib.pyplot as plt

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
        print("\n Rectangle Details")
        print("----------------------------")
        print("Color  :", self.color)
        print("Width  :", self.width)
        print("Height :", self.height)
        print("Area   :", area)

    def draw(self):
        plt.figure()
        rectangle = plt.Rectangle((0, 0), self.width, self.height, color=self.color)
        plt.gca().add_patch(rectangle)
        plt.xlim(0, self.width + 2)
        plt.ylim(0, self.height + 2)
        plt.title("Simple Rectangle Visualization")
        plt.axis("equal")
        plt.show()


rect = Rectangle("lightblue", 6, 3)


rect.describe()
rect.draw()
