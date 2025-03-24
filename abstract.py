from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass

# Circle Class Derived from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Rectangle Class Derived from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def circumference(self):
        return 2 * (self.length + self.width)

# Demonstration
if __name__ == "__main__":
    # Create a Circle object
    circle = Circle(5)
    print(f"Circle: Area = {circle.area():.2f}, Circumference = {circle.circumference():.2f}")

    # Create a Rectangle object
    rectangle = Rectangle(4, 6)
    print(f"Rectangle: Area = {rectangle.area()}, Circumference = {rectangle.circumference()}")
