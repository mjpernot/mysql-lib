#!/usr/bin/python
# Classification (U)

"""Program:  Server_is_connected.py

    Description:  Unit testing of Server.is_connected in mysql_class.py.

    Usage:
        test/unit/mysql_class/Server_is_connected.py

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
import mock

# Local
sys.path.append(os.getcwd())
import lib.gen_libs as gen_libs
import mysql_class
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class which is a representation of a Server class.

    Super-Class:  object

    Sub-Classes:

    Methods:
        __init__ -> Initialize environment.
        is_connected -> Test of is_connected method.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialize environment.

        Arguments:

        """

        pass

    def is_connected(self):

        """Function:  is_connected

        Description:  Test of is_connected method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_is_connected_true -> Test is_connected is True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.conn = Server()

    def test_is_connected_true(self):

        """Function:  test_is_connected_true

        Description:  Test is_connected is True.

        Arguments:

        """

        mysqldb = self.conn

        self.assertTrue(mysqldb.is_connected())


if __name__ == "__main__":
    unittest.main()
