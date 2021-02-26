"""
Unittesting the login functions
"""

# Python libraries---------------------------------------------------------------------------------
import unittest

# Overall consts-----------------------------------------------------------------------------------
from scripts.files.const import DATA_HANDLE, WRONG_PW_REPEAT, EMAIL_USED, REGISTER_INSERT_ERROR
from scripts.files.const import EMAIL_NOT_KNOWN, WRONG_LOGIN_PW

# Other necessarities------------------------------------------------------------------------------
from scripts.files.database import connect_mariadb

# Functions from module to test--------------------------------------------------------------------
from scripts.files.login import register_user, verify_login


# Create connection to the Database
connect_mariadb()


class LoginTest(unittest.TestCase):
    """
    Creating unittest for the module login.py
    """

    def test_register_user(self):
        """
        Testing function verify_login from login.py
        """

        # Creating a data_array with not the same passwords
        data_array = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", "pw_1"], ["", "pw_2"]]
        self.assertEqual(True, WRONG_PW_REPEAT == register_user(data_array))

        # Data Array with already used email
        data_array = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", "alexm01@freenet.de"], ["", ""], ["", ""]]
        self.assertEqual(True, EMAIL_USED == register_user(data_array))

        # Data Array with false values; here a string where an int should be with unknown Email
        data_array = [["", ""], ["", ""], ["", ""], ["", "DefinetlyAnInt"], ["", ""], ["", "test@unknown.mail"], ["", ""], ["", ""]]
        self.assertEqual(True, REGISTER_INSERT_ERROR == register_user(data_array))


    def test_verify_login(self):
        """
        Testing function verify_login from login.py
        """

        # Creating a data array with unknown mail
        data_array = [["email", "test@unknown.mail"], ["password", ""]]
        self.assertEqual(True, EMAIL_NOT_KNOWN == verify_login(data_array))

        # Creating a data array with known mail but wrong pw
        data_array = [["email", "alexm01@freenet.de"], ["password", "Gabelstaplerfachverkäufer"]]
        self.assertEqual(True, WRONG_LOGIN_PW == verify_login(data_array))
