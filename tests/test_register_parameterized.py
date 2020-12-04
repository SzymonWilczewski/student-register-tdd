import unittest

from register.register import *
from parameterized import parameterized, parameterized_class


class TestRegisterParameterizedExpand(unittest.TestCase):

    def setUp(self):
        self.register = Register()

    @parameterized.expand([
        ("Jan", None, None, ["Jan"]),
        (None, "Kamiński", None, ["Kamiński"]),
        (None, None, 2, [2]),
        ("Jan", "Kamiński", None, ["Jan", "Kamiński"]),
        ("Jan", None, 2, ["Jan", 2]),
        (None, "Kamiński", 2, ["Kamiński", 2]),
        ("Jan", "Kamiński", 2, ["Jan", "Kamiński", 2]),
    ])
    def test_edit_student_expand(self, new_first_name, new_last_name, new_year, expected):
        actual = self.register.edit_student("dc338aff-d851-4c08-a319-ed4e18640b36", new_first_name, new_last_name,
                                            new_year)
        self.assertEqual(expected, actual)

    @parameterized.expand([
        (["Jan"], None, None),
        (None, ["Kamiński"], None),
        (None, None, "2"),
        (["Jan"], ["Kamiński"], None),
        (["Jan"], None, "2"),
        (None, ["Kamiński"], "2"),
        (["Jan"], ["Kamiński"], "2"),
        (True, None, None),
        (None, True, None),
        (None, None, True),
    ])
    def test_edit_student_expand_exceptions(self, new_first_name, new_last_name, new_year):
        with self.assertRaises(TypeError):
            self.register.edit_student("dc338aff-d851-4c08-a319-ed4e18640b36", new_first_name, new_last_name, new_year)

    def tearDown(self):
        self.register = None


@parameterized_class(("new_first_name", "new_last_name", "new_year", "expected"), [
    ("Jan", None, None, ["Jan"]),
    (None, "Zieliński", None, ["Zieliński"]),
    (None, None, 2, [2]),
    ("Jan", "Zieliński", None, ["Jan", "Zieliński"]),
    ("Jan", None, 2, ["Jan", 2]),
    (None, "Zieliński", 2, ["Zieliński", 2]),
    ("Jan", "Zieliński", 2, ["Jan", "Zieliński", 2]),
])
class TestRegisterParameterizedClass(unittest.TestCase):

    def setUp(self):
        self.register = Register()

    def test_edit_student_class(self):
        actual = self.register.edit_student("dc338aff-d851-4c08-a319-ed4e18640b36", self.new_first_name,
                                            self.new_last_name, self.new_year)
        self.assertEqual(self.expected, actual)

    def tearDown(self):
        self.register = None


if __name__ == '__main__':
    unittest.main()
