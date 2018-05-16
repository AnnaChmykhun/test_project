import unittest

from func_year_leap import is_year_leap


class YearLeapTests(unittest.TestCase):
    def test_one(self):
        res = is_year_leap(1696)
        self.assertEqual(res, True)

    def test_two(self):
        res = is_year_leap(1900)
        self.assertEqual(res, False)

    def test_three(self):
        res = is_year_leap(2000)
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main()
