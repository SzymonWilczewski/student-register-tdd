import unittest

from register.register import *


class TestRegisterUnittest(unittest.TestCase):

    def setUp(self):
        self.register = Register()

    def test_add_student(self):
        expected = ["f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", 1]
        actual = self.register.add_student("f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", 1)
        self.assertEqual(expected, actual)

    def tearDown(self):
        self.register = None


if __name__ == '__main__':
    unittest.main()
