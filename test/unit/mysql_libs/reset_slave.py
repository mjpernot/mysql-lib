# Classification (U)

"""Program:  reset_slave.py

    Description:  Unit testing of reset_slave in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/reset_slave.py

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
        cmd_sql

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = None
        self.version = (8, 0, 28)

    def cmd_sql(self, cmd):

        """Method:  cmd_sql

        Description:  Stub holder for mysql_class.Server.cmd_sql method.

        Arguments:
            (input) cmd

        """

        self.cmd = cmd

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_post_8022
        test_pre_8022
        test_reset_slave

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_post_8022(self):

        """Function:  test_post_8022

        Description:  Test with post-MySQL 8.0.22 version.

        Arguments:

        """

        self.assertFalse(mysql_libs.reset_slave(self.server))

    def test_pre_8022(self):

        """Function:  test_pre_8022

        Description:  Test with pre-MySQL 8.0.22 version.

        Arguments:

        """

        self.server.version = (8, 0, 21)

        self.assertFalse(mysql_libs.reset_slave(self.server))

    def test_reset_slave(self):

        """Function:  test_reset_slave

        Description:  Test reset_slave function.

        Arguments:

        """

        self.assertFalse(mysql_libs.reset_slave(self.server))


if __name__ == "__main__":
    unittest.main()
