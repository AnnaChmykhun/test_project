import unittest

from func_triangle import triangle


class Triangle2Tests(unittest.TestCase):
    def test_one(self):
        res = triangle(0, 0, 0)
        self.assertEqual(res, 'Not a triangle')

    def test_two(self):
        res = triangle(4, 4, 4)
        self.assertEqual(res, 'Equilateral triangle')

    def test_three(self):
        res = triangle(6, 6, 2)
        self.assertEqual(res, 'Isosceles triangle')

    def test_four(self):
        res = triangle(3, 4, 5)
        self.assertEqual(res, 'Versatile triangle')

    def test_five(self):
        res = triangle(7, 2, 12)
        self.assertEqual(res, 'Not a triangle')

    def test_six(self):
        res = triangle(-3, -4, -5)
        self.assertEqual(res, 'Not a triangle')


if __name__ == "__main__":
    unittest.main()
