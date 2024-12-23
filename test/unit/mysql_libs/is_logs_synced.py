# Classification (U)

"""Program:  is_logs_synced.py

    Description:  Unit testing of is_logs_synced in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/is_logs_synced.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
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

    def __init__(                           # pylint:disable=R0913
            self, name, gtid_mode, exe_gtid, relay_log, mst_pos):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.gtid_mode = gtid_mode
        self.exe_gtid = exe_gtid
        self.relay_mst_log = relay_log
        self.exec_mst_pos = mst_pos


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_logs_not_synced_non_gtid
        test_logs_synced_non_gtid
        test_logs_not_synced_gtid
        test_logs_synced_gtid

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

    def test_logs_not_synced_non_gtid(self):

        """Function:  test_logs_not_synced_non_gtid

        Description:  Test with logs not synced with non-GTID.

        Arguments:

        """

        master = MasterRep("Master", None, None, "File1", 12345)
        slave = SlaveRep("Slave", None, None, "File1", 12346)

        self.assertFalse(mysql_libs.is_logs_synced(master, slave))

    def test_logs_synced_non_gtid(self):

        """Function:  test_logs_synced_non_gtid

        Description:  Test with logs synced with non-GTID.

        Arguments:

        """

        master = MasterRep("Master", None, None, "File1", 12345)
        slave = SlaveRep("Slave", None, None, "File1", 12345)

        self.assertTrue(mysql_libs.is_logs_synced(master, slave))

    def test_logs_not_synced_gtid(self):

        """Function:  test_logs_not_synced_gtid

        Description:  Test with logs not synced with GTID.

        Arguments:

        """

        master = MasterRep("Master", "Yes", 12345, None, None)
        slave = SlaveRep("Slave", "Yes", 12346, None, None)

        self.assertFalse(mysql_libs.is_logs_synced(master, slave))

    def test_logs_synced_gtid(self):

        """Function:  test_logs_synced_gtid

        Description:  Test with logs synced with GTID.

        Arguments:

        """

        master = MasterRep("Master", "Yes", 12345, None, None)
        slave = SlaveRep("Slave", "Yes", 12345, None, None)

        self.assertTrue(mysql_libs.is_logs_synced(master, slave))


if __name__ == "__main__":
    unittest.main()
