from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Example usage:
circle = Circle(radius=5.0)
rectangle = Rectangle(length=4.0, width=3.0)

circle_area = circle.calculate_area()
rectangle_area = rectangle.calculate_area()

print(f"Circle Area: {circle_area}")
print(f"Rectangle Area: {rectangle_area}")
