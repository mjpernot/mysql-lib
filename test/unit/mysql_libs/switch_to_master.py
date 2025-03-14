# Classification (U)

"""Program:  switch_to_master.py

    Description:  Unit testing of switch_to_master in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/switch_to_master.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mysql_libs                           # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():                             # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__
        sql

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.retrieved_gtidset = 12345

    def upd_gtid_pos(self):

        """Method:  upd_gtid_pos

        Description:  Stub holder for mysql_class.Server.upd_gtid_pos method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_status_fail
        test_status_good

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.slave = Server()
        self.master = Server()

    @mock.patch("mysql_libs.select_wait_until")
    def test_status_fail(self, mock_wait):

        """Function:  test_status_fail

        Description:  Test with good status.

        Arguments:

        """

        mock_wait.return_value = [(-1,)]

        self.assertEqual(mysql_libs.switch_to_master(self.slave, self.master),
                         -1)

    @mock.patch("mysql_libs.select_wait_until")
    @mock.patch("mysql_libs.mysql_class.slave_start")
    @mock.patch("mysql_libs.change_master_to")
    @mock.patch("mysql_libs.mysql_class.slave_stop")
    def test_status_good(self, mock_stop, mock_chg, mock_start, mock_wait):

        """Function:  test_status_good

        Description:  Test with good status.

        Arguments:

        """

        mock_stop.return_value = True
        mock_chg.return_value = True
        mock_start.return_value = True
        mock_wait.return_value = [(0,)]

        self.assertEqual(mysql_libs.switch_to_master(self.slave, self.master),
                         0)


if __name__ == "__main__":
    unittest.main()
