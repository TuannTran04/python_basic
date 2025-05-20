class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:1f} cm"

    @property
    def height(self):
        return f"{self._height:1f} cm"

    @width.setter
    def width(self, new_width: float):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be positive")

    @height.setter
    def height(self, new_height: float):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be positive")

    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")


rectangle1 = Rectangle(5.0, 10.0)

rectangle1.width = -15.0
rectangle1.height = 20.0

del rectangle1.width
del rectangle1.height

print(rectangle1.width)
print(rectangle1.height)
