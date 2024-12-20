# Classification (U)

"""Program:  purge_bin_logs.py

    Description:  Unit testing of purge_bin_logs in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/purge_bin_logs.py

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
        test_purge_bin_logs

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_purge_bin_logs(self):

        """Function:  test_purge_bin_logs

        Description:  Test purge_bin_logs function.

        Arguments:

        """

        self.assertFalse(mysql_libs.purge_bin_logs(self.server, "TO",
                                                   "Filename"))


if __name__ == "__main__":
    unittest.main()
