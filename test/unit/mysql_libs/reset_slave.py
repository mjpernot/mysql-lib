#!/usr/bin/python
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
        sql -> Stub holder for mysql_class.Server.sql method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        pass

    def sql(self, cmd, var):

        """Method:  sql

        Description:  Stub holder for mysql_class.Server.sql method.

        Arguments:
            (input) cmd -> Query command.
            (input) var -> Global variable name.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_reset_slave -> Test reset_slave function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Server = Server()

    def test_reset_slave(self):

        """Function:  test_reset_slave

        Description:  Test reset_slave function.

        Arguments:

        """

        self.assertTrue(mysql_libs.reset_slave(self.Server))


if __name__ == "__main__":
    unittest.main()
