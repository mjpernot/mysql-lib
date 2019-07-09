#!/usr/bin/python
# Classification (U)

"""Program:  show_master_stat.py

    Description:  Unit testing of show_master_stat in mysql_class.py.

    Usage:
        test/unit/mysql_class/show_master_stat.py

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

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        __init__ -> Class initialization.
        col_sql -> Stub holder for Server.col_sql method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        pass

    def col_sql(self, cmd):

        """Method:  col_sql

        Description:  Stub holder for Server.col_sql method.

        Arguments:
            (input) cmd -> Stub holder for argument.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_show_master_stat -> Test show_master_stat function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Server = Server()

    def test_show_master_stat(self):

        """Function:  test_show_master_stat

        Description:  Test show_master_stat function.

        Arguments:

        """

        self.assertTrue(mysql_class.show_master_stat(self.Server))


if __name__ == "__main__":
    unittest.main()