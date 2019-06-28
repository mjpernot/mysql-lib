#!/usr/bin/python
# Classification (U)

"""Program:  fetch_global_var.py

    Description:  Unit testing of fetch_global_var in mysql_class.py.

    Usage:
        test/unit/mysql_class/fetch_global_var.py

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
        sql -> Stub holder for Server.sql method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        pass

    def sql(self, cmd, var, res_set):

        """Method:  sql

        Description:  Stub holder for Server.sql method.

        Arguments:
            (input) cmd -> Stub holder for argument.
            (input) var -> Global variable name.
            (input) res_set -> row|all - Single row or all rows returned.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_fetch_global_var -> Test fetch_global_var function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Server = Server()

    def test_fetch_global_var(self):

        """Function:  test_fetch_global_var

        Description:  Test fetch_global_var function.

        Arguments:

        """

        self.assertTrue(mysql_class.fetch_global_var(self.Server, "Variable"))


if __name__ == "__main__":
    unittest.main()
