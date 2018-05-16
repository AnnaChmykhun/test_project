import unittest

from Task_1_ITEmployee import ITEmployee


class ITEmployeeTests(unittest.TestCase):
    def setUp(self):
        self.ite = ITEmployee('Sergio Ch', 1992, 'Java Developer', 1, 100)

    def test_empty_skills(self):
        self.assertEqual(len(self.ite.skills), 0)

    def test_add_skill(self):
        self.ite.add_skill('Java')
        self.assertIn('Java', self.ite.skills)

    def test_add_skills(self):
        self.ite.add_skills('Java Script', 'Python')
        self.assertIn('Java Script', self.ite.skills)
        self.assertIn('Python', self.ite.skills)


if __name__ == "__main__":
    unittest.main()
