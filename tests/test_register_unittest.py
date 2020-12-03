import unittest

from register.register import *


class TestRegisterUnittest(unittest.TestCase):

    def setUp(self):
        self.register = Register()

    def tearDown(self):
        self.register = None


if __name__ == '__main__':
    unittest.main()
