# Classification (U)

"""Program:  sync_delay.py

    Description:  Unit testing of sync_delay in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/sync_delay.py

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
import lib.gen_libs as gen_libs             # pylint:disable=E0401,R0402,C0413
import mysql_libs                           # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class MasterRep():                          # pylint:disable=R0903

    """Class:  MasterRep

    Description:  Class stub holder for mysql_class.MasterRep class.

    Methods:
        __init__

    """

    def __init__(                           # pylint:disable=R0913
            self, name, gtid_mode, exe_gtid, filename, pos):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.gtid_mode = gtid_mode
        self.exe_gtid = exe_gtid
        self.file = filename
        self.pos = pos


class SlaveRep():                           # pylint:disable=R0903

    """Class:  SlaveRep

    Description:  Class stub holder for mysql_class.SlaveRep class.

    Methods:
        __init__

    """

    def __init__(self, gtid_mode):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.gtid_mode = gtid_mode

    def stop_slave(self):

        """Method:  stop_slave

        Description:  Stub holder for mysql_class.Server.stop_slave method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_io_sync_fail_non_gtid
        test_io_sync_good_non_gtid
        test_io_sync_fail_gtid
        test_io_sync_good_gtid

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

    @mock.patch("mysql_libs.wait_until")
    @mock.patch("mysql_libs.start_slave_until")
    @mock.patch("mysql_libs.is_rep_delay")
    def test_io_sync_fail_non_gtid(self, mock_delay, mock_until, mock_wait):

        """Function:  test_io_sync_fail_non_gtid

        Description:  Test with IO sync fail with non-GTID.

        Arguments:

        """

        master = MasterRep("Master", None, None, "File1", 12345)
        slave = SlaveRep(None)
        mock_delay.return_value = True
        mock_until.return_value = (True, "Error Message")
        mock_wait.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.sync_delay(master, slave, "IO"))

    @mock.patch("mysql_libs.wait_until")
    @mock.patch("mysql_libs.start_slave_until")
    @mock.patch("mysql_libs.is_rep_delay")
    def test_io_sync_good_non_gtid(self, mock_delay, mock_until, mock_wait):

        """Function:  test_io_sync_good_non_gtid

        Description:  Test with IO sync good with non-GTID.

        Arguments:

        """

        master = MasterRep("Master", None, None, "File1", 12345)
        slave = SlaveRep(None)
        mock_delay.return_value = True
        mock_until.return_value = (False, None)
        mock_wait.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.sync_delay(master, slave, "IO"))

    @mock.patch("mysql_libs.wait_until")
    @mock.patch("mysql_libs.start_slave_until")
    @mock.patch("mysql_libs.is_rep_delay")
    def test_io_sync_fail_gtid(self, mock_delay, mock_until, mock_wait):

        """Function:  test_io_sync_fail_gtid

        Description:  Test with IO sync fail with GTID.

        Arguments:

        """

        master = MasterRep("Master", "Yes", 12345, None, None)
        slave = SlaveRep("Yes")
        mock_delay.return_value = True
        mock_until.return_value = (True, "Error Message")
        mock_wait.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.sync_delay(master, slave, "IO"))

    @mock.patch("mysql_libs.wait_until")
    @mock.patch("mysql_libs.start_slave_until")
    @mock.patch("mysql_libs.is_rep_delay")
    def test_io_sync_good_gtid(self, mock_delay, mock_until, mock_wait):

        """Function:  test_io_sync_good_gtid

        Description:  Test with IO sync good with GTID.

        Arguments:

        """

        master = MasterRep("Master", "Yes", 12345, None, None)
        slave = SlaveRep("Yes")
        mock_delay.return_value = True
        mock_until.return_value = (False, None)
        mock_wait.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.sync_delay(master, slave, "IO"))


if __name__ == "__main__":
    unittest.main()
