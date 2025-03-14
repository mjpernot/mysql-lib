# Classification (U)

"""Program:  select_wait_until.py

    Description:  Unit testing of select_wait_until in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/select_wait_until.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_libs                           # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():                             # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__
        sql

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = None
        self.res_set = None

    def sql(self, cmd, res_set):

        """Method:  sql

        Description:  Stub holder for mysql_class.Server.sql method.

        Arguments:
            (input) cmd
            (input) res_set

        """

        self.cmd = cmd
        self.res_set = res_set

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_select_wait_until

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_select_wait_until(self):

        """Function:  test_select_wait_until

        Description:  Test select_wait_until function.

        Arguments:

        """

        self.assertTrue(mysql_libs.select_wait_until(self.server, "Gtidpos"))


if __name__ == "__main__":
    unittest.main()
