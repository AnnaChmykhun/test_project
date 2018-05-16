import unittest

from func_is_triangle import is_triangle


class TriangleTests(unittest.TestCase):
    def test_one(self):
        res = is_triangle(0, 0, 0)
        self.assertEqual(res, False)

    def test_two(self):
        res = is_triangle(4, 4, 4)
        self.assertEqual(res, True)

    def test_three(self):
        res = is_triangle(6, 6, 2)
        self.assertEqual(res, True)

    def test_four(self):
        res = is_triangle(3, 4, 5)
        self.assertEqual(res, True)

    def test_five(self):
        res = is_triangle(7, 2, 12)
        self.assertEqual(res, False)

    def test_six(self):
        res = is_triangle(-3, -4, -5)
        self.assertEqual(res, False)


if __name__ == "__main__":
    unittest.main()
