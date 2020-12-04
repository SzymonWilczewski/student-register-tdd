import unittest

from register.register import *
from parameterized import parameterized


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

    def tearDown(self):
        self.register = None


if __name__ == '__main__':
    unittest.main()
