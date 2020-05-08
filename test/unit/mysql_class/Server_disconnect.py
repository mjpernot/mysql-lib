#!/usr/bin/python
# Classification (U)

"""Program:  Server_disconnect.py

    Description:  Unit testing of Server.disconnect in mysql_class.py.

    Usage:
        test/unit/mysql_class/Server_disconnect.py

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

    Description:  Class stub holder for Server class.

    Methods:
        __init__ -> Initialize environment.
        disconnect -> Test of disconnect method.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialize environment.

        Arguments:

        """

        pass

    def disconnect(self):

        """Function:  disconnect

        Description:  Test of disconnect method.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_disconnect -> Test disconnect method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.conn = Server()

    def test_disconnect(self):

        """Function:  test_disconnect

        Description:  Test disconnect method.

        Arguments:

        """

        mysqldb = self.conn

        self.assertFalse(mysqldb.disconnect())


if __name__ == "__main__":
    unittest.main()
