#!/usr/bin/python
# Classification (U)

"""Program:  show_slave_stat.py

    Description:  Unit testing of show_slave_stat in mysql_class.py.

    Usage:
        test/unit/mysql_class/show_slave_stat.py

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
import mysql_class
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__
        col_sql

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = None
        self.version = (8, 0, 28)

    def col_sql(self, cmd):

        """Method:  col_sql

        Description:  Stub holder for Server.col_sql method.

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
        test_show_slave_stat

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_post_8022(self):

        """Function:  test_post_8022

        Description:  Test with post-MySQL 8.0.22.

        Arguments:

        """

        self.assertTrue(mysql_class.show_slave_stat(self.server))

    def test_pre_8022(self):

        """Function:  test_pre_8022

        Description:  Test with pre-MySQL 8.0.22.

        Arguments:

        """

        self.server.version = (8, 0, 21)

        self.assertTrue(mysql_class.show_slave_stat(self.server))

    def test_show_slave_stat(self):

        """Function:  test_show_slave_stat

        Description:  Test show_slave_stat function.

        Arguments:

        """

        self.assertTrue(mysql_class.show_slave_stat(self.server))


if __name__ == "__main__":
    unittest.main()
