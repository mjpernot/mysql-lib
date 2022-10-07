# Classification (U)

"""Program:  _io_wait_chk.py

    Description:  Unit testing of _io_wait_chk in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/_io_wait_chk.py

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
import lib.gen_libs as gen_libs
import mysql_libs
import version

__version__ = version.__version__


class SlaveRep(object):

    """Class:  SlaveRep

    Description:  Class stub holder for mysql_class.SlaveRep class.

    Methods:
        __init__

    """

    def __init__(self, gtid_mode="Yes"):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.gtid_mode = gtid_mode
        self.name = "Slave"
        self.retrieved_gtid = 10
        self.mst_log = "mst_log"
        self.mst_read_pos = 12345
        self.exe_gtid = 12345
        self.relay_mst_log = "relay_mst_log"
        self.exec_mst_pos = 12345

    def upd_slv_status(self):

        """Method:  upd_slv_status

        Description:  Stub holder for mysql_class.Server.upd_slv_status method.

        Arguments:

        """

        self.retrieved_gtid = 10
        self.mst_read_pos = 12345


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_io_non_gtid_update
        test_io_non_gtid_good
        test_io_gtid_update
        test_io_gtid_good

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.slave = SlaveRep()
        self.slave2 = SlaveRep(False)

    def test_io_non_gtid_update(self):

        """Function:  test_io_non_gtid_update

        Description:  Test in non-GTID Mode with update status.

        Arguments:

        """

        self.slave2.mst_read_pos = 1111

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs._io_wait_chk(
                self.slave2, log_file="mst_log", log_pos=12345, gtid=10))

    def test_io_non_gtid_good(self):

        """Function:  test_io_non_gtid_good

        Description:  Test in non-GTID Mode with good status.

        Arguments:

        """

        self.slave.gtid_mode = None

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs._io_wait_chk(
                self.slave2, log_file="mst_log", log_pos=12345, gtid=10))

    def test_io_gtid_update(self):

        """Function:  test_io_gtid_update

        Description:  Test in GTID Mode with update status.

        Arguments:

        """

        self.slave.retrieved_gtid = 11

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs._io_wait_chk(self.slave, 10, None,
                                                     None))

    def test_io_gtid_good(self):

        """Function:  test_io_gtid_good

        Description:  Test in GTID Mode with good status.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs._io_wait_chk(self.slave, 10, None,
                                                     None))


if __name__ == "__main__":
    unittest.main()
