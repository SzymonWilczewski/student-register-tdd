import unittest
from hamcrest import *

from register.register import *


class TestRegisterPyHamcrest(unittest.TestCase):

    def setUp(self):
        self.register = Register()

    def test_add_student(self):
        expected = ["f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", 1]
        actual = self.register.add_student("f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", 1)
        assert_that(actual, equal_to(expected))

    def test_edit_student(self):
        expected = [2]
        actual = self.register.edit_student("dc338aff-d851-4c08-a319-ed4e18640b36", new_first_name=None,
                                            new_last_name=None, new_year=2)
        assert_that(actual, equal_to(expected))

    def tearDown(self):
        self.register = None


if __name__ == '__main__':
    unittest.main()
