class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def area(self):
        pass

    def describe(self):
        print(
            f"A {self.color} shape that is {'filled' if self.is_filled else 'not filled'}.")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def describe(self):
        super().describe()
        print(f"A {self.color} circle with a radius of {self.radius} that is {'filled' if self.is_filled else 'not filled'}.")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def area(self):
        return self.width ** 2


circle = Circle("red", True, 5)
print(f"Circle area: {circle.describe()}")
