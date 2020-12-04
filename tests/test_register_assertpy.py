import unittest
from assertpy import *

from register.register import *


class TestRegisterAssertpy(unittest.TestCase):

    def setUp(self):
        self.register = Register()

    def test_add_student(self):
        expected = ["f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", 1]
        actual = self.register.add_student("f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", 1)
        assert_that(actual).is_equal_to(expected)

    def test_edit_student(self):
        expected = [2]
        actual = self.register.edit_student("dc338aff-d851-4c08-a319-ed4e18640b36", new_first_name=None,
                                            new_last_name=None, new_year=2)
        assert_that(actual).is_equal_to(expected)

    def test_remove_student(self):
        expected = "dc338aff-d851-4c08-a319-ed4e18640b36"
        actual = self.register.remove_student("dc338aff-d851-4c08-a319-ed4e18640b36")
        assert_that(actual).is_equal_to(expected)

    def test_student_id(self):
        expected = ["dc338aff-d851-4c08-a319-ed4e18640b36"]
        actual = self.register.student_id("Andrzej", "Kowalski")
        assert_that(actual).is_equal_to(expected)

    def test_add_subject(self):
        expected = "Informatyka"
        actual = self.register.add_subject("dc338aff-d851-4c08-a319-ed4e18640b36", "Informatyka")
        assert_that(actual).is_equal_to(expected)

    def test_edit_subject(self):
        expected = "Informatyka"
        actual = self.register.edit_subject("dc338aff-d851-4c08-a319-ed4e18640b36", 0, "Informatyka")
        assert_that(actual).is_equal_to(expected)

    def test_remove_subject(self):
        expected = "Język polski"
        actual = self.register.remove_subject("dc338aff-d851-4c08-a319-ed4e18640b36", 0)
        assert_that(actual).is_equal_to(expected)

    def test_add_grade(self):
        expected = 2.5
        actual = self.register.add_grade("dc338aff-d851-4c08-a319-ed4e18640b36", 0, 2.5)
        assert_that(actual).is_equal_to(expected)

    def test_add_grade_is_greater_than_2(self):
        actual = self.register.add_grade("dc338aff-d851-4c08-a319-ed4e18640b36", 0, 2.5)
        assert_that(actual).is_greater_than(2)

    def test_edit_grades(self):
        expected = [5, 2.5, 3, 1.5, 1]
        actual = self.register.edit_grades("dc338aff-d851-4c08-a319-ed4e18640b36", 0, [5, 2.5, 3, 1.5, 1])
        assert_that(actual).is_equal_to(expected)

    def test_edit_grades_3_in_grades(self):
        actual = self.register.edit_grades("dc338aff-d851-4c08-a319-ed4e18640b36", 0, [5, 2.5, 3, 1.5, 1])
        assert_that(actual).contains(3)

    def test_average_from_subject(self):
        expected = 2.6
        actual = self.register.average_from_subject("dc338aff-d851-4c08-a319-ed4e18640b36", 0)
        assert_that(actual).is_equal_to(expected)

    def test_average_from_subject_less_or_equal_3(self):
        actual = self.register.average_from_subject("dc338aff-d851-4c08-a319-ed4e18640b36", 0)
        assert_that(actual).is_less_than_or_equal_to(3)

    def test_average_from_all_subjects(self):
        expected = 4.44
        actual = self.register.average_from_all_subjects("dc338aff-d851-4c08-a319-ed4e18640b36")
        assert_that(actual).is_equal_to(expected)

    def test_average_from_all_subjects_is_close_to_4_4(self):
        actual = self.register.average_from_all_subjects("dc338aff-d851-4c08-a319-ed4e18640b36")
        assert_that(actual).is_close_to(4.4, 0.05)

    def test_add_comment(self):
        expected = "Uczeń przeszkadza w prowadzeniu zajęć"
        actual = self.register.add_comment("dc338aff-d851-4c08-a319-ed4e18640b36",
                                           "Uczeń przeszkadza w prowadzeniu zajęć")
        assert_that(actual).is_equal_to(expected)

    def test_edit_comment(self):
        expected = "Uczeń przeszkadza w prowadzeniu zajęć"
        actual = self.register.edit_comment("dc338aff-d851-4c08-a319-ed4e18640b36", 0,
                                            "Uczeń przeszkadza w prowadzeniu zajęć")
        assert_that(actual).is_equal_to(expected)

    # EXCEPTIONS

    def test_add_student_exception(self):
        assert_that(self.register.add_student).raises(TypeError).when_called_with(
            "f53b878e-7105-4f44-9f88-f1cc5d8b63f5", "Anna", "Nowak", "1")

    def test_edit_student_exception(self):
        assert_that(self.register.edit_student).raises(TypeError).when_called_with(
            "dc338aff-d851-4c08-a319-ed4e18640b36", new_first_name=None, new_last_name=None, new_year="2")

    def test_remove_student_exception(self):
        assert_that(self.register.remove_student).raises(TypeError).when_called_with(123)

    def test_student_id_exception(self):
        assert_that(self.register.student_id).raises(TypeError).when_called_with("Andrzej", [])

    def test_add_subject_exception(self):
        assert_that(self.register.add_subject).raises(TypeError).when_called_with(
            "dc338aff-d851-4c08-a319-ed4e18640b36", True)

    def test_edit_subject_exception(self):
        assert_that(self.register.edit_subject).raises(TypeError).when_called_with(
            "dc338aff-d851-4c08-a319-ed4e18640b36", 0, [])

    def test_remove_subject_exception(self):
        assert_that(self.register.remove_subject).raises(TypeError).when_called_with(
            "dc338aff-d851-4c08-a319-ed4e18640b36", False)

    def test_add_grade_exception(self):
        assert_that(self.register.add_grade).raises(TypeError).when_called_with("dc338aff-d851-4c08-a319-ed4e18640b36",
                                                                                0, "2.5")

    def test_edit_grades_exception(self):
        assert_that(self.register.edit_grades).raises(TypeError).when_called_with(
            "dc338aff-d851-4c08-a319-ed4e18640b36", 0, 5)

    def test_average_from_subject_exception(self):
        assert_that(self.register.average_from_subject).raises(TypeError).when_called_with(123, 0)

    def test_average_from_all_subjects_exception(self):
        assert_that(self.register.average_from_all_subjects).raises(TypeError).when_called_with([])

    def test_add_comment_exception(self):
        assert_that(self.register.add_comment).raises(TypeError).when_called_with(
            "dc338aff-d851-4c08-a319-ed4e18640b36", [])

    def test_edit_comment_exception(self):
        assert_that(self.register.edit_comment).raises(TypeError).when_called_with(
            "dc338aff-d851-4c08-a319-ed4e18640b36", True, "Uczeń przeszkadza w prowadzeniu zajęć")

    def tearDown(self):
        self.register = None


if __name__ == '__main__':
    unittest.main()
