#!/usr/bin/python
# Classification (U)

"""Program:  slave_start.py

    Description:  Unit testing of slave_start in mysql_class.py.

    Usage:
        test/unit/mysql_class/slave_start.py

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
        __init__ -> Class initialization.
        sql -> Stub holder for Server.sql method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def cmd_sql(self, cmd):

        """Method:  cmd_sql

        Description:  Stub holder for Server.cmd_sql method.

        Arguments:
            (input) cmd -> Query command.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_slave_start -> Test slave_start function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Server = Server()

    def test_slave_start(self):

        """Function:  test_slave_start

        Description:  Test slave_start function.

        Arguments:

        """

        self.assertFalse(mysql_class.slave_start(self.Server))


if __name__ == "__main__":
    unittest.main()
