# Classification (U)

"""Program:  start_slave_until.py

    Description:  Unit testing of start_slave_until in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/start_slave_until.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_libs
import version

__version__ = version.__version__


class Server(object):

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

        self.gtid_mode = "Yes"
        self.cmd = None
        self.version = (8, 0, 28)

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
        test_post_8026
        test_pre_8026
        test_post_8022
        test_pre_8022
        test_fail
        test_gtid
        test_non_gtid

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_post_8026(self):

        """Function:  test_post_8026

        Description:  Test with post-MySQL 8.0.26.

        Arguments:

        """

        self.assertEqual(
            mysql_libs.start_slave_until(
                self.server, gtid=12345, stop_pos="before"), (False, None))

    def test_pre_8026(self):

        """Function:  test_pre_8026

        Description:  Test with pre-MySQL 8.0.26.

        Arguments:

        """

        self.server.version = (8, 0, 24)

        self.assertEqual(
            mysql_libs.start_slave_until(
                self.server, gtid=12345, stop_pos="before"), (False, None))

    def test_post_8022(self):

        """Function:  test_post_8022

        Description:  Test with post-MySQL 8.0.22.

        Arguments:

        """

        self.assertEqual(
            mysql_libs.start_slave_until(
                self.server, gtid=12345, stop_pos="before"), (False, None))

    def test_pre_8022(self):

        """Function:  test_pre_8022

        Description:  Test with pre-MySQL 8.0.22.

        Arguments:

        """

        self.server.version = (8, 0, 21)

        self.assertEqual(
            mysql_libs.start_slave_until(
                self.server, gtid=12345, stop_pos="before"), (False, None))

    def test_fail(self):

        """Function:  test_fail

        Description:  Test failure option.

        Arguments:

        """

        self.assertEqual(
            mysql_libs.start_slave_until(self.server),
            (True, "One of the arguments is missing."))

    def test_gtid(self):

        """Function:  test_gtid

        Description:  Test with gtid mode.

        Arguments:

        """

        self.assertEqual(
            mysql_libs.start_slave_until(
                self.server, gtid=12345, stop_pos="before"), (False, None))

    def test_non_gtid(self):

        """Function:  test_non_gtid

        Description:  Test with non-gtid mode.

        Arguments:

        """

        self.assertEqual(
            mysql_libs.start_slave_until(
                self.server, log_file="Filename", log_pos=12345),
            (False, None))


if __name__ == "__main__":
    unittest.main()
