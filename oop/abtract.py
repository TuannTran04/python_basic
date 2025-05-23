from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(5), Square(4), Pizza("pepperoni", 3)]

for shape in shapes:
    print(f"Area: {shape.area()}")
