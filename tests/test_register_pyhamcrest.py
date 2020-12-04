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

    def test_remove_student(self):
        expected = "dc338aff-d851-4c08-a319-ed4e18640b36"
        actual = self.register.remove_student("dc338aff-d851-4c08-a319-ed4e18640b36")
        assert_that(actual, equal_to(expected))

    def test_student_id(self):
        expected = ["dc338aff-d851-4c08-a319-ed4e18640b36"]
        actual = self.register.student_id("Andrzej", "Kowalski")
        assert_that(actual, equal_to(expected))

    def test_add_subject(self):
        expected = "Informatyka"
        actual = self.register.add_subject("dc338aff-d851-4c08-a319-ed4e18640b36", "Informatyka")
        assert_that(actual, equal_to(expected))

    def test_edit_subject(self):
        expected = "Informatyka"
        actual = self.register.edit_subject("dc338aff-d851-4c08-a319-ed4e18640b36", 0, "Informatyka")
        assert_that(actual, equal_to(expected))

    def test_remove_subject(self):
        expected = "Język polski"
        actual = self.register.remove_subject("dc338aff-d851-4c08-a319-ed4e18640b36", 0)
        assert_that(actual, equal_to(expected))

    def test_add_grade(self):
        expected = 2.5
        actual = self.register.add_grade("dc338aff-d851-4c08-a319-ed4e18640b36", 0, 2.5)
        assert_that(actual, equal_to(expected))

    def test_edit_grades(self):
        expected = [5, 2.5, 3, 1.5, 1]
        actual = self.register.edit_grades("dc338aff-d851-4c08-a319-ed4e18640b36", 0, [5, 2.5, 3, 1.5, 1])
        assert_that(actual, equal_to(expected))

    def test_average_from_subject(self):
        expected = 2.6
        actual = self.register.average_from_subject("dc338aff-d851-4c08-a319-ed4e18640b36", 0)
        assert_that(actual, equal_to(expected))

    def test_average_from_all_subjects(self):
        expected = 4.44
        actual = self.register.average_from_all_subjects("dc338aff-d851-4c08-a319-ed4e18640b36")
        assert_that(actual, equal_to(expected))

    def test_add_comment(self):
        expected = "Uczeń przeszkadza w prowadzeniu zajęć"
        actual = self.register.add_comment("dc338aff-d851-4c08-a319-ed4e18640b36",
                                           "Uczeń przeszkadza w prowadzeniu zajęć")
        assert_that(actual, equal_to(expected))

    def test_edit_comment(self):
        expected = "Uczeń przeszkadza w prowadzeniu zajęć"
        actual = self.register.edit_comment("dc338aff-d851-4c08-a319-ed4e18640b36", 0,
                                            "Uczeń przeszkadza w prowadzeniu zajęć")
        assert_that(actual, equal_to(expected))

    # EXCEPTIONS

    def test_add_student_exception(self):
        assert_that(
            calling(self.register.add_student).with_args("f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", "1"),
            raises(TypeError))

    def test_edit_student_exception(self):
        assert_that(
            calling(self.register.edit_student).with_args("dc338aff-d851-4c08-a319-ed4e18640b36", new_first_name=None,
                                                          new_last_name=None, new_year="2"), raises(TypeError))

    def test_remove_student_exception(self):
        assert_that(calling(self.register.remove_student).with_args(123), raises(TypeError))

    def tearDown(self):
        self.register = None


if __name__ == '__main__':
    unittest.main()
