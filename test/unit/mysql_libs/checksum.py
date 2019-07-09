#!/usr/bin/python
# Classification (U)

"""Program:  checksum.py

    Description:  Unit testing of checksum in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/checksum.py

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
        col_sql -> Stub holder for mysql_class.Server.col_sql method.

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

        Description:  Stub holder for mysql_class.Server.col_sql method.

        Arguments:
            (input) cmd -> Query command.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_checksum -> Test checksum function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Server = Server()

    def test_checksum(self):

        """Function:  test_checksum

        Description:  Test checksum function.

        Arguments:

        """

        self.assertTrue(mysql_libs.checksum(self.Server, "Dbname", "Tblname"))


if __name__ == "__main__":
    unittest.main()