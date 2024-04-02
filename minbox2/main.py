import math


class Shape:
    def area(self):
        pass

    def is_right_triangle(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Используем формулу Герона для вычисления площади треугольника
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(
            semi_perimeter
            * (semi_perimeter - self.side1)
            * (semi_perimeter - self.side2)
            * (semi_perimeter - self.side3)
        )

    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        sides.sort()  # Сортировка сторон по возрастанию

        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2