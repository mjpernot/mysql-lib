#!/usr/bin/python
# Classification (U)

"""Program:  is_cfg_valid.py

    Description:  Unit testing of is_cfg_valid in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/is_cfg_valid.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import mysql_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for Server class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, name, def_file=None):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        self.name = name
        self.extra_def_file = def_file


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_no_extra_file -> Test with no extra file present.
        test_chk_fails -> Test with check file fails.
        test_cfg_valid -> Test with extra cfg file is valid.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Slave1 = Server("Slave1", "Extra_Def_File")
        self.Slave2 = Server("Slave2")

    @unittest.skip("Bug:  gen_libs.chk_crt_file fails if None is passed.")
    @mock.patch("mysql_libs.gen_libs.chk_crt_file")
    def test_no_extra_file(self, mock_chk):

        """Function:  test_no_extra_file

        Description:  Test with no extra file present.

        Arguments:

        """

        mock_chk.return_value = (False, "Error Message")

        self.assertEqual(mysql_libs.is_cfg_valid([self.Slave1]),
                         (False, "Error Message"))

    @mock.patch("mysql_libs.gen_libs.chk_crt_file")
    def test_chk_fails(self, mock_chk):

        """Function:  test_chk_fails

        Description:  Test with check file fails.

        Arguments:

        """

        mock_chk.return_value = (False, "Error Message")

        self.assertEqual(mysql_libs.is_cfg_valid([self.Slave1]),
                         (False, "Error Message"))

    @mock.patch("mysql_libs.gen_libs.chk_crt_file")
    def test_cfg_valid(self, mock_chk):

        """Function:  test_cfg_valid

        Description:  Test with extra cfg file is valid.

        Arguments:

        """

        mock_chk.return_value = (True, None)

        self.assertEqual(mysql_libs.is_cfg_valid([self.Slave1]), (True, None))


if __name__ == "__main__":
    unittest.main()
