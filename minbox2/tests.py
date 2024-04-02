import unittest

from main import Circle, Triangle


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)  # Проверка с точностью до 10 знаков после запятой

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6.0)

    def test_triangle_is_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())


unittest.main()
