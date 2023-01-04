# Classification (U)

"""Program:  disconnect.py

    Description:  Unit testing of disconnect in cmds_gen.py.

    Usage:
        test/unit/mysql_libs/disconnect.py

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

# Local
sys.path.append(os.getcwd())
import mysql_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class is a representation of Server class.

    Methods:
        __init__
        disconnect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Mail class.

        Arguments:

        """

        self.conn = True

    def disconnect(self):

        """Method:  disconnect

        Description:  Method is representation of disconnect method.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_combo_no_conn2
        test_combo_no_conn
        test_combo2
        test_combo
        test_list_no_conn3
        test_list_no_conn2
        test_list_no_conn
        test_single_no_conn
        test_list_entry3
        test_list_entry2
        test_list_entry
        test_single_entry

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.server2 = Server()
        self.server3 = Server()
        self.server4 = Server()

    def test_combo_no_conn2(self):

        """Function:  test_combo_no_conn2

        Description:  Test with combination and no connections.

        Arguments:

        """

        self.server4.conn = None
        self.server2.conn = None

        self.assertFalse(mysql_libs.disconnect(self.server, self.server4,
                                               [self.server2, self.server3]))

    def test_combo_no_conn(self):

        """Function:  test_combo_no_conn

        Description:  Test with combination and no connections.

        Arguments:

        """

        self.server4.conn = None

        self.assertFalse(mysql_libs.disconnect(self.server, self.server4,
                                               [self.server2, self.server3]))

    def test_combo2(self):

        """Function:  test_combo2

        Description:  Test with combination of list and single instances.

        Arguments:

        """

        self.assertFalse(mysql_libs.disconnect(self.server, self.server4,
                                               [self.server2, self.server3]))

    def test_combo(self):

        """Function:  test_combo

        Description:  Test with combination of list and single instances.

        Arguments:

        """

        self.assertFalse(mysql_libs.disconnect(self.server,
                                               [self.server2, self.server3]))

    def test_list_no_conn3(self):

        """Function:  test_list_no_conn3

        Description:  Test with database with no connection in list.

        Arguments:

        """

        self.server.conn = None
        self.server2.conn = None

        self.assertFalse(mysql_libs.disconnect([self.server, self.server2]))

    def test_list_no_conn2(self):

        """Function:  test_list_no_conn2

        Description:  Test with database with no connection in list.

        Arguments:

        """

        self.server.conn = None

        self.assertFalse(mysql_libs.disconnect([self.server, self.server2]))

    def test_list_no_conn(self):

        """Function:  test_list_no_conn

        Description:  Test with database with no connection in list.

        Arguments:

        """

        self.server.conn = None

        self.assertFalse(mysql_libs.disconnect([self.server]))

    def test_single_no_conn(self):

        """Function:  test_single_no_conn

        Description:  Test with database with no connection.

        Arguments:

        """

        self.server.conn = None

        self.assertFalse(mysql_libs.disconnect(self.server))

    def test_list_entry3(self):

        """Function:  test_list_entry3

        Description:  Test with disconnect in list.

        Arguments:

        """

        self.assertFalse(mysql_libs.disconnect([self.server, self.server2]))

    def test_list_entry2(self):

        """Function:  test_list_entry2

        Description:  Test with disconnect in list.

        Arguments:

        """

        self.assertFalse(mysql_libs.disconnect([self.server]))

    def test_list_entry(self):

        """Function:  test_list_entry

        Description:  Test with disconnect in list.

        Arguments:

        """

        self.assertFalse(mysql_libs.disconnect([]))

    def test_single_entry(self):

        """Function:  test_single_entry

        Description:  Test with single disconnect.

        Arguments:

        """

        self.assertFalse(mysql_libs.disconnect(self.server))


if __name__ == "__main__":
    unittest.main()
