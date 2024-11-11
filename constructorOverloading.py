class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length  # default to square if width is None

    def area(self):
        return self.length * self.width

# Demonstration
square = Rectangle(4)
rectangle = Rectangle(4, 5)
print("Square area:", square.area())
print("Rectangle area:", rectangle.area())
