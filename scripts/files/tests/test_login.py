"""
Unittesting the login functions
"""

import unittest

from ..const import DATA_HANDLE, WRONG_PW_REPEAT
from ..database import connect_mariadb
from ..login import register_user

connect_mariadb()


class LoginTest(unittest.TestCase):
    """
    Creating unittest for the module login.py
    """

    def test_register_user(self):
            """
            Unittest for register_user
            """

            # Creating a data_array with not the same passwords

            data_array = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", "pw_1"], ["", "pw_2"]]
            self.assertEqual(True, WRONG_PW_REPEAT == register_user(data_array))

