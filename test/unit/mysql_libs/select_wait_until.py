#!/usr/bin/python
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

    def sql(self, cmd, res_set, var):

        """Method:  sql

        Description:  Stub holder for mysql_class.Server.sql method.

        Arguments:
            (input) cmd -> Query command.
            (input) res_set -> Return set type.
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
        test_select_wait_until -> Test select_wait_until function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Server = Server()

    def test_select_wait_until(self):

        """Function:  test_select_wait_until

        Description:  Test select_wait_until function.

        Arguments:

        """

        self.assertTrue(mysql_libs.select_wait_until(self.Server, "Gtidpos"))


if __name__ == "__main__":
    unittest.main()
