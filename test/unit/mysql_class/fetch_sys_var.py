# Classification (U)

"""Program:  fetch_sys_var.py

    Description:  Unit testing of fetch_sys_var in mysql_class.py.

    Usage:
        test/unit/mysql_class/fetch_sys_var.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_class                          # pylint:disable=E0401,C0413
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
        self.var = None

    def vert_sql(self, cmd, var):

        """Method:  sql

        Description:  Stub holder for Server.vert_sql method.

        Arguments:
            (input) cmd
            (input) var

        """

        self.cmd = cmd
        self.var = var

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_fetch_sys_var

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_fetch_sys_var(self):

        """Function:  test_fetch_sys_var

        Description:  Test fetch_sys_var function.

        Arguments:

        """

        self.assertTrue(mysql_class.fetch_sys_var(self.server, "Variable"))


if __name__ == "__main__":
    unittest.main()
