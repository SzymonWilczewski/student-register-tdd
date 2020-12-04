import unittest

from register.register import *


class TestRegisterUnittest(unittest.TestCase):

    def setUp(self):
        self.register = Register()

    def test_add_student(self):
        expected = ["f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", 1]
        actual = self.register.add_student("f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", 1)
        self.assertEqual(expected, actual)

    def test_edit_student(self):
        expected = [2]
        actual = self.register.edit_student("dc338aff-d851-4c08-a319-ed4e18640b36", new_first_name=None,
                                            new_last_name=None, new_year=2)
        self.assertEqual(expected, actual)

    def test_remove_student(self):
        expected = "dc338aff-d851-4c08-a319-ed4e18640b36"
        actual = self.register.remove_student("dc338aff-d851-4c08-a319-ed4e18640b36")
        self.assertEqual(expected, actual)

    def test_student_id(self):
        expected = ["dc338aff-d851-4c08-a319-ed4e18640b36"]
        actual = self.register.student_id("Andrzej", "Kowalski")
        self.assertEqual(expected, actual)

    def test_add_subject(self):
        expected = "Informatyka"
        actual = self.register.add_subject("dc338aff-d851-4c08-a319-ed4e18640b36", "Informatyka")
        self.assertEqual(expected, actual)

    def test_edit_subject(self):
        expected = "Informatyka"
        actual = self.register.edit_subject("dc338aff-d851-4c08-a319-ed4e18640b36", 0, "Informatyka")
        self.assertEqual(expected, actual)

    def test_remove_subject(self):
        expected = "Język polski"
        actual = self.register.remove_subject("dc338aff-d851-4c08-a319-ed4e18640b36", 0)
        self.assertEqual(expected, actual)

    def tearDown(self):
        self.register = None


if __name__ == '__main__':
    unittest.main()
