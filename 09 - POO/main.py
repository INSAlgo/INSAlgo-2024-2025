

from math import sqrt

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return round(self.width * self.height, 6)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side_length={self.width})"

def increase_rectangle_area_by_10_percent(rectangle):
    rectangle.set_width(rectangle.width * 1.1)

def corrected_increase_rectangle_area_by_10_percent(rectangle):
    if isinstance(rectangle, Square):
        rectangle.set_side(rectangle.width * sqrt(1.1))
    else:
        rectangle.set_width(rectangle.width * 1.1)

# Example usage
rect = Rectangle(3, 4)
print(rect)  # Rectangle(width=3, height=4)
print("Area:", rect.get_area())  # Area: 12

square = Square(5)
print(square)  # Square(side_length=5)
print("Area:", square.get_area())  # Area: 25

shapes = [rect, square]
for shape in shapes:
    original_area = shape.width * shape.height
    corrected_increase_rectangle_area_by_10_percent(shape)
    print(shape, "Area:", shape.get_area(), end=" -> ")
    if shape.get_area() == round(original_area * 1.1, 6):
        print("Correct")
    else:
        print("Wrong")
